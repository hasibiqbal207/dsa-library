#!/usr/bin/env python3
"""
Script to check documentation links.
"""

import re
from pathlib import Path

def check_links():
    """Check all markdown files for broken links."""
    base_dir = Path(__file__).parent.parent
    docs_dir = base_dir / "docs"
    
    markdown_files = list(docs_dir.rglob("*.md"))
    
    broken_links = []
    
    for md_file in markdown_files:
        content = md_file.read_text()
        
        # Find all markdown links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, content)
        
        for link_text, link_path in links:
            # Skip external links
            if link_path.startswith('http'):
                continue
            
            # Resolve relative paths
            if link_path.startswith('/'):
                target = base_dir / link_path[1:]
            else:
                target = md_file.parent / link_path
            
            if not target.exists():
                broken_links.append((md_file, link_text, link_path))
    
    if broken_links:
        print("Broken links found:")
        for md_file, link_text, link_path in broken_links:
            print(f"  {md_file}: [{link_text}]({link_path})")
        return False
    
    print("All links are valid!")
    return True

if __name__ == "__main__":
    check_links()

