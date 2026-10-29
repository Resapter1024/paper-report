---
name: paper-report
description: Plan, draft, polish, run a language-only check, export, or prepare audience questions for an academic presentation from a paper, self-authored report, or course materials. Includes a portable Beamer style, planning questions, paired slide-and-speech examples, speaker scripts, and study notes.
---

# Paper and Research Report

Prepare a presentation the audience can understand without reading its source. A full package has report (slides for display), script (a slide-aligned speaker script, 讲稿), and notes (study notes developing the concepts and reasoning behind both). The guide replaces a separate read-aloud manuscript. For a narrow request, produce only the requested work.

Use drafting, revision, and rehearsal to help the presenter learn the material and deepen their understanding. Deliver a usable, checked draft, then refine report and script through the user's questions and practice; do not promise a flawless finished talk in one generation.

## Task entry points

Recognize these as task arguments, or infer the same intent from ordinary language. They do not require a separate command plugin.

| Invocation | Work and required reading |
|---|---|
| $paper-report plan | Resolve audience, purpose, knowledge, scope, and timing; propose a source-ordered outline with the prerequisites needed for its retained content. Read [report-dialogue.md](references/report-dialogue.md) and [paper-analysis.md](references/paper-analysis.md). |
| $paper-report draft | Read [paper-analysis.md](references/paper-analysis.md), including its content-integrity rules, even when planning is already settled. Write the requested artifacts using [deliverables.md](references/deliverables.md) and the existing style excerpts in [style-examples.md](references/style-examples.md). Apply [language-review.md](references/language-review.md) and [quality-checks.md](references/quality-checks.md) before handoff. |
| $paper-report polish | Revise the requested language, unnecessary defensive statements, and mixing of visible content, speech, and preparation instructions. Read [language-review.md](references/language-review.md), consult relevant style pairs, and preserve technical content. |
| $paper-report check | Read-only language audit: AI-like phrasing, unnecessary defensive statements, preparation/chat language leaking into the talk, and related wording/style issues. Read only [language-review.md](references/language-review.md); report quoted passages and wording suggestions by page. Do not review content selection, argument/slide order, technical correctness, layout, timing, or PDF compatibility. |
| $paper-report export | Generate requested layouts from the authoritative supplemental content. Read the format and synchronization sections of [deliverables.md](references/deliverables.md). |
| $paper-report questions | Generate likely audience questions from the current slides and speaker script, with slide locations and reasons. Read [audience-questions.md](references/audience-questions.md). |

Without an argument, infer the task. For a new report with consequential unknowns, begin with planning. For an authorized draft or targeted revision with a settled brief, continue without reopening every planning question.

Dispatch check and questions directly to their own references and stop after that task. They do not trigger the full drafting/verification workflow below. The task words are modes of this one skill, not separately installed skills or terminal commands.

## Essential rules

