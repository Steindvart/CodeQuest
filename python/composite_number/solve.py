# Classis solution  - algo: O(2^n/max); memory: O(1)

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

# Dynamic solution - algo: O(n); memory: O(n)

g_mem_composite_3_5_dynamic: dict[int, bool] = {}

def is_number_composite_3_5_dynamic(num: int) -> bool:
  if num <= 0:
    return False
  if num in g_mem_composite_3_5_dynamic:
    return g_mem_composite_3_5_dynamic[num]

  if (num % 3 == 0) or (num % 5 == 0):
    g_mem_composite_3_5_dynamic[num] = True
    return True

  if num >= 5:
    return is_number_composite_3_5(num - 5)
  if num >= 3:
    return is_number_composite_3_5(num - 3)

  g_mem_composite_3_5_dynamic[num] = False
  return False

# Classis solution - algo: O(2^n/max); memory: O(1)

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

# Dynamic solution - algo: O(n); memory: O(n)

g_mem_composite_of_dynamic: dict[int, dict[frozenset, bool]] = {}

def is_number_composite_of_dynamic(num: int, composite_of: set[int]) -> bool:
  if num <= 0:
    return False

  frozen_composite_of = frozenset(composite_of)

  if num in g_mem_composite_of_dynamic and frozen_composite_of in g_mem_composite_of_dynamic[num]:
    return g_mem_composite_of_dynamic[num][frozen_composite_of]

  for elem in composite_of:
    if (num % elem == 0):
      g_mem_composite_of_dynamic.setdefault(num, {})[frozen_composite_of] = True
      return True

  max_elem: int = max(composite_of)
  if max_elem > num:
    new_composite_of = composite_of - {max_elem}
    if new_composite_of:
      result = is_number_composite_of_dynamic(num, new_composite_of)
      g_mem_composite_of_dynamic.setdefault(num, {})[frozen_composite_of] = result
      return result

    g_mem_composite_of_dynamic.setdefault(num, {})[frozen_composite_of] = False
    return False

  result = is_number_composite_of_dynamic(num - max_elem, composite_of)
  g_mem_composite_of_dynamic.setdefault(num, {})[frozen_composite_of] = result
  return result