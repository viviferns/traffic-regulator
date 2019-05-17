'''This file is controller to update temporary admin password'''

from flask import request

@app.route('/admin-temp-password-controller',methods=['POST'])
def add_admin_control():

    user_name=request.form['user_name']
    temp_password=request.form['temp_password']
    re_enter_password=request.form['re_enter_password']

    if(temp_password==re_enter_password):

        obj_myDB=myDB()

        verbose_string=""

        verbose_string=obj_myDB.update_temp_admin_password(user_name,temp_password)

        return render_template('verbose-page.html', verbose_string)

    
    '''Below statments have been kept as comments as not sure of what they do'''
    '''
    if __name__ == '__main__':
    app.run(debug = True)
    '''
