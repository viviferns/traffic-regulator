'''File name - add-admin-controller'''

'''This page is a Contoller to Add Admin'''

from flask import request

@app.route('/add-admin-controller',methods=['POST'])
def add-admin-controller():

    adm_name=request.form['adm_name']
    adm_mobNo=request.form['adm_mobNo']
    adm_userName=request.form['adm_userName']
    adm_password=request.form['adm_password']
    
    verbose="Admin could not be Added"

    obj_myDB=myDB()

    verbose=obj_myDB.add_admin(adm_name,adm_mobNo,adm_userName,adm_password)

    return render_template('verbose-page.html', verbose)

'''Below statments have been kept as comments as not sure of what they do'''
'''
    if __name__ == '__main__':
    app.run(debug = True)
'''

''' Do not copy the below since the statements are not getting deleted'''
