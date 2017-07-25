"""
This is a script simulating the diffusion in 6 timesteps

"""
import numpy as np
import matplotlib.pyplot as plt

#######
# t0
#######
u = np.zeros(shape=(50,50))
u[23:26, 23:26] = 1
u[12:14, 12:14] = 1

# plot
fig, axes = plt.subplots(3,2, figsize=(10, 15))
axes.flatten()[0].matshow(u, cmap='Reds')
axes.flatten()[0].set_title('initial conditions')

#######
# t1
#######
# put 50, 50 size into parameters
u2 = u.copy()
M,N = u.shape
for i in range(50):
    for j in range(N):
        grid_xx = u[(i+1)%M,j] + u[(i-1)%M,j] - 2.0 * u[i,j]
        grid_yy = u[i,(j+1)%N] + u[i,(j-1)%N] - 2.0 * u[i,j]
        u2[i,j] = u[i,j] + 0.9 * (grid_xx + grid_yy) * 0.01

axes.flatten()[1].matshow(u2, cmap='Reds')
axes.flatten()[1].set_title('after 0.01s')

#######
# t2
#######
# this is after 1 second (100 * 0.01)
u3 = u.copy()
M,N = u.shape
for it in range(100):
    u3 = u3.copy()     # <==== This is the important iteration
    for i in range(50):
        for j in range(N):
            grid_xx = u3[(i+1)%M,j] + u3[(i-1)%M,j] - 2.0 * u3[i,j]
            grid_yy = u3[i,(j+1)%N] + u3[i,(j-1)%N] - 2.0 * u3[i,j]
            u3[i,j] = u3[i,j] + 0.9 * (grid_xx + grid_yy) * 0.01

axes.flatten()[2].matshow(u3, cmap='Reds')
axes.flatten()[2].set_title('after 1s')


####################################
# for the following code just copy-paste
# the code of t2 and set other D (0.9), dt (0.01) and iterations (the range at it)
# the full time is dt (0.01) times the iteration

# this is after 1.5 second (150 * 0.01)
u3 = u.copy()
M,N = u.shape
for it in range(150):
    u3 = u3.copy()     # <==== This is the important iteration
    for i in range(50):
        for j in range(N):
            grid_xx = u3[(i+1)%M,j] + u3[(i-1)%M,j] - 2.0 * u3[i,j]
            grid_yy = u3[i,(j+1)%N] + u3[i,(j-1)%N] - 2.0 * u3[i,j]
            u3[i,j] = u3[i,j] + 0.9 * (grid_xx + grid_yy) * 0.01

axes.flatten()[3].matshow(u3, cmap='Reds')
axes.flatten()[3].set_title('after 1.5s')


# this is after 2.5 second (200 * 0.01)
u3 = u.copy()
M,N = u.shape
for it in range(400):
    u3 = u3.copy()     # <==== This is the important iteration
    for i in range(50):
        for j in range(N):
            grid_xx = u3[(i+1)%M,j] + u3[(i-1)%M,j] - 2.0 * u3[i,j]
            grid_yy = u3[i,(j+1)%N] + u3[i,(j-1)%N] - 2.0 * u3[i,j]
            u3[i,j] = u3[i,j] + 0.9 * (grid_xx + grid_yy) * 0.01

axes.flatten()[4].matshow(u3, cmap='Reds')
axes.flatten()[4].set_title('after 4s')

# this is after 2.5 second (200 * 0.01)
u3 = u.copy()
M,N = u.shape
for it in range(100):
    u3 = u3.copy()     # <==== This is the important iteration
    for i in range(50):
        for j in range(N):
            grid_xx = u3[(i+1)%M,j] + u3[(i-1)%M,j] - 2.0 * u3[i,j]
            grid_yy = u3[i,(j+1)%N] + u3[i,(j-1)%N] - 2.0 * u3[i,j]
            u3[i,j] = u3[i,j] + 0.9 * (grid_xx + grid_yy) * 0.1         # <==== ACHTUNG!!! dt is bigger because script gets too slow.

axes.flatten()[5].matshow(u3, cmap='Reds')
axes.flatten()[5].set_title('after 10s')

# show all plots
plt.tight_layout()
plt.show()