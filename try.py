from pathlib import Path

file = Path("deepgraph/graph.py")
parts = file.parts
steam = file.stem
print(parts)
parts1 = parts[0]

print(parts1)
print(steam)
module_name = ".".join((parts1,steam))

print(module_name)