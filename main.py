# flask skt-learn pandas pickle-mixin 
from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

data = pd.read_csv('Cleaned data BHH NEW.csv')
pq = pickle.load(open('Final BHPP.pkl','rb'))


@app.route("/")
def index():

    locations = sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict',methods=['POST'])
def predict():

    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    print(location,bhk,bath,sqft)
    df = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    predi = pq.predict(df)[0]  
    print(predi)  
    return str(np.round(predi,2))
    #return jsonify({'Price':predi})

if __name__ == "__main__":
    app.run(debug=True)