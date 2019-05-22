#This page is controller to payment-details page

from fpdf import FPDF
from flask import request

class printPdf:

    def print_Pdf():

        obj_myDB=myDB()

        time_stamp,car_no,loc_name,fine_amount,email_id,verbose_string=""

        mob_number=request.form['mob_number']
        selected_function=request.form['number_code']

        if(selected_function=="generate-pdf"):

            result=obj_myDB.fetch_record(mob_number)

            if (result=="Error while fetching record"):

                verbose_string=result
                return render_template('verbose-page.html', verbose_string)

            else:
            
                for row in result:
                    time_stamp=row["TIME_STAMP"]
                    car_no=row["CAR_NO"]
                    loc_name=row["LOC_NAME"]
                    fine_amount=row["FINE_AMOUNT"]
                    violation_image=row["VIOLATION_IMAGE"]
                    email_id=row["EMAIL_ID"]

                    pdf_name=time_stamp,".pdf"

                verbose_string="PDF sent to Email Address:'",email_id,","

                pdf = FPDF()
                # compression is not yet supported in py3k version
                pdf.compress = False
                pdf.add_page()
                # Unicode is not yet supported in the py3k version; use windows-1252 standard font
                pdf.set_font('Arial', '', 14)  
                pdf.ln(10)
                pdf.write("Time Stamp/Unique Id:     ",time_stamp,"\n")
                pdf.write("Car Number:               ",car_no,"\n")
                pdf.write("Location:                 ",loc_name,"\n")
                pdf.write("Fine Amount:              ",fine_amount,"\n")
                pdf.write("Image:\n",violation_image)
                pdf.image("pyfpdf/tutorial/logo.png", 50, 50)
                pdf.output(pdf_name, 'F')

                return render_template('verbose-page.html', verbose_string)

        elif(selected_function=="payment"):

            if (result=="Error while fetching record"):

                verbose_string=result
                return render_template('verbose-page.html', verbose_string)

            else:
            
                result=obj_myDB.fetch_record(mob_number)

                return render_template('payment.html', result)
