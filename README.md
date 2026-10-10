# Research & Creative Prompts

**120 条中文原创提示词，覆盖科研、深度学习、图像创作、个人 Agent 与产品验证。** 每条都有填写变量、完整示例、预期输出和适用边界，按实际任务查找即可。

这些模板由 AI 辅助编写，未复制外部提示词。**全部尚未经过模型运行验证**；目录与链接检查通过不代表模型输出质量已验证。不需要安装应用；使用时将模板复制到支持相应输入的助手。模型服务、文件阅读、图片生成和工具执行由你使用的平台提供。

## 选择一个任务

| 类别 | 数量 | 从这里开始 |
| --- | --- | --- |
| [科研选题与文献](prompts/research-literature/README.md) | 15 | [证据矩阵](prompts/research-literature/evidence-matrix.md)、[研究空白核查](prompts/research-literature/gap-validation.md) |
| [论文写作与审稿回复](prompts/academic-writing/README.md) | 15 | [摘要](prompts/academic-writing/evidence-bound-abstract.md)、[审稿回复](prompts/academic-writing/reviewer-response.md) |
| [深度学习实验](prompts/deep-learning/README.md) | 15 | [低照度评测](prompts/deep-learning/low-light-evaluation.md)、[单目 3D 检测检查](prompts/deep-learning/monocular-3d-review.md) |
| [图像生成与编辑](prompts/image-generation/README.md) | 15 | [产品主视觉](prompts/image-generation/product-hero.md)、[局部编辑](prompts/image-generation/localized-edit.md) |
| [科研图表与结果展示](prompts/scientific-figures/README.md) | 15 | [网络结构图](prompts/scientific-figures/architecture-spec.md)、[3D 框可视化](prompts/scientific-figures/3d-box-visualization.md) |
| [编程与个人 Agent](prompts/coding-agents/README.md) | 15 | [知识库问答](prompts/coding-agents/rag-evidence-answer.md)、[助手记忆](prompts/coding-agents/personal-assistant-memory.md) |
| [创业与产品验证](prompts/startup-product/README.md) | 15 | [MVP 范围](prompts/startup-product/mvp-scope.md)、[用户访谈](prompts/startup-product/interview-guide.md) |
| [学习与技术表达](prompts/learning-communication/README.md) | 15 | [学习计划](prompts/learning-communication/study-plan.md)、[项目介绍](prompts/learning-communication/project-introduction.md) |

## 怎么用

1. 打开一个模板，先看“适用与边界”。
2. 把 `{{变量}}` 替换成你的真实材料；“示例输入”演示的是填写方式。
3. 复制“复制模板”里的完整内容，按需附上文件或图片。
4. 核对事实、引用、代码与结果；缺失证据就保留未知，不让模型补造。

例如，在“低照度增强的分层评测”中填写自己的方法、配对/无配对数据和评测重点。模板会请求分别设计协议；无配对数据不会被要求报告无法计算的全参考 PSNR。这里描述的是模板目标，尚无实际模型输出验证。

图像生成类模板分为“让文字助手起草生成指令”和“将该指令交给图像工具”两步。图像编辑需要真实参考图；科研网络图需要真实结构；结果图与测试表格需要真实实验数据。

## 文件与维护

- [data/prompts.json](data/prompts.json)：120 条模板的唯一内容源，可用于搜索或程序集成。
- [prompts/](prompts/)：按类别生成的可读页面；修改内容时编辑 JSON。
- [tools/catalog.py](tools/catalog.py)：目录生成与一致性检查，Python 3.10+，只用标准库，无联网或模型调用。
- [CONTRIBUTING.md](CONTRIBUTING.md)：新增、修改和验证方法。

```bash
python3 tools/catalog.py build
python3 tools/catalog.py check
```

检查范围：类别数量、唯一 ID/标题/正文、变量和示例对应、来源和待验证状态、生成页面一致性、本地链接。**这些检查不评价提示词的实际效果。**

## English

120 original, Chinese-first prompt templates across eight practical categories. Every entry includes variables, a complete example input, intended output, scope, limitations, provenance and verification status. All prompts are **untested with models**. Replace the variables, provide your real materials, and review the output. The catalog validator checks structure and local links; it does not measure prompt quality.

Templates are model-agnostic. File reading, image generation and agent actions require capabilities provided by your chosen platform. This repository does not call any model or send messages.

## 许可

本库原创模板、说明与维护脚本按 [MIT License](LICENSE) 发布。使用本库不会授予第三方论文、图片、数据、模型或商标的权利。示例中注明的演示数据与虚构条目仅用于说明，不能作为研究证据。
