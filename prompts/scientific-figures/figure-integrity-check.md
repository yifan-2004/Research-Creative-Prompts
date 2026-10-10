# 发布前核对图像与数据一致性

[分类目录](README.md) · [总目录](../../README.md)

ID：`scientific-figures/figure-integrity-check`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `assets` | 待发布图 |
| `sources` | 对应来源 |
| `processing` | 处理记录 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
assets：{{assets}}
sources：{{sources}}
processing：{{processing}}

为每个面板核对来源文件、生成脚本、选择规则和处理记录。检查坐标截断、缺失样本、不同显示参数、重复图和标签错位；区分允许的统一排版处理与会改变证据的修改。输出可追溯清单，未知来源不能直接通过。
```

## 示例输入

```json
{
  "assets": "性能柱状图、增强对比图、3D 检测图",
  "sources": "results.csv；sample_03 输出；检测 predictions.json",
  "processing": "统一裁剪、缩放；无额外修图"
}
```

## 预期输出

逐面板发布检查表与需修复项。

## 适用与边界

适合论文和 GitHub 结果展示前。

检查需访问实际文件，文字审查不能认证图像真实性。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
