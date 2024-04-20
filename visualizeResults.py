import numpy as np
import matplotlib.pyplot as plt
import json

data = open("simulationResult.txt", "r").readlines()[0]
simulationResult = json.loads(data)

x = [i for i in range(len(simulationResult))]

coef = np.polyfit(x,simulationResult,1)
print(coef)
poly1d_fn = np.poly1d(coef)


plt.plot(x, simulationResult, 'yo', x, poly1d_fn(x), '--k')
plt.title("Simulation with TaggingFactor of 10^5")
plt.show()
