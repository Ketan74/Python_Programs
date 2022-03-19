""""""""""""""""""""""""""""""""
" Student Name:- Ketan Tiwari  "
" Student ID:- 20CE149         "
""""""""""""""""""""""""""""""""

"""Aim:-
    --> Generate PDF file of your 3rd Semester Mark-sheet."""

# ----------------------------------------------------------------------------------------------------------------------
# ***** SOLUTION ***** #
# ----------------------------------------------------------------------------------------------------------------------
from reportlab.pdfgen import canvas

write = canvas.Canvas("20CE149_Sem3_Result.pdf")

write.setFont('Times-Roman', 32)
write.drawString(30, 770, 'CHARUSAT')

write.setFontSize(6.2)
write.drawString(30, 760, 'CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY')

write.setFont('Helvetica-Bold', 12)
write.drawString(220, 782, 'CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY')

write.setFont('Helvetica', 8.8)
write.drawString(220, 770, 'CHARUSAT Campus, Changa - 388421 , Off Nadiad - Petlad Highway, Gujarat (India)')
write.drawString(220, 760, 'Ph. # +91-2697-265001,265021 Fax. # +91-2697-265007')
write.drawString(220, 750, 'Web : www.charusat.ac.in | Email : info@charusat.ac.in')
write.drawString(100, 730, '(Formed under Gujarat State Act No. 8 of 2009, and degreed conferred u/s 22 of UGC Act. 1956)')
write.drawString(220, 720, '(Accredited with Grade \'A\' by NAAC)')

write.setFont('Helvetica-Bold', 18)
write.drawString(175, 700, 'SEMESTER GRADE REPORT')
write.setFont('Helvetica-Bold', 16)
write.drawString(106, 670, 'FACULTY OF TECHNOLOGY AND ENGINEERING')

write.setFont('Times-Roman', 14)
write.drawString(30, 640, 'No. :R4257')
write.drawString(430, 640, 'Date : 22/12/2021')
write.drawString(30, 620, 'Name : TIWARI KETANKUMAR CHANDRAKANT')
write.drawString(30, 600, 'Programme : B.TECH.(COMPUTER)')
write.drawString(430, 600, 'ID.No. : 20CE149')
write.drawString(30, 580, 'Month & Year : November 2021')
write.drawString(280, 580, 'Semester : 3')
write.drawString(430, 580, 'Aadhar : 871315826737')

write.drawString(220, 540, 'Course')

write.drawString(30, 520, 'CE244')
write.drawString(100, 520, 'SOWFTWARE GROUP PROJECT-I')
write.drawString(320, 520, 'PRACTICAL')

write.drawString(30, 500, 'CE251')
write.drawString(100, 500, 'JAVA PROGRAMMING')
write.drawString(320, 500, 'THEORY')
write.drawString(320, 480, 'PRACTICAL')

write.drawString(30, 460, 'CE252')
write.drawString(100, 460, 'DIGITAL ELECTRONICS')
write.drawString(320, 460, 'THEORY')
write.drawString(320, 440, 'PRACTICAL')

write.drawString(30, 420, 'CE257')
write.drawString(100, 420, 'DATA COMMUNICATION')
write.drawString(320, 420, 'THEORY')
write.drawString(100, 400, ' & NETWORK')
write.drawString(320, 400, 'PRACTICAL')

write.drawString(30, 380, 'HS121.02A')
write.drawString(100, 380, 'CREATIVIY, PROBLEM SOLVING')
write.drawString(100, 360, 'AND INOVATION')
write.drawString(320, 380, 'PRACTICAL')

write.drawString(30, 340, 'IT281.01')
write.drawString(100, 340, 'ICT RESOURCES & MULTIMEDIA')
write.drawString(320, 340, 'PRACTICAL')

write.drawString(30, 320, 'MA253')
write.drawString(100, 320, 'DISCRETE MATHAMATICS')
write.drawString(100, 300, 'AND ALGEBRA')
write.drawString(320, 320, 'THEORY')

write.drawString(420, 540, 'Credit')

write.drawString(425, 520, '2.00')

write.drawString(425, 500, '3.00')
write.drawString(425, 480, '2.00')

write.drawString(425, 460, '3.00')
write.drawString(425, 440, '1.00')

write.drawString(425, 420, '4.00')
write.drawString(425, 400, '1.00')

write.drawString(425, 380, '2.00')
write.drawString(425, 340, '2.00')

write.drawString(425, 320, '4.00')

write.drawString(500, 540, 'Grade')

write.drawString(510, 520, 'AA')

write.drawString(510, 500, 'BB')
write.drawString(510, 480, 'AA')

write.drawString(510, 460, 'AA')
write.drawString(510, 440, 'BB')

write.drawString(510, 420, 'BB')
write.drawString(510, 400, 'AA')

write.drawString(510, 380, 'AA')

write.drawString(510, 340, 'AA')

write.drawString(510, 320, 'AB')

write.drawString(90, 250, 'Semester Performance')
write.drawString(30, 230, 'Total Credits')
write.drawString(50, 210, '24.00')
write.drawString(120, 230, 'Credit Earned')
write.drawString(140, 210, '24.00')
write.drawString(210, 230, 'SGPA')
write.drawString(215, 210, '9.17')

write.drawString(320, 250, 'Cumilative Performance')
write.drawString(260, 230, 'Total Credits')
write.drawString(280, 210, '61.00')
write.drawString(350, 230, 'Credit Earned')
write.drawString(370, 210, '61.00')
write.drawString(440, 230, 'CGPA')
write.drawString(445, 210, '9.48')

write.drawString(515, 250, 'Class')
write.drawString(500, 220, 'Distinction')

write.drawString(30, 180, 'Previous SGPA : 9.63')
write.drawString(230, 180, 'Previous CGPA : 9.68')
write.drawString(420, 180, 'No. of BackLog : 0')

write.setFont('Helvetica', 24)
write.drawString(450, 140, 'Sign')
write.setFont('Times-Roman', 14)
write.drawString(448, 120, 'Registrar')

write.setFont('Helvetica', 9)
write.drawString(240, 160, 'EX/REG/CE/NT/3/21/034')

write.setFont('Helvetica', 7)
write.drawString(210, 30, 'NB : Any infringement / tampering of this document is a legal offence.')
write.drawString(500, 30, 'Details overleaf')
write.save()