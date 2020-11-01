import numpy as np
import matplotlib.pyplot as plt

t, d, dd = np.loadtxt('data_exer7.txt', skiprows=4, unpack=True)

v = (d[1:] - d[:-1])/(t[1:] - t[:-1])
tv = (t[1:] + t[:-1])/2


a = (v[1:] - v[:-1])/(tv[1:] - tv[:-1])
ta = (tv[1:] + tv[:-1])/2

dv = np.sqrt(((1/(t[1:]-t[:-1]))*dd[1:])**2+((1/(t[1:]-t[:-1]))*dd[:-1])**2)
da = np.sqrt(((1/(tv[1:]-tv[:-1]))*dv[1:])**2+((1/(tv[1:]-tv[:-1]))*dv[:-1])**2)



fig = plt.figure(figsize=(9, 7))

ax1 = fig.add_subplot(3,1,1)
ax1.plot(t, d, 'g--')
ax1.errorbar(t, d, fmt='oC1', label='data', yerr = dd, ecolor='black' )
ax1.set_xlabel('Time(s)')
ax1.set_ylabel('Displacement(m)')

ax2 = fig.add_subplot(3, 1, 2)
ax2.plot(tv, v, 'b--')
ax2.errorbar(tv, v, fmt='oC2', label='data', yerr = dv, ecolor='black')
ax2.set_xlabel('Time(s)')
ax2.set_ylabel('Velocity(m/s)')

ax3 = fig.add_subplot(3, 1, 3)
ax3.plot(ta, a, 'r--')
ax3.errorbar(ta, a, fmt='oC2', label='data', yerr = da, ecolor='black')
ax3.set_xlabel('Time(s)')
ax3.set_ylabel('Acceleration (m/s2)')


fig.tight_layout()
fig.show()

