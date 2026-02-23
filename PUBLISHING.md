# Publishing Guide

## PyPI (Python package)

### First-time setup
```bash
py -m pip install build twine
```

Create a PyPI account at https://pypi.org/account/register/ and generate an API token.

### Build & Publish
```bash
py -m build                        # Creates dist/
py -m twine check dist/*           # Verify package
py -m twine upload dist/*          # Upload to PyPI
```

### After publishing
Users can install with:
```bash
pip install codecks-mcp
codecks-mcp                        # Run via console script
python -m codecks_mcp              # Run as module
```

## Important Note
This package depends on `codecks-cli` from GitHub. Before publishing, ensure
the latest codecks-cli is pushed to https://github.com/rangogamedev/codecks-cli.

## Version Bumps
Update `version` in `pyproject.toml`, then rebuild and upload.
