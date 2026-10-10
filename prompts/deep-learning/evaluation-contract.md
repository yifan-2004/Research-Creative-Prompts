# 冻结可复用的评测协议

[分类目录](README.md) · [总目录](../../README.md)

ID：`deep-learning/evaluation-contract`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `task` | 任务 |
| `metric_choices` | 指标选择 |
| `data` | 评测数据 |
| `known_rules` | 已知规则 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
task：{{task}}
metric_choices：{{metric_choices}}
data：{{data}}
known_rules：{{known_rules}}

明确色彩空间、位深、范围、裁边、重采样、模型输出处理和聚合方式。区分逐图均值与先汇总误差再算指标，记录工具版本及默认参数。对未确定参数提出必须冻结的决策，不自行声称与某论文官方协议一致。提供结果文件字段和异常样本规则。
```

## 示例输入

```json
{
  "task": "图像增强",
  "metric_choices": "PSNR、SSIM、LPIPS",
  "data": "RGB 配对图像，含不同尺寸",
  "known_rules": "裁边 0；输出裁剪到 [0,1]；不对齐颜色"
}
```

## 预期输出

完整评测协议、结果表 schema 与复核清单。

## 适用与边界

适合团队统一评测与论文复现。

需对照官方脚本验证；仅指标名称相同不代表协议相同。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
