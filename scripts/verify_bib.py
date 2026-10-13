import os
import re
import sys

# Ensure UTF-8 output on Windows console
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

def verify_citations():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sections_dir = os.path.join(base_dir, "sections")
    bib_file = os.path.join(base_dir, "ref.bib")

    # 1. Parse BibTeX keys
    with open(bib_file, "r", encoding="utf-8") as f:
        bib_content = f.read()
    bib_keys = set(re.findall(r"@\w+\s*{\s*([^,\s]+)", bib_content))

    # 2. Parse citations from all .tex files
    cited_keys = set()
    tex_files = [os.path.join(base_dir, "main.tex")]
    if os.path.exists(sections_dir):
        for f in os.listdir(sections_dir):
            if f.endswith(".tex"):
                tex_files.append(os.path.join(sections_dir, f))

    for tf in tex_files:
        if os.path.exists(tf):
            with open(tf, "r", encoding="utf-8") as f:
                content = f.read()
                matches = re.findall(r"\\cite\s*\{([^}]+)\}", content)
                for match in matches:
                    for key in match.split(","):
                        cited_keys.add(key.strip())

    # 3. Analyze differences
    missing_in_bib = cited_keys - bib_keys
    uncited_in_tex = bib_keys - cited_keys

    print("==================================================")
    print(" SWR302 BIBLIOGRAPHY & CITATION AUDIT REPORT")
    print("==================================================")
    print(f"Total BibTeX entries defined in ref.bib: {len(bib_keys)}")
    print(f"Total unique citations in .tex files   : {len(cited_keys)}")
    print("--------------------------------------------------")

    if missing_in_bib:
        print(f"❌ ERROR: Found {len(missing_in_bib)} missing citation(s) in ref.bib:")
        for k in sorted(missing_in_bib):
            print(f"   - {k}")
    else:
        print("✅ SUCCESS: All cited keys are present in ref.bib!")

    if uncited_in_tex:
        print(f"\nℹ️ NOTICE: {len(uncited_in_tex)} BibTeX entry/entries not yet cited in .tex files:")
        for k in sorted(uncited_in_tex):
            print(f"   - {k}")
    else:
        print("\n✅ All BibTeX entries are actively cited!")
    print("==================================================")

if __name__ == "__main__":
    verify_citations()
