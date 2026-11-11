"""Fetch an arXiv paper (HTML first, PDF fallback) and split it into clean sections."""

import copy

import httpx
import pymupdf
from bs4 import BeautifulSoup


def clean_text(el):
    el = copy.copy(el)
    for fig in el.find_all("figure", class_="ltx_figure"):
        fig.decompose()
    for m in el.find_all("math"):
        m.replace_with(f" ${m.get('alttext', '')}$ ")
    title = el.find(class_="ltx_title")
    if title:
        title.decompose()
    return " ".join(el.get_text(" ").split())


def fetch_html(arxiv_id):
    r = httpx.get(f"https://arxiv.org/html/{arxiv_id}", follow_redirects=True)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    sections = []
    abstract = soup.find(class_="ltx_abstract")
    if abstract:
        sections.append({"id": "abstract", "title": "Abstract", "text": clean_text(abstract)})
    for sec in soup.find_all("section", class_="ltx_section"):
        text = clean_text(sec)
        if not text:
            continue
        title = sec.find(class_="ltx_title").get_text(" ", strip=True)
        sections.append({"id": sec.get("id"), "title": title, "text": text})
    return {"arxiv_id": arxiv_id, "title": soup.title.get_text(strip=True), "source": "html", "sections": sections}


def fetch_pdf(arxiv_id):
    r = httpx.get(f"https://arxiv.org/pdf/{arxiv_id}", follow_redirects=True)
    r.raise_for_status()
    doc = pymupdf.open(stream=r.content, filetype="pdf")
    sections = [
        {"id": f"page{i + 1}", "title": f"Page {i + 1}", "text": " ".join(page.get_text().split())}
        for i, page in enumerate(doc)
    ]
    return {"arxiv_id": arxiv_id, "title": doc.metadata.get("title") or arxiv_id, "source": "pdf", "sections": sections}


def fetch_paper(arxiv_id):
    try:
        return fetch_html(arxiv_id)
    except httpx.HTTPStatusError:
        return fetch_pdf(arxiv_id)