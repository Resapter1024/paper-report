# paper-report

将论文、自己撰写的研究报告或课程研究材料，整理为 Beamer Slides、按页对应的讲稿和准备笔记。

这个 skill 通过分阶段提问确定听众、主线和重点，重视核心思路及证据，提供可直接使用的封面与正文样式，并检查讲述连贯性、语言和排版。

## 任务入口

在支持 SKILL.md 的工具中加载本目录后，可以使用以下任务入口，也可以直接用自然语言描述需求：

| 入口 | 功能 |
|---|---|
| $paper-report plan | 确认听众基础、课程要求、重点与时长，提出报告结构 |
| $paper-report draft | 根据材料和已确定的方向生成请求的交付物 |
| $paper-report polish | 修正文风、过度防御及内容、口述、准备提示混用 |
| $paper-report check | 只读检查内容、语言、排版与时间安排 |
| $paper-report export | 从同一份讲稿正文导出对照版或纯文字版 |

这些是由 skill 识别的任务入口，不是独立的终端命令。

## 输入与输出

通常需要提供研究材料、听众背景、汇报要求和目标时长。有明确模板时遵循模板，否则使用内置样式。报告人姓名和其他身份信息等待用户提供。

完整报告通常包含：

- Slides：研究问题、核心思路、关键公式和必要证据。
- 讲稿：配合各页 Slides 说出的解释、推导、例子和衔接。
- 准备笔记：背景、完整推导、来源、备答和准备提示。

讲稿以听众没有读过材料为前提，保留理解所需的中间步骤。方法报告与实证研究根据各自的主线分配篇幅，不要求每份报告都包含定理、模拟或应用。

## 目录

    SKILL.md                 skill 入口和主要约定
    agents/openai.yaml       展示信息和默认提示词
    references/              规划、语言、范例和检查规范
    assets/starter/          可复用的 LaTeX 起始文件
    scripts/build-latex.ps1  LaTeX 编译辅助脚本
    AGENTS.md                本仓库的开发约定

## LaTeX 使用与依赖

将 assets/starter/ 的内容复制到一个报告工作目录，再根据研究材料替换示例内容。内置示例用于说明版式，不代表用户的研究结果。

需要 XeLaTeX 和常用 TeX 宏包。内置样式使用 ctex，并提供 Fandol 字体回退；无需原项目中的校徽、字体文件或参考报告。

编译顺序为 Slides 在先、嵌入 Slides 的讲稿在后。例如，将起始文件复制到仓库旁的 my-report/ 后，在本仓库中运行：

    .\scripts\build-latex.ps1 -TexFile ..\my-report\slides\report.tex -Strict
    .\scripts\build-latex.ps1 -TexFile ..\my-report\script\script.tex -Strict
    .\scripts\build-latex.ps1 -TexFile ..\my-report\script\text-only.tex -Strict

script.tex 与 text-only.tex 共用 supplements.tex。通过 ReportSlide 的参数分别记录 Slides 编号和 PDF 物理页码，避免目录页引起对应错误。

编译脚本主要在 Windows/PowerShell 下验证。其他系统可以直接调用 XeLaTeX，按项目需要运行 BibTeX 或 Biber，并继续编译至引用稳定。

humanizer 是可选的外部 skill；本仓库不打包其源码，未安装时仍可使用内置语言审查规则。

## 开发

本仓库是该 skill 的开发源。修改工作流、规范或资产时同步检查相关引用；在仓库外的临时目录中进行模板编译和视觉检查，避免将构建产物写入资产目录。

## 发布状态与许可证

当前尚未选择开源许可证，也未配置 GitHub 远程仓库。公开发布前需要补充 LICENSE，确定公开署名，并确认借用内容的许可与致谢。
