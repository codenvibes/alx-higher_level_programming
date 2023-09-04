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

<br>
<br>
<p align="center">*******************************</p>
<br>

In the code example provided earlier:

```python
class CustomError(ValueError):
    pass
```

The `pass` statement is used as a placeholder that does nothing. In Python, it's a way to indicate that you want to define a block of code (in this case, the body of the `CustomError` class) but you don't want to add any functionality or statements within that block at the moment. It's often used when syntactically a statement is required but you don't want to execute any code.

In the context of defining a custom exception class, the `pass` statement indicates that you're intentionally leaving the class definition empty for now, and you might later add more attributes, methods, or custom behavior to the class. It's a common approach when you're creating a placeholder for future development or when you're creating a subclass of an existing class and you want to inherit its behavior without adding anything new immediately.

For example, you might later add custom methods to your `CustomError` class:

```python
class CustomError(ValueError):
    def __init__(self, message):
        super().__init__(message)
    
    def log_error(self):
        print("An error occurred:", self.args[0])
```

In this updated example, the `CustomError` class now has a custom constructor (`__init__`) and a method called `log_error`. These additions can be made at a later stage while keeping the structure of the class defined earlier.
</details>

<details>
<summary><h3>When do we need to implement a clean-up action after an exception</h3></summary>

Implementing a clean-up action after an exception is necessary when your code has acquired resources or initiated processes that need to be properly handled and released, even if an exception occurs during their use. Clean-up actions are essential for maintaining the integrity of your program and preventing resource leaks or unintended side effects. Here are some scenarios where implementing a clean-up action after an exception is important:

1. **File Handling:**
   If your code opens files for reading or writing, it's crucial to ensure that the files are properly closed, regardless of whether an exception is raised or not. Failing to close files can lead to resource leaks and potential data corruption. Using a `finally` block for file closure guarantees that the file will be closed even if an exception occurs.

2. **Database Connections:**
   When connecting to databases or other external resources, you should ensure that connections are closed properly to release resources and prevent potential issues like connection leaks. Clean-up actions in the form of `finally` blocks can help close database connections, even if an exception disrupts the normal flow of your code.

3. **Network Connections:**
   Similar to database connections, network connections should be closed properly to avoid leaving sockets open indefinitely. Properly closing network connections can prevent issues such as running out of available sockets.

4. **Memory Allocation and Deallocation:**
   If your code involves manual memory management, as is the case in some low-level programming scenarios, you need to ensure that allocated memory is properly deallocated, even if an exception is raised.

5. **Resource Locking:**
   In multi-threaded or multi-process applications, clean-up actions can be used to release locks or other synchronization mechanisms, ensuring that resources are not left locked in case of exceptions.

6. **Temporary Files:**
   When creating temporary files, you should ensure that they are deleted after they're no longer needed. Clean-up actions can be used to delete temporary files, helping to avoid clutter and potential security risks.

7. **External Hardware:**
   If your code interacts with external hardware devices, such as sensors or actuators, clean-up actions may be needed to put the hardware in a safe state before exiting, even if an exception occurs.

8. **Transactions and State Management:**
   In applications that involve transactions or state changes, clean-up actions can be used to roll back changes made before the exception occurred, ensuring that the system is left in a consistent state.

In all of these scenarios, the `finally` block is a powerful tool to ensure that clean-up code is executed regardless of whether an exception is raised. The `finally` block is executed after the `try` block, regardless of whether an exception was raised or not, making it suitable for implementing clean-up actions.

```python
try:
    # Code that may raise an exception
    file = open("data.txt", "r")
    # ...
except SomeException:
    # Exception handling
finally:
    # Clean-up code
    file.close()  # Ensure the file is closed even if an exception occurred
```

By implementing appropriate clean-up actions, you can make your code more reliable, secure, and resilient in the face of unexpected exceptions.
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

### 0. Safe list printing
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

### 1. Safe printing of an integers list
`mandatory`

File: [1-safe_print_integer.py]()
</summary>

Write a function that prints an integer with `"{:d}".format()`.

-   Prototype: `def safe_print_integer(value):`
-   `value` can be any type (integer, string, etc.)
-   The integer should be printed followed by a new line
-   Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
-   Otherwise, returns `False`
-   You have to use `try: / except:`
-   You have to use `"{:d}".format()` to print as integer
-   You are not allowed to import any module
-   You are not allowed to use `type()`

```bash
guillaume@ubuntu:~/0x05$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/0x05$

```
</details>

