# paper-report

[中文](#中文) · [English](#english)

## 中文

面向课堂展示和学术报告，在同一工作流中并行地学习论文、自写研究报告或课程材料，准备和练习汇报，并编写相关文件。

生成结果是需要继续打磨的初稿，用户不能期待一次对话直接生成可以使用的报告。围绕 **report 和 script 进行逐页精修、练习讲述与答疑，同时学习材料、加深理解**，是这个 skill 的主要用法。

### 三类输出

| 文件 | 作用 |
|---|---|
| **report** | 用于向听众展示的 slides，呈现主线、关键公式、图表与结论。 |
| **script** | 配合 report 进行讲述的讲稿，按页补充解释、例子、推导和衔接，帮助讲清 slides。 |
| **notes** | 用于深入学习的笔记，展开 report 和 script 中的概念、假设、推导与背景，帮助报告人理解材料。 |

可生成源码与 PDF，也可只处理指定部分。文件名可沿用已有项目。

### 需要提供什么

- **研究材料与范围**：论文、自写研究报告或课程材料，以及需要汇报的部分。
- **展示要求**：听众基础、目标时长（是否含问答）、重点、语言和课程要求；缺项会通过提问补齐。
- **模板与输出**：指定模板和输出位置可选，无模板时使用内置样式；报告人信息由用户提供。
- **已有文件**：修改或导出时提供对应文件；生成听众问题时提供当前 report 和 script。

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

For classroom presentations and academic talks, this skill lets you study a paper, your own research report, or course materials while preparing and rehearsing the presentation and writing its supporting files.

The generated material is an initial draft that needs further refinement. Do not expect a ready-to-use presentation from a single conversation. The main workflow is to **refine report and script page by page, rehearse the explanation and Q&A, and learn the material more deeply throughout that process**.

### Three outputs

| File | Purpose |
|---|---|
| **report** | Slides for the audience, presenting the main argument, key equations, figures, and conclusions. |
| **script** | A speaker script used alongside report, adding explanations, examples, derivations, and transitions for each slide. |
| **notes** | Study notes that develop the concepts, assumptions, derivations, and background behind report and script for deeper understanding. |

Outputs can include source files and PDFs, or only the requested parts. Existing project filenames can be retained.

### What to provide

- **Materials and scope:** a paper, your own research report, or course materials, and the parts to present.
- **Presentation requirements:** audience background, time limit including whether Q&A counts, focus, language, and course requirements. Missing details are clarified through questions.
- **Template and output:** a template and output location are optional; otherwise, the bundled style is used. You supply the presenter information.
- **Existing files:** provide the relevant files for revision or export, and the current report and script for audience questions.

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
