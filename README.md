# paper-report

[中文](#中文) · [English](#english)

## 中文

`paper-report` 面向课堂展示和学术报告，旨在帮助用户在同一工作流中并行地完成学习论文、撰写展示用 slides，准备和练习汇报。

本 Skill 的生成结果是需要继续打磨的初稿，用户不能期待一次对话就生成可以直接使用的报告文件。围绕 report 和 script 进行逐页精修、练习讲述与答疑，在精修过程中对直接生成的材料补充自己的看法，同时学习相关材料、加深对论文的理解，是这个 skill 的主要用法。实际的工作流可能为：

<table border="1" width="100%" cellpadding="16" cellspacing="12">
  <tr>
    <td width="220" rowspan="2" align="center" valign="middle"><strong>生成初稿</strong><br><br>report · script · notes</td>
    <td width="48" rowspan="2" align="center" valign="middle">→</td>
    <td width="300" height="120" align="center" valign="middle"><strong>逐页精修</strong><br><br>确认内容、完善汇报细节<br>补充自己的看法</td>
    <td width="48" rowspan="2" align="center" valign="middle">→</td>
    <td width="220" rowspan="2" align="center" valign="middle"><strong>汇报练习</strong><br><br>练习讲述与答疑</td>
  </tr>
  <tr>
    <td width="300" height="120" align="center" valign="middle"><strong>学习理解</strong><br><br>借助 notes 阅读论文<br>理解概念与推导</td>
  </tr>
</table>

中间的精修与学习并行推进，相互补充。

### 三类输出

| 文件 | 作用 |
|---|---|
| **report** | 用于向听众展示的 slides，呈现主线、关键公式、图表与结论。 |
| **script** | 配合 report 进行讲述的讲稿，逐页补充解释、例子、推导和衔接，帮助讲清 slides。 |
| **notes** | 用于深入学习的笔记，展开 report 和 script 中的概念、假设、推导与背景，帮助报告人理解材料。 |

**备选页（backup slides）** 按需附在 report 主体之后，保留补充推导、技术细节或额外结果，供答疑时调用或有余时展开。若将它们纳入正式讲述，需要计入报告总时长。主线必需的定义、假设和定理结论仍应放在正文中。

可生成源码与 PDF，也可只处理指定部分。

### 需要提供什么

- **研究材料与范围**：论文、自写研究报告或课程材料，以及需要汇报的部分。
- **展示要求**：听众基础、目标时长（是否含问答）、重点、语言和课程要求。
- **模板与输出**：指定模板和输出位置可选，无模板时使用内置样式；报告人信息由用户提供。

### 命令与输出

| 命令 | 功能 | 输出 |
|---|---|---|
| `$paper-report plan` | 确认听众、重点与结构 | 待确认问题、报告提纲、时间分配 |
| `$paper-report draft` | 编写报告初稿 | report、script、notes 的源码与 PDF，或指定部分 |
| `$paper-report polish` | 修正文风、过度防御和提示语言混用 | 修订文件与简短修改说明 |
| `$paper-report check` | 只读审查 AI 式表述、防御性文本、提示语言混用等语言问题 | 带原句、页码和措辞建议的清单；不评价内容编排、技术、排版或时长 |
| `$paper-report export` | 导出已有讲稿 | Slides 对照版或纯文字版的源码与 PDF |
| `$paper-report questions` | 根据当前 report 和 script 模拟听众提问 | 问题清单，附页码／标题与提问缘由；可另行请求答案 |

## English

`paper-report` helps you study papers, write slides, and prepare and rehearse classroom presentations and academic talks within a single workflow.

The skill produces an initial draft that needs further refinement. Do not expect ready-to-use presentation files from a single conversation. Its main use is to refine report and script page by page, practice delivery and Q&A, and add your own perspective while studying the material and deepening your understanding of the paper. A typical workflow is:

<table border="1" width="100%" cellpadding="16" cellspacing="12">
  <tr>
    <td width="220" rowspan="2" align="center" valign="middle"><strong>Generate a draft</strong><br><br>report · script · notes</td>
    <td width="48" rowspan="2" align="center" valign="middle">→</td>
    <td width="300" height="120" align="center" valign="middle"><strong>Refine each slide</strong><br><br>Check content and details<br>Add your own perspective</td>
    <td width="48" rowspan="2" align="center" valign="middle">→</td>
    <td width="220" rowspan="2" align="center" valign="middle"><strong>Rehearse the talk</strong><br><br>Practice delivery and Q&amp;A</td>
  </tr>
  <tr>
    <td width="300" height="120" align="center" valign="middle"><strong>Study the material</strong><br><br>Use notes to understand<br>concepts and derivations</td>
  </tr>
</table>

Refinement and learning proceed in parallel, informing each other.

### Three outputs

| File | Purpose |
|---|---|
| **report** | Slides for the audience, presenting the main argument, key equations, figures, and conclusions. |
| **script** | A speaker script used alongside report, adding explanations, examples, derivations, and transitions for each slide. |
| **notes** | Study notes that develop the concepts, assumptions, derivations, and background behind report and script for deeper understanding. |

**Backup slides** can be appended to report as needed, retaining supplementary derivations, technical details, or additional results for Q&A or extra discussion when time allows. Include them in the total presentation time if you plan to present them. Definitions, assumptions, and theorem conclusions required by the main argument still belong in the main slides.

Outputs can include source files and PDFs, or only the requested parts.

### What to provide

- **Materials and scope:** a paper, your own research report, or course materials, and the parts to present.
- **Presentation requirements:** audience background, time limit including whether Q&A counts, focus, language, and course requirements.
- **Template and output:** a template and output location are optional; otherwise, the bundled style is used. You supply the presenter information.

### Commands and outputs

| Command | Purpose | Output |
|---|---|---|
| `$paper-report plan` | Establish the audience, focus, and structure | Open questions, an outline, and time allocations |
| `$paper-report draft` | Write the initial presentation files | Source files and PDFs for report, script, and notes, or selected parts |
| `$paper-report polish` | Improve wording, excessive defensive statements, and misplaced preparation instructions | Revised files and a brief change note |
| `$paper-report check` | Audit AI-like wording, defensive statements, and instruction residue without editing | Quoted passages, page locations, and wording suggestions; no content-structure, technical, layout, or timing review |
| `$paper-report export` | Export an existing script | Source files and PDFs with slides alongside the script or as text only |
| `$paper-report questions` | Anticipate audience questions from the current report and script | Questions with slide numbers/titles and reasons for asking; answers can be requested separately |

## License / 许可证

[MIT](LICENSE)
