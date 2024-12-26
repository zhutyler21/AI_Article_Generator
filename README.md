# AI Academic Article Generator 🎓

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

AI Academic Article Generator 是一个专业的学术论文写作辅助工具集，它结合了文档处理工具、标准化写作模板和优化的 AI 提示词系统，帮助研究人员高效地完成学术论文写作。

## ✨ 主要特性

- 📄 PDF 文献智能处理与转换
- 📝 标准化学术写作模板
- 💡 优化的 AI 提示词系统
- 🎯 逻辑框架提取与分析
- 🔍 文献重点内容提取

## 📁 项目结构

### Python 工具
- `pdf_to_markdown.py`: PDF 转 Markdown 工具
  - 将 PDF 文献转换为结构化的 Markdown 格式
  - 支持页面编号和段落格式化
  - 使用方法: `python pdf_to_markdown.py <pdf_path> [output_dir]`

- `extract_bold.py`: Word 文档加粗内容提取工具
  - 提取 Word 文档中的加粗文本
  - 自动保存提取结果
  - 使用方法: `python extract_bold.py`

### Markdown 模板
- `Logic_Outline_template.md`: 论文逻辑框架模板
  - 标准化的引言部分结构
  - 文献综述框架指南
  - 写作要点和规范

- `Writing_template.md`: 详细写作模板
  - 完整的论文结构框架
  - 分段写作指导
  - 引用规范示例

### 提示词系统
- `Prompt.md`: AI 写作提示词集合
  - 逻辑框架提取提示词
  - 写作模板生成提示词
  - 文献要点提取提示词
  - 论文写作辅助提示词

## 🚀 使用指南

1. 文献预处理：
   ```bash
   python pdf_to_markdown.py "your_paper.pdf"
   python extract_bold.py  # 提取 Word 文档中的加粗内容
   ```

2. 使用写作模板：
   - 参考 `Logic_Outline_template.md` 构建论文框架
   - 使用 `Writing_template.md` 进行详细写作

3. 使用 AI 提示词：
   - 按照 `Prompt.md` 中的提示词指南进行写作
   - 根据需要选择不同类型的提示词

## 📝 注意事项

- 确保安装所需的 Python 依赖：`pypdf`, `python-docx`
- 使用前请仔细阅读各模板中的使用说明
- AI 提示词仅作为写作辅助，最终内容需要人工审核

## 🤝 贡献指南

欢迎提交 Issues 和 Pull Requests！

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 👥 团队

- 项目负责人：[zhutyler21](https://github.com/zhutyler21) 
