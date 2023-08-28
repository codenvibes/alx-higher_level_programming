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

> **What's the difference between Compilation time and Runtime:**<br>
   ***Compilation Time***: *This is the phase where the source code is translated into machine-readable code and checked for syntax errors. It is a preparatory step before the program can be executed.*<br>
   ***Runtime***: *This is the phase where the compiled code is actually executed by the computer's processor. It involves processing data, performing calculations, and carrying out the tasks defined by the program.*
</details>

<details>
<summary><h3>What are exceptions and how to use them</h3></summary>

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
</details>

<details>
<summary><h3>When do we need to use exceptions</h3></summary>

You should use exceptions in Python whenever you want to handle runtime errors or exceptional situations in a controlled and graceful manner. Exceptions are particularly useful when you want to prevent your program from crashing due to unexpected errors and provide meaningful feedback to users or take specific actions to recover from the errors.

Here are some scenarios where you might want to use exceptions along with code examples:

1. **Input Validation:**
   When you're accepting user input, it's a good practice to validate the input and handle invalid cases using exceptions. For example, when converting user input to an integer:

   ```python
   try:
       user_input = input("Enter an integer: ")
       value = int(user_input)
   except ValueError:
       print("Invalid input. Please enter a valid integer.")
   ```

2. **File Operations:**
   When working with files, exceptions can help you handle cases where the file doesn't exist or there are issues during reading/writing:

   ```python
   try:
       with open("myfile.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found.")
   except IOError:
       print("An error occurred while reading the file.")
   ```

3. **Networking:**
   When dealing with network-related operations, like making HTTP requests, exceptions can handle connectivity issues:

   ```python
   import requests

   try:
       response = requests.get("https://example.com")
       response.raise_for_status()  # Raises an exception for HTTP errors
   except requests.exceptions.RequestException:
       print("Error occurred while making the request.")
   ```

4. **Arithmetic Operations:**
   Handle cases where mathematical operations might result in exceptions, like division by zero:

   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero.")
   ```

5. **Custom Exceptions:**
   You can create your own custom exceptions to handle specific situations in your code:

   ```python
   class CustomError(Exception):
       pass

   try:
       if some_condition:
           raise CustomError("Custom error message")
   except CustomError as ce:
       print("Caught custom error:", ce)
   ```

6. **Resource Management:**
   When working with external resources (like databases or external services), exceptions can ensure proper resource cleanup:

   ```python
   try:
       db_connection = connect_to_database()
       # Code that uses the database connection
   except DatabaseError:
       print("An error occurred while accessing the database.")
   finally:
       db_connection.close()  # Ensures the connection is closed even if an error occurs
   ```

In general, use exceptions when you expect that certain operations might fail due to unforeseen circumstances, and you want to handle these situations without causing your program to crash. It's important to provide informative error messages to users and to log detailed error information for debugging purposes.
</details>

<details>
<summary><h3>How to correctly handle an exception</h3></summary>

Handling exceptions in Python involves using `try` and `except` blocks to manage potential errors in your code. Here's a step-by-step guide on how to correctly handle an exception:

1. **Identify the Risky Code:**
   Determine which part of your code might raise an exception. This is the code you'll place inside the `try` block.

2. **Wrap the Risky Code in a `try` Block:**
   Enclose the potentially problematic code within a `try` block. If an exception occurs within this block, the program will jump to the corresponding `except` block.

3. **Specify the Exception Type:**
   After the `try` block, add one or more `except` blocks. Each `except` block should specify the type of exception it can handle. You can catch multiple exception types by using multiple `except` blocks or a single `except` block with multiple exception types.

4. **Handle the Exception:**
   Inside the `except` block, write code to handle the exception. This could involve displaying an error message, logging the issue, attempting an alternative action, or any other appropriate response.

5. **Optionally Include an `else` Block:**
   If you have code that should run only if no exception occurs, place it inside an `else` block after all the `except` blocks.

6. **Optionally Include a `finally` Block:**
   If you have code that should always run, regardless of whether an exception occurred or not, place it inside a `finally` block.

Here's an example demonstrating the correct handling of an exception:

```python
try:
    dividend = int(input("Enter a number to divide: "))
    divisor = int(input("Enter a divisor: "))
    result = dividend / divisor
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Result:", result)
finally:
    print("Division operation completed.")
