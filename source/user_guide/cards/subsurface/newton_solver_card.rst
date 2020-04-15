Back to :ref:`card-index`

.. _newton-solver-card:

NEWTON_SOLVER
=============
Specifies Newton solver parameters associated with solving the nonlinear system of equations.

Required Cards:
---------------
NEWTON_SOLVER
 Opens the Newton solver block.

Optional Cards:
---------------
*Note: See process model cards for additional NEWTON_SOLVER cards that are process model specific.*

**Note: See the** PETSc_ **users manual for a more definitive explanation of the solver ATOL, DTOL, RTOL and STOL tolerances below.**

.. _PETSc: http://www.mcs.anl.gov/petsc/documentation/index.html

ATOL <float>
 Declare convergence when the 2-norm of residual is less than ATOL :math:`\left(\|f(x_n)\|<\text{ATOL}\right)`. (default: :math:`10^{-50}`).

CONVERGENCE_INFO
 Opens a block for toggling ON/OFF convergence information in screen output (default: YES to all). See example below.

 * 2R, FNORM, 2NORMR - 2-norm of residual
 * 2X, XNORM, 2NORMX - 2-norm of solution
 * 2U, UNORM, 2NORMU - 2-norm of update
 * IR, INORMR - inifinity norm of residual
 * IU, INORMU - inifinity norm of update

DTOL <float>
 Declare divergence (cut the time step) when the 2-norm of the residual is greater than DTOL times the 2-norm of the initial residual :math:`\left(\frac{\|f(x_n)\|}{\|f(x_0)\|}>\text{DTOL}\right)`. (default: :math:`10^{4}`).

ITOL <float>
 Delare convergence when the infinity norm of residual is less than ITOL :math:`\left(\|f(x_n)\|_{inf}<\text{ITOL}\right)`. (default: not used).

ITOL_UPDATE <float>
 Declare convergence when the infinity norm of update is less than ITOL_UPDATE :math:`\left(\|x_n-x_{n-1}\|_{inf}<\text{ITOL_UPDATE}\right)`. (default: not used).

MATRIX_TYPE <string>
 Format of main solver matrix. PETSc Mat (i.e. AIJ, BAIJ, or HYPRESTRUCT).

MAXF <int>
 Maximum number of function evaluations before reporting failed convergence.

MAXIMUM_NUMBER_OF_ITERATIONS <int>
 Maximum number of Newton iterations before reporting failed convergence.

MAX_NORM <float>
 Declare divergence (cut the time step) when the infinity norm of the residual is greater than MAX_NORM :math:`\left(\|f(x_n)\|_{inf}>\text{MAX_NORM}\right)`. (default: :math:`10^{20}`).

MINIMUM_NUMBER_OF_ITERATIONS <int>
 Newton solver convergence requires at least MINIMUM_NUMBER_OF_ITERATIONS.

NO_FORCE_ITERATION
 Toggle off the forcing of at least 1 linear iteration.  The default is to force at least 1 linear iteration.  In a quasi-stationary state, the initial residual may be sufficiently small for convergence, but often it is better to force at least one iteration.

NO_INFINITY_NORM
 Toggle off calculation of infinity norm on residual and update vectors.  The default is to calculate the infinity norm.

NO_PRINT_CONVERGENCE
 Toggle off printing of convergence information.

PRECONDITIONER_MATRIX_TYPE <string >
 Format of preconditioning matrix. PETSc Mat (i.e. AIJ, BAIJ, or HYPRESTRUCT).  Default is same as solver.

PRINT_DETAILED_CONVERGENCE
 Toggle on printing of detailed convergence information.

PRINT_LINEAR_ITERATIONS
 Prints the number of linear iterations for each Newton iteration to the screen.

RTOL <float>
 Declare convergence when the 2-norm of the residual is less than RTOL times the 2-norm of the initial residual :math:`\left(\frac{\|f(x_n)\|}{\|f(x_0)\|}<\text{RTOL}\right)`. (default: :math:`10^{-8}`).

STOL <float>
 Declare convergence when the 2-norm of the update divided by the 2-norm of the solution is less than STOL :math:`\left(\frac{\|x_n-x_{n-1}\|}{\|x_{n-1}\|}<\text{STOL}\right)`. (default: :math:`10^{-8}`).

VERBOSE_LOGGING
 Prints additional convergence information to screen.

Examples
--------
 ::
  
  NEWTON_SOLVER
    ITOL_UPDATE 1.d0
  /

  NEWTON_SOLVER
    PRECONDITIONER_MATRIX_TYPE AIJ
    RTOL 1.d-8
    ATOL 1.d-8
    STOL 1.d-30
    ITOL_UPDATE 1.d0
  /

  NEWTON_SOLVER
    PRECONDITIONER_MATRIX_TYPE AIJ
    RTOL 1.d-12
    ATOL 1.d-12
    STOL 1.d-30
    MAXIT 10
    NO_INFINITY_NORM
    NO_PRINT_CONVERGENCE
  /

  NEWTON_SOLVER
    CONVERGENCE_INFO
      2R YES
      2X NO
      2U NO
      IR NO
      IU YES
    /
  /
