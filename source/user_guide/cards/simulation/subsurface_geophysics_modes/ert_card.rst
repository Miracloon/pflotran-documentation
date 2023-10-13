Back to :ref:`card-index`

Back to :ref:`subsurface-geophysics-card`

Back to :ref:`subsurface-geophysics-mode-card`

.. _ert-card:

ERT
===

Defines options for the ERT geophysics mode

:ref:`ert-simulation-options`

.. _ert-simulation-options:

SIMULATION Options 
------------------
*(under SUBSURFACE_GEOPHYSICS in SIMULATION PROCESS_MODELS block)*

**Basic Settings**

COMPUTE_JACOBIAN
 Toggles on the calculation of the ERT Jacobian (derivatives of ERT measurements with respectd to bulk electrical conductivity).

NO_ANALYTICAL POTENTIAL
 An analytical potential is calculated as the initial guess for the iterative linear solve after calculating an averaged conductvity model. This flag turns the calculation off.

Examples
--------
::

 SIMULATION
   SIMULATION_TYPE SUBSURFACE
   PROCESS_MODELS
     SUBSURFACE_GEOPHYSICS geophysics
       MODE ERT
       OPTIONS
         COMPUTE_JACOBIAN
         NO_ANALYTICAL POTENTIAL
       /
     /
   /
 END


