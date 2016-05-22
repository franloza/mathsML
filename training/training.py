from sklearn import linear_model
from sklearn.externals import joblib

def train (df):

	sumData = df[(df.Operator == 1)]
	sumTarget = sumData.Time;
	sumData = sumData.drop(sumData.columns[[1,3]], axis=1)

	subData = df[(df.Operator == 2)]
	subTarget = subData.Time;
	subData = subData.drop(subData.columns[[1,3]], axis=1)

	mulData = df[(df.Operator == 3)]
	mulTarget = mulData.Time;
	mulData = mulData.drop(mulData.columns[[1,3]], axis=1)

	divData = df[(df.Operator == 4)]
	divTarget = divData.Time;
	divData = divData.drop(divData.columns[[1,3]], axis=1)

	print(mulData,mulTarget)

	#Train models
	sumModel = linear_model.Lasso(alpha = 0.1,max_iter=1000)
	subModel = linear_model.Lasso(alpha = 0.1,max_iter=1000)
	mulModel = linear_model.Lasso(alpha = 0.1,max_iter=1000)
	divModel = linear_model.Lasso(alpha = 0.1,max_iter=1000)
	sumModel.fit(sumData,sumTarget)
	subModel.fit(subData,subTarget)
	mulModel.fit(mulData,mulTarget)
	divModel.fit(divData,divTarget)

	#Export models
	print ("Exporting models...")
	joblib.dump(sumModel, 'models/sumModel.pkl')
	joblib.dump(subModel, 'models/subModel.pkl')
	joblib.dump(mulModel, 'models/mulModel.pkl')
	joblib.dump(divModel, 'models/divModel.pkl')
