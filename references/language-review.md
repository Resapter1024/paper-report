# Language review for slides and speech

Read for polish, check, and the language pass of draft. Preserve the author's meaning while removing AI-like wording, unnecessary defensive statements, and preparation/chat language mixed into the presentation.

## Scope and mode

Check is a read-only language audit of every requested page, not a general report review. Inspect formulaic AI phrasing, filler and inflated claims, unnecessary defensive wording, instruction/chat residue, awkward oral language, inconsistent terminology, and sentence-style slide titles. Judge wording in its local context; a single word or detector score is not proof of AI authorship.

Do not assess content selection, chapter/slide order, emphasis, missing results or derivations, technical correctness, layout, timing, or PDF compatibility under check. Do not suggest moving, adding, deleting, splitting, or merging sections/pages. A useful suggestion outside that scope still belongs in a separately requested review, not in the language-audit findings. In particular, do not read quality-checks.md or run the PDF checker as part of check.

Polish applies authorized wording edits with the same content-preservation boundary. Draft uses these rules while writing. The broader artifact acceptance checks belong to draft/export or an explicitly requested broader review.

## Process

1. Read every requested slide and its corresponding supplement. Identify whether a sentence belongs to visible content, actual speech, or preparation. Use the supplied text as context; do not turn check into a source-paper or mathematical review.
2. Preserve a semantic checklist: claims, defined terms, quantities, comparisons, conditions, citations, and steps that make the argument understandable.
3. If humanizer is available, read and apply it. Adapt its academic-prose defaults to this oral report using the rules below. If absent, use this reference directly without blocking the task.
4. Identify excessive ceremony, unnecessary defensive language, and misplaced editorial instructions. For check, propose wording only; for polish/draft, apply it within the authorized scope.
5. Compare with the checklist, read the speech aloud, and check the neighboring transitions.
6. For polish, summarize the scoped edits. For check, use the audit output format below.

An optional detector can flag passages, but a score or isolated keyword is not evidence that a sentence should be removed. Do not describe this review as proof of human authorship.

## Adapt humanizer to the artifact

- Prefer concrete actors, objects, and verbs over vague evaluative phrases. Replace "充分体现了方法的强大优势" with the specific measured result or mechanism.
- Vary sentence length. Keep paragraphs that develop one step of reasoning; do not compress an explanation into a dense academic abstract.
- Preserve useful spoken connectives: "先看……", "由于……", "因此……", and "接下来……" can orient listeners. Remove repeated announcements of the writing process.
- Preserve precise technical vocabulary, necessary repetition, symbol introductions, numbers, citations, equations, and conditions.
- Retain the presenter's role. "作者发现" or "本文的结果" may suit a paper explanation; "我们发现" requires that the finding belongs to the presenter's study.
- Remove decorative emphasis and inflated certainty. Do not automatically strengthen "相关" to "影响", "显示" to "证明", or numerical differences to statistically significant effects.
- Prefer ordinary punctuation to chains of parenthetical asides. Keep conventional Chinese punctuation and mathematical notation; do not mechanically apply English typography rules.
- Remove chat residue and generic praise. Audit commentary stays in the review response, not in the deck or guide.

Humanizing changes expression, not the coverage, scientific examples, or order of the explanation. Preserve the existing steps and the source's conditions.

## Three language layers

| Layer | Suitable sentence | Unsuitable intrusion |
|---|---|---|
| Slide | 多个结局共同帮助估计个体特征。 | 报告重点是解释共享潜变量为什么有用。 |
| Spoken supplement | 同一个家庭在各商品的模型中共用这组特征，因此其他商品的购买记录也能帮助估计它。 | 这一页应强调多结局信息共享。 |
| Preparation | 本页预留90秒；完整推导可作为板书或备答。 | Do not place this instruction into audience-facing content. |

A sentence about how the author should write or deliver the report is preparation. Distinguish it from actual speech by function, not by searching for the word "报告". Inspect titles for phrase form only; do not use a title-style finding to propose a different topic or narrative.

"接下来先看购买记录的结构" can be actual speech. "这里需要补充一个例子" is a preparation instruction; keep the reminder in notes or explain an existing source example within the authorized edit. Do not invent an example to repair the wording.

## Unnecessary defensive language versus necessary limits

Look for sentences such as "论文没有给出……", "论文不足以说明……", "不能据此认为……", and "这并不意味着……". Classify their function in context.

| Function | Action |
|---|---|
| Needed assumption, evidence boundary, unresolved result, or correction of a likely misreading | Keep it concisely with the relevant claim, using a positive scope statement where equivalent. |
| Unrequested comparison with every possible method or application | Remove the tangent or move it to preparation/Q&A. |
| Agent uncertainty about a source or technical point | Do not add it as a generic disclaimer. Technical verification belongs to drafting or a separately requested technical explanation, not to check. |
| Drafting or time-allocation comment | Move it to preparation. |
| Substantive source limitation central to the argument | Explain it directly; do not erase it for stylistic confidence. |

Examples, assuming the stated scoped result is supported:

- "论文不足以说明该方法在所有情况下都更好。" -> "在这些模拟设置中，该方法的估计误差较低。"
- "论文没有给出所有场景下的因果结论。" -> If the study estimates associations, state "这里估计的是变量间的关联。" Retain an explicit causal limitation if the audience otherwise would misunderstand the claim.
- "这个FDR很低，但不能说没有任何问题。" -> Explain the relevant distinction: "显著结果中的误报比例控制得较好；是否漏掉真实关联，还要结合漏报指标来看。"
- "这一页不用讲太细，只需突出创新。" -> Preparation instruction. Supply the actual spoken explanation of the idea and omit the instruction from the guide body.

Do not delete low coverage, null or adverse findings, selection bias, missing-data assumptions, local-optimum concerns, or incomplete analyses just because they qualify a result. Do not invent a positive conclusion to avoid a negative sentence.

## Audit output

For each finding, report page/title, layer, the quoted wording, language category, a brief reason, and a meaning-preserving wording suggestion. Cover the requested files rather than sampling a few pages; combine repeated phrasing issues with their locations instead of repeating the same advice. If there are no in-scope findings, say so without manufacturing content or layout objections. Keep the audit outside the presentation and leave files unchanged under check. Do not claim to have proved that all AI authorship is absent.
