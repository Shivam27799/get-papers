
---

```markdown
# 🧬 Get Papers from PubMed

A Python command-line tool to search PubMed for research papers based on a user-specified query. The tool fetches only those papers that have at least one author affiliated with a **pharmaceutical or biotech company**, and exports the results in CSV format.

---

## 📁 Project Structure

```
get-papers/
├── get_papers/
│   ├── __init__.py
│   └── fetch.py             # Core logic to fetch and filter papers
├── cli.py                   # Command-line interface to run the tool
├── pyproject.toml           # Poetry config for dependencies & packaging
└── README.md                # Project documentation
```

---

## 🧰 Tools & Libraries Used

- [**Poetry**](https://python-poetry.org/) – For dependency management and packaging.
- [**Biopython**](https://biopython.org/) – For accessing the PubMed API using `Entrez`.
- [**pandas**](https://pandas.pydata.org/) – For handling tabular data and exporting to CSV.
- [**argparse**](https://docs.python.org/3/library/argparse.html) – For parsing command-line arguments.
- [PubMed API / Entrez](https://www.ncbi.nlm.nih.gov/books/NBK25501/) – Source of biomedical paper metadata.

> ⚙️ Built with help from an LLM (ChatGPT) to design structure and troubleshoot commands.

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/get-papers.git
cd get-papers
```

### 2. Install Poetry (if not already installed)
```bash
pip install poetry
```

### 3. Install Dependencies
```bash
poetry install
```

---

## 🔧 How to Use

### Option A: Print to Terminal
```bash
poetry run get-papers-list --query "mRNA vaccine"
```

### Option B: Save Output to a CSV File
```bash
poetry run get-papers-list --query "mRNA vaccine" --file result.csv
```

### Optional Flags:
- `--debug` or `-d` : Print debug info
- `--file` or `-f <filename>` : Save results as a CSV

---

## 🧪 Example Output

```csv
PubmedID,Title,Publication Date,Non-academicAuthor(s),CompanyAffiliation(s),Corresponding Author Email
12345678,"mRNA vaccines in oncology",2024-03-20,"Dr. Jane Smith","Pfizer","jane.smith@pfizer.com"
...
```

---

