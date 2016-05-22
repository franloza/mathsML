from flask import Flask, request
import numpy as np
app = Flask(__name__)

from sklearn.externals import joblib

# Cargo el modelo que he entrenado previamente.
sumRegr = joblib.load('models/sumModel.pkl')
subRegr = joblib.load('models/subModel.pkl')
mulRegr = joblib.load('models/mulModel.pkl')
divRegr = joblib.load('models/divModel.pkl')

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/predict/', methods=['GET'])
def predict():

    op1 = int(request.args.get('op1'))
    op2 = int(request.args.get('op2'))
    opType = request.args.get('opType')

    #debug
    debugSwitcher = {
        '+': 'sum',
        '-': 'sub',
        '*': 'mul',
        '/': 'div',
    }
    print (debugSwitcher.get(str(opType),'Nada'))


    switcher = {
        '+': sumRegr,
        '-': subRegr,
        '*': mulRegr,
        '/': divRegr,
    }

    regr = switcher.get(str(opType),False)

    #SumOperators = op1 + op2
    big10Op1 = op1 > 10
    big10Op2 = op2 > 10
    big50Op1 = op1 > 50
    big50Op2 = op2 > 50

    if (regr):
        input = np.array([op1,op2,big10Op1,big10Op2,big50Op1,big50Op2]).reshape(1, -1)
        print(input)
        return str(regr.predict(input))
    else:
    	return '';

if __name__ == "__main__":
    app.run(debug=True)

# Desde Rails podéis llamarlo así

# def estimate
#   self.estimation = HTTP.get("http://localhost:5000/predict/#{op1.to_f}/").to_s
# end
