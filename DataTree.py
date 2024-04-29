from rich.console import Console
from rich.tree import Tree

console = Console()

tree = Tree("Root")

tree.add("Node 1")
tree.add("Node 2")
sub_tree = tree.add("Node 3")
sub_tree.add("Subnode 3.1")
sub_tree.add("Subnode 3.2")

console.print(tree)
