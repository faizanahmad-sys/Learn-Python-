# Python Chapter 3 — Lists and Tuples

## Lists
A list stores a collection of values and can hold different data types (int, float, string, etc.).

```python
marks = [10, 20, 30, 59]
student = ["ali", 45.5, 100]

print(type(marks))   # <class 'list'>
print(marks[0])       # 10
print(len(student))   # 3
```

**Mutability:** Strings are immutable, but lists are mutable.
```python
student[0] = "faizan"
print(student)
```

**Slicing:** `list[start:stop]` — stop index is excluded.
```python
let_marks = [1, 2, 3, 4, 5]
print(let_marks[1:3])   # [2, 3]
```

**Common List Functions**
```python
my_list = [1, 2, 3, 4]
my_list.append(5)            # adds element at end
my_list.sort()                 # ascending order
my_list.sort(reverse=True)   # descending order
my_list.reverse()              # reverses order
my_list.insert(2, 99)          # inserts at index
```

## Tuples
Tuples are like lists but **immutable** (cannot be changed after creation).

```python
tup = (1, 2, 3)
print(tup[0])   # 1

empty_tuple = ()
print(type(empty_tuple))   # <class 'tuple'>
```

## Practice Question
