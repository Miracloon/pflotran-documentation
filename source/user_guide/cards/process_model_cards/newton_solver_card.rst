Back to :ref:`card-index`

.. _newton_solver-card:

NEWTON_SOLVER
=============
Specifies nonlinear solver parameters associated with convergence and Jacobian matrix format

Required Cards:
---------------
NEWTON_SOLVER <string>
 Specifies nonlinear solver for flow or transport (i.e. FLOW or TRANSPORT).

Optional Cards:
---------------
NO_INFINITY_NORM
 Toggle off calculation of infinity norm on residual and update vectors.  The default is to calculate infinity norm.

NO_FORCE_ITERATION
 Toggle off the forcing of at least 1 linear iteration.  The default is to force at least 1 linear iteration.  In a quasi-stationary state, the initial residual may be sufficiently small for convergence, but sometimes it is better to force at least one iteration.

NO_PRINT_CONVERGENCE
 Toggle off printing of convergence information.

PRINT_DETAILED_CONVERGENCE
 Toggle on printing of detailed convergence information.  Warning: this can be a lot of information to parse.

PRINT_LINEAR_ITERATIONS
 Prints the number of linear iterations for each Newton iteration to the screen.

**Note: See the** PETSc_ **users manual for a more definitive explanation of the solver atol, rtol, and stol tolerances below.**

.. _PETSc: http://www.mcs.anl.gov/petsc/documentation/index.html

ATOL <float>
 Absolute tolerance.  Absolute size of 2-norm of residual, i.e. 
  |
  | ||f(x_n)|| < ATOL
  |

RTOL <float>
 Relative tolerance.  Relative decrease in size of 2-norm of residual, i.e.
  |
  | ||f(x_n)||/||f(x_0)|| < RTOL
  |

STOL <float>
 Relative update tolerance.  Relative decrease in size of 2-norm of solution, i.e. 
  |
  | ||x_n-x_(n-1)||/||x_(n-1)-x_(n-2)|| < STOL
  |

ITOL <float>
 Infinity tolerance. Size of infinity norm of residual, i.e.
  |
  | ||f(x_n)||_inf < ITOL
  |

ITOL_UPDATE <float>
 Infinity tolerance. Size of infinity norm of update, i.e.              
  |
  | ||x_n-x_(n-1)||_inf < ITOL_UPDATE
  |

DTOL <float>
 Divergence tolerance at which the Newton solver fails.
  |
  | ||f(x_n)||/||f(x_0)|| > DTOL
  |

MAX_NORM <float>
 Maximum infinity norm at which the Newton solver fails.
  |
  | ||f(x_n)||_inf > MAX_NORM
  |

MAXIMUM_NUMBER_OF_ITERATIONS <int>
 Maximum number of Newton iterations before reporting failed convergence. Abbreviated card: MAXIT

MINIMUM_NEWTON_ITERATIONS <int>
 Newton solver convergence requires at least MINIMUM_NEWTON_ITERATIONS.

MAXF <int>
 Maximum number of function evaluations before reporting failed convergence.

MATRIX_TYPE <string>
 Format of main solver matrix. PETSc Mat (i.e. AIJ, BAIJ, or HYPRESTRUCT).

PRECONDITIONER_MATRIX_TYPE <string >
 Format of preconditioning matrix. PETSc Mat (i.e. AIJ, BAIJ, or HYPRESTRUCT).  Default is same as solver.

CONVERGENCE_INFO
 Opens a block for toggling ON/OFF convergence information in screen output (default: YES). See example below.

 * 2R, FNORM, 2NORMR - 2-norm of residual
 * 2X, XNORM, 2NORMX - 2-norm of solution
 * 2U, UNORM, 2NORMU - 2-norm of update
 * IR, INORMR - inifinity norm of residual
 * IU, INORMU - inifinity norm of update

Examples
--------
 ::
  
  NEWTON_SOLVER FLOW
    ITOL_UPDATE 1.d0
  /

  NEWTON_SOLVER FLOW
    PRECONDITIONER_MATRIX_TYPE AIJ
    RTOL 1.d-8
    ATOL 1.d-8
    STOL 1.d-30
    ITOL_UPDATE 1.d0
  /

  NEWTON_SOLVER TRANSPORT
    PRECONDITIONER_MATRIX_TYPE AIJ
    RTOL 1.d-12
    ATOL 1.d-12
    STOL 1.d-30
    MAXIT 10
    NO_INFINITY_NORM
    NO_PRINT_CONVERGENCE
  /

  NEWTON_SOLVER TRANSPORT
    CONVERGENCE_INFO
      2R YES
      2X NO
      2U NO
      IR NO
      IU YES
    /
  /
