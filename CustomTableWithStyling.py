from rich.console import Console
from rich.table import Table

if __name__ == "__main__":
    console = Console()

    table = Table(title="Student Grades")
    table.add_column("Name", style="bold cyan")
    table.add_column("Math", style="bold yellow")
    table.add_column("Science", style="bold yellow")

    table.add_row("Alice", "A", "B")
    table.add_row("Bob", "B", "A")
    table.add_row("Charlie", "A", "A")

    console.print(table)
