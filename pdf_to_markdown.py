from pypdf import PdfReader
import re
import os

def convert_pdf_to_markdown(pdf_path: str, output_dir: str = None) -> str:
    """
    Convert PDF file to Markdown format with enhanced error handling
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save the output file (optional)
    
    Returns:
        str: Path to the converted Markdown file
    """
    try:
        # Validate input file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
        # Create output directory if specified and doesn't exist
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Generate output path
        filename = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = os.path.join(output_dir if output_dir else os.path.dirname(pdf_path), 
                                 f"{filename}.md")
        
        # Read PDF and convert to markdown
        reader = PdfReader(pdf_path)
        markdown_content = []
        
        # Convert each page
        for page_num, page in enumerate(reader.pages, 1):
            try:
                # Extract text from page
                text = page.extract_text()
                
                # Basic formatting improvements
                # 1. Add page number as header
                markdown_content.append(f"\n## Page {page_num}\n")
                
                # 2. Process paragraphs
                paragraphs = text.split('\n\n')
                for paragraph in paragraphs:
                    # Clean up the paragraph
                    clean_para = re.sub(r'\s+', ' ', paragraph).strip()
                    if clean_para:
                        # Detect if it might be a header (heuristic approach)
                        if len(clean_para) < 100 and clean_para.endswith(':'):
                            markdown_content.append(f"\n### {clean_para}\n")
                        else:
                            markdown_content.append(f"\n{clean_para}\n")
                
            except Exception as e:
                print(f"Warning: Error processing page {page_num}: {str(e)}")
                markdown_content.append(f"\n> Error processing page {page_num}\n")
                continue
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))
        
        print(f"Successfully converted PDF to Markdown: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error converting PDF to Markdown: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    pdf_file = "认知和情感共情与负性情绪 情绪调节的作用机制.pdf"
    try:
        output_file = convert_pdf_to_markdown(pdf_file)
        print(f"Conversion completed. Output file: {output_file}")
    except Exception as e:
        print(f"Conversion failed: {str(e)}") 