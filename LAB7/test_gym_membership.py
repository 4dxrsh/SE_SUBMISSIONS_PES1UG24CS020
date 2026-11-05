import string

from hypothesis import given, strategies as st

from gym_membership import parse_plan, calculate_bmi, average_workout


# ---------- 1. No-crash fuzz tests (skeleton, completed) ----------

@given(st.text() | st.none())
def test_parse_plan_no_crash(s):
    try:
        parse_plan(s)
    except Exception as e:
        assert False, f"parse_plan crashed with {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_calculate_bmi_no_crash(s):
    try:
        calculate_bmi(s)
    except Exception as e:
        assert False, f"calculate_bmi crashed with {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_average_workout_no_crash(s):
    try:
        average_workout(s)
    except Exception as e:
        assert False, f"average_workout crashed with {type(e).__name__}: {e}"


# ---------- 2. Wider fuzzing: any type, plus structured text ----------

ANY_INPUT = st.one_of(
    st.none(), st.integers(), st.floats(), st.booleans(),
    st.text(), st.lists(st.integers()),
)
STRUCTURED_TEXT = st.text(alphabet="0123456789.,-+eEnaifty \t", max_size=30)


@given(ANY_INPUT | STRUCTURED_TEXT)
def test_parse_plan_any_input_no_crash(x):
    try:
        parse_plan(x)
    except Exception as e:
        assert False, f"parse_plan crashed with {type(e).__name__}: {e}"


@given(ANY_INPUT | STRUCTURED_TEXT)
def test_calculate_bmi_any_input_no_crash(x):
    try:
        calculate_bmi(x)
    except Exception as e:
        assert False, f"calculate_bmi crashed with {type(e).__name__}: {e}"


@given(ANY_INPUT | STRUCTURED_TEXT)
def test_average_workout_any_input_no_crash(x):
    try:
        average_workout(x)
    except Exception as e:
        assert False, f"average_workout crashed with {type(e).__name__}: {e}"


# ---------- 3. Correctness on valid input ----------

@given(
    st.text(alphabet=string.ascii_letters, min_size=1, max_size=15),
    st.integers(min_value=1, max_value=120),
)
def test_parse_plan_valid(plan, months):
    assert parse_plan(f"{plan}-{months}") == (plan.upper(), months)


@given(
    st.floats(min_value=1, max_value=500),
    st.floats(min_value=0.5, max_value=3),
)
def test_calculate_bmi_valid(weight, height):
    assert calculate_bmi(f"{weight},{height}") == round(weight / (height ** 2), 1)


@given(st.lists(st.integers(min_value=0, max_value=1000), min_size=1, max_size=20))
def test_average_workout_valid(values):
    text = " ".join(str(v) for v in values)
    assert average_workout(text) == sum(values) // len(values)


# ---------- 4. Invalid input must be rejected cleanly (return None) ----------

@given(st.text().filter(lambda s: "-" not in s))
def test_parse_plan_missing_dash_rejected(s):
    assert parse_plan(s) is None


@given(st.floats(min_value=1, max_value=500))
def test_calculate_bmi_zero_height_rejected(weight):
    assert calculate_bmi(f"{weight},0") is None


@given(st.text(alphabet=" \t\n", max_size=10))
def test_average_workout_empty_rejected(s):
    assert average_workout(s) is None