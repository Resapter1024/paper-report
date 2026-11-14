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

The starter contains neutral layout placeholders so it compiles immediately. Replace them with actual source content under [content integrity and selection](paper-analysis.md#content-integrity-and-selection); placeholders are not proposed teaching examples or a prescribed report structure. Replace title/context/source placeholders from current inputs, keeping presenter empty until the user supplies it.

Compile and finalize slides/report.tex first, including PDF font/mapping checks, then compile the requested guide layout. Both guide layouts input script/supplements.tex, the single authoritative supplemental body. Do not maintain a second read-aloud manuscript or generate a separate learning document. Follow [PDF compatibility](quality-checks.md#pdf-compatibility) for every requested PDF.

The bundle must work with its own relative files and standard TeX packages. No original report folder, institutional logo, proprietary font file, humanizer installation, or external reference deck is required.

## Template precedence and cover

1. A mandatory template requirement overrides bundled geometry or layout.
2. Otherwise use the bundled cover hierarchy, adapting its color and typography to the actual template.
3. Without a supplied template, use the standalone theme and cover. Do not stop to request a reference image.

For a custom theme without a prescribed cover, copy report-cover.tex, load etoolbox, define ReportPresenter from current user input, and input the cover file after the theme. Its standard Beamer fields use the existing title, subtitle, institute, and date. Define ReportSourceAuthors and ReportSourceLine for source authors and publication/year; use the Beamer date field for the presentation date. Set the title color explicitly if the supplied theme does not give it sufficient contrast. Do not load the whole bundled theme merely to reuse the cover.

Cover hierarchy:

- A wide rectangular title-color band with centered Chinese title and a smaller English title when available.
- Immediately below the title band, put source authors and journal/publication (including publication year when supplied) on one centered line. Below that, place presenter, report context, and report date on separate centered lines, in that order.
- Show only the values: omit labels such as “汇报人”“汇报场合”“汇报日期”. Use the same font size for report context and report date. Keep source publication/year distinct from the actual presentation date.
- When revising an existing cover, preserve the title-band content unless the user explicitly requests changes. Before compiling, ask for materially missing report context/date; never substitute today’s date or a publication year for the presentation date. Follow the user’s requested date format (for example, YYYY.MM.DD).
- Clear whitespace between levels; no decorative cards, slogans, duplicate institutional text, or invented English titles.
- Separate presenter identity from source authorship. ReportPresenter is empty by default and shows a draft placeholder. Source authors belong to the attribution line below the title band.
- Institution logos or watermarks are optional configured assets, not fixed identities. Optional absent fields leave no empty labeled boxes.

Do not infer a presenter from a source, sample, account, old report, or file owner. Ask for the current report's name/identifier if absent and continue independent work. An unfilled presenter is explicitly pending in the draft handoff.

## Slides and script responsibilities

Use [content integrity and selection](paper-analysis.md#content-integrity-and-selection) to decide what may be shortened and what must remain visible. The artifacts serve different purposes:

| Artifact | Responsibility |
|---|---|
| Slides | Present the claims, complete selected formal statements, and source-specific foundations needed to interpret current and subsequent pages. |
| Speaker script | Explain the visible content, the meaning and role of conditions, the reasoning being taught, and the connections between pages. |

Write and verify the required slide content before relying on the script's explanations. A complete spoken explanation does not repair an incomplete displayed statement, and private preparation does not establish listener knowledge. Necessary repetition across slides and speech is welcome when it helps the audience follow the argument.

If a complete statement needs several slides, split it into readable, explicitly connected consecutive pages and keep the page map and script aligned. Do not offload its required parts to the script or conversation to fit a layout.

## Section grouping

When a report contains both simulations and empirical applications, place them together in one main section, “模拟与实证”, retaining their source order. Put “结论” in its own final main section instead of merging it with the empirical application. If only one evidence type is present, name that section accordingly; do not add missing material. Use the same automatic contents hook for these sections. When regrouping an existing deck, synchronize physical page mappings, embedded slides, guide references, notes, and timing checkpoints. Current explicit user requirements override this default.

## Concrete slide defaults

The standalone starting point is 4:3, 11pt, approximately 0.65cm left/right margins, 3pt paragraph spacing, and restrained dark red RGB(151,31,48) on white. The source theme provides top section navigation, a title bar, and compact footer. Keep the chosen template's explicit aspect ratio and mandatory typography.

Chinese sources must be UTF-8 and use XeLaTeX for this starter. Chinese text prefers an available Kai-style face with a TeX-distributed Fandol fallback; Latin and mathematics use standard TeX fonts. Keep the explicit fontset and editor engine directives. Check that the distribution has ctex, Fandol, and Adobe CMap resources; do not require one machine's absolute font path or assume Windows fonts exist elsewhere.

Use Beamer's centered frame alignment ([c]) so the content group is vertically centered in the available body between the title bar and footer. Keep paragraphs left-aligned, with limited emphasis and clear spacing between a short colored subheading, explanation, and a displayed equation. Mathematical displays may be centered; a numerical example followed by a prose interpretation should align both lines to the body left edge. Do not use [t] globally, pin sparse content to the top, or reserve a bottom strip for provenance. Use columns or tables for meaningful comparisons, not on every page. Orient figures briefly and explain their implication in the supplement.

Prohibit block, alertblock, and exampleblock environments in slide content, even for important theorems. Ordinary text, equations, and restrained bold or theme color are sufficient.

Use a short noun phrase or verb phrase for each slide title, naming its main object, method, operation, or result category. Examples: “纵向观测结构”, “统计目标”, “估计误差速率”, “构造置信区间”. Apply the [Chinese heading and formal-label conventions](language-review.md#chinese-wording-and-reference-defaults). Reject full sentences, questions, and conclusion-like slogans: “持续查看数据，改变了需要控制的事件” becomes “持续监测下的覆盖事件”; “共享信息如何改善回归系数估计” becomes “回归系数的估计误差”. Sentence explanations belong in the body or script. Avoid preparation reminders such as “报告重点” or “本页讲解安排”. Use only the contents-page scheme below for an outline.

Do not generate gray “来源：…” lines, small source strips, per-slide source footers, or helper macros that append them. Put page-specific source locations and detailed provenance in the source/page map. Necessary author attribution, citation beside a borrowed claim, or licensed-figure credit can remain concise and in context; do not convert this into a repeated footer. Keep the existing cover attribution and template metadata separate from these prohibited source strips.

Resolve density through readable pagination or selection under the content-integrity rules before shrinking text. Retained statements and foundations must remain complete and legible. Avoid overlays unless the task requires them. A references display page is optional; traceable source records remain in the source/page map.

### Figures, tables, and captions

Center a standalone table horizontally within the slide body, including a table followed by several explanatory lines. For a table inside a column, center it within that column. Keep the surrounding substantive explanations left-aligned.

Place figure/table captions close to the corresponding visual, usually immediately below it, in a smaller readable font. Center the caption on the visual or visual group, not on an unrelated text column or the entire page when the visual occupies only part of it. Give a multi-line caption a bounded width associated with its visual. Treat legends, sample-size notes, and similar reading aids as captions; keep findings, numerical examples, and interpretation in the normal body text. A numerical-change line followed by its explanation should share the body left edge even when the figure above is centered.

Use layout according to the material: enlarge a small plot when it is the main visual, align comparable panels and their plot areas, and use a clear gap and top alignment for a figure beside a table. Account for different crop margins before adjusting panel spacing. Preserve original aspect ratios, axes, data, and vector quality where available. Balance the whole content group so titles, captions, conclusions, and footers have breathing room; do not fix crowding by shrinking everything or stretching a plot. Update positional figure references after moving a visual or its caption.

In Beamer, keep centering local to the visual/caption group and restore left alignment for body paragraphs. Closing a center environment before the caption can introduce an unwanted gap and lose the caption's alignment. The default display-math environment centers its contents even after raggedright; use an appropriate left-aligned mathematical or text container for a numerical example. Avoid beginning the frame body with a bare brace group that Beamer can interpret as an optional subtitle; an ignored subtitle template can otherwise hide the group's contents. Verify the rendered result.

### One contents-page scheme

Physical PDF page 1 is the title page and page 2 is the clickable contents page. The first unstarred section must immediately follow the cover in the source: its AtBeginSection hook emits page 2. The same hook emits one contents page at every later main-section opening, showing the same section list and highlighting the current section. Do not insert a second manual tableofcontents frame after the title, or duplicate the first section's contents page.

Use section titles from the actual report and clickable destinations to their section openings. A supplied theme can retain its compact navigation bar, but disable any additional automatic section-title pages or subsection agendas that would duplicate this scheme. Do not add “报告路线”, “本节概览”, hand-written agenda lists, or a miniature contents panel on ordinary content slides. Content comparisons and explanations remain valid when they serve a substantive point rather than restating the report structure.

Navigation-only pages use no substantive slide number by default. Keep physical PDF pages distinct from displayed numbers.

## Speaker script: actual supplemental speech

The default guide is a slide above a coherent spoken supplement. It supplies the actual speech needed to explain that slide under the artifact responsibilities above. Follow the [mathematical notation rule](language-review.md#mathematical-notation) for written symbols.

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

Once the slide statement is complete, add the reasoning and interpretation needed for the agreed audience. Omit nonessential proof detail from the main talk or retain it in explicitly selected backup slides; discuss deeper questions in conversation when asked. When a new topic lacks required visible foundations, repair the slides within the authorized scope instead of explaining the omission away in the script.

### Guide layout

The starter uses A4, 12pt, margins 15mm left/right, 12mm top, 14mm bottom, 1.16 line spacing, 7pt paragraph spacing, and a subtle theme-color separator. Directly embed the actual compiled slide PDF to preserve equations and vector text.

Each substantive slide normally begins a new page. Do not force a dense supplement into tiny type to preserve this convention; permit a clearly labeled continuation or shorten genuinely optional explanation under the content-integrity rules.

Use the ReportSlide environment in supplements.tex with displayed number, physical PDF page, title, and optional timing label. Keep timings and preparation reminders out of the spoken body.

The text-only root uses the same supplements with 11pt type, bold slide-number labels, and compact readable spacing. It suppresses embedded slides and timing metadata. Avoid orphan labels and awkward splits; preserve mathematical content and wording unless editing is requested.

## Work records and language layers

Apply the [artifact responsibilities](#slides-and-script-responsibilities) above. Keep source verification, settled decisions, and timing metadata in the existing source/page map or brief conversation records. These support production and continuity; do not expand them into a separate study guide or automatically saved Q&A document.

Use [learning through dialogue](report-dialogue.md#learning-through-dialogue) for conceptual explanations and derivations. Save selected discussion content only when explicitly requested. Preserve users' existing supplementary files; removing a default output does not authorize deleting their work.

Keep audience-facing text, speech, and editorial records distinct using [language-review.md](language-review.md). Preserve true qualifications; avoid inserting each unresolved editorial concern as a generic audience-facing disclaimer.

## Mapping, terminology, and timing

Use one authoritative page map with stable identity, displayed number/title, physical slide-PDF page, supplement, source location, and planned time. Include the prerequisite and statement-coverage fields from the [source map](paper-analysis.md#build-a-compact-source-map) in that same record. Existing project metadata is enough; no extra configuration framework is needed.

Maintain terminology across headings, navigation, slide content, supplements, and exports within the edit scope. Protect source titles and unrelated files during replacements.

Count visible content, supplements, navigation, transitions, pauses, and live derivations. Reserve practical slack; around ten percent is an adjustable starting point. Mark optional backup separately.

After structural edits, update mapping, references, timings, and guide embeds. Build the deck first, then dependent exports. Preserve original files for a requested separate-folder export.
