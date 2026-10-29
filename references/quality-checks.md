# Verification and handoff

Use this reference for internal acceptance of draft/export artifacts and authorized revisions. For a narrow revision, verify the changed content and affected dependencies without reopening the report's content design. This reference is not the language-only $paper-report check command; that mode uses [language-review.md](language-review.md) exclusively.

## Content acceptance

For drafts and substantive revisions, perform the following two passes in order. [Content integrity and selection](paper-analysis.md#content-integrity-and-selection) is the governing content standard; the script or notes cannot compensate for a failure of the first pass. For a reproduction-only export, verify preservation and synchronization rather than reopening the content design.

### Source-to-slides verification

Compare the actual final slides with the source and source/page map, without using the script as a substitute for displayed content. A connected group of statement pages and explicitly referenced earlier condition pages can be assessed together.

| Check | Acceptance criterion |
|---|---|
| Formal statement coverage | Every required component of each selected formal result is mapped from its full source statement to visible slides; no condition-only result, missing conclusion, or script-only statement component remains. |
| Referenced conditions | Conditions used by a result have their actual requirements, symbols, and ranges displayed before or at first use; later references resolve to those slide locations. |
| Foundations | Each page's required source-specific definitions, setup, and prior results are introduced on slides before or at first use. |
| Mathematical fidelity | The displayed statement preserves the source's domains, quantifiers, restrictions, conditioning, mathematical relations, probability meaning, and conclusions. |
| Source and evidence | Claims are supported and traceable; interpretations, incomplete work, authorship, and borrowed methods are distinguishable. |
| Order and selection | Local expansions follow the source's references; the main narrative and source examples retain their context unless the user specifically requested otherwise. Omissions leave no dangling prerequisite. |

Walk the slides in their final order using only the agreed general prerequisites and material already introduced. For each new required object or condition, check its introduction location. Follow source references and compare statement components individually, not merely theorem headings or assumption counts. An unexplained label, source citation, takeaway sentence, or detailed note is not evidence of a complete displayed statement. Record and resolve source gaps before treating a result as verified.

Reject unfilled starter placeholders in a purported completed report. Verify phrase-form titles, readable mathematical content, and the [slide defaults](deliverables.md#concrete-slide-defaults). Compilation success, extracted text, and keyword matching do not establish scientific completeness.

### Slide-and-speech comprehension

After slide-content acceptance, review each page together with its spoken supplement using only the audience's agreed prerequisites and what the talk has introduced so far.

| Check | Acceptance criterion |
|---|---|
| Purpose and continuity | Speech explains why the page appears here, connects it to preceding content, and prepares the next step without assumed knowledge of the source. |
| Meaning | Source-specific terminology, displayed conditions, and formal conclusions receive an understandable explanation. |
| Reasoning | The argument includes the intermediate reasoning needed for the agreed audience, without conflating a statement, its proof, and its interpretation. |
| Supported takeaway | The explanation states what follows, its scope, and how it advances the central argument. |

Read difficult passages aloud or rehearse them as speech. Replace compressed jargon and editorial directions with the actual explanation. Do not infer understanding from mathematical training alone. Check distinctions appropriate to the work and verify user-suggested mathematical corrections against the source.

Check that the central question and idea remain visible through the talk. Judge the time earned by simulations and applications according to this report's purpose. Use [language-review.md](language-review.md) for the language pass; do not duplicate its audit here.

## Timing

Include time for substantive slides, supplements, navigation, transitions, pauses, and planned board work. Separate optional backup and Q&A from the main-talk estimate.

Check the allocation against what will actually be said. If it is too long, apply [foundations and shortening](paper-analysis.md#foundations-and-shortening) to optional content and update the prerequisite map and estimate. Recheck affected statement coverage and dependency chains. Do not claim a shorter talk by changing timestamps alone.

Leave a practical reserve compatible with the user's limit. Describe the duration as a plan or rehearsal estimate, not a guaranteed speaking time.

## Compile the requested artifacts

Use XeLaTeX for ctex, fontspec, or system-font documents. A typical BibTeX build is:

    XeLaTeX -> BibTeX -> XeLaTeX -> XeLaTeX

Use scripts/build-latex.ps1 when appropriate. It reads UTF-8 sources/logs, rejects a conflicting engine for the starter's XeLaTeX directive, detects BibTeX or Biber in ordinary projects, and completes the final LaTeX passes. Verify the actual bibliography setup rather than assuming every project needs BibTeX. The build helper does not certify PDF compatibility.

Compile the deck before any guide that embeds its PDF. Rebuild dependent exports after relevant source changes. Do not modify a source midway through its build.

Check the final logs for:

- LaTeX errors, undefined control sequences, and emergency stops.
- Undefined citations or references.
- Missing fonts, missing characters/glyphs (including nonfatal “Missing character:” messages), images, themes, or bibliography files.
- Overfull boxes that visibly clip or collide with content.

A pre-existing nonfatal template warning may remain only after its visual impact is checked. Missing glyphs and undefined citations are not harmless template warnings. If the compiler fails, identify the engine, encoding, package, or font error from the first relevant message; do not claim that this compatibility workflow proves an unrelated compilation failure has been fixed.

## PDF compatibility

Apply this to every final requested report, script, notes, and optional text-only PDF. Successful compilation and a single reader's display are insufficient.

1. Use UTF-8 sources and the declared XeLaTeX engine. Use embeddable fonts available in the current environment, with the starter's Fandol fallback rather than an assumed system font. Never force embedding against font licensing restrictions; choose an embeddable alternative.
2. Audit the actual final PDF with pdffonts: fonts must be embedded, and Chinese text must have explicit embedded ToUnicode maps. Font subsetting is acceptable when all used glyphs are present. A font can display using a reader's standard CJK collection while omitting its own ToUnicode map; that does not meet this delivery requirement. Extensible mathematical drawing pieces can lack a textual Unicode counterpart; the helper records unmapped fonts and rejects missing maps for composite text fonts rather than treating every decorative math glyph as a Chinese mapping error. Inspect these recorded fonts during visual/text review.
3. Run scripts/check-pdf.py on the generated PDF. It requires Python with pypdf and PyMuPDF, plus pdffonts, pdftotext, and pdftoppm on PATH. For example:

       python scripts/check-pdf.py <generated.pdf> --output-dir <qa-directory> --embed-cjk-maps

   The optional --embed-cjk-maps flag updates only the specified generated PDF, embedding missing standard Adobe collection maps found through the TeX distribution's kpsewhich. It preserves the pages, links, and bookmarks. Omit this flag for a read-only check or a supplied source PDF. Do not invent identity mappings, copy text from a different font, rasterize Chinese, or outline all text as a substitute for correct embedding. Unsupported missing maps must be fixed through the actual font/driver configuration and checked again.
4. The helper writes fonts.txt, both engines' extracted text, audit.json, and a PNG for every page under poppler/ and mupdf/. Inspect both render sets page by page at readable resolution, checking Chinese titles/body/bold text, equations, punctuation, clipping, and layout. pdftoppm and pdftocairo both use Poppler and do not count as independent engines. Compare extracted Chinese against the source, including titles, numbers, symbols, and changed text; confirm copy/search works. Matching extracted text alone cannot prove visual correctness.
5. Finish the deck's font/mapping processing before embedding it into a script. Rebuild and recheck dependent PDFs after any later deck change. Record the tested PDF, page counts, font/mapping findings, renderer names, and actual visual review. The helper's successful exit only proves its automated checks passed; visual_review_required remains true. Missing tools or unreviewed pages mean verification is incomplete and must be reported at handoff.

## Portable starter checks

When changing bundled assets, copy them into an isolated directory with no original project files. Compile the cover, both content-layout slots, and both guide layouts. Layout placeholders are acceptable for a template smoke test, never as actual research content. Inspect actual PDFs, not only skill/YAML validity.

Check that the presenter remains a visible draft placeholder until supplied, optional metadata can be empty, the cover can be reused with a supplied theme, and alternate aspect ratios do not clip. Test a Chinese path containing spaces. Exercise the Fandol fallback even when KaiTi is installed, and verify the Chinese maps rather than relying on rendering alone. No original author, student number, institutional logo, or original report path may leak into generic metadata.

Both guide roots must consume the same supplement body. Compare page mappings, labels, text preservation, timing suppression in text-only output, and the absence of slide images in that export.

## Render and inspect

Use both complete render sets from the PDF compatibility procedure above, including the cover, contents, body, and any backup. A changed font, map, or imported slide can affect pages outside the directly edited frame.

Verify readable type, no clipping or overlap, usable tables and equations, correct titles and metadata, and adherence to the supplied template. Confirm the contents is physical page 2, appears once at each later section opening, highlights the current section, and links to the correct section destinations. Reject extra agendas, route maps, subsection outlines, and other contents-like panels. Check that ordinary slide bodies are vertically centered and have no gray “来源：…” line or repeated source strip. Check that slide content does not use block, alertblock, or exampleblock.

For the slide-and-supplement guide, verify that each embedded slide is the exact intended compiled page, remains legible, and has the correct supplement beneath it. For a text-only export, check slide-number labels, content preservation, and page breaks.

## Synchronization and edit scope

Use the page map and actual compiled PDFs to verify:

- Displayed slide numbers versus physical PDF pages.
- All substantive slides have the correct supplement; excluded navigation and backup pages are intentional.
- Titles, equations, terminology, notation, and assumptions agree across the linked artifacts.
- Source locations, note references, time allocations, and cumulative times remain correct.
- All requested exports use the current authoritative supplemental content.
- A targeted edit has not unintentionally changed protected content; use source comparisons or rendered comparisons when warranted.

Pay attention to inserted pages, removed sections, automatically split frames, and title/author changes. Keep presenter metadata separate from source attribution.

## Final handoff

Link the requested source files and PDFs. State the numbered slide count and physical PDF page count separately when they differ, the planned main-talk duration and reserve, and any material unresolved issues.

For an explanation-only request, answer the question; do not claim to have changed or compiled files. For a revised artifact, report the changes and checks actually completed. Preserve original files when the user requested a separate export.
