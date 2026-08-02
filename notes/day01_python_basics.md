# Day 01 — Python Core Syntax Refresh

## Variables & Dynamic Typing
- Python variables don't have a fixed type — a variable just points to whatever object is assigned to it, and it can point to a different type later.
- e.g. `x = 5` (int) then `x = "5"` (str) — both valid, no error.

## Data Types
- `int` — whole numbers
- `float` — decimals
- `str` — text
- `bool` — True/False
- `complex` — numbers with an imaginary part (e.g. `2 + 3j`)

## Type Casting
- `int()`, `float()`, `str()` convert between types.
- `int("42")` → 42, but `int("3.5")` throws an error — use `float("3.5")` first, then `int(...)` if you need to drop the decimal.

## Operators

**Arithmetic**: `+ - * / // % **`
- `/` = true division, always returns float (`7/2 = 3.5`)
- `//` = floor division — **not just truncation**. It rounds toward negative infinity.
  - `7 // 2 = 3` but `-7 // 2 = -4` (not -3!) — gotcha to remember.

**Comparison**: `== != > < >= <=`

**Logical**: `and or not` — short-circuits (stops evaluating as soon as the result is known).

**Bitwise**: `& | ^ ~ << >>`
- `&` = AND, `|` = OR, `^` = XOR, `~` = NOT (flips bits)
- `<<` shifts bits left, fills with 0 on the right — same as multiplying by `2**n`
  - `5 << 2` → `0101` becomes `010100` → 20 (5 × 4)
- `>>` shifts bits right — same as floor-dividing by `2**n`

**Assignment shorthand**: `+= -= *= /= //= **=`

## Conditionals
- Standard `if / elif / else` — needs a colon `:` after every condition (forgot this once today — Python won't let you skip it).
- **Ternary syntax**: `value_if_true if condition else value_if_false`
  - Condition sits in the *middle* — unlike C-style `condition ? true : false`.
  - Nested ternary example (num sign checker):
```python
    num = int(input())
    sign = "zero" if num == 0 else "positive" if num > 0 else "negative"
```
  - Nesting evaluates right to left — keep it to 2 levels max, beyond that use if/elif for readability.

## Mistakes / things to remember
- `//` rounds toward negative infinity, not zero — matters with negative numbers.
- `bool("False")` is `True` — any non-empty string is truthy, even the string `"False"`.