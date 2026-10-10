# 具体而诚实地写局限

[分类目录](README.md) · [总目录](../../README.md)

ID：`academic-writing/limitations-section`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `evidence` | 实验覆盖 |
| `assumptions` | 方法假设 |
| `observed_failures` | 已观察问题 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
evidence：{{evidence}}
assumptions：{{assumptions}}
observed_failures：{{observed_failures}}

区分覆盖不足、方法假设、已知失败与部署成本。每项说明受影响的使用场景和已有证据，再给可行验证方向；不把未来计划写成已经解决。避免空泛“仍有改进空间”，也不夸大未观察到的问题。
```

## 示例输入

```json
{
  "evidence": "只在两套静态图像集测试，未测移动端与视频",
  "assumptions": "输入已经完成去马赛克与白平衡",
  "observed_failures": "强色偏时输出不稳定"
}
```

## 预期输出

3—5 条具体局限与对应验证路径。

## 适用与边界

适合论文讨论与模型说明。

局限取决于输入证据，不是完整风险评估。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
