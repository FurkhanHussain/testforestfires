import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application=Flask(__name__)
app=application

##importing ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('model/ridge.pkl','rb'))
standard_scaler=pickle.load(open('model/scaler.pkl','rb'))
logistic=pickle.load(open('model/logistic.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        WS=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        DC=float(request.form.get('DC'))
        BUI=float(request.form.get('BUI'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        

        new_data_scaled=standard_scaler.transform([[Temperature,RH,WS,Rain,FFMC,DMC,DC,ISI,Classes,Region,BUI]])
        result=ridge_model.predict(new_data_scaled)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')
    
@app.route('/thyroid',methods=['GET','POST'])
def predict_thyroid():
    if request.method=="POST":
        Age=float(request.form.get('Age'))
        Gender=float(request.form.get('Gender'))
        HxRadiothreapy=float(request.form.get('Hx Radiothreapy'))
        Focality=float(request.form.get('Focality'))
        Risk=float(request.form.get('Risk'))
        T=float(request.form.get('T'))
        N=float(request.form.get('N'))
        M=float(request.form.get('M'))
        Stage=float(request.form.get('Stage'))
        Recurred=float(request.form.get('Recurred'))
        
        logistic_data_scaled=standard_scaler.transform([[Age,Gender,HxRadiothreapy,Focality,Risk,T,N,M,Stage,Recurred]])
        result=ridge_model.predict(logistic_data_scaled)
        return render_template('thyroid.html',results=result[0])
    else:
        return render_template('thyroid.html')
    

if __name__=="__main__":
    app.run(host="0.0.0.0")