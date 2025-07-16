# pubmed_paper_scraper/fetcher.py

import requests
from typing import List

# PubMed API URLs
BASE_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
BASE_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def search_pubmed(query: str, retmax: int = 10, debug: bool = False) -> List[str]:
    """
    Search PubMed with a topic and return a list of paper IDs.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }

    response = requests.get(BASE_SEARCH_URL, params=params)
    
    if debug:
        print("[DEBUG] Search URL:", response.url)
        print("[DEBUG] Search Response JSON:", response.text)

    response.raise_for_status()  # stop if error
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])


def fetch_details(pubmed_ids: List[str], debug: bool = False) -> str:
    """
    Fetch full XML data for a list of PubMed paper IDs.
    """
    if not pubmed_ids:
        return ""

    ids = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": ids,
        "retmode": "xml"
    }

    response = requests.get(BASE_FETCH_URL, params=params)
    
    if debug:
        print("[DEBUG] Fetch URL:", response.url)
        print("[DEBUG] Fetched XML Length:", len(response.text))

    response.raise_for_status()
    return response.text
