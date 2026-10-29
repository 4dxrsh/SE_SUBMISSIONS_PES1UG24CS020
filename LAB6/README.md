# L6_L7_21_gym_membership: Gym Membership

Lab 6: Code and Branch Coverage Analysis

**Name:** Adarsh Rajesh
**SRN:** PES1UG24CS020 (Section A)
**Course:** Software Engineering, PES University

## About

A small Python module that works out gym membership costs with discounts and trainer add-ons, checks entry rules, and reports BMI category. The lab is about measuring how much of this code the tests actually exercise, using line coverage and branch coverage.

## Files

- `gym_membership.py`: the module under test
- `test_gym_membership.py`: starter test file (left unchanged)
- `CodeCoverageTest_gym_membership.py`: tests written to reach full line coverage
- `BranchCoverageTest_gym_membership.py`: tests written to reach full branch coverage
- `code_coverage.png`: terminal screenshot of the line coverage report
- `branch_coverage.png`: terminal screenshot of the branch coverage report

## Setup

```
pip install coverage pytest
```

On Windows, if the commands are not recognised, use `python -m coverage` and `python -m pytest` instead.

## How to run

**Line coverage:**

```
python -m coverage run -m pytest CodeCoverageTest_gym_membership.py
python -m coverage report -m
```

**Branch coverage:**

```
python -m coverage run --branch -m pytest BranchCoverageTest_gym_membership.py
python -m coverage report -m
```

## Results

**Line coverage:** 15 tests, 35 of 35 statements covered, 100%.

**Branch coverage:** 25 tests, 35 of 35 statements and 26 of 26 branches covered, 100%.

Running the line coverage tests with `--branch` gives 98%, with branch `16->18` missing. That is the case where `with_trainer` is true but the plan is not yearly. Line coverage cannot see this, because every line already ran once. This is the gap that the branch coverage tests close.

## What the tests cover

**membership_cost:** unknown plan, age below 14, age 14, age 59 and 60 boundary, senior discount, student discount, a senior who is also a student (only the senior discount applies), trainer on monthly and yearly plans.

**can_enter:** inactive plan, hours 4, 5, 22 and 23, women-only slot for F and M, normal slot.

**bmi_category:** invalid height, all four categories, and the exact boundaries 18.5, 25 and 30.

## Commits

1. Code coverage tests and report screenshot
2. Branch coverage tests and report screenshot
