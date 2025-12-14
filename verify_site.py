import os
import re
from urllib.parse import unquote

ROOT_DIR = r"c:/Users/Aakanksha/.gemini/antigravity/scratch/lexi_services_website"

def get_html_files(root_dir):
    html_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def check_file(filepath):
    print(f"Checking: {os.path.basename(filepath)}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find links and images
    # Simple regex for href="..." and src="..."
    # note: this is a simple checker, might miss edge cases but good for static site
    hrefs = re.findall(r'href=["\'](.*?)["\']', content)
    srcs = re.findall(r'src=["\'](.*?)["\']', content)

    issues = []

    all_refs = hrefs + srcs
    for ref in all_refs:
        if ref.startswith(('http', 'https', '#', 'mailto:', 'tel:', 'wa.me')):
            continue
        
        # Remove anchor part
        clean_ref = ref.split('#')[0]
        if not clean_ref:
            continue

        # Resolve path
        # Current file directory
        current_dir = os.path.dirname(filepath)
        target_path = os.path.normpath(os.path.join(current_dir, clean_ref))
        
        if not os.path.exists(target_path):
            issues.append(f"  [MISSING] {ref} (resolved: {target_path})")

    if issues:
        for issue in issues:
            print(issue)
    else:
        print("  [OK] No broken links found.")
    print("-" * 40)

def main():
    print(f"Starting verification in: {ROOT_DIR}\n")
    html_files = get_html_files(ROOT_DIR)
    for html_file in html_files:
        check_file(html_file)
    print("\nVerification Complete.")

if __name__ == "__main__":
    main()
