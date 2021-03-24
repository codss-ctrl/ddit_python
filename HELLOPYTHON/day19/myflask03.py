from flask import Flask,render_template

app = Flask(__name__)

@app.route('/render')
def render():
    list = ["홍길동","전우치","이순신"]
    return render_template('index.html',list=list,str="대한민국위인들")

if __name__ == '__main__':
    app.run(debug=True)