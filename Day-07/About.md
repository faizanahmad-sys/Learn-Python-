# Python File Input / Output (I/O) — Study Notes 📂



---

## 📌 1. Introduction to File I/O

When we save data inside variables while running a Python program, that data is stored in volatile memory (RAM) and gets deleted as soon as the program terminates. To store data **permanently**, we use **Files**.

Python supports two main categories of files:
1. **Text Files:** `.txt`, `.py`, `.java`, `.html`, etc. (Structured as human-readable characters).
2. **Binary Files:** `.mp4`, `.png`, `.jpg`, `.pdf`, etc. (Structured as raw machine-readable bytes).

---

## 📂 2. Operations on a File

To work with any file in Python, you must follow a strict three-step lifecycle:
1. **Open** the file using the built-in `open()` function.
2. **Process** the data by either Reading or Writing.
3. **Close** the file using the `close()` function to free up system memory resources.

### Basic Syntax
```python
f = open("file_name.txt", "mode")
# ... perform read or write operations ...
f.close()