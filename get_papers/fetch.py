from typing import List, Dict
from Bio import Entrez
import xml.etree.ElementTree as ET

Entrez.email = "vermashivam27799@gmail.com" 

def fetch_paper_details(query: str, max_results: int = 10) -> List[Dict]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    ids = record["IdList"]

    results = []

    for pmid in ids:
        try:
            fetch_handle = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
            fetch_data = fetch_handle.read()
            fetch_handle.close()

            root = ET.fromstring(fetch_data)
            article = root.find(".//PubmedArticle")

            title = article.findtext(".//ArticleTitle", default="Not Found")

            pub_date = article.findtext(".//PubDate/Year")
            if not pub_date:
                pub_date = article.findtext(".//DateCompleted/Year", default="Unknown")

            authors = article.findall(".//Author")
            non_academic_authors = []
            company_affiliations = []
            corresponding_email = "Not Found"

            for author in authors:
                lastname = author.findtext("LastName", default="")
                forename = author.findtext("ForeName", default="")
                full_name = f"{forename} {lastname}".strip()

                affiliation = ""
                affiliation_infos = author.findall("AffiliationInfo")
                for aff in affiliation_infos:
                    affil_text = aff.findtext("Affiliation")
                    if affil_text:
                        affiliation += affil_text + " "

                # Debug print
                print(f"Author: {full_name}")
                print(f"Affiliation: {affiliation.strip()}")

                if any(keyword in affiliation.lower() for keyword in ["pharma", "biotech", "inc", "ltd", "gmbh", "therapeutics", "company", "moderna", "pfizer"]):
                    non_academic_authors.append(full_name)
                    company_affiliations.append(affiliation.strip())

                if "@" in affiliation and corresponding_email == "Not Found":
                    words = affiliation.split()
                    email_candidates = [word for word in words if "@" in word]
                    if email_candidates:
                        corresponding_email = email_candidates[0]

            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academicAuthor(s)": "; ".join(non_academic_authors) or "Not Found",
                "CompanyAffiliation(s)": "; ".join(company_affiliations) or "Not Found",
                "Corresponding Author Email": corresponding_email
            })

        except Exception as e:
            results.append({
                "PubmedID": pmid,
                "Title": "Fetch Error",
                "Publication Date": "Unknown",
                "Non-academicAuthor(s)": "Error",
                "CompanyAffiliation(s)": str(e),
                "Corresponding Author Email": "Not Available"
            })

    return results
