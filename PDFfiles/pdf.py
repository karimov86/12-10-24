import PyPDF2
import sys
import os
from pathlib import Path

# Function to apply watermark to a single PDF
def watermark(pdf_path: Path, watermark_path: Path, output_dir: Path):
    reader = PyPDF2.PdfReader(pdf_path)
    writer = PyPDF2.PdfWriter()

    # Applying watermark to each page
    for page in reader.pages:
        stamp_page = PyPDF2.PdfReader(watermark_path).pages[0]
        stamp_page.merge_page(page)
        stamp_page.mediabox = page.mediabox
        writer.add_page(stamp_page)

    # Save the watermarked PDF to an output directory
    output_path = output_dir / pdf_path.name
    with open(output_path, 'wb') as output_pdf:
        writer.write(output_pdf)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python script.py <watermark.pdf> <output_directory>")
        sys.exit(1)

    watermark_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process all PDFs in the current directory
    for file_name in os.listdir():
        if file_name.lower().endswith(".pdf"):
            pdf_path = Path(file_name)
            watermark(pdf_path, watermark_path, output_dir)

    print(f"Watermarked PDFs saved in {output_dir}")