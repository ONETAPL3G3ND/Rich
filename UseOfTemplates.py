from rich.console import Console
from rich.text import Text
from rich.theme import Theme

my_theme = Theme({"info": "italic bold blue", "warning": "bold red", "error": "bold red"})

console = Console(theme=my_theme)

console.print(Text("This is information", style="info"))
console.print(Text("This is a warning", style="warning"))
console.print(Text("This is error", style="error"))
