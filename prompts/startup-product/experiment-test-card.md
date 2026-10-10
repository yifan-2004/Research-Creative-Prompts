# 把产品假设写成实验卡

[分类目录](README.md) · [总目录](../../README.md)

ID：`startup-product/experiment-test-card`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `hypothesis` | 假设 |
| `participants` | 样本 |
| `constraints` | 条件 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
hypothesis：{{hypothesis}}
participants：{{participants}}
constraints：{{constraints}}

定义主要指标、对照、分配方式、观察窗口与停止规则。控制内容差异和学习效应，记录样本流失与异常；小样本可优先探索性分析，不预设显著。说明知情同意和不采集的个人信息，明确结果能支持与不能支持的结论。
```

## 示例输入

```json
{
  "hypothesis": "带页码来源的摘要比普通摘要更能促使研究者回看原文",
  "participants": "12 名自愿参与的研究生",
  "constraints": "一周，使用同一组论文，不改变摘要事实内容"
}
```

## 预期输出

实验卡、记录表与结果解释边界。

## 适用与边界

适合产品机制验证。

不替代正式人类受试研究审批或统计设计。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
