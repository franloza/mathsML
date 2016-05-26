from sklearn import cross_validation, linear_model
import numpy as np

def benchmark (df):

predictors = ["LinearRegression","Lasso"]
predictorsMapper = {
	'LinearRegression': linear_model.LinearRegression(),
    'Lasso': linear_model.Lasso(alpha = 0.1,max_iter=1000)
}

loo = cross_validation.LeaveOneOut(len(target))

#Separate data by operators
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

for p in predictors:
	scoreTotal = 0
	sumRegr = predictorsMapper.get(p,False)
	subRegr = predictorsMapper.get(p,False)
	mulRegr = predictorsMapper.get(p,False)
	divRegr = predictorsMapper.get(p,False)
	scoreSum = cross_validation.cross_val_score(sumRegr, sumData, sumTarget, scoring='mean_squared_error', cv=loo)
	scoreSub = cross_validation.cross_val_score(subRegr, sumData, sumTarget, scoring='mean_squared_error', cv=loo)
	scoreMul = cross_validation.cross_val_score(mulRegr, sumData, sumTarget, scoring='mean_squared_error', cv=loo)
	scoreDiv = cross_validation.cross_val_score(divRegr, sumData, sumTarget, scoring='mean_squared_error', cv=loo)
	scoreTotal = scoreSum + scoreSub + scoreMul + scoreDiv
	print ("Mean Squared Error (by operator):")
	print ("\tSum regressor" + scoreSum)
	print ("\tSubstraction regressor" + scoreSub)
	print ("\tMultiplication regressor" + scoreMul)
	print ("\tDivision regressor" + scoreDiv)
	print ("\tTotal: " + scoreTotal)