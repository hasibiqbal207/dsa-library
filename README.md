# DSA Library

A comprehensive library of data structures and algorithms implementations with documentation.

## Structure

This repository follows a **language-first for code + topic-first for docs/indexing** structure:

- `docs/` - Topic-first documentation organized by category
- `python/` - Python package with implementations
- `javascript/` - JavaScript project with implementations
- `scripts/` - Helper scripts for documentation and maintenance

## Documentation

See [docs/index.md](docs/index.md) for the complete index of topics.

## Quick Start

### Python

```bash
cd python
pip install -e .
```

### JavaScript

```bash
cd javascript
npm install
```

## Contributing

When adding new topics:

1. Create documentation in `docs/topics/`
2. Add implementations in the appropriate language directories
3. Update `docs/index.md` with links to your new topic
4. Use the scripts in `scripts/` to help maintain consistency

## File Naming Conventions

- **Docs:** kebab-case (`segment-tree.md`)
- **Python:** snake_case (`segment_tree.py`)
- **JavaScript:** camelCase (`segmentTree.js`)
