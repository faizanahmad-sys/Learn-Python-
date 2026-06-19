# ============================================================
#  Python Loops - Notes & Practice
#  Topics: while loop, for loop, break, continue, range(), pass
# ============================================================


# ------------------------------------------------------------
# THEORY
# ------------------------------------------------------------

# Why use loops?
#   - To repeat a block of code multiple times
#   - To make code shorter and cleaner

# Python has 2 main types of loops:
#   1. while loop
#   2. for loop


# ============================================================
# 1. WHILE LOOP
# ============================================================

# Syntax:
# ---------
# count = start_value
# while condition:
#     # do something
#     count += 1   # update condition (required, otherwise infinite loop)

# Execution Flow:
#   Initialization → Condition Check → Execute → Update → Repeat


# --- Practice Q1: Print name 5 times ---
count = 1
while count <= 5:
    print("Faizan Ahmad")
    count += 1


# --- Practice Q2: Print multiplication table of 3 ---
n = 1
while n <= 10:
    print(n * 3)
    n += 1


# --- Practice Q3: Print all elements of a list ---
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# --- Practice Q4: Print family names from a list ---
names = ["Faizan", "Affaq", "Riaz", "Waqar", "Imtiaz"]
i = 0
while i < len(names):
    print(names[i])
    i += 1


# --- Practice Q5: Search for number x in a tuple ---
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 81
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        break
    i += 1


# ============================================================
# IMPORTANT KEYWORDS: break & continue
# ============================================================

# break     → terminates the loop immediately when encountered
# continue  → skips the current iteration and moves to the next one


# ============================================================
# 2. FOR LOOP
# ============================================================

# When to use:
#   - When iterating over a sequence (list, tuple, string)
#   - When the number of iterations is known in advance

# Syntax:
# ---------
# for element in sequence:
#     # do something

# for-else Syntax:
# -----------------
# for element in sequence:
#     print(element)
# else:
#     print("Loop finished")   # runs only when loop completes without break


# --- Example: for loop on a list ---
numbers = [1, 2, 3, 4, 5]
for val in numbers:
    print(val)


# --- Example: for loop on a tuple ---
names_tuple = ("Ali", "Hussain", "Abbas")
for val in names_tuple:
    print(val)


# --- Example: for-else with break ---
text = "faizanahmad"
for char in text:
    if char == 'n':
        print("Found 'n'!")
        break
    print(char)
else:
    print("Loop ended without finding 'n'")


# --- Practice Q6: Print list elements using for loop ---
num_list = [1, 5, 6, 6, 7, 2, 6, 7, 6, 66, 64, 646]
for val in num_list:
    print(val)


# --- Practice Q7: Find all occurrences of x in a tuple ---
num_tuple = (1, 5, 6, 6, 7, 2, 6, 7, 6, 66, 64, 646)
x = 6
for idx, val in enumerate(num_tuple):
    if val == x:
        print(f"Found {x} at index {idx}")


# ============================================================
# range() FUNCTION
# ============================================================

# range() returns a sequence of numbers
# Syntax: range(start, stop, step)
#   - start  → optional, default = 0
#   - stop   → required (this value is NOT included)
#   - step   → optional, default = 1

for i in range(10):        # 0 to 9
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)


# ============================================================
# pass STATEMENT
# ============================================================

# pass is a null statement — it does nothing
# Used as a placeholder when you plan to add code later

for i in range(5):
    pass  # TODO: add logic here later


# ============================================================
# PRACTICE QUESTIONS
# ============================================================

# Q1: Find sum of first n natural numbers
n = 5
total = 0
for i in range(n + 1):
    total += i
print("Sum =", total)  # Output: Sum = 15


# Q2: Find factorial of n
# Bug fix: original code had "fact *= 1" which always gives 1
n2 = 6
factorial = 1
for i in range(1, n2 + 1):
    factorial *= i
print("Factorial =", factorial)  # Output: Factorial = 720