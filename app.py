from flask import Flask,request, render_template
app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
@app.route("/flask2")
def show_firstPage():
    return render_template("index2.html")

@app.route("/nextPage",methods=['GET', 'Post'])
def next_page():
    return render_template("nextPage.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")