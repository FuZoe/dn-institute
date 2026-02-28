#!/usr/bin/env python3
"""
Update Dashboard Script

Updates the embedded JSON data in index.html from enriched_bounties.json.
This allows the dashboard to work both as a static file and stay in sync with data updates.
"""

import json
import re

ENRICHED_FILE = "enriched_bounties.json"
DASHBOARD_FILE = "index.html"


def main():
    print(f"Loading enriched data from {ENRICHED_FILE}...")
    with open(ENRICHED_FILE, "r", encoding="utf-8") as f:
        bounties = json.load(f)
    
    # Create compact JSON for embedding (remove body field to save space)
    compact_bounties = []
    for b in bounties:
        compact = {
            "number": b["number"],
            "title": b["title"],
            "url": b["url"],
            "state": b["state"],
            "labels": b["labels"],
            "comment_count": b["comment_count"],
            "repository": b["repository"],
            "created_at": b["created_at"],
            "updated_at": b["updated_at"],
            "author": b["author"],
            "hunter_intelligence": b["hunter_intelligence"]
        }
        compact_bounties.append(compact)
    
    embedded_json = json.dumps(compact_bounties, ensure_ascii=False)
    
    print(f"Reading {DASHBOARD_FILE}...")
    with open(DASHBOARD_FILE, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Pattern to find and replace the EMBEDDED_DATA
    pattern = r"const EMBEDDED_DATA = \[.*?\];"
    replacement = f"const EMBEDDED_DATA = {embedded_json};"
    
    new_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
    
    if new_html == html_content:
        print("Warning: No EMBEDDED_DATA found to update!")
        return
    
    print(f"Writing updated {DASHBOARD_FILE}...")
    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)
    
    print(f"Done! Updated dashboard with {len(compact_bounties)} bounties.")


if __name__ == "__main__":
    main()
