from flask import Flask,render_template, jsonify, request

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/')
@app.route('/sample')
def render():
    list = []
   
    list.append({'survey_id':'1','s_seq':'1','question':'맛있는_ 식당은?','a1':'맥도날드','a2':'요우란','a3':'사쿠사쿠', 'a4':'한성식당','c1':1,'c2':2,'c3':3,'c4':4})
    list.append({'survey_id':'1','s_seq':'1','question':'당신은_ 누굴 좋아해?','a1':'송중기','a2':'남주혁','a3':'심하은', 'a4':'심은하','c1':1,'c2':1,'c3':1,'c4':1})
    return render_template('sample.html',list=list,enumerate=enumerate)

@app.route('/sample2')
def render_sample2():
    list = []
   
    list.append({'survey_id':'1','s_seq':'1','question':'맛있는_ 식당은?','a1':'맥도날드','a2':'요우란','a3':'사쿠사쿠', 'a4':'한성식당','c1':1,'c2':1,'c3':1,'c4':1})
    list.append({'survey_id':'1','s_seq':'1','question':'당신은_ 누굴 좋아해?','a1':'송중기','a2':'남주혁','a3':'심하은', 'a4':'심은하','c1':1,'c2':1,'c3':1,'c4':1})
    return render_template('sample2.html',list=list,enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    