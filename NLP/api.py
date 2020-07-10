from flask import Flask, request, render_template,jsonify
app = Flask(__name__)
def do_something(text1,option):
    import numpy as np
    import pandas as pd
    df = pd.read_csv('C:\\Users\\Phoenix-PC\\Desktop\\bbc\\Project\\bbc-text.csv')
    import string
    import gensim
    from gensim.models.doc2vec import TaggedDocument, Doc2Vec
    print(option)
    if(option=='t'):
        model = Doc2Vec.load('C:\\Users\\Phoenix-PC\\Desktop\\bbc\\Project\\modelt')
        df=df[df.category=='tech']
    if(option=='b'):
        model = Doc2Vec.load('C:\\Users\\Phoenix-PC\\Desktop\\bbc\\Project\\modelb')
        df=df[df.category=='business']
    if(option=='s'):
        model = Doc2Vec.load('C:\\Users\\Phoenix-PC\\Desktop\\bbc\\Project\\models')
        df=df[df.category=='sport']
    if(option=='e'):
        model = Doc2Vec.load('C:\\Users\\Phoenix-PC\\Desktop\\bbc\\Project\\modele')
        df=df[df.category=='entertainment']
    if(option=='p'):
        model = Doc2Vec.load('C:\\Users\\Phoenix-PC\\Desktop\\bbc\\Project\\modelp')
        df=df[df.category=='politics']
    q = text1.split()
    new_vector = model.infer_vector(q, alpha=0.025, min_alpha=0.01, steps=100)
    sims = model.docvecs.most_similar([new_vector],topn=5)
    k= []
    for x in sims:
        k.append(x[0])
    dicttext = {}
    j=0
    td = list(df.iloc[k].text)
    for i in k:
        i=str(i)
        dicttext[i]= td[j]
        j=j+1
    return dicttext
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    option = request.form['category']
    combine = do_something(text1,option)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    #return jsonify(result=result)
    return jsonify(combine)
if __name__ == '__main__':
    app.run(debug=True)