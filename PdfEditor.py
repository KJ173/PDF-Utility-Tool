from PyPDF2 import PdfFileReader, PdfFileWriter
import io
from reportlab.lib.pagesizes import letter, legal
from reportlab.pdfgen import canvas
import io


class PdfEditor(object):
    '''Class for modifying a previously existing PDF's.
    note::
    Currently only works 1 page PDF's.
    Origin is on LOWER left corner.
    '''

    def __init__(self, filename, pageSize, strict=True):
        '''Args:
            filename (str): Location of the original PDF.
            pageSize (str): Either letter or legal.
        '''
        super(PdfEditor, self).__init__()
        self.pdf = PdfFileReader(filename, strict=strict).getPage(0)
        self.content = io.StringIO()
        self.parser = canvas.Canvas(self.content, pagesize=(letter if pageSize == 'letter' else legal))

    def drawString(self, x, y, content):
        '''Args:
            x (int): X coordinate.
            y (int): Y coordinate.
            content (str): String to be written.
        '''
        self.parser.drawString(x, y, content)

    def setFontSize(self, size):
        '''Args:
            size (int): Select size of the font.
        '''
        self.parser.setFontSize(int(size))

    def save(self, filename, write_file=True):
    
        self.parser.save()
        self.content.seek(0)
        text = PdfFileReader(self.content)
        output = PdfFileWriter()
        self.pdf.mergePage(text.getPage(0))
        output.addPage(self.pdf)
        if write_file:
            outputStream = open(filename, 'wb')
            output.write(outputStream)
        else:
            outputStream = io.BytesIO()
            output.write(outputStream)
        return outputStream
