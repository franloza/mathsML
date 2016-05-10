from sklearn import linear_model
from sklearn.externals import joblib 

def train (data):

	#Train models
	model = linear_model.Lasso(alpha = 0.1,max_iter=1000)
	sumModel=subModel=mulModel=divModel= model
	sumModel.fit(data[(data.opType == '+')])
	subModel.fit(data[(data.opType == '-')])
	mulModel.fit(data[(data.opType == '*')])
	divModel.fit(data[(data.opType == '/')])

	#Export models
	joblib.dump(sumModel, 'sumModel.pkl')
	joblib.dump(sumModel, 'subModel.pkl')
	joblib.dump(sumModel, 'mulModel.pkl')
	joblib.dump(sumModel, 'divModel.pkl')



