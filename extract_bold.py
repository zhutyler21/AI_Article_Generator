from docx import Document
from docx.shared import RGBColor

def extract_bold_text(docx_path):
    """提取Word文档中的加粗内容"""
    doc = Document(docx_path)
    bold_text = []
    
    # 遍历所有段落
    for paragraph in doc.paragraphs:
        # 遍历段落中的所有运行(runs)
        for run in paragraph.runs:
            try:
                # 检查是否为加粗文本
                if run.bold:
                    bold_text.append(run.text)
            except AttributeError:
                # 如果访问属性出错，跳过这个运行
                continue
    
    return bold_text

def main():
    try:
        # 使用示例
        docx_path = "认知和情感共情与负性情绪 情绪调节的作用机制.docx"  # 替换为你的文档路径
        bold_texts = extract_bold_text(docx_path)
        
        if not bold_texts:
            print("未找到加粗内容")
            return
            
        # 打印提取的内容
        print("提取的加粗内容：")
        for i, text in enumerate(bold_texts, 1):
            print(f"{i}. {text}")
        
        # 将结果保存到文件
        with open('bold_content.txt', 'w', encoding='utf-8') as f:
            for text in bold_texts:
                f.write(text + '\n')
                
        print("\n内容已保存到 bold_content.txt")
                
    except Exception as e:
        print(f"处理文档时出错: {str(e)}")

if __name__ == "__main__":
    main()