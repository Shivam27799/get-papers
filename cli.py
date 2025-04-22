import argparse
import pandas as pd
from get_papers.fetch import fetch_paper_details

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers related to pharmaceutical/biotech companies.")
    parser.add_argument('--query', type=str, required=True, help='Search query (PubMed query syntax supported)')
    parser.add_argument('--debug', '-d', action='store_true', help='Enable debug output')
    parser.add_argument('--file', '-f', type=str, help='Filename to save the CSV output')
    
    args = parser.parse_args()

    query = args.query
    debug = args.debug
    file_output = args.file

    if debug:
        print(f"[DEBUG] Fetching papers for query: '{query}'")

    papers = fetch_paper_details(query, max_results=20)

    df = pd.DataFrame(papers)

    if file_output:
        df.to_csv(file_output, index=False)
        print(f"\n✅ Output saved to {file_output}")
    else:
        print("\n🔍 Results:")
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()