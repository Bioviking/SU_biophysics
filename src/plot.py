#!/usr/bin/python2.7

############ IMPORTS ############

import numpy as np
import argparse
import matplotlib.pyplot as plt


############ CALCS ############

traj = np.loadtxt("traj.dat", dtype=int)
mstates = np.loadtxt("enth.dat")
T = 300

#Count microstate occupation
bins = np.bincount(traj)

#Convert int values to floats and put into a numpy array
simulation_dist = np.array([float(i) for i in bins])

#Set size of list for the predicted values
prediction_dist = np.zeros(4)

#Predict population using enthalpy values in mstates

prediction_dist = np.exp((-mstates)/T)  # for j in mstates


#Normalize the distributions
simulation_dist = simulation_dist / sum(simulation_dist)
prediction_dist = prediction_dist / sum(prediction_dist)

#Mulitplicity
new_simul = np.zeros(2)
new_simul[0] = sum(simulation_dist[0:3])
new_simul[1] = simulation_dist[-1]


new_pred = np.zeros(2)
new_pred[0] = np.exp(-(mstates[0]-T*np.log(3))/T)
new_pred[1] = np.exp(-(mstates[-1]/T))

new_pred /= new_pred.sum()


############ PLOT ############

ind = np.arange(2) # the x locations for the groups
width = 0.35 # the width of the bars

plt.bar(ind, new_pred, width, color='b',alpha=0.5, label='Predicted')
plt.bar(ind+width, new_simul, width, color='g',alpha=0.5, label='Simulation')
plt.legend(loc=4)
plt.show()
