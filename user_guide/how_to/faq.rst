.. _faq:

#. `How do I get help?`_
#. `How do I resolve installation issues?`_
#. `How do I make any sense of the screen output, in particular Newton iteration convergence?`_
#. `How do I create datasets and are there examples?`_
#. `Why does PFLOTRAN crash when printing provenance information to HDF5 formatted output?`_
#. `Does PFLOTRAN run on a machine with GPUs?`_
#. `What is the difference between MAPPED, GLOBAL, CELL_INDEXED, GRIDDED and ASCII datasets?`_

--------------------

.. _How do I get help?:

How do I get help?
==================

The PFLOTRAN developers and community can provide limited volunteer support for 
PFLOTRAN. Please send an email to the appropriate PFLOTRAN mailing lists.

Questions regarding PFLOTRAN installation (i.e. not answered by documentation 
below), bug reports: **pflotran-dev at googlegroups dot com**

Questions regarding running PFLOTRAN: **pflotran-users at googlegroups dot com**

Just saying "PFLOTRAN doesn't work" doesn't give us enough information to 
actually help you and often requires a lot of additional back and forth that 
delays the process. 

**Please provide the following information**:

#. Which Git revision of PFLOTRAN you are using:

    .. sourcecode:: bash

        git log -1

#. Whether you have modified PFLOTRAN:

    .. sourcecode:: bash

        git status


#. If you have modified PFLOTRAN? How? Is your version public for us to see?

#. Which version of PETSc you are using:

    .. sourcecode:: bash

        cd ${PETSC_DIR}
        git log -1 HEAD

#. Do the regression tests pass? If not, attach the test log.

    .. sourcecode:: bash

        cd ${PFLOTRAN_DIR}/src/pflotran
        make test

#. Attach the input file you are trying to run.

#. Attach the screen output or output files showing the error message and context:

    .. sourcecode:: bash

        ./pflotran -input_prefix my-problem &> my-problem.stdout.txt
        
--------------------

.. _How do I resolve installation issues?:

How do I resolve installation issues?
=====================================

No such file /conf/variables
----------------------------

Problem: When I run "make pflotran" I get the message:

::

    $ make pflotran
    "makefile:150: /conf/variables: No such file or directory"
    "makefile:151: /conf/rules: No such file or directory"
    "make: *** No rule to make target `/conf/rules'. Stop"

Solution: You have not set your PETSC_DIR and PETSC_ARCH environment variables.

In tcsh:

.. sourcecode:: csh

    setenv PETSC_DIR /path/to/petsc
    setenv PETSC_ARCH whatever_arch_was_installed

In bash:

.. sourcecode:: bash

    export PETSC_DIR=/path/to/petsc
    export PETSC_ARCH=whatever_arch_was_installed

To avoid having to type these commands in every shell, they should be added to 
your .cshrc (tcsh) or .bashrc (bash) files.

PFLOTRAN doesn't compile when I type ``make pflotran``.
-------------------------------------------------------

Many times when PFLOTRAN doesn't compile correctly (e.g. ``make pflotran``
does not complete due to errors), it is due to incorrect PETSc configuration.
PFLOTRAN uses a snapshot of the PETSc 'maint' (release) branch, obtained
by specifically checking out a changeset-id after cloning PETSc. The 
changeset-id that PFLOTRAN uses changes occasionally. If PFLOTRAN does not
compile, try reconfiguring PETSc, making sure you check out the correct
changeset-id. Details are provided on the installation pages: 
:ref:`installation`. An example is shown below. **The changeset-id shown below**
**is not be the most current. Please use the changeset-id provided on the** 
**installation pages:** :ref:`installation`.

.. code-block:: bash

    git clone https://bitbucket.org/petsc/petsc petsc
    cd petsc
    git checkout 987thisisnotthecorrectchangesetid1234567

--------------------

.. _How do I make any sense of the screen output, in particular Newton iteration convergence?:

How do I make any sense of the screen output, in particular Newton iteration convergence?
=========================================================================================

Standard Flow
-------------


