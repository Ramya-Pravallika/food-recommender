import numpy as np




def fit_theta(pre_experiment_metric, covariate):
theta = np.cov(pre_experiment_metric, covariate)[0, 1] / np.var(covariate)
return theta


def apply_cuped(y, covariate, theta):
return y - theta * (covariate - np.mean(covariate))
