# 选择微调策略与冻结范围

[分类目录](README.md) · [总目录](../../README.md)

ID：`deep-learning/transfer-learning-plan`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `source_model` | 预训练模型 |
| `target_data` | 目标数据 |
| `resources` | 资源 |
| `objective` | 目标 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
source_model：{{source_model}}
target_data：{{target_data}}
resources：{{resources}}
objective：{{objective}}

比较线性探测、部分微调与全量微调，给出各自需要的证据和过拟合迹象。设计分组验证与学习率范围搜索，优先小预算试验。讨论归一化层、输入分布和数据增强，避免将冻结层默认等同于冻结其运行统计。
```

## 示例输入

```json
{
  "source_model": "在白天道路图像训练的视觉 backbone",
  "target_data": "2,000 张带标注夜间道路图像",
  "resources": "16GB GPU，三天",
  "objective": "夜间检测准确率与稳定性"
}
```

## 预期输出

分阶段微调计划与停止/升级条件。

## 适用与边界

适合小数据域迁移。

具体超参需实测，预训练许可和数据兼容性需确认。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
