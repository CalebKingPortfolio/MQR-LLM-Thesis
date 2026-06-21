import json
import glob
import os
 
notebooks = glob.glob("**/*.ipynb", recursive=True)
 
if not notebooks:
    print("No .ipynb files found.")
else:
    for path in notebooks:
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)
 
        if "widgets" in nb.get("metadata", {}):
            del nb["metadata"]["widgets"]
            with open(path, "w", encoding="utf-8") as f:
                json.dump(nb, f, indent=1)
            print(f"Fixed: {path}")
        else:
            print(f"Skipped (no widgets): {path}")
 
print("\nDone.")