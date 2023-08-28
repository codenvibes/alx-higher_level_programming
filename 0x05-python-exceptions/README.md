# **0x05. PYTHON - EXCEPTIONS**
`Python`

<!-- # Background Context -->

# Resources
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4) (starting at minute 7)

<!-- man or help:
- `` -->

# Learning Objectives
<details>
<summary><h3>What’s the difference between errors and exceptions</h3></summary>

In Python, both errors and exceptions are types of issues that can occur during program execution, but they serve different purposes and are handled in distinct ways.

1. **Errors:**
Errors are issues that prevent the program from running successfully. They are generally more severe and occur when there is a problem that Python cannot recover from. Errors are typically detected during the program's compilation phase (before execution) and can include things like syntax errors or import errors.

   For example, if you have a syntax error like a missing parenthesis or an undefined variable, Python will raise an error and your program won't run at all.

2. **Exceptions:**
Exceptions are issues that occur during the execution of a program and can disrupt the normal flow of the program. They are usually caused by external factors or unexpected conditions that the programmer might not have anticipated. Python provides a mechanism to handle exceptions gracefully, allowing you to catch them and take appropriate action rather than letting the program crash.

   Exceptions can be caused by various reasons such as dividing by zero, attempting to access an index that doesn't exist in a list, or opening a file that doesn't exist. When an exception occurs, Python raises an exception object, and you can catch and handle it using `try` and `except` blocks.

Here's an example that demonstrates the difference between errors and exceptions in Python:

```python
# Error - Syntax error
print("Hello World"

try:
    # Exception - Division by zero
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

In this example, the syntax error (`print("Hello World"`) is an error that prevents the program from running, while the division by zero (`10 / 0`) is an exception that can be caught and handled using an exception handler.

To sum up, errors are issues detected during the program's compilation phase that prevent it from running, while exceptions are issues that occur during runtime and can be caught and managed using exception handling mechanisms.

<br>
<br>
<p align="center">***********</p>

> what's the difference between compilation time and runtime:<br>
   Compilation Time: This is the phase where the source code is translated into machine-readable code and checked for syntax errors. It is a preparatory step before the program can be executed.
   Runtime: This is the phase where the compiled code is actually executed by the computer's processor. It involves processing data, performing calculations, and carrying out the tasks defined by the program.
</details>

<details>
<summary><h3>What are exceptions and how to use them</h3></summary>
</details>

<details>
<summary><h3>When do we need to use exceptions</h3></summary>
</details>

<details>
<summary><h3>How to correctly handle an exception</h3></summary>
</details>

<details>
<summary><h3>What’s the purpose of catching exceptions</h3></summary>
</details>

<details>
<summary><h3>How to raise a builtin exception</h3></summary>
</details>

<details>
<summary><h3>When do we need to implement a clean-up action after an exception</h3></summary>
</details>

# Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

# Tasks
<details>
<summary>

### 0. 
`mandatory`

File: [0-safe_print_list.py]()
</summary>

Write a function that prints `x` elements of a list.
- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- Returns the real number of elements printed
- You have to use `try: / except:`
- You are not allowed to import any module
- You are not allowed to use `len()`
```bash
guillaume@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$ 
```
</details>

<details>
<summary>

### 1. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 2. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 3. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 4. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 5. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 6. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 6. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 7. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 8. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 9. 
`#advanced`

File: []()
</summary>


</details>

