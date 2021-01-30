"""
生成PDF
html转pdf
需要安装wkhtmltopdf软件，在https://wkhtmltopdf.org/downloads.html
pip install pdfkit
"""
import pdfkit

pdfkit.from_url('https://www.baidu.com/', 'out1.pdf')
# pdfkit.from_file('test.html', 'out2.pdf')
pdfkit.from_string('Hello', 'out3.pdf')
