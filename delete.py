import numpy as np
import matplotlib.pyplot as plt


states = np.array(
    ['California', 'Texas', 'New York', 'Florida', 'Illinois',
     'Pennsylvania', 'Ohio', 'New Jersey', 'Georgia', 'Washington']
)
gdp_2018 = np.array(
    [3.02, 1.82, 1.7, 1.06, 0.88, 0.8, 0.69, 0.63, 0.6, 0.58]
)
gdp_2017 = np.array(
    [2.75, 1.7, 1.55, 0.87, 0.82, 0.75, 0.65, 0.6, 0.65, 0.51]
)

fig, ax = plt.subplots()

ax.set_title('HDP US states')
ax.bar(states, gdp_2017, alpha=0.75)
ax.set_xticklabels(states, rotation=45, ha='right')
ax.set_ylabel('biliony USD')
ax.grid()

plt.show()
