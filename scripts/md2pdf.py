import sys
import os
import subprocess
import re
import urllib.parse

# ==========================================
# 1. AUTO-DEPENDENCY INSTALLATION ENGINE
# ==========================================
def install_dependencies():
    """
    Dynamically checks and installs required packages using the exact 
    Python executable currently running the script (sys.executable).
    This completely avoids pip vs pip3 path conflicts on macOS/Linux.
    """
    dependencies = {
        "markdown": "markdown>=3.5.1",
        "xhtml2pdf": "xhtml2pdf>=0.2.11"
    }
    
    for module_name, pip_package in dependencies.items():
        try:
            __import__(module_name)
        except ImportError:
            print(f"[{module_name}] not found. Auto-installing {pip_package} into the current Python environment...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_package])
                print(f"Successfully installed {pip_package}.")
            except Exception as e:
                print(f"Failed to install {pip_package}. Error: {e}")
                sys.exit(1)

# Ensure dependencies are installed before importing them globally
install_dependencies()

# Now it is safe to import external libraries
import markdown
from xhtml2pdf import pisa
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ==========================================
# 2. MATH RENDERING ENGINE
# ==========================================
def render_math_cloud(text):
    """
    Converts LaTeX math blocks ($...$ and $$...$$) into CodeCogs image tags.
    This allows xhtml2pdf to download and embed high-quality math images.
    """
    # Block math $$...$$
    def block_repl(match):
        math_expr = match.group(1).strip()
        encoded = urllib.parse.quote(math_expr)
        url = f"https://latex.codecogs.com/png.image?\\dpi{{300}}\\bg{{white}}{encoded}"
        return f'<div style="text-align: center; margin: 10px 0;"><img src="{url}" /></div>'
        
    text = re.sub(r'\$\$(.+?)\$\$', block_repl, text, flags=re.DOTALL)
    
    # Inline math $...$
    def inline_repl(match):
        math_expr = match.group(1).strip()
        encoded = urllib.parse.quote(math_expr)
        url = f"https://latex.codecogs.com/png.image?\\dpi{{300}}\\bg{{white}}{encoded}"
        return f'<img src="{url}" style="vertical-align: middle; height: 1.5em;" />'
        
    text = re.sub(r'\$(.+?)\$', inline_repl, text)
    return text

# ==========================================
# 3. PDF GENERATION LOGIC
# ==========================================
def convert_md_to_pdf(md_filepath, pdf_filepath, math_mode='local'):
    # Read Markdown
    with open(md_filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Pre-process math if cloud mode is enabled
    if math_mode == 'cloud':
        print("Math Mode: Cloud (Converting LaTeX to online images...)")
        md_text = render_math_cloud(md_text)
    else:
        print("Math Mode: Local (Rendering as raw unicode text...)")

    # Convert to HTML
    html_body = markdown.markdown(
        md_text, 
        extensions=['tables', 'fenced_code', 'nl2br']
    )
    
    # 100% Offline Robust Font Registration
    # Look for the packaged Songti.ttc in the same directory as this script
    font_path = os.path.join(os.path.dirname(__file__), "Songti.ttc")
    font_face_css = ""
    font_family = "Helvetica, Arial, sans-serif"
    
    if os.path.exists(font_path):
        try:
            # .ttc files are TrueType Collections. We extract the first font (subfontIndex=0)
            pdfmetrics.registerFont(TTFont('Songti', font_path, subfontIndex=0))
            font_face_css = f"""
            @font-face {{
                font-family: 'Songti';
                src: url('{font_path}');
            }}
            """
            font_family = "'Songti', Helvetica, Arial, sans-serif"
        except Exception as e:
            print(f"Font registration failed. Will fallback to defaults. Error: {e}")
    else:
        print(f"Warning: Packaged font {font_path} not found. Chinese characters may not render correctly.")

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            {font_face_css}
            @page {{
                size: a4 portrait;
                margin: 2cm;
            }}
            body {{
                font-family: {font_family};
                font-size: 11pt;
                line-height: 1.6;
                color: #333333;
                word-wrap: break-word;
                word-break: break-all;
            }}
            h1, h2, h3 {{
                color: #1a1a1a;
                margin-top: 1.5em;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 1em;
            }}
            th, td {{
                border: 1px solid #dddddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            code {{
                background-color: #f8f8f8;
                padding: 2px 4px;
                font-family: monospace;
            }}
            pre {{
                background-color: #f8f8f8;
                padding: 10px;
                border: 1px solid #ccc;
                white-space: pre-wrap;
            }}
            img {{
                max-width: 100%;
            }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # Generate PDF
    base_dir = os.path.dirname(os.path.abspath(md_filepath))
    os.makedirs(os.path.dirname(os.path.abspath(pdf_filepath)), exist_ok=True)
    
    # link_callback resolves local images correctly
    def link_callback(uri, rel):
        if uri.startswith('http://') or uri.startswith('https://'):
            return uri
        return os.path.join(base_dir, uri)
    
    with open(pdf_filepath, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(
            html_content,
            dest=result_file,
            link_callback=link_callback
        )

    if pisa_status.err:
        print(f"Error occurred during PDF generation.")
        return False
    else:
        print(f"Successfully generated PDF at: {pdf_filepath}")
        return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF (100% Offline with Cloud Math option).")
    parser.add_argument("--input", required=True, help="Input markdown file path.")
    parser.add_argument("--output", required=True, help="Output PDF file path.")
    parser.add_argument("--math-mode", choices=['local', 'cloud'], default='local', help="Math rendering strategy.")
    args = parser.parse_args()
    
    convert_md_to_pdf(args.input, args.output, args.math_mode)
