from rich.console import Console
from rich.style import Style

console = Console()

style = Style(bold=True, italic=True, underline=True, color="blue", bgcolor="yellow")
console.print("Rich Styles", style=style)
