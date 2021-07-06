
from apartment import Bill,FlatMate
from pdfgenerator import PdfReport
pe=input("Give the month and year of bill:")
am=float(input("Enter your Bill amount:"))
fmate1=input("Enter yor name:")
mate1_indays=int(input("Enter the number of days you stayed in:"))
fmate2=input("Enter your flat mates name:")
mate2_indays=int(input("Enter the number of days your flatmate stayed in:"))
the_bill=Bill(am,pe)
flatmate1=FlatMate(fmate1,mate1_indays)
flatmate2=FlatMate(fmate2,mate2_indays)
pf=PdfReport("{} bill.pdf".format(pe))
pf.generate(the_bill,flatmate1,flatmate2)
