PFLOTRAN Fortran Formatting Protocol
====================================

Guidelines
----------
* Free format
* Use & for continuation
* ==, >, <, >=, <= used instead of .eq., .eqv., .gt., .lt., .ge., .le.
* No tabs whatsoever, 2-space indentation, i.e.

 ::

   Level 1
     Level 2
       Level 3
         Level 4
           Level 5
             ...

* Maximum source width is 80 characters.  Use a continuation line beyond

 :: 

  123456789+123456789+123456789+123456789+123456789+123456789+123456789+123456789+
                   print \*, 'This sentence is just barely too long for a single &
                            &line.'
                   call subroutine_with_many_arguments(argument1, argument2, &
                                                       argument3, argument4)

* Maximum of 31 characters for subroutine/variable/etc. names.  Try to be as concise as possible.
* Capitalization

 * All fortran syntax should be lower case, e.g. 

   | subroutine, module, contains, use, .and., else, etc.

 * All variable names should be lower case.
 * Fortran parameters are all caps, e.g. 

   | MAXWORDLENGTH, RICHARDS_MODE, UNSTRUCTURED_GRID

 * All module names should be lower case with '_module' appended.
 * Use PETSc-style capitalization in subroutine/function names, e.g. 

   | VecGetArrayF90, VecDestroy

   For example, the following changes should take place:
   ::

        Grid_get_t -> GridGetTime
        Grid_setvel -> GridSetVel or GridSetVelocity
        Grid_update_dt -> GridUpdateDt or GridUpdateTimestep

* All fortran syntax with multiple words should have a space between words (e.g. end type, end subroutine), except for conditionals and loops:  elseif, endif, enddo.
* Pin all module, subroutine, function, and contains declarations up against the left side.  This leaves more room for indentation later on and is not confusing.
* The default private/public attribute for modules is 'private'
* 'implicit none' at top of every file, subroutine, function, interface
* 'PetscReal' instead of 'double precision' or 'real*8'
* 'PetscInt' instead of 'integer'
* 'PetscBool' instead of 'logical'
* 'PETSC_TRUE/PETSC_FALSE' instead of .true./.false.
* All variables in the function/subroutine argument list should be at the top of the routine with a blank line separating them from the 'implicit none'.  The local variables should come below with a blank line separating them from the variables in the subroutine argument list.

 ::

  subroutine Example(integer_in, real_in)

    implicit none
 
    PetscInt :: integer_in   ! subroutine arguments declared first
    PetscReal :: real_in
                             ! blank line separating local variables
    PetscBool :: whatever
    PetscInt :: i
    PetscInt :: integer1, integer2

    PetscInt :: iarray(5)
    PetscReal, pointer :: array(:)

* All pointers to PETSc data structures have '_p' appended (i.e. 'array_p')

 * NEVER use PETSc's F77 approach to pointers: a PetscInt/PetscReal array sized to 1 combined with a PetscOffset.  If you are not sure, ask Glenn.

* No goto's (this may not be possible with legacy portions)
* User appropriate spacing to improve readability:

 ::

  if(OneNumber>AnotherNumber.and.ALogical==PETSC_TRUE)then
 
 or

 ::

  if ( OneNumber>AnotherNumber.and.ALogical==PETSC_TRUE ) then

 are better viewed as

 ::

  if (OneNumber > AnotherNumber .and. ALogical == PETSC_TRUE) then

 ::

  pressure=rho*gravity*distance

 is better viewed as

 ::

  pressure = rho*gravity*distance

* Distinguish between natural, local, and local-ghosted coordinate indices: e.g. na, n, ng, respectively.  (GEH: This needs go be revised).
* Use integer exponents (e.g. x**3) instead of real exponents (e.g. x**3.d0) whenever possible. With the integer approach, the compiler creates a series of multiplication (i.e. x*x*x) which is less expensive to calculate than the x :sup:`3` = e :sup:`3 ln x`.

Filename and Module/Class Naming Convention
-------------------------------------------

* Modules and Classes are mixed case with underscores between words and '_module' (or '_class' for F03 classes) appended, e.g.

  | Reaction_Sandbox_module
  | Reaction_Sandbox_Base_class

* The corresponding filename is the module name with (1) '_module' or '_class' removed, (2) all lower case, and (3) '.F90' appended, e.g.

  | reaction_sandbox.F90
  | reaction_sandbox_base.F90

* Files containing base classes are always named XXX_base.F90
* Files containing functions/subroutines/modules that are often commonly shared between simulation modes, process models, or implementations are named XXX_common.F90, e.g.

  | output_common.F90
  | richards_common.F90

* Files containing low level functions/subroutines or non-extended derived types are named XXX_aux.F90, e.g.

  | output_aux.F90
  | ricards_aux.F90

* Should a derived type in an XXX_aux.F90 file be extended (e.g. in the case of process model aux_vars), the XXX_aux.F90 file should be renamed to XXX_base.F90.

* Files containing functions/subroutines that serve as drivers for all classes of a derived type, should be named XXX.F90 where XXX is the root function, e.g.

  | dataset.F90
  | richards.F90
  | reaction_sandbox.F90

Example Fortran Source Code
---------------------------

An example source would be (!comment denotes all commentary on example)
 ::

  module Example_module

    implicit none

    private  !comment: all variables/subroutines, etc. are private by default

  #include "whatever.h"

    public :: GridCreate, GridGetTime

    PetscReal, save :: file_global_variable

  contains

  !************************************************************************** !

  subroutine GridSetup(integer_in, real_in)
  !
  ! Initializes the grid.
  ! Author: John Doe
  ! Date: 01/01/07
  !
    use whatever_module

    implicit none
 
  #include "whatever.h"

    PetscInt :: integer_in  !comment: note that the subroutine arguments are
    PetscReal :: real_in      !comment: declared first

    PetscBool :: whatever    !comment: note that declarations are group by type
    PetscInt :: i
    PetscInt :: integer1, integer2
    PetscReal  :: real1, real2
    PetscReal  :: real3, real4
    character(len=MAXWORDLENGTH) :: word
    PetscReal, pointer :: real_p(:)

    ...
    ! use the newer relational operators in logical expressions
    if (grid%ndof >= 2 .and. (.not.logical_whatever .or. &
        integer1 /= integer2)) then
      do i=1,2
        call Whatever()
      enddo
    elseif (grid%ndof == 1) then
      call SomethingElse()
    endif

    ! fortran switch
    select case (word)
      case ('flow')
        call Whatever
      case ('transport')
        call Whatever2(argument1, argument2, argument3, argument4, &
                       argument5)
    end select
    ...
    nullify(real_p)

  end subroutine GridSetup

  !************************************************************************** !

  PetscReal function GridGetTime(...)
  !
  ! Returns the current time in the simulation.
  ! Author: John Doe
  ! Date: 01/01/07
  !
    use another_module

    implicit none

  #include "whatever.h"

    PetscInt :: integer1
    PetscReal :: real1
    character(len=MAXWORDLENGTH) :: word

    ...
    ...
    GridGetTime = x

  end function GridGetTime

  end module Example_module
