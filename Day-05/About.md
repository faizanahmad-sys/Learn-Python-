# 🐍 Python Loops - Notes & Practice

## Topics Covered
| Topic | Description |
|-------|-------------|
| `while` loop | Condition-based repetition |
| `for` loop | Sequence iteration |
| `break` | Exit the loop immediately |
| `continue` | Skip current iteration |
| `range()` | Generate number sequences |
| `pass` | Placeholder statement |
| `for-else` | Else block runs when loop finishes without break |

## While Loop Flow
Initialization → Condition Check → Execute → Update → Repeat

## range() Syntax
range(start, stop, step)
- start → optional (default 0)
- stop  → required, not included in output
- step  → optional (default 1)

## Practice Questions
| # | Question |
|---|----------|
| 1 | Print your name 5 times |
| 2 | Print multiplication table of 3 |
| 3 | Print all elements of a list |
| 4 | Print family names from a list |
| 5 | Search for number x in a tuple |
| 6 | Print list elements using for loop |
| 7 | Find all occurrences of x in a tuple |
| 8 | Sum of first n natural numbers |
| 9 | Factorial of n |

## Bug Fixes from Original Code
- `fact *= 1` → fixed to `fact *= i` (factorial was always returning 1)
- `str` renamed to `names` (str is a Python built-in, never use it as variable name)
- `enumerate()` used for cleaner index tracking in search problems

## File
| File | Description |
|------|-------------|
| `loops_notes.py` | All notes + practice code |

*Part of CodeByFaizan Python Learning Series 🚀*