from rich.console import Console
from rich.panel import Panel

console = Console()

panel = Panel.fit("Panel Contents", title="Panel", border_style="red")
console.print(panel)