::

 == GENERAL FLOW ================================================================
   1 2r: 4.13E-13 2x: 1.30E+08 2u: 4.47E-01 ir: 4.42E-14 iu: 2.44E-02 rsn:   0
   2 2r: 6.06E-13 2x: 1.30E+08 2u: 5.63E-01 ir: 5.65E-14 iu: 5.23E-02 rsn:   0
   3 2r: 2.21E-13 2x: 1.30E+08 2u: 3.67E-01 ir: 1.90E-14 iu: 3.05E-02 rsn:   0
   4 2r: 2.45E-13 2x: 1.30E+08 2u: 3.33E-01 ir: 2.20E-14 iu: 2.42E-02 rsn: itol_post_check

  Step   5498 Time=  9.89040E+03 Dt=  1.04142E+01 [y] snes_conv_reason:   12
   newton =   4 [   31891] linear =    75 [    645652] cuts =  0 [ 915]
   --> SNES Linear/Non-Linear Iterations =           75  /            4
   --> SNES Residual:   2.452466E-13  2.335682E-16  2.200252E-14
   --> max chng: dpl=   2.7064E-03 dpg=   1.1357E-01 dpa=   1.1357E-01
                 dxa=   1.3283E-11  dt=   0.0000E+00 dsg=   2.9327E-08

* 2r: 2-norm of residual
* 2x: 2-norm of current solution
* 2u: 2-norm of update
* ir: inf-norm of residual
* iu: inf-norm of update
* rsn: converged reason (corresponding integer in brackets)

 + 0: iterating (not converged)
 + atol[2]: 2r < ATOL
 + rtol[3]: 2r < RTOL * 2r_initial
 + stol[4]: 2u < STOL * 2x
 + itol_res[10]: ir < ITOL_RES
 + itol_upd[11]: iu < ITOL_UPDATE
 + itol_post_check[12]: mode-specific convergence criteria defined in XXXCheckUpdatePost()

* Time: current simulation time
* Dt: time step size
* snes_conv_reason: integer value for 'rsn'
* newton: number of Newton iterations for time step [simulation total in brackets]
* linear: number of linear iterations for time step [simulation total in brackets]
* cuts: number of time step cuts for time step [simulation total in brackets]
* SNES Linear/Non-Linear Iterations: self explanatory
* SNES Residual: 2r 2r/#cell ir 
* max chng: maximum change in a primary dependent variable

 + dpl: liquid pressure [Pa]
 + dpg: gas pressure [Pa]
 + dpa: air pressure [Pa]
 + dxa: air mole fraction in liquid phase [-]
 + dt: temperature [C]
 + dsg: gas saturation [-]
 

GENERAL mode compiled with debug_gen=2
--------------------------------------

 
The following information is printed for every Newton iteration when PFLOTRAN 
is run with the GENERAL flow mode and the code is compiled with 'debug_gen=2' 
on the command line.

::

  2 2r: 1.78E-13 2x: 1.80E+07 2u: 6.26E+01 ir: 1.20E-13 iu: 3.13E+01 rsn:   0
    -+  dpl:  2.9148E+00  dxa:  9.5553E-10  dt:  1.8149E-10
    -+  dpg:  0.0000E+00  dpa:  0.0000E+00  dt:  0.0000E+00
    -+  dpg:  4.2500E+00  dsg:  8.4871E-07  dt:  1.8331E-10
    -+ rupl:  5.6408E-07 ruxa:  5.3914E-02 rut:  6.7219E-12
    -+ rupg:  0.0000E+00 rupa:  0.0000E+00 rut:  0.0000E+00
    -+ rupg:  7.0889E-07 rusg:  9.1508E-06 rut:  6.7894E-12
    -+  srl:  4.8899E-06  srg:  6.5988E-10 sre:  2.0326E-07
    -+  srl:  0.0000E+00  srg:  0.0000E+00 sre:  0.0000E+00
    -+  srl:  4.9007E-06  srg:  1.6427E-07 sre:  1.7585E-07
    -+ ru1 icell:      6  st:  3  X:  5.995E+06  dX: -4.250E+00  R: -5.672E-14
    -+ ru2 icell:      7  st:  1  X:  1.772E-08  dX: -9.555E-10  R: -7.638E-18
    -+ ru3 icell:      1  st:  3  X:  2.700E+01  dX:  1.833E-10  R: -9.295E-16
    -+ sr1 icell:      6  st:  3  X:  5.995E+06  dX: -4.250E+00  R: -5.672E-14
    -+ sr2 icell:      6  st:  3  X:  9.275E-02  dX: -8.487E-07  R:  1.901E-15
    -+ sr3 icell:      7  st:  1  X:  2.700E+01  dX:  1.788E-10  R:  1.200E-13

Data is organized in rows of three corresonding to either the states of the 
system (1-single phase liquid, 2-single phase gas, 3-two phase) or the governing 
equation (1-liquid component [water] mass, 2-gas component [air] mass, 3-energy).

The first set of three (i.e. three rows) prints the maximum change of each of 
the three primary dependent variables (column) for each state (row: 1-liquid, 
2-gas, 3-two-phase). Only cells possessing a primary dependent variable for a 
given state considered in each calculation:

