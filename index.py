from flask import request

@app.route('/index',methods=['POST'])
def index():

	return render_template('index.html')
	
if __name__ == '__main__':
    app.run(debug = True)