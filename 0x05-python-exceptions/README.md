<h1 align="center"><b>0x05. PYTHON - EXCEPTIONS</b></h1>
<div align="center"><code>Python</code></div>

<!-- <br>

## Background Context -->


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/tutorial/errors.html">Errors and Exceptions</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=7vbgD-3s-w4">Learn to Program 11 Static & Exception Handling</a> (starting at minute 7)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<!-- <br>

**man or help:**
- `` -->

<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>Why Python programming is awesome</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What’s the difference between errors and exceptions</b></summary><br>

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

**To sum up, errors are issues detected during the program's compilation phase that prevent it from running, while exceptions are issues that occur during runtime and can be caught and managed using exception handling mechanisms.**

<br>
<br>
<p align="center">***********</p>

> **What's the difference between Compilation time and Runtime:**<br>
   ***Compilation Time***: *This is the phase where the source code is translated into machine-readable code and checked for syntax errors. It is a preparatory step before the program can be executed.*<br>
   ***Runtime***: *This is the phase where the compiled code is actually executed by the computer's processor. It involves processing data, performing calculations, and carrying out the tasks defined by the program.*

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are exceptions and how to use them</b></summary><br>

Exceptions in Python are a way of handling and managing runtime errors or exceptional conditions that can arise during the execution of a program. Instead of letting the program crash when an error occurs, you can use exception handling to gracefully handle these errors and continue the program's execution. This prevents abrupt termination and allows you to provide meaningful feedback to users or take specific actions to recover from the error.

In Python, exceptions are represented by classes, and each type of exception corresponds to a specific class. For example, the built-in `ZeroDivisionError` class represents an exception that occurs when you attempt to divide by zero. When an exception is raised, Python generates an exception object containing information about the error, such as its type and a description.

The basic structure for handling exceptions in Python is the `try` and `except` block:

```python
try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero.")
```

In this example, the code inside the `try` block attempts to divide `10` by `0`, which raises a `ZeroDivisionError` exception. The program then jumps to the corresponding `except` block, where you can provide instructions on how to handle the exception. In this case, the message "Cannot divide by zero." will be printed.

You can also catch multiple types of exceptions by using multiple `except` blocks or a single `except` block with multiple exception types:

```python
try:
    # Code that might raise exceptions
    value = int("not_an_integer")  # This will raise a ValueError
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid integer value.")
```

If you want to catch all exceptions (not recommended in most cases), you can use a more general `except` block without specifying the exception type:

```python
try:
    # Code that might raise exceptions
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An exception occurred.")
```

In addition to `try` and `except`, you can use other clauses with exception handling:

- `else`: Code in the `else` block is executed if no exceptions are raised in the `try` block.
- `finally`: Code in the `finally` block is always executed, regardless of whether an exception was raised. It's often used for cleanup tasks like closing files or releasing resources.

```python
try:
    # Code that might raise an exception
    value = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", value)
finally:
    print("Done.")
```

By using exception handling, you can make your Python programs more robust and user-friendly by gracefully handling errors and ensuring that your program can recover from unexpected situations.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>When do we need to use exceptions</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to correctly handle an exception</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What’s the purpose of catching exceptions</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to raise a builtin exception</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>When do we need to implement a clean-up action after an exception</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
<!-- Add your requirements here -->

<!-- <br>

## More Info -->

<br>

## Tasks
<details>
<summary>

### 0. 
`mandatory`

File: []()
</summary>


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

<details>
<summary>

### 10. 
`#advanced`

File: []()
</summary>


</details>

