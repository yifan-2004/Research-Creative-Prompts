# 审查训练配置的可复现性

[分类目录](README.md) · [总目录](../../README.md)

ID：`deep-learning/reproduction-config`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `config` | 配置摘要 |
| `run_record` | 运行记录 |
| `target` | 复现要求 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
config：{{config}}
run_record：{{run_record}}
target：{{target}}

检查随机源、数据顺序、依赖锁定、数据指纹、代码版本、硬件与算子确定性。按必要、建议、平台相关列出补充字段，解释严格确定性的速度成本。给出配置与运行元数据示例，不保证不同硬件能逐位一致。
```

## 示例输入

```json
{
  "config": "seed=42，AMP=true，batch=8，workers=8；依赖只有 torch>=2",
  "run_record": "记录了 loss 与 epoch，未记录 git commit 或数据版本",
  "target": "同平台重复主要指标趋势"
}
```

## 预期输出

缺失字段清单、运行元数据 schema 与复跑验收方式。

## 适用与边界

适合发布训练代码前。

配置完整也不自动保证所有第三方算子确定。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
