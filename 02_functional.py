"""
This is a file simulating diffusion by defining a simulation function. Can be used as a command line tool
"""
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import color
from numba import jit
import sys, time


def load_data(path):
    return color.rgb2gray(imread(path))


def plot_current_state(img, ax, title=None):
    ax.imshow(img, cmap='Reds')
    if title is not None:
        ax.set_title(title)


@jit
def evolve(u, dt, D):
    u2 = u.copy()
    M,N = u.shape
    for i in range(M):
        for j in range(N):
            grid_xx = u[(i+1)%M,j] + u[(i-1)%M,j] - 2.0 * u[i,j]
            grid_yy = u[i,(j+1)%N] + u[i,(j-1)%N] - 2.0 * u[i,j]
            u2[i,j] = u[i,j] + D * (grid_xx + grid_yy) * dt
    return u2


def simulation(img, runs, step, D):
    fig, ax = plt.subplots(1,2)
    plot_current_state(img, ax[0], 't0')

    u = img.copy()
    for _ in range(runs):
        # evolve the u
        u = evolve(u, step, D)

        # just writing
        if _ % 10 == 0:
            print('{0}%      '.format(round(_ / runs * 100), 1), end='\r')
    print('Done.      ')

    plot_current_state(u, ax[1], 't0 + %.1f sec' % (runs * step))


if __name__ == '__main__':
    # load the params
    img_path = sys.argv[1]
    D = float(sys.argv[2])
    dt = float(sys.argv[3])
    runs = int(sys.argv[4])

    # load the image
    img = load_data(img_path)
    print('Loaded matrix of %s; running simulation of %d * %f dt evolutions...' % (str(img.shape), runs, dt))

    # simulate
    t0 = time.time()
    simulation(img, runs, dt, D)
    t1 = time.time()

    print('\n========================================\nCalculated {0} steps of dt = {1} sec in {2} sec.'.format(runs, dt, t1 - t0))

    plt.show()