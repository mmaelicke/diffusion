Diffusion.py
============

This package is used to calculate 2-dimensional diffusion on a regular grid with the initial conditions
defined in a png file. The border conditions are handeled by rolling over to the oposite edge and using the
value specified there.
This module is the final state in a row of examples for solving the same problem. All examples, shifting the very
first quick&dirty soultion over a function-based version to this version are published in the GIT-project:

https://github.com/mmaelicke/diffusion.git

This module was programmed in order to illustrate proper programming for scientist using an easy to understand
example. It does neither claim to be performant nor comprehensive to solve diffusion problems.
The example was taken from the great book: High Performance Python by Micha Gorelick and Ian Ozsvald (O'Reilly).
[Copyright 2014 Micha Gorelick and Ian Ozsvald, 978-1-449-36159-4].


Installation
~~~~~~~~~~~~

Install this package using:

.. code-block:: bash

  pip install diff2d



Usage
~~~~~

There is a command line tool called `diffusion.py` that takes an image with the initial conditions as a first
argument, The diffusion parameter D as a second argument, the time step per increment dt as third argument and
the total time steps to be simulated as fourth argument.

.. code-block:: bash

  python diffusion.py image.png D dt iterations