<details>
<summary>

### 2. Print and count integers
`mandatory`

File: [2-safe_print_list_integers.py]()
</summary>

Write a function that prints the first `x` elements of a list and only integers.

-   Prototype: `def safe_print_list_integers(my_list=[], x=0):`
-   `my_list` can contain any type (integer, string, etc.)
-   All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
-   `x` represents the number of elements to access in `my_list`
-   `x` can be bigger than the length of `my_list` - if it's the case, an exception is expected to occur
-   Returns the real number of integers printed
-   You have to use `try: / except:`
-   You have to use `"{:d}".format()` to print an integer
-   You are not allowed to import any module
-   You are not allowed to use `len()`

```bash
guillaume@ubuntu:~/0x05$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers =\
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/0x05$

```
</details>

<details>
<summary>

### 3. Integers division with debug
`mandatory`

File: [3-safe_print_division.py]()
</summary>

Write a function that divides 2 integers and prints the result.

-   Prototype: `def safe_print_division(a, b):`
-   You can assume that `a` and `b` are integers
-   The result of the division should print on the `finally:` section preceded by `Inside result:`
-   Returns the value of the division, otherwise: `None`
-   You have to use `try: / except: / finally:`
-   You have to use `"{}".format()` to print the result
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x05$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$

```

</details>

<details>
<summary>

### 4. Divide a list
`mandatory`

File: [4-list_division.py]()
</summary>

Write a function that divides element by element 2 lists.

-   Prototype: `def list_division(my_list_1, my_list_2, list_length):`
-   `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
-   `list_length` can be bigger than the length of both lists
-   Returns a new list (length = `list_length`) with all divisions
-   If 2 elements can't be divided, the division result should be equal to `0`
-   If an element is not an integer or float:
    -   print: `wrong type`
-   If the division can't be done (`/0`):
    -   print: `division by 0`
-   If `my_list_1` or `my_list_2` is too short
    -   print: `out of range`
-   You have to use `try: / except: / finally:`
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x05$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

guillaume@ubuntu:~/0x05$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/0x05$

```
</details>

<details>
<summary>

### 5. Raise exception
`mandatory`

File: [5-raise_exception.py]()
</summary>

Write a function that raises a type exception.

-   Prototype: `def raise_exception():`
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

guillaume@ubuntu:~/0x05$ ./5-main.py
Exception raised
guillaume@ubuntu:~/0x05$

```
</details>

<details>
<summary>

### 6. Raise a message
`mandatory`

File: [6-raise_exception_msg.py]()
</summary>

Write a function that raises a name exception with a message.

-   Prototype: `def raise_exception_msg(message=""):`
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x05$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/0x05$ ./6-main.py
C is fun
guillaume@ubuntu:~/0x05$

```

</details>

<details>
<summary>

### 7. Safe integer print with error message
`#advanced`

File: [100-safe_print_integer_err.py]()
</summary>

Write a function that prints an integer.
- Prototype: `def safe_print_integer_err(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
- Otherwise, returns `False` and prints in `stderr` the error precede by `Exception:`
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print as integer
- You are not allowed to use `type()`
```bash
guillaume@ubuntu:~/0x05$ cat 100-main.py
#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

guillaume@ubuntu:~/0x05$ ./100-main.py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
School is not an integer
guillaume@ubuntu:~/0x05$ ./100-main.py 2> /dev/null
89
-89
School is not an integer
guillaume@ubuntu:~/0x05$ 
```
</details>

<details>
<summary>

### 8. Safe function
`#advanced`

File: [101-safe_function.py]()
</summary>

Write a function that executes a function safely.
- Prototype: `def safe_function(fct, *args):`
- You can assume `fct` will be always a pointer to a function
- Returns the result of the function,
- Otherwise, returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception:`
- You have to use `try: / except:`
```bash
guillaume@ubuntu:~/0x05$ cat 101-main.py
#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

guillaume@ubuntu:~/0x05$ ./101-main.py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
guillaume@ubuntu:~/0x05$ ./101-main.py 2> /dev/null
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None
guillaume@ubuntu:~/0x05$ 
```
</details>

<details>
<summary>

### 9. ByteCode -> Python #4
`#advanced`

File: [102-magic_calculation.py]()
</summary>

Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```bash
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
- Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)
</details>

<details>
<summary>

### 10. CPython #2: PyFloatObject
`#advanced`

File: [103-python.c]()
</summary>


</details>

