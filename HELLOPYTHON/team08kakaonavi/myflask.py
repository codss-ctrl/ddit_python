import requests
from flask import Flask,  render_template

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/navi')
def navi():
    return render_template('kakaonavi.html')

# main()
if __name__ == "__main__":
    app.run(host='192.168.41.3',debug=True)
    
    