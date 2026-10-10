# 搭建引言的论证链

[分类目录](README.md) · [总目录](../../README.md)

ID：`academic-writing/introduction-logic`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `motivation` | 实际问题 |
| `prior_evidence` | 已有研究证据 |
| `contribution` | 已实现贡献 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
motivation：{{motivation}}
prior_evidence：{{prior_evidence}}
contribution：{{contribution}}

用应用问题、已有路线、证据支持的局限、本文切入点和贡献搭建引言。每个过渡写清逻辑，不把某个数据集上的局限扩大到全部方法。引用仅保留给定标识；缺少证据的判断改写或标为待补。输出段落草稿和论证链检查。
```

## 示例输入

```json
{
  "motivation": "夜间道路图像噪声与低对比度影响感知",
  "prior_evidence": "[R1] 改善亮度；[R2] 指出颜色失真；均只提供摘要。",
  "contribution": "引入可解释的颜色一致性约束，并评估下游检测"
}
```

## 预期输出

4—5 段引言与逐段证据需求。

## 适用与边界

适合有文献笔记后的引言写作。

不能凭摘要确认全部现有工作局限。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
