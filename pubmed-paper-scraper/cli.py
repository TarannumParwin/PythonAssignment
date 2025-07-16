import typer
import pandas as pd
from rich import print
from pubmed_paper_scraper.fetcher import search_pubmed, fetch_details
from pubmed_paper_scraper.parser import parse_pubmed_xml

app = typer.Typer()

@app.command()
def main(
    query: str = typer.Argument(..., help="Search topic for research papers"),
    file: str = typer.Option(None, "-f", "--file", help="Save results to a CSV file"),
    debug: bool = typer.Option(False, "-d", "--debug", help="Show extra info while running")
):
    """
    Fetches papers from PubMed based on your query and outputs details.
    """
    print(f"[bold cyan]Searching for:[/bold cyan] {query}")

    ids = search_pubmed(query, debug=debug)
    if not ids:
        print("[red]No papers found.[/red]")
        raise typer.Exit()

    print(f"[green]Found {len(ids)} papers[/green]")

    xml = fetch_details(ids, debug=debug)
    data = parse_pubmed_xml(xml)

    if not data:
        print("[yellow]No valid data extracted from XML.[/yellow]")
        raise typer.Exit()

    if file:
        df = pd.DataFrame(data)
        df.to_csv(file, index=False)
        print(f"[bold green]Saved results to:[/bold green] {file}")
    else:
        print("[bold magenta]Results:[/bold magenta]")
        for paper in data:
            print("-" * 60)
            for key, value in paper.items():
                print(f"[cyan]{key}:[/cyan] {value}")

if __name__ == "__main__":
    app()