::

    -+  dpl:  2.9148E+00  dxa:  9.5553E-10  dt:  1.8149E-10
    -+  dpg:  0.0000E+00  dpa:  0.0000E+00  dt:  0.0000E+00
    -+  dpg:  4.2500E+00  dsg:  8.4871E-07  dt:  1.8331E-10

* d: - delta [X_(p+1) - X_p]

* dpl: liquid pressure
* dxa: air mole fraction in liquid phase
* dt: temperature
* dpg: gas pressure
* dpa: air pressure
* dsg: gas saturation

Rows 4-6 print the infinity norm of the relative update (dX/X) for each of the 
three primary dependent variables for each state:

::

    -+ rupl:  5.6408E-07 ruxa:  5.3914E-02 rut:  6.7219E-12
    -+ rupg:  0.0000E+00 rupa:  0.0000E+00 rut:  0.0000E+00
    -+ rupg:  7.0889E-07 rusg:  9.1508E-06 rut:  6.7894E-12

* ru - relative update of X [dX/X]

* rupl: liquid perssure
* ruxa: air mole fraction in liquid phase
* rut: temperature
* rupg: gas pressure
* rupa: air pressure
* rusg: gas saturation

Rows 7-9 print the infinity norm of the scaled residual (R / A) for each of the 
three governing equations for each state.  Here A is the fixed portion of the 
accumulation time (portion of time derivative at time t as opposed to t + dt):

::

    -+  srl:  4.8899E-06  srg:  6.5988E-10 sre:  2.0326E-07
    -+  srl:  0.0000E+00  srg:  0.0000E+00 sre:  0.0000E+00
    -+  srl:  4.9007E-06  srg:  1.6427E-07 sre:  1.7585E-07

* sr - scaled residual [R/A]   

* srl: liquid (water) equation
* srg: gas (air) equation
* sre: energy equation

Rows 10-12 print the cell id, state (st), value (X), update (dX), and residual 
(R) for primary dependent variable with the largest relative update (dX/X) for 
each governing equation:

::

    -+ ru1 icell:      6  st:  3  X:  5.995E+06  dX: -4.250E+00  R: -5.672E-14
    -+ ru2 icell:      7  st:  1  X:  1.772E-08  dX: -9.555E-10  R: -7.638E-18
    -+ ru3 icell:      1  st:  3  X:  2.700E+01  dX:  1.833E-10  R: -9.295E-16

* ru - relative update

* ru1: liquid equation
* ru2: gas equation
* ru3: energy equation

Rows 13-15 print the cell id, state (st), value (X), update (dX), and residual 
(R) for primary dependent variable with the largest scaled residual (R/A) for 
each governing equation:

::

    -+ sr1 icell:      6  st:  3  X:  5.995E+06  dX: -4.250E+00  R: -5.672E-14
    -+ sr2 icell:      6  st:  3  X:  9.275E-02  dX: -8.487E-07  R:  1.901E-15
    -+ sr3 icell:      7  st:  1  X:  2.700E+01  dX:  1.788E-10  R:  1.200E-13

* sr - scaled residual

* sr1: liquid equation
* sr2: gas equation
* sr3: energy equation

.. _How do I create datasets and are there examples?:

How do I create datasets and are there examples?
================================================

**It is highly recommended that you download and install HDFView, which greatly 
facilitates understanding/managing HDF5 files with PFLOTRAN.**

Permeability and/or Porosity
----------------------------

Permeability and porosity datasets are cell-indexed HDF5 datasets, but they 
differ slightly from all other datasets in that they are not placed in a group 
and they must be named "Permeability" and "Porosity".  This will change in the 
future, but for now, they must use those names.  See the :ref:`dataset-card` 
card.

Useful python scripts: 

PFLOTRAN_DIR/src/python/conceptual_model/DataLoader.py

Useful examples:

PFLOTRAN_DIR/regression_tests/default/543/543_hanford_srfcplx_param.in
PFLOTRAN_DIR/regression_tests/default/infiltrometer/16m.in
PFLOTRAN_DIR/regression_tests/shortcourse/regional_doublet/stochastic_regional_doublet_small.in

Material IDs
------------

Material IDs must be defined for all grid cells in a single HDF5 file under an 
HDF5 Group named "Materials".  The STRATA_ card provides an example of how to 
set up a Material ID dataset.

Useful python scripts:

PFLOTRAN_DIR/src/python/conceptual_model/material_and_region_loader.py

Useful examples:

PFLOTRAN_DIR/regression_tests/default/543/543_flow.in

