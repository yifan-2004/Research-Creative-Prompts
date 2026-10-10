# 设计性能与效率权衡图

[分类目录](README.md) · [总目录](../../README.md)

ID：`scientific-figures/pareto-frontier`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `measurements` | 数据字段 |
| `goal` | 决策限制 |
| `unknowns` | 测量不确定性 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
measurements：{{measurements}}
goal：{{goal}}
unknowns：{{unknowns}}

以延迟为横轴、准确率为纵轴，明确定义支配关系和可行区域。只基于真实数据识别 Pareto 点，不把不同硬件的测量混合排序。给出预热、同步与分位数汇总的记录要求，以及标注模型名和预算线的方法。
```

## 示例输入

```json
{
  "measurements": "model、AP、latency_ms、params_million；同硬件同 batch",
  "goal": "AP 尽量高，延迟低于 40ms",
  "unknowns": "每个延迟测 50 次，原始记录可提供"
}
```

## 预期输出

绘图规格、支配判定规则与测量核查项。

## 适用与边界

适合部署选型和论文效率分析。

端到端与纯模型延迟不能混用，结论依赖测量协议。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
