import pytest

from python.composite_number.solve import is_number_composite_3_5, is_number_composite_of

@pytest.mark.parametrize(
  "num",
  [
    3, 5, 15, 17
  ]
)
def test_normal_positive_is_number_composite_3_5(num):
  assert is_number_composite_3_5(num) == True

@pytest.mark.parametrize(
  "num",
  [
    1, 2, 4, 7
  ]
)
def test_normal_negative_is_number_composite_3_5(num):
  assert is_number_composite_3_5(num) == False

@pytest.mark.parametrize(
  "num",
  [
    0, -2, -3, -5
  ]
)
def test_edge_negative_is_number_composite_3_5(num):
  assert is_number_composite_3_5(num) == False


@pytest.mark.parametrize(
  ("num", "composite_of"),
  [
    (3, {3, 5}),
    (15, {3, 5}),
    (17, {3, 5}),
    (17, {2, 3, 5}),
    (15, {2, 3}),
    (18, {2, 3})
  ]
)
def test_normal_positive_is_number_composite_of(num, composite_of):
  assert is_number_composite_of(num, composite_of) == True

@pytest.mark.parametrize(
  ("num", "composite_of"),
  [
    (1, {3, 5}),
    (2, {3, 5}),
    (4, {3, 5}),
    (7, {3, 5})
  ]
)
def test_normal_negative_is_number_composite_of(num, composite_of):
  assert is_number_composite_of(num, composite_of) == False

@pytest.mark.parametrize(
  ("num", "composite_of"),
  [
    (0, {3, 5}),
    (-2, {3, 5}),
    (-3, {3, 5}),
    (-5, {3, 5})
  ]
)
def test_edge_negative_is_number_composite_of(num, composite_of):
  assert is_number_composite_of(num, composite_of) == False


if __name__ == "__main__":
  pytest.main([__file__])