from __future__ import division
from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

infile = 'data_200g.txt'

# Find recording frequency
file = open(infile, 'r')
freq = file.readline()
file.close()
freq = freq.replace('frequency=', '')
freq = freq.replace('\n', '')
freq = int(freq)
print(freq)

M = pd.read_csv(infile,
                skiprows = [0, 1],
                names = "V")

# Zero wave based on the first 0.5 s
M.V_zero = M.V - M.V[0:(freq // 2)].mean()

# Make a time column
M.time = np.linspace(0, len(M)//freq, len(M))


fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(2, 1, 1)
plt.plot(M.time, M.V, 'b-')
ax1 = fig.add_subplot(2, 1, 2)
plt.plot(M.time, M.V_zero, 'r-')

#plt.savefig('figpath.pdf')
