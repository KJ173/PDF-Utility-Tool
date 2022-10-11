from PdfEditor import PdfEditor

editor = PdfEditor('test.pdf', 'letter')
editor.drawString(3, 3, 'HELLO!')
editor.save('test-gen.pdf')
