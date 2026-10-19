from pathlib import Path
graph = {
    "main": ["users", "payments"],
    "users": ["database"],
    "payments": [],
    "database": ["main"]
}
def has_cycle(graph):
    visited = set()
    active_path = set()
    def dfs(module):
 
        if module in active_path:
            return True
        if module in visited:
            return False
        visited.add(module)
        active_path.add(module)
        for dependency in graph.get(module,[]):
            if dfs(dependency):
                return True
        active_path.remove(module)
        return False
    for module in graph:
        if dfs(module):
            return True
    return False

print(has_cycle(graph))

def discover_python_files(root):
    root = Path(root)
    if  root.exists() and root.is_dir():
        colledted_files=[]
        for file in root.rglob("*.py"):
            colledted_files.append(file)
        return colledted_files
    return f"there is no dirctory name {root}"
    

print(discover_python_files("deepgraph"))
root = Path("Deepgraph")
dirname = Path("deepgraph/test")
def module_generator(dirname,root):
    
    relative_path = dirname.relative_to(root)
    parts = relative_path.parts
    stem = relative_path.stem
    module_parts = parts[:-1] + (stem,)
    print(relative_path.parts)
    module_name = ".".join(module_parts)
    return module_name
print(module_generator(dirname,root))