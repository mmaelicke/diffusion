diffusion
=========

This module is used as an example for shifting scientific code from quick&dirty solutions towards modular, tested
code that could be published on PyPI. It was created for a micro-lecture at the chair for hydrology at the
Karlsruhe Institute for Technology (KIT).

It includes three different modules:

- 01_script.py
- 02_functional.py
- diff2d module

All three modules solve the same problem: a two dimensional diffusion calculated iteratively on a regular grid
with the border conditions rolling over to the opposite edge.
This example was implemented as an easy to understand usecase, most natural scientists can easily understand and
reflect to thier problems.
The example was taken from the great book: High Performance Python by Micha Gorelick and Ian Ozsvald (O'Reilly).
[Copyright 2014 Micha Gorelick and Ian Ozsvald, 978-1-449-36159-4].

01_script.py
~~~~~~~~~~~~

The first script is a quick&dirty solution for only one use case creating a static output.
A number of flaws I experienced as a environmental scientists, when digging into foreign code are implemented.


02_functional.py
~~~~~~~~~~~~~~~~

The second example represents a version of 01_script.py, that does not include any static paths, parameters or
global variables the user would have to change. The code was broken down into different functions, that can
be imported by an application script. Additionally, the script is a command line tool as well, using passed
arguments to run the diffusion function as an example.

diff2d
~~~~~~

diff2d is a modular version with only some minor changes. Now the `simulate` and `evolve` function do not
plot anymore on their own, but return the `numpy.array` containing the new diffusion state.
This package can be installed using pip and is in fact already published on PyPI. As an straightforward example
the functionality was shifted into a `core` module, while the application is present in the `diffusion.py`
command line tool. One could now easily extend the functionality or add new command line tools.
The most important change compared to 02_functional.py is the usage of `ņosetests` and `coverage.py`, that
scientists should get more familiar with.