---
name: paper-report
description: Plan, draft, polish, check, export, or prepare audience questions for an academic presentation from a research paper, self-authored report, or course materials. Includes a portable Beamer style, focused planning questions, paired slide-and-speech examples, supplemental speaker scripts, and research-aware language review.
---

# Paper and Research Report

Prepare a presentation the audience can understand without reading its source. A full package has report (slides for display), script (a slide-aligned speaker script, 讲稿), and notes (study notes developing the concepts and reasoning behind both). The guide replaces a separate read-aloud manuscript. For a narrow request, produce only the requested work.

Use drafting, revision, and rehearsal to help the presenter learn the material and deepen their understanding. Deliver a usable, checked draft, then refine report and script through the user's questions and practice; do not promise a flawless finished talk in one generation.

## Task entry points

Recognize these as task arguments, or infer the same intent from ordinary language. They do not require a separate command plugin.

| Invocation | Work and required reading |
|---|---|
| $paper-report plan | Resolve audience, purpose, knowledge, scope, and timing; propose a source-informed outline. Read [report-dialogue.md](references/report-dialogue.md) and [paper-analysis.md](references/paper-analysis.md). |
| $paper-report draft | Write the requested artifacts from the materials and settled direction. Read [deliverables.md](references/deliverables.md), all four short pairs in [style-examples.md](references/style-examples.md), then use [language-review.md](references/language-review.md) and [quality-checks.md](references/quality-checks.md) before handoff. |
| $paper-report polish | Revise the requested language, unnecessary defensive statements, and mixing of visible content, speech, and preparation instructions. Read [language-review.md](references/language-review.md), consult relevant style pairs, and preserve technical content. |
| $paper-report check | Inspect without changing report files. Read the applicable language and quality checks; report concrete page locations and proposed corrections. |
| $paper-report export | Generate requested layouts from the authoritative supplemental content. Read the format and synchronization sections of [deliverables.md](references/deliverables.md). |
| $paper-report questions | Generate likely audience questions from the current slides and speaker script, with slide locations and reasons. Read [Final rehearsal and questions](references/quality-checks.md#final-rehearsal-and-questions). Do not assume listeners have read the source or have deep subject knowledge; provide answers only when requested. |

Without an argument, infer the task. For a new report with consequential unknowns, begin with planning. For an authorized draft or targeted revision with a settled brief, continue without reopening every planning question.

## Essential rules

- Identify paper explanation, the user's own research, course investigation, or proposal. Do not force a published-paper structure or novelty claim onto every report.
- Organize around the question, idea or research approach, supported contribution or finding, and evidence. The source's section order is a reading map, not a mandatory talk outline.
- For a method-focused talk, shorten simulations and applications to their role in the argument. For empirical work, preserve central design and findings.
- Assume the agreed prerequisites and no reading of the source. Explain new objects, consequential assumptions, intermediate steps, and conclusions.
- Use an explicitly required template. Otherwise use the bundled successful layout; no external reference deck is required. Prohibit block, alertblock, and exampleblock environments in slide content.
- Obtain the presenter from the user for this report. Keep an empty field or a visible draft placeholder until supplied; never copy identity from a sample, source author, account, or old project. Other work can proceed while this field is pending.
- Keep audience-facing content, actual spoken supplements, and preparation instructions distinct. Place editorial reminders and audit findings in preparation material or the review response.
- Preserve attribution and important qualifications. Replace unnecessary defensive disclaimers with precise scoped statements; do not erase real limits or unfinished work.
- Maintain enough explanation to be understood. Avoiding repetition or AI-like prose is not permission to turn the guide into a terse outline.

## Workflow

### 1. Understand and plan

Inspect the available materials, template, prior answers, and assignment requirements. Ask at most two or three consequential unresolved questions per round, with useful options and a recommendation. Do not ask the user to do the source analysis.

Record what the audience already knows, what needs introduction, and what the report should enable them to understand. Include whether the time limit covers Q&A and board work.

Read the relevant source in full and enough prerequisites to establish the objects and evidence. Verify consequential equations, figures, and tables in their rendered form. For self-authored reports, distinguish completed, preliminary, reproduced, and planned analyses.

Propose a central message, supported contributions or findings, a timed outline, and explicit omissions or backup. Offer alternatives only for meaningful tradeoffs. Resolve materially open choices; proceed when the direction is already determined.

### 2. Start from the usable assets

For a new project without an overriding template, copy the contents of [assets/starter](assets/starter/report-metadata.tex) into the output project. The bundle contains a standalone Beamer theme and cover, both guide layouts using one supplement source, and a preparation-note starter.

Fill report metadata from current inputs. Optional English title, source attribution, course information, and background image remain optional. Keep institution branding separate from layout. Never depend on the original longitudinal-data report's path.

When a supplied template fixes the cover, use it. Otherwise adapt [report-cover.tex](assets/starter/slides/report-cover.tex) to retain the bundled title hierarchy without replacing the rest of the user's theme. Detailed precedence and copy instructions are in deliverables.md.

### 3. Write the slides and speaker script together

Read the paired examples before the first draft. Slides supply visible claims, figures, and key formulas; the guide supplies the actual explanation needed to connect them. Reintroduce visible information when this helps listeners follow the argument.

For each page, establish its purpose, explain the needed reasoning, state what follows, and connect to the next page. Use concrete examples with defined symbols. Choose depth by page type rather than applying one fixed paragraph pattern.

Keep one page map distinguishing displayed numbers from physical PDF pages. Maintain one authoritative supplement source for the comparison and text-only guides. Mark optional backup outside the main talk.

### 4. Review language and revise within scope

Apply the language-review process after a new draft and during polish. Use the installed humanizer skill when available, adapted to Chinese oral presentation and speaker identity; the bundled rules remain sufficient when it is unavailable.

Read the slide, supplement, relevant note, and source before answering a conceptual page question. Verify suggested mathematical corrections. A request for explanation is not automatically a request to edit files.

For authorized edits, preserve unaffected content and review boundaries. Update affected terminology, maps, timings, cross-references, and embedded slides. Do not insert every technical concern as an audience-facing disclaimer.

### 5. Verify and deliver

Reserve time for transitions, explanations, board work, and navigation. Reduce actual content if over budget. Read the quality checks, compile the slides before dependent guides, and render the requested outputs.

Use [scripts/build-latex.ps1](scripts/build-latex.ps1) when appropriate. Preserve the user's paths and files. Preparation questions should follow from the final talk and audience rather than a generic examination.

Link requested sources and PDFs. State numbered slides separately from physical PDF pages when they differ, planned timing and reserve, and material pending inputs or limitations. Presenter placeholders identify a draft; do not call identity metadata complete until the user supplies it.
