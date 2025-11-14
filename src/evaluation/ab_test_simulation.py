import numpy as np
from .cuped import fit_theta, apply_cuped




def simulate_ab_test(control_mean=0.05, treatment_mean=0.055, n=5000):
covariate = np.random.normal(loc=0.1, scale=0.02, size=n)


control = np.random.binomial(1, control_mean, n)
treatment = np.random.binomial(1, treatment_mean, n)


theta = fit_theta(control, covariate)


control_adj = apply_cuped(control, covariate, theta)
treatment_adj = apply_cuped(treatment, covariate, theta)


raw_lift = (treatment_mean - control_mean) / control_mean
cuped_lift = (np.mean(treatment_adj) - np.mean(control_adj)) / np.mean(control_adj)


return {
"raw_lift": raw_lift,
"cuped_lift": cuped_lift,
"theta": theta,
}
