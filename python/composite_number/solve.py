def is_number_composite_3_5(num: int) -> bool:
  if num <= 0:
    return False
  if (num % 3 == 0) or (num % 5 == 0):
    return True

  if num >= 5:
    return is_number_composite_3_5(num - 5)
  if num >= 3:
    return is_number_composite_3_5(num - 3)

  return False


def is_number_composite_of(num: int, composite_of: set[int]) -> bool:
  if num <= 0:
    return False

  for elem in composite_of:
    if (num % elem == 0):
      return True

  max_elem: int = max(composite_of)
  if max_elem > num:
    new_composite_of = composite_of - {max_elem}
    if new_composite_of:
      return is_number_composite_of(num - max_elem, composite_of)
    return False

  return is_number_composite_of(num - max_elem, composite_of)
