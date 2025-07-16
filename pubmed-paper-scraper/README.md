# PubMed Paper Scraper

This is a Python command-line tool that fetches research papers from PubMed based on a user-specified query. It identifies documents that have at least one author affiliated with a **pharmaceutical or biotech company**, and returns the results in a structured CSV file.

---

## 📁 Project Structure

pubmed-paper-scraper/

├── pubmed_paper_scraper/        ← ✅ This is your module
│   ├── fetcher.py

│   ├── parser.py

│   └── __init__.py


├── cli.py                        ← ✅ This is your command-line interface


---

## 🚀 Features

- Search PubMed with full query syntax
- Filter for non-academic authors based on affiliation
- Extract company affiliations and emails
- Save output to CSV or view in the terminal
- Supports command-line flags (`--help`, `--debug`, `--file`)

---

## 🛠️ Installation & Usage

### ✅ Step 1: Install Poetry 


### ✅ Step 2: Clone the repository and install dependencies

```bash
git clone https://github.com/your-username/pubmed-paper-scraper.git
cd pubmed-paper-scraper
poetry install


### ✅ Step 3: Run the program

poetry run get-papers-list "AI in drug discovery" --file results.csv --debug

This command will:
Search for papers related to the topic
Extract titles, authors, company affiliations, publication date, and corresponding emails
Save the result to results.csv

🧰 Tools and Libraries Used
🐍 Python 3.12
📦 Poetry – for dependency and package management
🛠️ Typer – to build the CLI
📊 Pandas – to manage and export CSV data
🎨 Rich – for colorful and formatted terminal output
📡 NCBI E-utilities API – to query PubMed data
💡  LLMs (such as ChatGPT) were utilized to accelerate development and design.

🙋‍♀️ Author
Tarannum Parwin
GitHub: https://github.com/TarannumParwin
Email: tarannumparwin1995@gmail.com

