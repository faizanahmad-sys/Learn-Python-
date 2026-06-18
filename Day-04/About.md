# Python — Dictionary & Set

Practice file covering core concepts of dict and set in Python.

Language: Python 3  
Level: Beginner

---

## What this file covers

### Dictionary basics
Creating a dict with key-value pairs, accessing values by key, nesting dicts,
and using methods like .keys(), .values(), .items(), .get(), .update()

### Set basics
Creating a set, automatic removal of duplicates, unordered nature,
empty set creation with set(), and methods: .add(), .remove(), .clear(), .pop()

### Set operations
Using .intersection() to find common elements and .union() to combine two sets.

### Practice questions
Storing word meanings in a dict, and using a set to count unique subjects
(classrooms needed).

---

## Bugs to fix

1. `let_set` used before defined
   Variable let_set is never initialized.
   Fix: add `let_set = set()` before using it.

2. `set.add(1,2,4,5)` — wrong syntax
   .add() takes only one element at a time.
   Fix: use `.update([1,2,4,5])` to add multiple elements.

3. `set1.union(seT1)` — wrong variable name
   set1 is undefined.
   Fix: should be `set0.union(seT1)` to match the defined variable.

4. Overwriting built-ins
   Variables named `set` and `dict` shadow Python's built-in types.