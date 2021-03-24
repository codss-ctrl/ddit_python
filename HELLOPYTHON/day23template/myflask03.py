from flask import Flask,render_template

app = Flask(__name__, static_url_path="", static_folder="static")


@app.route('/suser')
def suser():
    return render_template('suser.html',test="hello1")

@app.route('/survey')
def survey():
    return render_template('survey.html',test="hello2")

@app.route('/sdetail')
def sdetail():
    return render_template('sdetail.html',test="hello3")

if __name__ == '__main__':
    app.run(debug=True)