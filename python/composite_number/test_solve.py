import pytest

from python.composite_number.solve import (
  is_number_composite_3_5, is_number_composite_3_5_dynamic,
  is_number_composite_of, is_number_composite_of_dynamic)


normal_positive_data_composite_3_5: list[int] = [3, 5, 15, 17, 121, 122, 558, 621, 11111111]

@pytest.mark.parametrize("num", normal_positive_data_composite_3_5)
def test_normal_positive_is_number_composite_3_5(num):
  assert is_number_composite_3_5(num) == True


@pytest.mark.parametrize("num", normal_positive_data_composite_3_5)
def test_normal_positive_is_number_composite_3_5_dynamic(num):
  assert is_number_composite_3_5_dynamic(num) == True


normal_negative_data_composite_3_5: list[int] = [1, 2, 4, 7]

@pytest.mark.parametrize("num", normal_negative_data_composite_3_5)
def test_normal_negative_is_number_composite_3_5(num):
  assert is_number_composite_3_5(num) == False

@pytest.mark.parametrize("num", normal_negative_data_composite_3_5)
def test_normal_negative_is_number_composite_3_5_dynamic(num):
  assert is_number_composite_3_5_dynamic(num) == False


edge_negative_data_composite_3_5: list[int] = [0, -2, -3, -5]

@pytest.mark.parametrize("num", edge_negative_data_composite_3_5)
def test_edge_negative_is_number_composite_3_5(num):
  assert is_number_composite_3_5(num) == False


@pytest.mark.parametrize("num", edge_negative_data_composite_3_5)
def test_edge_negative_is_number_composite_3_5_dynamic(num):
  assert is_number_composite_3_5_dynamic(num) == False


normal_positive_data_composite_of: list[tuple[int, set[int]]] = [
  (3, {3, 5}),
  (15, {3, 5}),
  (17, {3, 5}),
  (17, {2, 3, 5}),
  (15, {2, 3}),
  (18, {2, 3}),
  (20, {5, 10}),
  (155, {5, 10})
]

@pytest.mark.parametrize(("num", "composite_of"), normal_positive_data_composite_of)
def test_normal_positive_is_number_composite_of(num, composite_of):
  assert is_number_composite_of(num, composite_of) == True

@pytest.mark.parametrize(("num", "composite_of"), normal_positive_data_composite_of)
def test_normal_positive_is_number_composite_of_dynamic(num, composite_of):
  assert is_number_composite_of_dynamic(num, composite_of) == True


normal_negative_data_composite_of: list[tuple[int, set[int]]] = [
  (1, {3, 5}),
  (2, {3, 5}),
  (4, {3, 5}),
  (7, {3, 5}),
  (32, {5, 10}),
  (122, {5, 10})
]

@pytest.mark.parametrize(("num", "composite_of"), normal_negative_data_composite_of)
def test_normal_negative_is_number_composite_of(num, composite_of):
  assert is_number_composite_of(num, composite_of) == False

@pytest.mark.parametrize(("num", "composite_of"), normal_negative_data_composite_of)
def test_normal_negative_is_number_composite_of_dynamic(num, composite_of):
  assert is_number_composite_of_dynamic(num, composite_of) == False


edge_negative_data_composite_of: list[tuple[int, set[int]]] = [
  (0, {3, 5}),
  (-2, {3, 5}),
  (-3, {3, 5}),
  (-5, {3, 5})
]

@pytest.mark.parametrize(("num", "composite_of"), edge_negative_data_composite_of)
def test_edge_negative_is_number_composite_of(num, composite_of):
  assert is_number_composite_of(num, composite_of) == False

@pytest.mark.parametrize(("num", "composite_of"), edge_negative_data_composite_of)
def test_edge_negative_is_number_composite_of_dynamic(num, composite_of):
  assert is_number_composite_of_dynamic(num, composite_of) == False


if __name__ == "__main__":
  pytest.main([__file__])