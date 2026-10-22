# Reading and argument mapping

Use this reference while reading source materials, planning/drafting a report, or answering a requested technical question. It is not part of the language-only check mode.

## Establish the source and the presenter's role

Use the actual materials: a published paper, a self-authored research report, a course investigation, a proposal, or a combination. Read the relevant work and its prerequisites before selecting presentation content.

For someone else's paper, distinguish the authors' claims from the presenter's interpretation. For the user's own research, identify their question, decisions, analyses, and findings, while crediting borrowed methods and prior work. Match the speaking voice to this role.

A supplied report establishes scope and intended claims, but does not independently prove every assertion. Trace important results to available equations, proofs, analysis outputs, data descriptions, or primary citations. Mark material gaps without inventing evidence. Do not replace the supplied work with a different study because an expected component is absent.

Record the audience's actual prerequisites. Mathematical maturity does not imply familiarity with the paper's notation or research setting. Explain the objects at their original point of introduction, using the source's own examples when available.

## Narrative and example boundaries

Keep the relative order of the source's sections and the concepts, arguments, examples, formulas, figures, and results selected from them. Shortening a section, splitting a dense page, or merging adjacent material must preserve this order. Only a specific user request authorizes a different sequence. Do not move a later application or construct a new example to manufacture an opening. For several unordered sources, settle the primary source/order from the user's brief before drafting.

For each slide example, identify its actual source location or the user's specific request. Do not create a scenario, substitute convenient numbers, specialize a general parameter (for example, set a general mu to zero), or change a hypothesis merely to make a new teaching example. Mathematical correctness and a “for clarity” label do not authorize such additions. The source's own examples remain usable in their original context, with their conditions intact. Additional learning illustrations can be developed in conversation or notes, clearly labeled, and must not migrate into the talk automatically.

## Build a compact source map

Use the source map to preserve both traceability and narrative order in the presentation. Record the corresponding source location for every substantive slide.

| Field | What to record |
|---|---|
| Question | The specific problem and why it matters in this setting |
| Idea or approach | What the method or research design does and how it addresses the problem |
| Contribution or finding | What is established, relative to which baseline or prior work |
| Objects | Data structure, variables, indices, dimensions, parameters, and relevant populations |
| Conditions | Modeling, identification, sampling, design, or asymptotic assumptions |
| Evidence | Theorem, derivation, simulation, empirical result, or other supporting analysis |
| Source | Exact section, equation, table, figure, or analysis output |
| Limits | Scope of the claim, unresolved issues, and work not yet completed |
| Presentation role | Main slide, oral supplement, backup/preparation note, or omission |

State one central message and a small set of supported contributions or findings. Distinguish a motivating example, an established technique used by the work, and the work's actual contribution. Do not label every component an innovation.

A course report can make a useful argument through a careful design, reproduction, comparison, or interpretation. A proposal can explain a question and a justified plan. Neither requires an invented novelty claim or fabricated results.

## Select evidence to serve the argument

For each candidate section or result, ask what central claim it supports and what the audience needs in order to understand it. Omit material outside the agreed scope while retaining the original order of what remains.

For a method-focused talk:

- Explain how the idea changes modeling, estimation, computation, or inference.
- Keep simulation settings needed to judge the evidence, rather than a full parameter catalog.
- Select results that test the claimed advantage, with relevant comparison conditions and limitations.
- Keep applications brief when they only illustrate use.

For an empirical or self-authored research talk:

- Preserve the research question, design, data, measurement, analysis choices, and findings needed to assess the conclusion.
- Give central empirical evidence adequate time even if there is no new algorithm or theorem.
- Separate observed associations from causal claims, and completed results from expected results.

For a review, represent cited contributions specifically by author, year, method, and supported result when needed. Do not flatten a literature discussion into "many studies have shown."

## Audit equations and technical claims

For each important displayed equation or theoretical statement:

1. State the question it answers and define its symbols, indices, and dimensions.
2. Identify whether it is a definition, assumption, model, estimator, identity, approximation, or limit result.
3. Check conditioning, independence, and what is random, fixed, observed, latent, or estimated.
4. State the assumptions needed for the consequence being explained, including the relevant sample-size regime.
5. Include intermediate reasoning the audience needs. Its length is determined by the argument, not a fixed two- or three-line rule.
6. Explain the conclusion in ordinary language and its role in the next step.

Check distinctions when relevant:

- Optimization convergence versus statistical consistency.
- Pointwise, average, and uniform error; convergence in probability versus bounded stochastic order.
- Error of a combined fitted quantity versus separately identified components.
- Invariance under a change of coordinates versus an oracle comparison with known nuisance quantities.
- Conditions for identification versus conditions for estimation, inference, or missing-data handling.

Use topic-specific checks only when the work needs them. Operator domains, inverse stability, and spectral truncation matter for some functional-data reports; sampling, measurement, and design may matter more for others.

## Audit results and attribution

Define each reported metric and its denominator or averaging operation. Separate false discoveries from missed associations, uncertainty coverage from point-estimation accuracy, and finite-sample results from asymptotic guarantees.

Check what changes jointly in a comparison. Do not attribute an improvement to one dimension when the study varies several, or claim universal superiority from simulations generated under one favorable model.

Separate a supported explanation of a mechanism from a demonstrated causal explanation of a numerical result. Avoid inventing significance, robustness, or practical impact that the source did not establish.

Use primary sources for consequential external claims when available. Record source-version differences when consulting a preprint, appendix, or implementation. Keep interpretations and recommendations identifiable as such.
