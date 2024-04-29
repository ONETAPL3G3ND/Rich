from rich.columns import Columns
from rich.console import Console

console = Console()

columns = Columns([ "Colum 1", "Colum 2", "Colum 3"])
console.print(columns)
