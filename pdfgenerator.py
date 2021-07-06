from fpdf import FPDF
import os
import webbrowser
class PdfReport:
    
    """
    df class to generate la pdf file having all info..

    """
    def __init__(self,filename):
        self.filename=filename
     
    def generate(self,bill,flatmate1,flatmate2):
        pdf=FPDF(orientation='P',unit='pt',format='A4')
        pdf.add_page()
        # inserting image
        pdf.image('files/house.png',w=45,h=45)
        pdf.set_font(family='Times',style='B',size=24)
        #insertion of title
        pdf.cell(w=0,h=100,border=0,txt="FlatMate's Bill",align='C',ln=1)
        #inserting period 
        pdf.set_font(family='Times',style='B',size=19)
        pdf.cell(w=100,h=60,txt="Period :",border=0)
        pdf.set_font(family='Times',size= 17)
        pdf.cell(w=130,h=60,txt=bill.period,border=0,ln=1)
        #insering content
        pdf.set_font(family='Times',size=17)
        pdf.cell(w=100,h=40,txt='{0:<15}{1:^3}'.format(flatmate1.name,'::'),border=0,ln=0)
        pdf.cell(w=100,h=40,txt=f"{flatmate1.amount_topay(bill,flatmate2)}",border=0,ln=1)        
        pdf.cell(w=100,h=40,txt='{0:<14}{1:^3}'.format(flatmate2.name,'::'),border=0,ln=0)
        pdf.cell(w=100,h=40,txt=f"{flatmate2.amount_topay(bill,flatmate1)}",border=0)
        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)