# Documentation for pygbm

This directory contains the Sphinx documentation for the pygbm package.

## Building the Documentation

To build the documentation locally:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Build the HTML documentation:
   ```bash
   cd docs
   make html
   ```

3. View the documentation by opening `build/html/index.html` in a web browser.

## Documentation Structure

- `source/conf.py` - Sphinx configuration file
- `source/index.rst` - Main documentation page
- `source/modules.rst` - API reference documentation
- `requirements.txt` - Documentation build dependencies
- `Makefile` - Build automation for Unix/Linux/macOS
- `make.bat` - Build automation for Windows

## Read the Docs Integration

This documentation is configured to be built automatically by Read the Docs.
The configuration is in the `.readthedocs.yaml` file in the repository root.
