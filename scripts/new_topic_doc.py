#!/usr/bin/env python3
"""
Script to generate a new topic documentation file.
"""

import sys
import os
from pathlib import Path

def create_topic_doc(topic_name, category="data-structures"):
    """Create a new topic documentation file."""
    base_dir = Path(__file__).parent.parent
    docs_dir = base_dir / "docs" / "topics" / category
    
    topic_file = docs_dir / f"{topic_name}.md"
    
    if topic_file.exists():
        print(f"Error: {topic_file} already exists!")
        return False
    
    template = f"""# {topic_name.replace('-', ' ').title()}

## Overview

[Brief description of the topic]

## Implementations

- Python: `python/src/dsa/[path]`
- JavaScript: `javascript/src/[path]`
"""
    
    topic_file.write_text(template)
    print(f"Created: {topic_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python new_topic_doc.py <topic-name> [category]")
        print("Categories: data-structures, algorithms, math")
        sys.exit(1)
    
    topic_name = sys.argv[1]
    category = sys.argv[2] if len(sys.argv) > 2 else "data-structures"
    
    create_topic_doc(topic_name, category)

