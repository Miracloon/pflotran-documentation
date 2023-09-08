.. _mode-ert:

ERT Mode
--------

Governing Equations
~~~~~~~~~~~~~~~~~~~

The ``ERT`` geophysics mode solves the following electrostatic Poisson equation

.. math::
   :label: conservation-ert

    \pmb{\nabla} \cdot \sigma(\mathbf{r}) \pmb{\nabla} \phi(\mathbf{r}) = -I\delta(\mathbf{r}-\mathbf{r}_\mathrm{s})

where :math:`\phi` is the electrical potential at position :math:`\mathbf{r}` for a given conductivity :math:`\sigma(\mathbf{r})` due to a current :math:`I` injected through a point located at :math:`\mathbf{r}_\mathrm{s}`; and :math:`\delta` is the Dirac delta function. For brevity, hereinafter, the dependencies on :math:`\mathbf{r}` will be omitted except where necessary to show.
   

