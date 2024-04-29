from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel

console = Console()

layout = Layout()

layout.split(Layout(name="top", ratio=2), Layout(name="bottom"))

layout["top"].update(Panel("Top Layer", title="Top Layer", border_style="blue"))
layout["bottom"].update(
    Panel("Bottom Layer", title="Bottom Layer", border_style="green")
)

console.print(layout)