```

In this example:
- The `try` block contains code that may raise exceptions (division by zero or invalid input).
- There are two `except` blocks to handle the `ZeroDivisionError` and `ValueError` exceptions separately.
- The `else` block prints the result if no exception occurs.
- The `finally` block ensures that the final message is displayed, regardless of exceptions.

When handling exceptions, it's important to provide meaningful error messages and take appropriate actions to prevent program crashes and to guide users through troubleshooting.
</details>

<details>
<summary><h3>What’s the purpose of catching exceptions</h3></summary>

Catching exceptions serves several important purposes in programming:

1. **Error Handling and Recovery:** Catching exceptions allows you to handle unexpected errors or exceptional conditions gracefully without crashing the entire program. Instead of letting an error propagate and disrupt the program's execution, you can provide alternative behavior or take corrective actions to recover from the error. This is crucial for maintaining the stability and reliability of your application.

2. **User-Friendly Feedback:** When exceptions occur, users are often presented with cryptic error messages that they may not understand. By catching exceptions and providing meaningful error messages or instructions, you can improve the user experience and help users understand what went wrong and how to proceed.

3. **Program Robustness:** Exception handling helps make your program more robust by allowing it to handle unexpected situations and errors that might occur during runtime. This prevents your program from abruptly crashing and helps it continue functioning in the presence of errors.

4. **Logging and Debugging:** When you catch and handle exceptions, you can log information about the exception, including its type, message, and potentially the stack trace. This information is valuable for diagnosing and debugging issues in your application, as it provides insight into what caused the error and where it occurred.

5. **Resource Cleanup:** Exception handling can be used to ensure that resources, such as files, network connections, or database connections, are properly closed or released, even if an error occurs. The `finally` block is often used for this purpose to guarantee cleanup operations.

6. **Control Flow:** By catching exceptions, you can control the flow of your program in response to different conditions. For instance, you might want to retry an operation if it fails due to a temporary network issue or proceed with an alternative strategy if a specific exception occurs.

7. **Security:** Handling exceptions can help protect sensitive information from leaking in error messages. By catching and handling exceptions appropriately, you can prevent exposing details that could potentially be exploited by malicious users.

8. **Third-Party Libraries:** When using third-party libraries, you might encounter exceptions specific to those libraries. Catching these exceptions allows you to handle library-specific issues and continue your application's execution without being disrupted by external errors.

Overall, catching exceptions enables you to write more reliable and user-friendly software by managing errors, maintaining control over the program's execution, and enhancing the overall user experience.
</details>

<details>
<summary><h3>How to raise a builtin exception</h3></summary>

In Python, you can create custom exceptions by defining new classes that inherit from built-in exception classes. This allows you to extend and customize the behavior of exception handling in your code. To raise a built-in exception from a custom exception class, you need to create a class that inherits from the desired built-in exception class and then raise an instance of your custom exception class. Here's how you can do it:

Let's say you want to create a custom exception named `CustomError` that inherits from the built-in `ValueError` exception. Here's how you can achieve that:

```python
class CustomError(ValueError):
    pass

def some_function(value):
    if value < 0:
        raise CustomError("Value must be non-negative")

try:
    some_function(-5)
except CustomError as e:
    print("Custom error:", e)
except ValueError as e:
    print("ValueError:", e)
```

<br>
<br>
<p align="center">*******************************</p>
<br>

```python
class CustomError(ValueError):
    pass
```

Here, a new custom exception class named `CustomError` is defined. This class inherits from the built-in `ValueError` class. By inheriting from `ValueError`, `CustomError` will have all the properties and behavior of a `ValueError` exception, and you can also customize it further if needed.

```python
def some_function(value):
    if value < 0:
        raise CustomError("Value must be non-negative")
```

A function named `some_function` is defined. This function takes a `value` as an argument. Inside the function, there's a condition that checks if the `value` is negative. If the condition is true (i.e., the value is negative), the function raises an instance of the `CustomError` exception with the error message "Value must be non-negative."

```python
try:
    some_function(-5)
except CustomError as e:
    print("Custom error:", e)
except ValueError as e:
    print("ValueError:", e)
```

This code is inside a `try` block, which means it's trying to execute the code within it. The `some_function(-5)` call inside the `try` block would raise a `CustomError` exception since the value `-5` is negative. In the `except` block, we catch the `CustomError` exception using `except CustomError as e:`. Here, `e` will be the instance of the raised `CustomError` exception. We print a message indicating that a custom error occurred and provide the details of the exception.

Since `CustomError` is a subclass of `ValueError`, you might expect that the `except ValueError as e:` block could also catch the exception. However, due to the way exception handling works, Python will prioritize catching the most specific exception type first, which is `CustomError`. If the `except CustomError` block was not present, then the `ValueError` block would catch the exception.

The output of this code, when executed, would be something like:
```
Custom error: Value must be non-negative
```

This example demonstrates how you can create and raise custom exceptions in Python by inheriting from built-in exception classes, allowing you to design more meaningful and context-specific error handling in your code.

When you catch exceptions using `except` blocks, it's important to catch the more specific exceptions first before catching more general ones. In this example, we catch `CustomError` before catching `ValueError`, since `CustomError` is a subclass of `ValueError`.

Remember that when creating custom exceptions, you can define additional attributes or methods in your custom exception class to provide more context or behavior specific to your application's needs.
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

