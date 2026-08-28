from common.parameters import OPT_TOL
from numerical.parameter_checks import boundary_cases,generate_admissible
from numerical.regression_checks import assert_pass,direct_opt_errors,efforts,gaps_derivatives,run_checks
def test_deterministic_sample(): assert generate_admissible(3)==generate_admissible(3)
def test_admissible_effort_ordering():
    for x in generate_admissible(100):
        ep,ec,ew=efforts(x); assert 0<ep<ec<ew; dcp,dwp=gaps_derivatives(x); assert dcp>0 and dwp>0
def test_direct_optimization_matches_closed_forms():
    for x in generate_admissible(10): assert max(direct_opt_errors(x))<OPT_TOL
def test_full_numerical_regression_10k():
    r=run_checks(10_000); assert_pass(r)
def test_boundary_cases_exist_and_are_admissible_smoke_inputs(): assert len(boundary_cases())==5
