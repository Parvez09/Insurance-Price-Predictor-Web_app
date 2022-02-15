from flask import Flask, request, render_template
import requests
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Insurance_rfr_Pipe_Sc.pkl", "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form["age"])
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])

    #Sex(Gender)
        sex = request.form["sex"]
        if(sex=="male"):
            male=1
        else:
            female=0
        #Smoker
        smoker = request.form["smoker"]
        if(smoker=="yes"):
            yes=1
        else:
            no=0
        #Region
        region = request.form["region"]
        if(region=="southwest"):
            southwest = 1
            southeast = 0
            northwest = 0
            northeast = 0 
        elif(region=="southeast"):
            southwest = 0
            southeast = 1
            northwest = 0
            northeast = 0
        elif(region=="northwest"):
            southwest = 0
            southeast = 0
            northwest = 1
            northeast = 0  
        else:
            southwest = 0
            southeast = 0
            northwest = 0
            northeast = 1 

        prediction = model.predict(pd.DataFrame([[age,sex,bmi,children,smoker,region]],columns=['age','sex','bmi','children','smoker','region']))

        output = round(prediction[0],2)
        if(output<0):
            return render_template('index.html',prediction_text="Sorry, You did not select for Insurance")
        else:
            return render_template('index.html',prediction_text="Your Insurance Price is Rs. {}".format(output))

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)








            

        
        
        




    

