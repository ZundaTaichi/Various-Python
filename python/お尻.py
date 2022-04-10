import numpy as np
import matplotlib.pyplot as plt
theta_list = np.arange(0, 2*np.pi, 0.05)
r_list = 1 + np.cos(theta_list)
plt.polar(theta_list, r_list)
plt.show()