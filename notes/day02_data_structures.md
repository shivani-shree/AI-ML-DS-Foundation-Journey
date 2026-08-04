# Day 02 — Data Structures Refresh

## Comparison Table — List vs Tuple vs Set vs Dict

| Feature | List | Tuple | Set | Dict |
|---|---|---|---|---|
| **Mutability** | Mutable (can change after creation) | Immutable (cannot change after creation) | Mutable (can add/remove elements) | Mutable (can add/remove/update key-value pairs) |
| **Ordering** | Ordered (preserves insertion order) | Ordered (preserves insertion order) | Unordered (no guaranteed order) | Ordered (preserves insertion order, guaranteed since Python 3.7) |
| **Duplicates** | Allowed | Allowed | Not allowed (auto-dedupes) | Keys must be unique; values can repeat |
| **Indexing/Access** | By position (`lst[0]`) | By position (`tup[0]`) | No indexing — only membership check (`x in s`) | By key (`d[key]`) |
| **Hashable (usable as dict key / set element)** | No | Yes (if all contents are also immutable) | No | No |
| **Typical use-case** | Ordered collection that changes — e.g. a growing list of scores, a queue | Fixed records that shouldn't change — e.g. coordinates `(x, y)`, RGB values, function returns of multiple values | Uniqueness + fast membership checks — e.g. deduping, common-elements problems | Key-based lookup — e.g. word counts, contact books, any "label → data" mapping |
| **Lookup time (average)** | O(n) — linear scan for `in` checks | O(n) — linear scan for `in` checks | O(1) — hash-based | O(1) — hash-based |
| **Memory** | Higher — allocates extra room to allow growth | Lower — fixed size known at creation, no extra allocation | Higher — hash table overhead | Higher — hash table overhead |

## Why Tuples Are Faster Than Lists
- Tuples are immutable, so Python knows the exact size upfront and never needs to over-allocate memory for future growth (unlike lists, which reserve extra space in case of `.append()`).
- Because tuples can't change, they're **hashable** (as long as everything inside them is also immutable) — this is why tuples can be used as dictionary keys or set elements, but lists cannot.
- Choose a tuple over a list when the data represents a fixed, unchanging record (e.g. `(latitude, longitude)`) or when it needs to be hashable (e.g. as a dict key).

## How Python Dictionaries Achieve O(1) Lookup
- Each key is passed through a **hash function** (`hash(key)`), which converts it into a number.
- That number determines which **bucket** (slot in an internal array) the key-value pair is stored in.
- On lookup, Python re-hashes the requested key and jumps **directly** to that bucket — no scanning through every item like a list's `in` check would require.
- This direct jump is why average-case lookup is O(1), regardless of how many items are in the dictionary.
- **Collisions**: two different keys can hash to the same bucket. Python resolves this internally (probing for another slot), which is why lookup is *average* O(1), not a strict guarantee in every case.

## Mistakes / Things to Remember
- `dict1 = dict2` does **not** create a copy — both names point to the *same* dictionary object. Mutating one mutates the other. Use `dict(dict1)` (or `.copy()`) to get an independent copy.
- `.update()` merges in place and returns `None` — never do `d = d.update(...)`, it wipes out `d`.
- `dict.get(key, default)` is the standard idiom for safe counting/lookup without a `KeyError` — used throughout today's word-frequency and contact-book tasks.
- `word.isalpha()` returns `False` for apostrophes — stripping punctuation with only `isalpha()`/`isspace()` will break contractions (`"isn't"` → `"isnt"`) unless you explicitly allow `'` too.
- Average of a list of values (e.g. average word length) must sum over **every occurrence**, not just unique values — dividing by unique count instead of total count gives a different (wrong) number when there are duplicates.