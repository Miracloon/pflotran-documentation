Intro to PFLOTRAN's QA Test Suite
=================================

How To Run The Test Suite
-------------------------
To run the test suite, open a terminal and navigate to the ``qa_tests/`` 
directory:

.. code-block:: bash

   $ hg clone ssh://hg@bitbucket.org/pflotran/pflotran-doc-sandbox pflotran-doc-qa
   $ cd pflotran-doc-qa/qa_tests

Run the python script from within the ``qa_tests/`` directory, and use the ``-E`` 
flag to indicate which pflotran executable you want to use. To run all 
tests, you must include the ``-ALL`` argument flag also.

.. code-block:: bash

   $ python run_qa_tests.py -E=$PFLOTRAN_DIR/src/pflotran/pflotran -ALL
   
The script also includes several options which allow you to run only part of the
test suite. The following options are available. Several options can be chosen
at a time (but ``-E`` must always be indicated).

.. code-block:: bash

  Usage: 

  The -E flag is required and must indicate the path to the 
  PFLOTRAN executable which will run the QA tests.
  
    -E=path/to/PFLOTRAN/executable 

  If mpirun is not the MPI executable you desire, please the 
  correct path to the executable using the -MPI flag.

    -MPI=path/to/MPI/executable 

  At least one of the following flags must also be given: 

    -ALL
    -1D             -2D             -3D
    -GENERAL_MODE   -RICHARDS_MODE  -TH_MODE
    -THERMAL        -FLOW           -GAS
    -STEADY         -TRANSIENT
    -NUM_TRIES=
    -REMOVE
    -SCREEN_ON
    -HELP

   
Inside The ``run_qa_tests.sh`` Script
-------------------------------------
Each test is executed via it's unique python function, which must be called
in the test's directory location. 

.. code-block:: bash

  os.chdir('thermal/steady/1D/BC_1st_kind/th_mode'); cwd = os.getcwd()
  qa.thermal_steady_1D_BC1stkind(cwd,'1D_steady_thermal_BC_1st_kind',remove,screen_on,pf_exe)
  os.chdir('../../../../..')

The unique test scripts reside in the file ``qa_tests_engine.py``. Within this
script, each test generates the analytical solution, runs the PFLOTRAN simulation,
reads the PFLOTRAN output, and compares the PFLOTRAN solution to the analytical 
solution both mathematically and visually. If the test does not pass, then the
script will reduce the grid spacing by a factor of 2, and re-run the test. The
test will be re-run for ``-NUM_TRIES`` number of times. For example,
``-NUM_TRIES=5``. The default number of tries is 3.

The graph that visually compares the PFLOTRAN solution against the analytical
solution will be created in the specific test directory called 
``comparison_plot.png``. To view it, you must navigate to the desired test 
directory and open the file.


.. _python-helper-functions:

Python Helper Functions
-----------------------
The unique, test-specific functions use several general helper functions, 
defined in the module ``qa_tests_helper`` in the file ``qa_tests_helper.py``. 
The member functions are documented below.

.. literalinclude:: ../../qa_tests/qa_tests_helper.py


.. _report-card:

QA Tests Report Card
--------------------
The most recent report card is included below:

.. literalinclude:: ../../qa_tests/report.txt
