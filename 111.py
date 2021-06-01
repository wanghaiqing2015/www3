import traceback
import pdfkit
from platform import system

def get_pdf(report_uuid, html_content):
    
    # html_content = html_content.replace('class="new_table"', 'class="table table-striped table-bordered"')
    # html_content = html_content.replace("class='new_table'", 'class="table table-striped table-bordered"')
    
    filename = "{}.pdf".format(report_uuid)
    try:
        options = {
            'page-size': 'A3', # A3、A4各有优缺点。A3看不清文字，但是不会太拥挤。
            'encoding': 'UTF-8',
            'javascript-delay': '8000',
            'margin-top': '0.5in',          
            'margin-bottom': '0.5in',       
            'margin-left': '0in',           
            'margin-right': '0in',          
            'quiet': '',
            'footer-center' : '第[page]页',
            # 'disable-smart-shrinking': '', #禁止使用WebKit的智能战略收缩，使像素/ DPI比没有不变
         }
 
        if system()=='Windows':
            config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        else:
            config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
            
        pdf_content = pdfkit.from_string(html_content, False, options=options, configuration=config)
    except Exception as e:
        exstr = traceback.format_exc()
        print(exstr)
        pdf_content = b''
        
    return pdf_content, filename
    

f = open("111.html", "r", encoding="utf8")
html_content = f.read()
f.close()

pdf_content, filename = get_pdf("11111111", html_content)

f = open("111111.pdf", "wb")
f.write(pdf_content)
f.close()