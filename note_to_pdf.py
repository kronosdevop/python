import os
from nbconvert import PDFExporter
from nbconvert.writers import FilesWriter

def convert_ipynb_to_pdf(notebook_path, output_path):
    pdf_exporter = PDFExporter()
    pdf_data, _ = pdf_exporter.from_filename(notebook_path)
    writer = FilesWriter(build_directory=os.path.dirname(output_path))
    written, resources = writer.write(pdf_data, resources={}, notebook_name=os.path.basename(output_path))
    return written[0]

notebook_path = "sonar.ipynb"  
output_path = "sonar_ml.pdf"  

pdf_path = convert_ipynb_to_pdf(notebook_path, output_path)
if pdf_path:
    print("PDF created successfully at:", pdf_path)
else:
    print("PDF creation failed.")


