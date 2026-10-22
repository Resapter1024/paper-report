# Deliverables, portable style, and synchronization

Read when drafting or changing layout, supplemental depth, or output format. Read the paired style examples before the first draft.

## Usable starter and project layout

Preserve an existing project. For a new project without a mandatory template, copy the contents of [assets/starter](../assets/starter/report-metadata.tex) into the chosen output directory:

    report-metadata.tex
    slides/report.tex
    slides/report-style.sty
    slides/report-cover.tex
    script/script.tex
    script/text-only.tex
    script/guide-style.sty
    script/supplements.tex
    notes/preparation-notes.tex

The starter contains explicitly labeled measurement examples so it compiles immediately; replace those pages and supplements with the actual report. They are not research findings to reuse. Replace title/context/source placeholders from current inputs, keeping presenter empty until the user supplies it.

Compile slides/report.tex first, then the requested guide and notes. Both guide layouts input script/supplements.tex, the single authoritative supplemental body. Do not maintain a second read-aloud manuscript.

The bundle must work with its own relative files and standard TeX packages. No original report folder, institutional logo, proprietary font file, humanizer installation, or external reference deck is required.

## Template precedence and cover

1. A mandatory template requirement overrides bundled geometry or layout.
2. Otherwise use the bundled cover hierarchy, adapting its color and typography to the actual template.
3. Without a supplied template, use the standalone theme and cover. Do not stop to request a reference image.

For a custom theme without a prescribed cover, copy report-cover.tex, load etoolbox, define ReportPresenter from current user input, and input the cover file after the theme. Its standard Beamer fields use the existing title, subtitle, institute, and date. Set the title color explicitly if the supplied theme does not give it sufficient contrast. Do not load the whole bundled theme merely to reuse the cover.

Cover hierarchy:

- A wide rectangular title-color band with centered Chinese title and a smaller English title when available.
- Presenter below the band, then course/report context, then source publication/year or report date.
- Clear whitespace between levels; no decorative cards, slogans, duplicate institutional text, or invented English titles.
- Separate presenter identity from source authorship. ReportPresenter is empty by default and shows a draft placeholder. Source authors can appear in short attribution/footer fields.
- Institution logos or watermarks are optional configured assets, not fixed identities. Optional absent fields leave no empty labeled boxes.

Do not infer a presenter from a source, sample, account, old report, or file owner. Ask for the current report's name/identifier if absent and continue independent work. An unfilled presenter is explicitly pending in the draft handoff.

## Concrete slide defaults

The standalone starting point is 4:3, 11pt, approximately 0.65cm left/right margins, 3pt paragraph spacing, and restrained dark red RGB(151,31,48) on white. The source theme provides top section navigation, a title bar, and compact footer. Keep the chosen template's explicit aspect ratio and mandatory typography.

Chinese text prefers an available Kai-style face with a TeX-distributed Fandol fallback; Latin and mathematics use standard TeX fonts. Do not require one machine's absolute font path.

Use left-aligned text, limited emphasis, and clear spacing between a short colored subheading, explanation, and centered equation. Use columns or tables for meaningful comparisons, not on every page. Orient figures briefly and explain their implication in the supplement.

Prohibit block, alertblock, and exampleblock environments in slide content, even for important theorems. Ordinary text, equations, and restrained bold or theme color are sufficient.

Make titles informative: "共享信息如何改善回归系数估计" identifies the claim being examined. Avoid slogans and writing reminders such as "报告重点" or "本页讲解安排" on content pages. A legitimate outline/navigation page remains allowed.

Resolve density through selection, organization, or pagination before shrinking text. Avoid overlays unless the task requires them. A references display page is optional; traceable citations and source records remain necessary.

Navigation-only pages use no substantive slide number by default. Keep physical PDF pages distinct from displayed numbers.

## Speaker script: actual supplemental speech

The default guide is a slide above a coherent spoken supplement. It adds what the presenter needs to say while using that slide.

Assume listeners have the agreed prerequisites but have not read the source. Do not make them infer source-specific objects, terminology, conditioning, or intermediate steps.

Supplemental coverage is determined by understanding, not by a fixed short word count. Necessary repetition of visible content is welcome when it connects the reasoning. Avoiding duplication must not remove symbol introductions, examples, or logical steps.

Use the page's function to choose what to explain:

| Page type | Explanation needed |
|---|---|
| Motivation | A concrete setting, its difficulty, and why the new idea addresses it |
| Formula/model | What question it answers, objects and terms, relevant conditions, key calculation, and meaning |
| Algorithm | Fixed versus updated quantities, records used, response/predictors/offsets, and purpose of the update |
| Theory | Object, consequential conditions, exact result, and its use in the argument |
| Results | Minimal reading instructions, metric, relevant comparison, connection to the idea, and supported conclusion |
| Empirical design | Variables, design decisions, evidence, and the interpretation they allow |

These are checkpoints, not mandatory five-part paragraphs. Follow the visible order when it helps. Open with the actual conceptual connection and end with the next question when useful, without repetitive stock transitions.

Write the actual explanation. "强调创新", "解释图形", and "这里补充一个例子" are preparation instructions; replace them with the substance or keep them outside the spoken body.

Keep important mathematics complete enough for the intended audience. Use the linked slide for the central formula and add necessary steps beneath it. Put nonessential long proofs and branches in clearly marked backup/preparation notes. A central new topic with no visible context may require revising the slide within the authorized scope.

### Guide layout

The starter uses A4, 12pt, margins 15mm left/right, 12mm top, 14mm bottom, 1.16 line spacing, 7pt paragraph spacing, and a subtle theme-color separator. Directly embed the actual compiled slide PDF to preserve equations and vector text.

Each substantive slide normally begins a new page. Do not force a dense supplement into tiny type to preserve this convention; simplify its delivery, move optional detail to backup, or permit a clearly labeled continuation.

Use the ReportSlide environment in supplements.tex with displayed number, physical PDF page, title, and optional timing label. Keep timings and preparation reminders out of the spoken body.

The text-only root uses the same supplements with 11pt type, bold slide-number labels, and compact readable spacing. It suppresses embedded slides and timing metadata. Avoid orphan labels and awkward splits; preserve mathematical content and wording unless editing is requested.

## Preparation notes and language layers

Slides (report) contain what the audience sees. The speaker script (script) contains the speech that explains and connects those slides. Study notes (notes) develop the concepts, assumptions, derivations, and background needed to understand both; they may also contain source checks, editorial choices, reminders, timing decisions, and optional answers.

Keep these layers distinct using [language-review.md](language-review.md). Preserve true qualifications; avoid inserting each unresolved editorial concern as a generic audience-facing disclaimer.

The notes support the presenter's deeper understanding rather than duplicating the guide or serving only as a task checklist. Include relevant definitions, design choices, alternative explanations, computations, and background. Cross-reference stable slide identities and sources; do not require a model, theorem, or simulation section in every report.

## Mapping, terminology, and timing

Use one authoritative page map with stable identity, displayed number/title, physical slide-PDF page, supplement, source location, and planned time. Existing project metadata is enough; no extra configuration framework is needed.

Maintain terminology across headings, navigation, slide content, supplements, notes, and exports within the edit scope. Protect source titles and unrelated files during replacements.

Count visible content, supplements, navigation, transitions, pauses, and live derivations. Reserve practical slack; around ten percent is an adjustable starting point. Mark optional backup separately.

After structural edits, update mapping, references, timings, and guide embeds. Build the deck first, then dependent exports. Preserve original files for a requested separate-folder export.