Regions
-------

Regions are located in an HDF5 file under an HDF5 Group named "Regions".  Within 
the Regions group, one creates Groups whose names match the regions in the 
PFLOTRAN input file.  Each of these groups provides a list of "Cell Ids" and 
"Face Ids".  Face ids are not required for regions not associated with boundary 
conditions.

Useful python scripts:

PFLOTRAN_DIR/src/python/conceptual_model/material_and_region_loader.py

Useful examples:

PFLOTRAN_DIR/regression_tests/default/543/543_flow.in

Other Cell-Indexed Datasets
---------------------------

Other cell-indexed HDF5 datasets can have arbitrary names.  These datasets are 
used to define pressure, temperature, concentration, mineral volume fractions, 
etc. over all grid cells in the domain.

Useful python scripts:

PFLOTRAN_DIR/src/python/cell_indexed_dataset_loader.py

Useful examples:

PFLOTRAN_DIR/regression_tests/default/543/543_hanford_srfcplx_param.in
PFLOTRAN_DIR/regression_tests/default/543/543_flow.in (initializing pressure field from a file)

Gridded Datasets
----------------

Gridded HDF5 datasets are defined on a uniform Cartesian grid and interpolated 
to the PFLOTRAN structured or unstructured grid internally.  These grids are 
particularly useful for setting up nonlinear boundary or initial conditions.

Useful python scripts:

PFLOTRAN_DIR/src/python/gridded_dataset_loader.py

Useful examples:

PFLOTRAN_DIR/regression_tests/default/condition/datum_dataset.in
PFLOTRAN_DIR/regression_tests/default/condition/543_datum_dataset.in

ASCII Datasets
--------------

ASCII dataset are used to define scalar or vector quantities over time (e.g. a 
datum, gradient, or pressure associated with a FLOW_CONDITION that varies over 
time).

Useful python scripts:

Currently don't have a script.

Useful examples:

PFLOTRAN_DIR/regression_tests/default/condition/543_timeseries.in
PFLOTRAN_DIR/regression_tests/shortcourse/regional_doublet/regional_doublet_small.in (see "river" FLOW_CONDITION)

.. _DATASET: QuickGuide/DatasetNew
.. _STRATA: QuickGuide/Strata

.. _Why does PFLOBTRAN crash when printing provenance information to HDF5 formatted output?:

Why does PFLOTRAN crash when printing provenance information to HDF5 formatted output?
======================================================================================

Ensure that there is a carriage return character on the last line of your input 
file.  This should resolve the issue.

.. _Does PFLOTRAN run on a machine with GPUs?:

Does PFLOTRAN run on a machine with GPUs?
=========================================

PFLOTRAN will run on a machine with GPUs, but it will not leverage any GPU (or 
any other accelerator) capability.  The code is not currently written to utilize 
the GPUs on such machines, but only the CPU.

Note: Before you make a significant investment in codes that claim to use GPUs, 
research the codes' scalability on GPUs (or perform your own scalability study) 
to ensure that your investment is worthwhile. Codes that solve implicit systems 
of equations (as does PFLOTRAN) have demonstrated only minimal speedup on GPUs 
(e.g. 4x). At this point in time, I (Glenn) consider a large investment in GPU 
capability to be ineffective since one can employ 4 times as many cores to get 
the same speedup.

.. _What is the difference between MAPPED, GLOBAL, CELL_INDEXED, GRIDDED and ASCII datasets?:

What is the difference between MAPPED, GLOBAL, CELL_INDEXED, GRIDDED and ASCII datasets?
========================================================================================

ASCII: Text-based datasets entered in the input file are stored internally 
within PFLOTRAN in ASCII datasets.

CELL_INDEXED:  A dataset that prescribes a value for each grid cell in a list 
of cells. The user must define a list of cells IDs aligned with the values. 
Theoretically, the user could provide a list of cells that is a subset of the 
global domain, but this has not been tested. The list of cells is usually 
aligned with the global grid, and thus, this dataset is usually aligned with 
the GLOBAL dataset.  

GLOBAL: A dataset that prescribes a value for each grid cell in the (global) 
domain.

GRIDDED: A 1D, 2D, or 3D uniformly-spaced grid of values from which values can 
be interpolated given a point in space.

MAPPED: A dataset that maps few distinct data values on multiple grid cells. 
e.g. A simulation for a 3D domain (NX x NY x NZ) in which a vertical profile 
(NZ) of transpiration sink is applied homogeneously for each horizontal layer. 
At a z-th level, all grid cells in x- and y-direction are prescribed z-th 
transpiration dataset.
