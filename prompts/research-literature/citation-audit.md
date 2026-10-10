# 检查引用条目的可靠性

[分类目录](README.md) · [总目录](../../README.md)

ID：`research-literature/citation-audit`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `bibliography` | 引用条目 |
| `claims` | 引用承担的主张 |
| `verified_records` | 已核实元数据 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
bibliography：{{bibliography}}
claims：{{claims}}
verified_records：{{verified_records}}

区分格式问题、元数据缺失与主张支持问题。没有浏览或检索工具时不得声称查到 DOI；给出按标题、作者、出版源逐层核验的步骤。对已提供核实记录逐字段比对，标出不一致。输出可执行核查列表，不把疑似错误直接等同于不存在。
```

## 示例输入

```json
{
  "bibliography": "示例：Li, A. 2024. Night Vision Enhancement. DOI 未提供。",
  "claims": "该论文支持“自监督低照度增强优于监督方法”。",
  "verified_records": "没有已核实记录"
}
```

## 预期输出

引用核查表，含状态、疑点与下一步证据。

## 适用与边界

适合清理参考文献与防止虚构引用。

离线状态不能认证文献存在；示例条目为虚构演示。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
