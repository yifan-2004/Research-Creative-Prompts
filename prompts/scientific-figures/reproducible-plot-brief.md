# 生成可复现绘图需求

[分类目录](README.md) · [总目录](../../README.md)

ID：`scientific-figures/reproducible-plot-brief`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `dataset` | 数据文件说明 |
| `plot` | 绘图目标 |
| `environment` | 环境要求 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
dataset：{{dataset}}
plot：{{plot}}
environment：{{environment}}

先定义数据 schema、单位、缺失值与重复键规则，再制定确定性排序、配色和导出参数。要求脚本读取文件而不是硬编码论文数字，明确不修改原始数据。提供绘图实现的任务书与验收样例，避免声称未运行脚本已成功。
```

## 示例输入

```json
{
  "dataset": "results.csv，列 method,dataset,seed,psnr",
  "plot": "按数据集分面显示每个方法的种子点与均值",
  "environment": "Python，matplotlib，导出 PDF 与 PNG"
}
```

## 预期输出

绘图任务书、输入校验要求与验收检查。

## 适用与边界

适合交给代码助手实现正式图。

需要真实数据和实际渲染检查。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
