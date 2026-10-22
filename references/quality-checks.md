# Verification and handoff

Use this reference after structural changes and before delivering the requested report artifacts. For a narrow revision, focus checks on the changed content and affected dependencies.

For check, report findings without modifying files. For draft or polish, complete the relevant checks after the scoped edits. Use [language-review.md](language-review.md) for language classification and repair.

## Content and audience comprehension

Review each substantive page together with its spoken supplement, using only the audience's agreed prerequisites and what the talk has introduced so far.

| Check | Acceptance criterion |
|---|---|
| Purpose | The audience can understand why this page appears here. |
| Objects | Important symbols, indices, variables, and metrics have been introduced. |
| Reasoning | Necessary assumptions and intermediate steps are available in the slide or supplement. |
| Conclusion | The explanation states what follows and how it advances the argument. |
| Continuity | The next page does not depend on unexplained source-specific context. |
| Evidence | Claims are supported, with interpretation and incomplete work identifiable. |
| Attribution | The presenter's work, source authors' work, and borrowed methods remain distinct. |

Read difficult passages aloud or rehearse them as speech. Replace compressed phrases, unexplained jargon, and editorial directions with the actual explanation. Do not assume a mathematically trained listener has already inferred the paper's argument.

Check that the report's central question and idea or approach remain visible through the outline and conclusion. Simulations and applications should earn their time through their role in the argument. For an empirical report, do not remove central design or result content merely because applications were short in a previous methods talk.

Check consequential distinctions appropriate to the work: conditioning levels, identified objects, average versus uniform statements, optimization versus statistical convergence, and observed evidence versus causal or general claims. Verify user-suggested corrections against the source.

Check that visible claims, actual speech, and preparation instructions remain in their proper layers. Review generic defensive sentences in context; retain necessary assumptions and limits. Verify that polishing has preserved examples, intermediate steps, and natural transitions.

## Timing

Include time for substantive slides, supplements, navigation, transitions, pauses, and planned board work. Separate optional backup and Q&A from the main-talk estimate.

Check the allocation against what will actually be said. If it is too long, identify the content to shorten, omit, or move to backup, then revise the estimate. Do not claim a shorter talk by changing timestamps alone.

Leave a practical reserve compatible with the user's limit. Describe the duration as a plan or rehearsal estimate, not a guaranteed speaking time.

## Compile the requested artifacts

Use XeLaTeX for ctex, fontspec, or system-font documents. A typical BibTeX build is:

    XeLaTeX -> BibTeX -> XeLaTeX -> XeLaTeX

Use scripts/build-latex.ps1 when appropriate. It detects BibTeX or Biber in ordinary projects and completes the final LaTeX passes. Verify the actual bibliography setup rather than assuming every project needs BibTeX.

Compile the deck before any guide that embeds its PDF. Rebuild dependent exports after relevant source changes. Do not modify a source midway through its build.

Check the final logs for:

- LaTeX errors, undefined control sequences, and emergency stops.
- Undefined citations or references.
- Missing fonts, images, themes, or bibliography files.
- Overfull boxes that visibly clip or collide with content.

A pre-existing nonfatal template warning may remain only after its visual impact is checked. Undefined citations are not a harmless template warning.

## Portable starter checks

When changing bundled assets, copy them into an isolated directory with no original project files. Compile a cover, a formula page, a result page, and both guide layouts using only the bundle and new source material. Inspect actual PDFs, not only skill/YAML validity.

Check that the presenter remains a visible draft placeholder until supplied, optional metadata can be empty, the cover can be reused with a supplied theme, and alternate aspect ratios do not clip. Use configured standard fonts or their documented fallback. No original author, student number, institutional logo, or original report path may leak into generic metadata.

Both guide roots must consume the same supplement body. Compare page mappings, labels, text preservation, timing suppression in text-only output, and the absence of slide images in that export. Starter examples are layout demonstrations, never evidence about a new study.

## Render and inspect

Render the slide PDF. For a new deck, inspect every substantive frame and section transition. For later revisions, inspect changed frames, neighboring frames, and affected transitions or numbering.

Verify readable type, no clipping or overlap, usable tables and equations, correct titles and metadata, consistent navigation, and adherence to the supplied template. Check that slide content does not use block, alertblock, or exampleblock.

Render the speaker script and preparation notes as well. Review the page sequence and inspect dense pages, equations, boundaries, and changed content at readable scale.

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

## Final rehearsal and questions

Use this section for $paper-report questions, natural-language requests for likely audience questions, and requested Q&A rehearsal. Work from the current slides and actual speaker script, including an unfinished draft when that is what the user supplies. Inspect existing project files before requesting them. If only one artifact is available, use it and state the coverage; if neither is available, request the presentation materials rather than inventing a talk from the paper.

Use the audience background already agreed for the report. When unspecified, assume classmates who have heard the talk but have not read the source and do not have deep knowledge of the paper or related field. Do not restart planning for an otherwise self-contained questions request.

Follow the presentation's sequence and identify questions prompted by a visible claim, example, equation, figure, or spoken explanation. Questions may connect several pages or return to an earlier claim; never require the listener to know a result, appendix, or specialist term available only in the source or study notes. The source may be consulted to verify an answer, but must not supply assumed listener knowledge.

Prioritize plausible questions about meaning, motivation, assumptions, how a procedure works, interpreting evidence, or applying a stated result. A skeptical follow-up is appropriate when the talk itself invites it. Avoid a generic examination, leading questions that advertise the method, and forced technical objections. Explain an unfamiliar object in ordinary language within a question when needed; do not manufacture questions by pretending a clear explanation was absent.

By default, return a concise numbered list of questions in the conversation. For each, include the displayed slide number/title (or a clearly labeled physical PDF page when no slide mapping is available) and a brief reason tied to what the listener saw or heard. Select the number and depth to suit the talk, covering likely points of confusion and substantive follow-ups without padding. Do not provide answers unless requested. Do not edit slides or scripts, or save a separate question file, unless the user asks.

When answers are requested, give a short oral answer first, then optional technical detail and relevant limits. Verify consequential answers against the available source or analysis, distinguish supported conclusions from conjecture, and use accessible language. Save Q&A in notes when requested; do not automatically insert it into the talk.

## Final handoff

Link the requested source files and PDFs. State the numbered slide count and physical PDF page count separately when they differ, the planned main-talk duration and reserve, and any material unresolved issues.

For an explanation-only request, answer the question; do not claim to have changed or compiled files. For a revised artifact, report the changes and checks actually completed. Preserve original files when the user requested a separate export.
