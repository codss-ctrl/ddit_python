from flask import Flask,request


app = Flask(__name__)

@app.route('/gugu')
def gugu():
    dan = request.args.get('dan')
    int_dan = int(dan)
    rtn = ""
    rtn += dan+"*"+str(1)+"="+str(1*int_dan)+"<br>\n"
    rtn += dan+"*"+str(2)+"="+str(2*int_dan)+"<br>\n"
    rtn += dan+"*"+str(3)+"="+str(3*int_dan)+"<br>\n"
    rtn += dan+"*"+str(4)+"="+str(4*int_dan)+"<br>\n"
    rtn += dan+"*"+str(5)+"="+str(5*int_dan)+"<br>\n"
    rtn += dan+"*"+str(6)+"="+str(6*int_dan)+"<br>\n"
    rtn += dan+"*"+str(7)+"="+str(7*int_dan)+"<br>\n"
    rtn += dan+"*"+str(8)+"="+str(8*int_dan)+"<br>\n"
    rtn += dan+"*"+str(9)+"="+str(9*int_dan)+"<br>\n"

    
    return rtn

if __name__ == '__main__':
    app.run(debug=True)