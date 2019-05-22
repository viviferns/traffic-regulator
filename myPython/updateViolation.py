#This page is controller to payment page

from flask import request

class updateViolation:

    def update_violation():

        time_stamp=request.form['time_stamp']

        obj_myDB=myDB()

        verbose_string=obj_myDB.update_violation_record(time_stamp)

        return render_template('verbose-page.html', verbose_string)

