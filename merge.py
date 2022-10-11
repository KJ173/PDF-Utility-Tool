from PyPDF2 import PdfFileReader,PdfFileMerger

pdf_file1=(PdfFileReader("1.pdf"))
pdf_file2=(PdfFileReader("2.pdf"))

output=PdfFileMerger()
output.append(pdf_file1)
output.append(pdf_file2)

output.write("merged.pdf")
