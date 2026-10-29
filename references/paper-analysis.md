# Reading and argument mapping

Use this reference while reading source materials, planning/drafting a report, or answering a requested technical question. It is not part of the language-only check mode.

## Establish the source and the presenter's role

Use the actual materials: a published paper, a self-authored research report, a course investigation, a proposal, or a combination. Read the relevant work and its prerequisites before selecting presentation content.

For someone else's paper, distinguish the authors' claims from the presenter's interpretation. For the user's own research, identify their question, decisions, analyses, and findings, while crediting borrowed methods and prior work. Match the speaking voice to this role.

A supplied report establishes scope and intended claims, but does not independently prove every assertion. Trace important results to available equations, proofs, analysis outputs, data descriptions, or primary citations. Mark material gaps without inventing evidence. Do not replace the supplied work with a different study because an expected component is absent.

Record the audience's actual prerequisites. Mathematical maturity does not imply familiarity with the source's notation, conditions, definitions, or research setting. The audience's available knowledge consists of the agreed prerequisites and what the talk has already introduced.

## Content integrity and selection

This section governs content selection, compression, and artifact allocation. Wording, explanation depth, and readable pagination may change; the meaning of retained claims and their required foundations may not. Apply these boundaries before preferences for brevity, emphasis, avoidance of repetition, layout, or timing.

### Narrative order and explanatory freedom

Preserve the relative order of the source's main arguments and selected results. Splitting dense material or merging adjacent material must preserve their logical relationships. Only a specific user request authorizes a different main sequence; a general request for clarity, focus, or a shorter talk does not. For several unordered sources, settle the primary source/order from the user's brief before drafting.

At the point of first use, unpack definitions and conditions that the source references from elsewhere, including an appendix. This is local explanation of the current argument, not permission to relocate later results, applications, or examples to manufacture an opening. Equivalent restatement, explicit symbol definitions, source-grounded intermediate reasoning, and natural transitions are permitted. Do not introduce a new scientific claim or alter a condition to make the presentation easier.

For each slide example, identify its source location or the user's specific request. Do not create a scenario, data, parameter specialization, or modified hypothesis without that request. The source's own examples remain usable in context with their conditions intact. Additional learning illustrations belong in conversation or notes with their origin labeled; they must not migrate into the talk automatically.

### Complete formal statements on slides

For each theorem, proposition, lemma, corollary, or other formal result selected for presentation, recover the full statement from the source and its referenced context before drafting. Preserve:

- The objects, definitions, domains, indices, and quantifiers to which the result applies.
- Every assumption and condition required by that statement, including parameter restrictions, sampling or asymptotic regimes, and conditions referenced elsewhere in the work.
- Every conclusion and its mathematical form, with the original inequalities, rates, probability or convergence meaning, and scope of applicability.

Display this complete statement on the slides. It may span clearly connected consecutive pages; conditions already fully displayed on earlier slides may be explicitly referenced by their slide locations. At first use, an assumption label alone is insufficient: show the actual requirement and define its symbols and parameter ranges. Follow nested references far enough to expose the requirements needed to interpret the statement. A condition's verbal motivation supplements its mathematical content; it does not replace it.

Do not place required statement components only in the script, notes, or an external citation. A result used in the main talk cannot depend on statement components confined to backup; a result presented only in optional backup must be complete within that backup sequence. Do not substitute a qualitative takeaway for the conclusion, relabel an incomplete result to bypass completeness, silently strengthen or weaken assumptions, or convert a result to an unrequested special case. A missing or ambiguous source passage must be resolved or identified as pending in preparation material; do not invent its contents or present the result as verified.

Statement completeness does not require displaying the full proof. Select proof depth separately, retaining the reasoning needed for the talk's argument.

### Foundations and shortening

For each retained result, procedure, or interpretation, trace the definitions, model setup, assumptions, and prior results it needs. Introduce source-specific foundations on slides before or at first use, at sufficient precision to interpret the dependent content; use the script to explain their meaning and connections. Do not treat material confined to notes, an appendix outside the talk, or later slides as listener knowledge. Agreed general prerequisites need not be retaught.

Before omitting material, check which later pages depend on it. Retain the required foundation or revise/remove the dependent content within the agreed scope. Favor removing optional branches, redundant evidence, or nonessential proof detail over deleting parts of a retained statement or breaking its dependency chain. If the required scope cannot fit the time limit with complete statements and necessary foundations, present the concrete scope tradeoff rather than silently degrading correctness. These requirements govern both slide-only requests and paired slide-and-script drafting.

## Build a compact source map

Use the existing source/page map to preserve traceability, narrative order, and prerequisite coverage. Record source locations and planned slide locations; do not create a separate tracking framework.

| Field | What to record |
|---|---|
| Question | The specific problem and why it matters in this setting |
| Idea or approach | What the method or research design does and how it addresses the problem |
| Contribution or finding | What is established, relative to which baseline or prior work |
| Objects | Data structure, variables, indices, dimensions, parameters, and relevant populations |
| Conditions | Required assumptions and restrictions, their full source locations, and where they appear on slides |
| Prerequisites | Definitions, setup, and prior results used by each page, with their first-introduction slide locations |
| Evidence | Theorem, derivation, simulation, empirical result, or other supporting analysis |
| Statement coverage | Each selected formal result's complete source statement and the slide locations covering its objects, conditions, and conclusions |
| Source | Exact section, equation, table, figure, or analysis output |
| Limits | Scope of the claim, unresolved issues, and work not yet completed |
| Presentation role | Allocation under the content-integrity rules; complete statements and required foundations belong in the slide sequence where a retained result is presented |

State one central message and a small set of supported contributions or findings. Distinguish a motivating example, an established technique used by the work, and the work's actual contribution. Do not label every component an innovation.

A course report can make a useful argument through a careful design, reproduction, comparison, or interpretation. A proposal can explain a question and a justified plan. Neither requires an invented novelty claim or fabricated results.

## Select evidence to serve the argument

For each candidate section or result, ask what central claim it supports and what the audience needs to understand it. Select and shorten under [content integrity and selection](#content-integrity-and-selection); this section determines emphasis, not exceptions to completeness.

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

Verify formal results using the complete-statement requirements above. For other important displayed equations and technical claims:

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