- Identify paper explanation, the user's own research, course investigation, or proposal. Do not force a published-paper structure or novelty claim onto every report.
- Follow [content integrity and selection](references/paper-analysis.md#content-integrity-and-selection) for all content decisions. Equivalent wording, explanation depth, and pagination are adjustable; mathematical meaning and prerequisites of retained material are protected. Complete statements of selected formal results belong on slides, not only in the script or notes.
- Preserve the source's main narrative order. Expand referenced definitions and conditions where first needed, including those stated elsewhere in the source; this explains the current argument without relocating later arguments or creating a new opening. Reordering the main argument requires a specific user request.
- Use the source's own examples in their original context. Do not invent a motivating scenario, toy example, data, or special parameter case for the slides or paired script unless the user specifically requests it. Style samples and template placeholders do not grant that permission. Keep extra learning illustrations in conversation/notes and label their origin.
- Use a noun phrase or verb phrase naming each slide's main object or operation as its title. Do not use full sentences, questions, or conclusion-like slogans as titles.
- Select depth by the report's purpose: keep supporting simulations and applications brief in a method-focused talk, and preserve central design and findings in empirical work. Apply the content-integrity rules when shortening either.
- Assume only the agreed prerequisites and what earlier slides and speech have introduced. Do not assume familiarity with the source's notation, conditions, definitions, or argument; establish foundations before dependent content.
- Use an explicitly required template. Otherwise use the bundled successful layout; no external reference deck is required. Prohibit block, alertblock, and exampleblock environments in slide content.
- Put the clickable contents page on physical PDF page 2, immediately after the cover, and reuse that same section list at each later section opening with the current section highlighted. Use one automatic section hook; do not add separate agendas, roadmaps, section summaries, or other contents-like panels/pages.
- Center the content group vertically within the slide body, keeping paragraphs left-aligned. Do not add gray “来源：…” lines, source strips, or repeated source footers. Keep detailed provenance in notes; retain necessary attribution in context rather than appending it to every slide.
- Obtain the presenter from the user for this report. Keep an empty field or a visible draft placeholder until supplied; never copy identity from a sample, source author, account, or old project. Other work can proceed while this field is pending.
- Keep audience-facing content, actual spoken supplements, and preparation instructions distinct. Place editorial reminders and audit findings in preparation material or the review response.
- Preserve attribution and important qualifications. Replace unnecessary defensive disclaimers with precise scoped statements; do not erase real limits or unfinished work.
- Maintain enough explanation to be understood. Avoiding repetition or AI-like prose is not permission to turn the guide into a terse outline.

## Workflow

### 1. Understand and plan

Inspect the available materials, template, prior answers, and assignment requirements. Ask at most two or three consequential unresolved questions per round, with useful options and a recommendation. Do not ask the user to do the source analysis.

Record what the audience already knows, what needs introduction, and what the report should enable them to understand. Include whether the time limit covers Q&A and board work.

Read the relevant source in full, following references to the definitions and conditions used by retained results. Record complete statements and prerequisite locations in the existing source/page map. Verify consequential equations, figures, and tables in their rendered form. For self-authored reports, distinguish completed, preliminary, reproduced, and planned analyses.

Propose a central message, supported contributions or findings, a source-ordered timed outline, and explicit omissions or backup. Check that omissions leave no retained result without its foundations. Resolve materially open choices; proceed when the direction is already determined.

### 2. Start from the usable assets

For a new project without an overriding template, copy the contents of [assets/starter](assets/starter/report-metadata.tex) into the output project. The bundle contains a standalone Beamer theme and cover, both guide layouts using one supplement source, and a preparation-note starter.

Fill report metadata from current inputs. Optional English title, source attribution, course information, and background image remain optional. Keep institution branding separate from layout. Never depend on the original longitudinal-data report's path.

When a supplied template fixes the cover, use it. Otherwise adapt [report-cover.tex](assets/starter/slides/report-cover.tex) to retain the bundled title hierarchy without replacing the rest of the user's theme. Detailed precedence and copy instructions are in deliverables.md.

### 3. Write the slides and speaker script together

Follow the [artifact responsibilities](references/deliverables.md#slides-script-and-notes-responsibilities). Write complete visible statements and required foundations on slides first, then write the speech that explains and connects them. The style excerpts guide expression, not the permitted completeness of a new slide sequence.

For each page, check what the audience has learned so far, explain the current objects and reasoning, and connect to the next step. Choose explanatory depth by page type; the script must not compensate for a missing formal statement on the slide.

Keep one page map distinguishing displayed numbers from physical PDF pages. Maintain one authoritative supplement source for the comparison and text-only guides. Mark optional backup outside the main talk.

### 4. Review language and revise within scope

Apply the language-review process after a new draft and during polish. Use the installed humanizer skill when available, adapted to Chinese oral presentation and speaker identity; the bundled rules remain sufficient when it is unavailable.

Read the slide, supplement, relevant note, and source before answering a conceptual page question. Verify suggested mathematical corrections. A request for explanation is not automatically a request to edit files.

For authorized edits, preserve unaffected content and review boundaries. Update affected terminology, maps, timings, cross-references, and embedded slides. Do not insert every technical concern as an audience-facing disclaimer.

### 5. Verify and deliver

Apply the source-to-slides content acceptance checks before the combined slide-and-speech review. Reserve time for transitions, explanations, board work, and navigation; if over budget, reduce optional content under the selection rules. Compile with XeLaTeX for the bundled Chinese templates. Finalize the slides before compiling dependent guides.

Use [scripts/build-latex.ps1](scripts/build-latex.ps1) when appropriate. PDF delivery requires embedded fonts and explicit Chinese ToUnicode mappings, plus rendering and visual review of every page with Poppler and an independent engine such as MuPDF; a clean compilation log is insufficient. Use [scripts/check-pdf.py](scripts/check-pdf.py) and follow [PDF compatibility](references/quality-checks.md#pdf-compatibility) for font audits, mapping completion, and both render sets. If a tool is unavailable, report the incomplete verification instead of claiming compatibility.

Preserve the user's paths and files. Preparation questions should follow from the final talk and audience rather than a generic examination.

Link requested sources and PDFs. State numbered slides separately from physical PDF pages when they differ, planned timing and reserve, and material pending inputs or limitations. Presenter placeholders identify a draft; do not call identity metadata complete until the user supplies it.
