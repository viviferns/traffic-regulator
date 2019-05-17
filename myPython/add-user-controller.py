'''File name - add-user-controller'''

'''This page is a Contoller to Add User'''

from flask import request

@app.route('/add-user-controller',methods=['POST'])
def add_user_control():

    name_of_user=request.form['name_of_user']
    mobile_number=request.form['mobile_number']
    email_address=request.form['email_address']
    car_number=request.form['car_number']
    
    verbose="User could not be Added"

    obj_myDB=myDB()

    verbose=obj_myDB.user_details(name_of_user,mobile_number,email_address,car_number)

    return render_template('verbose-page.html', verbose)

'''Below statments have been kept as comments as not sure of what they do'''
'''
    if __name__ == '__main__':
    app.run(debug = True)
'''
