from rich.table import Table
from rich.console import Console

console = Console()

table = Table(show_header=True, header_style="bold cyan")
table.add_column("Name", style="italic", width=12)
table.add_column("Age", style="magenta")
table.add_row("John Doe", "30")
table.add_row("Jane Smith", "25")
console.print(table)
