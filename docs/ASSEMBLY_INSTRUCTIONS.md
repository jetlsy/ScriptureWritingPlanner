# Assembly Instructions

This document provides instructions on how to assemble the Scripture Writing Planner SVGs and Python script into a GoodNotes-compatible PDF.

## 1. Run the Build Script

The primary way to build the hyperlinked PDF is by running the Python build script `build_planner.py`. This script relies on the `reportlab` library.

### Prerequisites

You need Python 3 installed. Install the required dependency:

```bash
pip install reportlab
```

### Execution

Run the script to generate the PDF:

```bash
python3 build_planner.py
```

This will output `Scripture_Writing_Planner.pdf` in the same directory. The resulting PDF includes a cover, an index, a daily page, and a weekly page, all internally linked for easy navigation in apps like GoodNotes or Notability.

## 2. Using the SVG Assets

If you prefer to edit the assets visually using software like Adobe Illustrator, Affinity Designer, or Inkscape, you can use the files located in the `assets/` directory:

- `assets/color-palette.svg`: A visual reference of the color palette.
- `assets/cover.svg`: The vector cover design.
- `assets/page-template-daily.svg`: The daily layout design.
- `assets/page-template-weekly.svg`: The weekly layout design.

To make them GoodNotes-compatible, you can open them in your vector editor, export them as a single PDF, and manually add internal hyperlinks to the PDF using tools like Adobe Acrobat or Mac Preview before importing into GoodNotes.
