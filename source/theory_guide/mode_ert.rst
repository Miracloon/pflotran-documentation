.. _mode-ert:

ERT Mode
--------

Governing Equations
~~~~~~~~~~~~~~~~~~~

The ``ERT`` geophysics mode solves the following electrostatic Poisson equation for electrical potential $\porosity$ [V]

.. math::
   \pmb{\nabla} \cdot \bulkelectricalconductivity \pmb{\nabla} \porosity = -Q_I,
   :label: conservation-ert

where $\bulkelectricalconductivity$ is bulk electrical conductivity [S m$^{-1}$] and $Q_I$ is electrical current [A m$^{-3}$ s$^{-1}$] injected through an electrode at a point in space. Bulk electrical conductivity is calculated as a function of fluid and rock/soil conductivity, liquid saturation and porosity through empirical relationships (e.g., Archie's law).

Example of dummy reference to Eq. :eq:`conservation-ert`
