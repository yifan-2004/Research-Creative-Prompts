# 保留技术含义的英文润色

[分类目录](README.md) · [总目录](../../README.md)

ID：`academic-writing/english-polish`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `text` | 英文原文 |
| `terms` | 必须保留术语 |
| `tone` | 目标风格 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
text：{{text}}
terms：{{terms}}
tone：{{tone}}

修正语法、搭配与句间连接，保留原始结论强度及不利结果。提供最小修改版和流畅版，列出可能改变技术含义的修改供作者确认。不要增加实验、引用或形容词夸大性能；专有名词不确定时保留并提问。
```

## 示例输入

```json
{
  "text": "Our model make the dark image bright, but on outdoor data the color is sometimes worse.",
  "terms": "low-light enhancement, color fidelity",
  "tone": "简洁、客观的学术英文"
}
```

## 预期输出

两种润色版本与关键改动说明。

## 适用与边界

适合非母语作者润色已有段落。

需要作者核对术语，不能修复事实错误。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
