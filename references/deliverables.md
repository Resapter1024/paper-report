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

The starter contains neutral layout placeholders so it compiles immediately. Replace them with actual source content under [content integrity and selection](paper-analysis.md#content-integrity-and-selection); placeholders are not proposed teaching examples or a prescribed report structure. Replace title/context/source placeholders from current inputs, keeping presenter empty until the user supplies it.

Compile and finalize slides/report.tex first, including PDF font/mapping checks, then compile the requested guide and notes. Both guide layouts input script/supplements.tex, the single authoritative supplemental body. Do not maintain a second read-aloud manuscript. Follow [PDF compatibility](quality-checks.md#pdf-compatibility) for every requested PDF.

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

## Slides, script, and notes responsibilities

Use [content integrity and selection](paper-analysis.md#content-integrity-and-selection) to decide what may be shortened and what must remain visible. The artifacts serve different purposes:

| Artifact | Responsibility |
|---|---|
| Slides | Present the claims, complete selected formal statements, and source-specific foundations needed to interpret current and subsequent pages. |
| Speaker script | Explain the visible content, the meaning and role of conditions, the reasoning being taught, and the connections between pages. |
| Study notes | Develop deeper background, full proofs, optional branches, preparation decisions, and source verification for the presenter. |

Write and verify the required slide content before relying on the script's explanations. A complete spoken explanation does not repair an incomplete displayed statement, and detailed notes do not establish listener knowledge. Necessary repetition across slides and speech is welcome when it helps the audience follow the argument.

If a complete statement needs several slides, split it into readable, explicitly connected consecutive pages and keep the page map and script aligned. Do not offload its required parts to the script or notes to fit a layout.

## Concrete slide defaults

The standalone starting point is 4:3, 11pt, approximately 0.65cm left/right margins, 3pt paragraph spacing, and restrained dark red RGB(151,31,48) on white. The source theme provides top section navigation, a title bar, and compact footer. Keep the chosen template's explicit aspect ratio and mandatory typography.

Chinese sources must be UTF-8 and use XeLaTeX for this starter. Chinese text prefers an available Kai-style face with a TeX-distributed Fandol fallback; Latin and mathematics use standard TeX fonts. Keep the explicit fontset and editor engine directives. Check that the distribution has ctex, Fandol, and Adobe CMap resources; do not require one machine's absolute font path or assume Windows fonts exist elsewhere.

Use Beamer's centered frame alignment ([c]) so the content group is vertically centered in the available body between the title bar and footer. Keep paragraphs left-aligned, with limited emphasis and clear spacing between a short colored subheading, explanation, and centered equation. Do not use [t] globally, pin sparse content to the top, or reserve a bottom strip for provenance. Use columns or tables for meaningful comparisons, not on every page. Orient figures briefly and explain their implication in the supplement.

Prohibit block, alertblock, and exampleblock environments in slide content, even for important theorems. Ordinary text, equations, and restrained bold or theme color are sufficient.

Use a short noun phrase or verb phrase for each slide title, naming its main object, method, operation, or result category. Examples: “多元纵向数据的观测结构”, “统计目标与分析困难”, “一致性与估计误差速率”, “构造置信区间”. Reject full sentences, questions, and conclusion-like slogans: “持续查看数据，改变了需要控制的事件” becomes “持续监测下的覆盖事件”; “共享信息如何改善回归系数估计” becomes “回归系数的估计误差”. Sentence explanations belong in the body or script. Avoid preparation reminders such as “报告重点” or “本页讲解安排”. Use only the contents-page scheme below for an outline.

Do not generate gray “来源：…” lines, small source strips, per-slide source footers, or helper macros that append them. Put page-specific source locations and detailed provenance in notes. Necessary author attribution, citation beside a borrowed claim, or licensed-figure credit can remain concise and in context; do not convert this into a repeated footer. Keep the existing cover attribution and template metadata separate from these prohibited source strips.

Resolve density through readable pagination or selection under the content-integrity rules before shrinking text. Retained statements and foundations must remain complete and legible. Avoid overlays unless the task requires them. A references display page is optional; traceable source records remain in notes.

### One contents-page scheme

Physical PDF page 1 is the title page and page 2 is the clickable contents page. The first unstarred section must immediately follow the cover in the source: its AtBeginSection hook emits page 2. The same hook emits one contents page at every later main-section opening, showing the same section list and highlighting the current section. Do not insert a second manual tableofcontents frame after the title, or duplicate the first section's contents page.

Use section titles from the actual report and clickable destinations to their section openings. A supplied theme can retain its compact navigation bar, but disable any additional automatic section-title pages or subsection agendas that would duplicate this scheme. Do not add “报告路线”, “本节概览”, hand-written agenda lists, or a miniature contents panel on ordinary content slides. Content comparisons and explanations remain valid when they serve a substantive point rather than restating the report structure.

Navigation-only pages use no substantive slide number by default. Keep physical PDF pages distinct from displayed numbers.

## Speaker script: actual supplemental speech

The default guide is a slide above a coherent spoken supplement. It supplies the actual speech needed to explain that slide under the artifact responsibilities above.

Assume listeners know only the agreed prerequisites and what the report has already introduced. At each page, establish why the current content is needed, how it follows from earlier content, and what it enables next. Explain source-specific objects, terminology, conditioning, and required intermediate reasoning directly.

Supplemental coverage is determined by understanding, not by a fixed short word count. Necessary repetition of visible content is welcome when it connects the reasoning. Avoiding duplication must not remove symbol introductions, examples, or logical steps.

Use the page's function to choose what to explain:

| Page type | Explanation needed |
|---|---|
| Motivation | The source's setting, its difficulty, and the motivation introduced there |
| Formula/model | What question it answers, objects and terms, relevant conditions, key calculation, and meaning |
| Algorithm | Fixed versus updated quantities, records used, response/predictors/offsets, and purpose of the update |
| Theory | Meaning and role of the displayed conditions, interpretation of the complete displayed result, selected proof reasoning, and its use in the argument |
| Results | Minimal reading instructions, metric, relevant comparison, connection to the idea, and supported conclusion |
| Empirical design | Variables, design decisions, evidence, and the interpretation they allow |

These are checkpoints, not mandatory five-part paragraphs. Follow the slide and source sequence. Explain the local conceptual connection and link to the next step without adding a new prelude or repetitive stock transitions.

Write the actual explanation. "强调创新", "解释图形", and "这里补充一个例子" are preparation instructions. Explain the source content itself or keep the reminder outside the spoken body; a reminder to add an example does not authorize inventing one.

Once the slide statement is complete, add the reasoning and interpretation needed for the agreed audience. Put nonessential proof detail and optional branches in clearly marked backup or preparation notes. When a new topic lacks required visible foundations, repair the slides within the authorized scope instead of explaining the omission away in the script.

### Guide layout

The starter uses A4, 12pt, margins 15mm left/right, 12mm top, 14mm bottom, 1.16 line spacing, 7pt paragraph spacing, and a subtle theme-color separator. Directly embed the actual compiled slide PDF to preserve equations and vector text.

Each substantive slide normally begins a new page. Do not force a dense supplement into tiny type to preserve this convention; permit a clearly labeled continuation or shorten genuinely optional explanation under the content-integrity rules.

Use the ReportSlide environment in supplements.tex with displayed number, physical PDF page, title, and optional timing label. Keep timings and preparation reminders out of the spoken body.

The text-only root uses the same supplements with 11pt type, bold slide-number labels, and compact readable spacing. It suppresses embedded slides and timing metadata. Avoid orphan labels and awkward splits; preserve mathematical content and wording unless editing is requested.

## Preparation notes and language layers

Apply the [artifact responsibilities](#slides-script-and-notes-responsibilities) above. Preparation notes may contain source checks, editorial choices, reminders, timing decisions, and optional answers; none substitutes for required audience-facing content.

Keep these layers distinct using [language-review.md](language-review.md). Preserve true qualifications; avoid inserting each unresolved editorial concern as a generic audience-facing disclaimer.

The notes support the presenter's deeper understanding rather than duplicating the guide or serving only as a task checklist. Include relevant definitions, design choices, alternative explanations, computations, and background. Cross-reference stable slide identities and sources; do not require a model, theorem, or simulation section in every report.

## Mapping, terminology, and timing

Use one authoritative page map with stable identity, displayed number/title, physical slide-PDF page, supplement, source location, and planned time. Include the prerequisite and statement-coverage fields from the [source map](paper-analysis.md#build-a-compact-source-map) in that same record. Existing project metadata is enough; no extra configuration framework is needed.

Maintain terminology across headings, navigation, slide content, supplements, notes, and exports within the edit scope. Protect source titles and unrelated files during replacements.

Count visible content, supplements, navigation, transitions, pauses, and live derivations. Reserve practical slack; around ten percent is an adjustable starting point. Mark optional backup separately.

After structural edits, update mapping, references, timings, and guide embeds. Build the deck first, then dependent exports. Preserve original files for a requested separate-folder export.
