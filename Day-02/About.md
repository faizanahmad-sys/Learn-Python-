# Python Learning Journey: Strings & Conditional Statements

Welcome to today's study notes! This file covers the fundamentals of the **String data type** and **Conditional Statements** in Python, complete with syntax rules, built-in functions, and practical code examples.

---

## 📝 Part 1: String Data Type

A string is a sequence of characters. In Python, strings are **immutable** (meaning they cannot be changed after they are created).

### 1. Initialization & Syntax
Strings can be enclosed in single, double, or triple quotes. Triple quotes are typically used for multi-line strings.
* **Newline Character:** Use `\n` to insert a break and start a new line.
* **Concatenation:** You can join two or more strings together using the `+` operator.
* **Length:** Use the built-in `len()` function to get the total number of characters.

### 2. Indexing & Slicing
Python uses **0-based indexing**, meaning the first character starts at index `0`. Negative indexing allows you to count backward from the end of the string (e.g., `-1` is the last character).

* **Slicing Syntax:** `string[start:stop:step]`
    * `start`: The starting index (inclusive).
    * `stop`: The ending index (exclusive).
    * `step`: Determines the increment between each character (e.g., a step of `2` selects every second character).

> ⚠️ **Note on Immutability:** Attempting to modify a specific character via its index (like `str1[0] = "F"`) will result in a `TypeError`. To update a string, you must create a new one using concatenation and slicing: 
> `str1 = "F" + str1[1:]`

### 3. Essential String Methods
Python provides several built-in methods to manipulate and query strings:

| Method | Description | Example |
| :--- | :--- | :--- |
| `.upper()` | Converts all characters to uppercase. | `"hi".upper()` $\rightarrow$ `"HI"` |
| `.lower()` | Converts all characters to lowercase. | `"HI".lower()` $\rightarrow$ `"hi"` |
| `.strip()` | Removes leading and trailing whitespaces. | `"  hi  ".strip()` $\rightarrow$ `"hi"` |
| `.capitalize()` | Capitalizes only the very first character. | `"hello world".capitalize()` $\rightarrow$ `"Hello world"` |
| `.replace(old, new)` | Replaces occurrences of a substring with a new one. | `"hello".replace("e", "a")` $\rightarrow$ `"hallo"` |
| `.find(substring)` | Returns the index of the first occurrence of a substring. | `"hello".find("l")` $\rightarrow$ `2` |
| `.count(substring)` | Counts how many times a substring appears. | `"hello".count("l")` $\rightarrow$ `2` |
| `.startswith(prefix)` | Returns `True` if the string starts with the prefix. | `"hello".startswith("he")` $\rightarrow