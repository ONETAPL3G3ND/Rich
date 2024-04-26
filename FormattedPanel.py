from rich.console import Console
from rich.panel import Panel

if __name__ == "__main__":
    console = Console()

    panel = Panel("Welcome to Rich library!", title="Information", style="bold green")

    console.print(panel)
