from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx import Document

doc = Document('demo.docx')
paragraph = doc.add_paragraph("首行缩进2字符alignmentalignsssdddddddddddd"
                              "dddddddddddddddsssssssssssssss"
                              "sssssssssssssssssssssssssssssssssddddddddd"
                              "ddddddddddddddddddddddddddddssmentali")
# paragraph.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
#
# doc.save("demo.docx")





from docx.shared import Inches
from docx.shared import Pt
paragraph.paragraph_format.first_line_indent = Inches(0.3)  # 首行缩进2个字符  inches=0.3
paragraph.paragraph_format.line_spacing = 1.5


doc.save("demo.docx")
