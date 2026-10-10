# 给不同受众解释同一技术

[分类目录](README.md) · [总目录](../../README.md)

ID：`learning-communication/explain-for-audience`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `technical_facts` | 技术事实 |
| `audiences` | 受众 |
| `constraints` | 限制 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
technical_facts：{{technical_facts}}
audiences：{{audiences}}
constraints：{{constraints}}

为三类受众分别选择必要术语、类比和细节，保持同一事实边界。类比后说明哪里不对应真实机制；所有版本保留远距离不确定性，不能为了易懂说成“知道精确距离”。
```

## 示例输入

```json
{
  "technical_facts": "模型从单张图像估计目标深度和 3D 框，远距离误差较大",
  "audiences": "高中生、软件工程师、视觉研究者",
  "constraints": "每版 100 字左右，不使用自动驾驶安全保证"
}
```

## 预期输出

三种解释与共同事实核对表。

## 适用与边界

适合科普、产品介绍和跨团队沟通。

类比有局限，应按实际听众反馈调整。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
