from flask import Flask,render_template,url_for
app=Flask(__name__)
@app.route("/")
def home():
	return render_template('home.html')
@app.route("/about")	
def about():
	return render_template('about.html')
@app.route("/result")	
def result():
	return render_template('result.html')
@app.route("/buypage")		
def buypage():
	return render_template('buypage.html')
@app.route("/cartpage")		
def cartpage():
	return render_template('cartpage.html')	
@app.route("/signin")    
def signin():
	return render_template('signin.html')	
if __name__ == '__main__': 
    app.run(debug=True) 