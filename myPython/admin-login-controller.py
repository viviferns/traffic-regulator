'''File name - admin-login-controller'''

'''This page is a Contoller for Admin Login'''



from flask import request

@app.route('/add_admin_control',methods=['POST'])
def add_admin_control():

	user_name=request.form['user_name']
	pass_word=request.form['pass_word']
	
	return render_template('/myHtml/home.html')

    '''obj_myDB=myDB()

    login_string=obj_myDB.admin_login(user_name,pass_word)

    if(login_string!="SUCCESSFUL"):

        return render_template('admin-login.html')

    else:

        return render_template('home.html')'''

    
'''Below statments have been kept as comments as not sure of what they do'''

if __name__ == '__main__':
	
	app.run(debug = True)
    
