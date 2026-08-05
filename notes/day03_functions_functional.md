# Day 03 — Functions Deep Dive & Functional Programming

## `*args` and `**kwargs`
- `*args` collects extra **positional** arguments into a **tuple** — order matters, no names needed. Best for a variable number of similar-type values (e.g. `get_stats(*args)` over any count of numbers).
- `**kwargs` collects extra **keyword** arguments into a **dict** — names matter, order doesn't. Best for optional, self-describing settings (e.g. `build_config(**kwargs)`, or forwarding args into a wrapped function call).
- Neither enforces argument types — Python places no restriction on what goes into `args`/`kwargs`; any type-checking is on the function author.

## LEGB Scope Resolution
- Python resolves a variable name by searching, in order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in — and stops at the first match.
- If the name isn't found at any level, Python raises `NameError` — but only at the moment the line actually **runs**, not when the function is defined.
- **Referencing** a variable follows LEGB automatically. **Assigning** to a variable inside a function makes Python treat it as a new local by default — even if a same-named variable exists in an enclosing/global scope. This is why closures need the `nonlocal` keyword to explicitly modify an enclosing variable instead of shadowing it.

## Closures
- A closure is an inner function that "remembers" variables from its enclosing scope, even after the outer function has finished running.
- `nonlocal` is required to **modify** (not just read) an enclosing-scope variable from inside a nested function.
- Each call to the outer function creates a fresh, independent enclosing scope — so closures created from separate calls don't share state.

## `map()`, `filter()`, `reduce()`
- `map(func, iterable)` — applies `func` to every element, returns a map object (wrap in `list()` to see it).
- `filter(func, iterable)` — keeps only elements where `func` returns `True`.
- `reduce(func, iterable, initial)` — folds the iterable down to a single value. **Always pass an initial value** when the iterable might be empty — without it, `reduce()` raises `TypeError` on empty input. (Confirmed with `factorial(0)` and an empty-list pipeline today.)
- If `func` is just an existing function with no extra logic (e.g. `len`), pass it directly — no need to wrap it in a lambda (`map(len, words)` instead of `map(lambda w: len(w), words)`).

## `zip()` and `enumerate()`
- `zip()` pairs up multiple iterables element-by-element into tuples, and **silently truncates to the shortest one** on length mismatch — no error, no warning. (`itertools.zip_longest()` or `zip(..., strict=True)` in 3.10+ exist if that's not the wanted behavior.)
- `enumerate(iterable, start=1)` — pairs each element with an index, `start` controls where counting begins (useful for 1-based ranks instead of 0-based).
- `sorted()` is a **stable sort** — equal elements keep their original relative order. Confirmed hands-on with a tied leaderboard.

## Lambdas
- A `lambda` is an **expression** (evaluates to a function object, can be inlined anywhere a value is expected), unlike `def` which is a **statement** that binds a name.
- Because of this, `lambda` bodies can only contain a single expression — no loops, no multi-statement logic, no assignment. Ternary expressions (`lambda x: 'a' if cond else 'b'`) are fine since they're still expressions.
- Use `def` instead of `lambda` when logic needs more than one line, a loop, real branching, or reuse elsewhere (e.g. `prime_check(n)` needed a loop, so it couldn't be a lambda).

## Mistakes / Things to Remember
- `range()` requires integer arguments — `n**0.5` returns a float, so it must be wrapped in `int()` before use in `range()`.
- Validating "is this string a number" by stripping allowed characters (`.replace('.','').replace('-','')` then `.isdigit()`) is fragile and lets invalid strings like `'1.2.3'` or `'--5'` slip through. Wrapping the *actual* conversion in `try/except ValueError` is far more robust — trust Python's own parser instead of reimplementing its rules.
- `dict.update()` mutates in place and returns `None` — same trap as Day 2's dict notes, just resurfaced in a `**kwargs` context (`d = kwargs.update(...)` wipes `d` to `None`).
- The `|` merge operator (`dict1 | dict2`) is a clean, non-mutating way to combine dicts — later dict's keys win on conflict.
- `reduce()`'s initial value isn't just a nice-to-have — it's what avoids special-casing empty input (`n=0` in factorial, empty list in the functional pipeline) instead of writing manual `if` guards.