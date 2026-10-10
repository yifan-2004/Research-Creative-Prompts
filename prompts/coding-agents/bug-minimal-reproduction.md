# 先复现再修复缺陷

[分类目录](README.md) · [总目录](../../README.md)

ID：`coding-agents/bug-minimal-reproduction`  
状态：**待验证 / untested**

## 输入变量

| 变量 | 填写说明 |
| --- | --- |
| `bug` | 错误表现 |
| `environment` | 环境 |
| `expected` | 期望行为 |

## 复制模板

将下方变量替换为你的材料。不要将示例中的演示数据用于真实报告。

```text
bug：{{bug}}
environment：{{environment}}
expected：{{expected}}

读取入口与错误栈，构造最小失败样例并确认故障点。比较转 RGB 与拒绝灰度输入的兼容性，按现有接口选择一致行为。修复后验证失败样例与正常路径，解释根因；不能仅捕获所有异常来隐藏错误。
```

## 示例输入

```json
{
  "bug": "输入灰度 PNG 时推理维度错误",
  "environment": "Python 3.11，PyTorch，Pillow",
  "expected": "明确转 RGB 或返回易懂错误，保持彩色输入结果"
}
```

## 预期输出

最小复现、修复及回归验证说明。

## 适用与边界

适合可稳定复现的代码 bug。

需实际环境运行才能确认根因。

## 来源与验证

为本合集原创编写，AI 辅助起草；未复制外部提示词。

未经模型运行验证；示例输入用于说明填写方式，不代表已获得输出。
