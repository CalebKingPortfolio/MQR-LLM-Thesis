import json
import sys
 
# Usage: python fix_notebook.py yournotebook.ipynb
path = sys.argv[1] if len(sys.argv) > 1 else "Llama-3.2-3B-Instruct (Base).ipynb"
 
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)
 
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]
    print(f"Removed widgets metadata from {path}")
else:
    print("No widgets metadata found — nothing to fix.")
 
with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)
 
print("Done. Push to GitHub and the error should be gone.")