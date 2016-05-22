from sklearn import cross_validation, linear_model, ensemble, tree
import numpy as np

def benchmark (df):

	predictors = ["LinearRegression","Lasso","AdaBoostRegressor","RandomForestRegressor","DecisionTreeRegressor"]
	predictorsMapper = {
		'LinearRegression': linear_model.LinearRegression(),
	    'Lasso': linear_model.Lasso(alpha = 0.1,max_iter=1000),
		'AdaBoostRegressor': ensemble.AdaBoostRegressor(),
		'RandomForestRegressor': ensemble.RandomForestRegressor(),
		'DecisionTreeRegressor': tree.DecisionTreeRegressor()
	}


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

	sumLoo = cross_validation.LeaveOneOut(len(sumTarget))
	subLoo = cross_validation.LeaveOneOut(len(subTarget))
	mulLoo = cross_validation.LeaveOneOut(len(mulTarget))
	divLoo = cross_validation.LeaveOneOut(len(divTarget))

	for p in predictors:
		print ("Benchmarking " + p + "...")
		scoreTotal = 0
		sumRegr = predictorsMapper.get(p,False)
		subRegr = predictorsMapper.get(p,False)
		mulRegr = predictorsMapper.get(p,False)
		divRegr = predictorsMapper.get(p,False)
		scoreSum = abs(cross_validation.cross_val_score(sumRegr, sumData, sumTarget, scoring='mean_squared_error', cv=sumLoo).mean())
		scoreSub = abs(cross_validation.cross_val_score(subRegr, subData, subTarget, scoring='mean_squared_error', cv=subLoo).mean())
		scoreMul = abs(cross_validation.cross_val_score(mulRegr, mulData, mulTarget, scoring='mean_squared_error', cv=mulLoo).mean())
		scoreDiv = abs(cross_validation.cross_val_score(divRegr, divData, divTarget, scoring='mean_squared_error', cv=divLoo).mean())
		scoreTotal = scoreSum + scoreSub + scoreMul + scoreDiv
		print ("Mean Squared Error (by operator):")
		print ("\tSum regressor: " + str(scoreSum))
		print ("\tSubstraction regressor: " + str(scoreSub))
		print ("\tMultiplication regressor: " + str(scoreMul))
		print ("\tDivision regressor: " + str(scoreDiv))
		print ("\tTotal: " + str(scoreTotal))
