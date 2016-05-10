from flask import Flask
app = Flask(__name__)


from sklearn.externals import joblib

  # Cargo el modelo que he entrenado previamente.
sumRegr = joblib.load('sumModel.pkl') 
subRegr = joblib.load('subModel.pkl') 
mulRegr = joblib.load('mulModel.pkl') 
divRegr = joblib.load('divModel.pkl') 

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/predict/', methods=['GET'])
def predict():
    op1 = request.args.get('op1')
    op2 = request.args.get('op2')
    opType = request.args.get('opType')

    switcher = {
        '+': sumRegr,
        '-': subRegr,
        '*': mulRegr,
        '/': divRegr,
    }
    regr = switcher.get(opType, false)
    if (regr) {
    	str(regr.predict([op1,op2]))
    }
    else {
    	return '';
    }

if __name__ == "__main__":

    app.run()

# Desde Rails podéis llamarlo así

# def estimate
#   self.estimation = HTTP.get("http://localhost:5000/predict/#{op1.to_f}/").to_s
# end