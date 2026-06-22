# 典型交互示例 (Interaction Example)

这个文档展示了用户和 Agent 之间如何进行顺畅的“复习资料整理与出卷”工作流。

## 阶段 1：初始化

**User**: 我需要复习期末考试，帮我建立一下文件夹结构，课程名称是“高级人工智能”。
**Agent**: 好的，我已经为你创建了“高级人工智能”的文件夹体系：
- `高级人工智能/materials/Courseware`
- `高级人工智能/materials/Test papers and homework`
- `高级人工智能/result`
文件夹已建立完成，请将课程资料存入 `@materials` 中，完成后告诉我一声“开始整理”就好！

## 阶段 2：整理大纲

**User**: 资料上传完了，开始整理。
**Agent**: 收到！请问您需要详细、正常还是简略的大纲总结？
**User**: 正常就行，把核心考点标注清楚。
**Agent**: 正在启动后台子 Agent 进行处理...
*(内部：Agent1 生成大纲并使用原生 LaTeX 渲染公式，Agent2 校验内容，最后使用 scripts/md_merger.py 合并 MD 并用 scripts/md2pdf.py 渲染为 overviewreview.pdf)*
**Agent**: 课件整理已经完毕，文件已经生成在 `@result/Overview` 文件夹中（包含各章节大纲及合并后的精美 `overviewreview.pdf`），需要帮你出一套模拟卷的时候再来找我！

## 阶段 3：生成试卷

**User**: 帮我出套模拟卷吧。
**Agent**: 没问题，正在启动后台子 Agent 为您从题库和知识点中随机抽取生成模拟卷...
*(内部：Agent1 抽取试题生成 Markdown 试卷，Agent2 校验，最后使用 md_merger.py 合并并用 md2pdf.py 渲染为 overviewtest.pdf)*
**Agent**: 命题完毕，试卷文件已经生成在 `@result/Overview/overviewtest.pdf` 文件夹中，祝你复习顺利！
