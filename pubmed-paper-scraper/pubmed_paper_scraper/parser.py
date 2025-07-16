# pubmed_paper_scraper/parser.py

import xml.etree.ElementTree as ET
from typing import List, Dict

def is_non_academic(affiliation: str) -> bool:
    """
    Checks if the affiliation is from a non-academic organization.
    """
    academic_keywords = ["university", "institute", "college", "school", "hospital", "center", "centre"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def parse_pubmed_xml(xml_data: str) -> List[Dict[str, str]]:
    """
    Parses XML from PubMed and extracts paper info.
    Returns a list of dictionaries for each paper.
    """
    results = []
    root = ET.fromstring(xml_data)

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or "N/A"
        title = article.findtext(".//ArticleTitle") or "N/A"
        pub_date = article.findtext(".//PubDate/Year") or "N/A"
        if pub_date == "N/A":
            pub_date = article.findtext(".//PubDate/MedlineDate") or "N/A"

        non_academic_authors = []
        company_affiliations = []
        corresponding_email = None

        for author in article.findall(".//Author"):
            name_parts = []
            if author.find("LastName") is not None:
                name_parts.append(author.findtext("LastName"))
            if author.find("ForeName") is not None:
                name_parts.append(author.findtext("ForeName"))
            full_name = " ".join(name_parts)

            affiliation_info = author.find(".//AffiliationInfo/Affiliation")
            if affiliation_info is not None:
                affiliation = affiliation_info.text or ""

                if "@" in affiliation and not corresponding_email:
                    corresponding_email = affiliation.split()[-1]  # rough extraction

                if is_non_academic(affiliation):
                    non_academic_authors.append(full_name)
                    company_affiliations.append(affiliation)

        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(non_academic_authors) if non_academic_authors else "N/A",
            "Company Affiliation(s)": "; ".join(company_affiliations) if company_affiliations else "N/A",
            "Corresponding Author Email": corresponding_email or "N/A"
        })

    return results
