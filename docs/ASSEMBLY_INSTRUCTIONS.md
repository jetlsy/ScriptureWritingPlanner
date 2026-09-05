# Assembly Instructions — Scripture Writing Planner (US Letter, single-sided)

This document explains how to assemble the SVG assets in this repo into a single hyperlinked PDF optimized for GoodNotes.

Files added to this branch (scripture-planner-assets):
- assets/color-palette.svg — color swatches and hex codes
- assets/cover.svg — vector cover (title, subtitle, credit line)
- assets/decor-elements.svg — line-art and decorative elements
- assets/page-template-daily.svg
- assets/page-template-weekly.svg
- assets/page-template-monthly.svg
- assets/habit-tracker.svg
- assets/goals-meal-tracker.svg
- assets/scripture-list.svg
- assets/prayer-reflection.svg
- assets/notes-lined.svg
- assets/notes-dotted.svg
- assets/notes-plain.svg

Recommended workflow to create a GoodNotes-optimized PDF with internal links

1) Review & adjust fonts
   - The designs use Cormorant Garamond for headings and Montserrat for UI/labels. If you want the text preserved as selectable text in the PDF, install these fonts locally before exporting from your design tool.
   - Alternatively, convert text to outlines before exporting to avoid font embedding issues (this makes text non-selectable but preserves appearance).

2) Import & arrange pages
   - Open a vector editor or page-layout tool that supports US Letter (8.5 x 11 inches) and SVG import. Recommended: Affinity Designer, Adobe Illustrator, Inkscape (free), or Affinity Publisher / InDesign for multi-page export.
   - Create a new document sized to US Letter, 8.5" x 11", portrait, 300 DPI. Use single-sided pages (one template per page).
   - Import each SVG as a full page and align to the artboard. Page order suggestion:
     1. Cover
     2. Table of Contents (create in your layout tool — see step 4)
     3. Weekly / Monthly / Daily templates (repeat daily pages as needed)
     4. Habit Tracker, Goals & Meal Planner, Scripture Lists, Prayer & Reflection
     5. Notes pages (lined, dotted, plain)
     6. Decorative sticker/art page
     7. Back cover

3) Export pages as PDF
   - Export each page as a PDF page (single multi-page PDF). In Illustrator/Publisher/Indesign you can export a single multi-page PDF directly. In Affinity Designer you can export pages or use Publisher to assemble.
   - Ensure "crop marks" and bleed are turned off for digital-only planner use.
   - Embed fonts if available, or convert to outlines.

4) Create a hyperlinked Table of Contents (TOC)
   - Create a TOC page in your layout tool, with a clean list of sections and page numbers.
   - Add internal hyperlinks (tools vary): In Adobe InDesign you can add hyperlinks to page destinations and export them. In Acrobat you can add link annotations to jump to pages.
   - GoodNotes recognizes internal PDF links and bookmarks. Also add PDF bookmarks for each major section (InDesign/Acrobat export supports bookmarks).

5) Add page tabs (optional)
   - Create small visual tabs on the right edge of pages (or a linked tab page) and add internal link annotations that jump to the start of each section. Keep the tabs within the safe area (no crop needed for digital).

6) Optimize for GoodNotes
   - Keep pages single-sided and 8.5" x 11".
   - Avoid interactive form fields — GoodNotes does not support filling PDF form fields reliably. Instead, leave blank boxes/areas for handwriting input (the assets in this repo use blank boxes).
   - Keep vector elements and line-weights moderate so they appear crisp but not visually heavy when zoomed.

7) Final checks
   - Open the exported PDF on an iPad or in a desktop PDF viewer and click each internal link and bookmark to ensure they work.
   - If you want the PDF to open to the first page without a page thumbnail shown, export without page thumbnails.

8) (Optional) Add GoodNotes custom link types
   - GoodNotes supports internal PDF links and will follow them. If you want a behavior like "open a page in 2 taps", keep links large and visually clear.

What I added to the repository
- All SVG page templates and decorative elements in assets/
- This assembly instructions file (docs/ASSEMBLY_INSTRUCTIONS.md)

Next steps I can take for you (pick any or all):
- Assemble these SVGs into a single hyperlinked PDF and push the exported PDF to exports/ in the repo.
- Convert typography to outlines and export a final PDF to ensure consistent appearance across devices.
- Create multiple size variants (iPad 12.9, iPad 11, A4) from the same source artboards.

If you want me to produce the assembled hyperlinked PDF now, reply "Generate PDF" and I will proceed to assemble and export the GoodNotes-optimized PDF and push it to the scripture-planner-assets branch under exports/.
