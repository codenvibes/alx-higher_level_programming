<h1 align="center"><b>0x01. PYTHON - IF/ELSE, LOOPS, FUNCTIONS</b></h1>
<div align="center"><code>Python</code></div>

<!-- <br>

## Background Context -->


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->
<br><div align="center"><img src="https://github.com/codenvibes/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/images/code.png"></div>

<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/tutorial/controlflow.html">More Control Flow Tools</a> (Read until “4.6. Defining Functions” included)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=1QXOd2ZQs-Q">IndentationError</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3">How To Use String Formatters in Python 3</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt">Learn to Program</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt">Learn to Program 2 : Looping</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://pypi.org/project/pycodestyle/">Pycodestyle – Style Guide for Python Code</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

**man or help:**
- `python3`

<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>Why Python programming is awesome</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Why indentation is so important in Python</b></summary><br>

Indentation is crucial in Python because it is used to define the structure of the code, particularly for control flow and defining blocks of code. In Python, indentation (typically using spaces or tabs) is used to denote the beginning and end of code blocks such as loops, conditional statements, function definitions, and classes. The indentation level indicates which lines of code are part of these blocks.

For example, in Python, a typical if-else statement might look like this:

```python
if condition:
    # Code block 1
    statement1
    statement2
else:
    # Code block 2
    statement3
    statement4
```

In this example, the lines of code indented under the `if` and `else` statements are part of the respective code blocks. The indentation makes the code visually clear and helps Python understand the structure of the program.

The use of indentation in Python also eliminates the need for explicit block-delimiting characters (like curly braces in C/C++ or Java), which can lead to more readable and consistent code. However, it's important to be consistent with the choice of indentation (spaces or tabs) throughout the codebase to avoid confusion and potential errors.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>if</code>, <code>if ... else</code> statements</b></summary><br>

In Python, you can use `if`, `if...else`, and `if...elif...else` statements for conditional execution of code. Here's a brief overview of how each of these works:

1. **`if` statement**:

The `if` statement is used to execute a block of code only if a specified condition is true. If the condition is false, the block of code is skipped.

```python
if condition:
    # Execute this block if the condition is True
    statement1
    statement2
# Code continues here outside the if block
```

2. **`if...else` statement**:

The `if...else` statement is used to execute one block of code if a condition is true, and another block if the condition is false.

```python
if condition:
    # Execute this block if the condition is True
    statement1
    statement2
else:
    # Execute this block if the condition is False
    statement3
    statement4
# Code continues here outside the if...else block
```

3. **`if...elif...else` statement**:

The `if...elif...else` statement is used when you have multiple conditions to check. It allows you to check multiple conditions and execute a block of code as soon as one of the conditions is true.

```python
if condition1:
    # Execute this block if condition1 is True
    statement1
    statement2
elif condition2:
    # Execute this block if condition1 is False and condition2 is True
    statement3
    statement4
else:
    # Execute this block if both condition1 and condition2 are False
    statement5
    statement6
# Code continues here outside the if...elif...else block
```

In all of these statements, `condition` is an expression that evaluates to either `True` or `False`. If the condition is `True`, the indented block of code following the `if` statement is executed. If the condition is `False`, the block of code is skipped (unless there is an `else` block or subsequent `elif` condition that is `True`).

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use comments</b></summary><br>

In Python, you can use comments to annotate your code. Comments are ignored by the Python interpreter and are there to provide explanations or notes to make your code more understandable to other developers (or yourself in the future). There are two main ways to write comments in Python:

1. **Single-line comments**: Use the `#` character to indicate that the rest of the line is a comment.

```python
# This is a single-line comment
print("Hello, World!")  # This comment is at the end of a line of code
```

2. **Multi-line comments**: Although Python doesn't have a built-in syntax for multi-line comments, you can achieve a similar effect by using triple quotes (`'''` or `"""`) as a string delimiter. When used as the first thing in a file, function, or class definition, they are often considered as docstrings (documentation strings).

```python
'''
This is a multi-line comment.
It spans multiple lines and is enclosed in triple quotes.
'''
print("Hello, World!")
```

It's worth noting that while triple-quoted strings are often used for multi-line comments, they are actually string literals in Python. However, when they're not assigned to a variable or used as a docstring, Python treats them as comments because they're not being used for any purpose in the code.

For code readability, it's important to use comments judiciously. They should be used to explain why the code is written a certain way or to provide context that is not immediately obvious from the code itself. Over-commenting can make the code harder to read, so it's best to use comments sparingly and focus on writing clear and understandable code.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to affect values to variables</b></summary><br>

In Python, you can assign values to variables using the assignment operator `=`. Here are some examples of how to do this:

1. **Simple assignment**:

   ```python
   x = 5
   ```

   In this example, the value `5` is assigned to the variable `x`. After this assignment, whenever you use `x` in your code, it will represent the value `5`.

2. **Multiple assignments**:

   ```python
   a, b = 10, 20
   ```

   This is a way to assign multiple values to multiple variables in a single line. In this case, `a` is assigned the value `10` and `b` is assigned the value `20`.

3. **Assignment with arithmetic operations**:

   ```python
   y = 3
   y += 2  # equivalent to y = y + 2
   ```

   This is a way to update the value of a variable using an arithmetic operation. In this case, `y` is initially assigned the value `3`, and then `2` is added to its current value using the `+=` operator.

4. **Assignment with other operators**:

   ```python
   z = 7
   z *= 3  # equivalent to z = z * 3
   ```

   This is another example of updating the value of a variable using a different operator (`*=` in this case).

5. **Assignment with expressions**:

   ```python
   a = 5
   b = a * 2 + 3
   ```

   In this example, the value of `a` is used in an expression to calculate the value of `b`, which is then assigned to `b`.

6. **Assignment with function calls**:

   ```python
   def my_function():
       return 42

   result = my_function()
   ```

   Here, the result of calling the `my_function` function is assigned to the variable `result`.

These are just a few examples of how you can assign values to variables in Python. The assignment operator `=` is used to assign a value to a variable, and you can use various expressions and operations on the right-hand side of the assignment to calculate the value to be assigned.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>while</code> and for <code>loops</code></b></summary><br>

In Python, you can use `while` and `for` loops for iteration. Here's how they work:

1. **`while` loop**:

The `while` loop is used to repeatedly execute a block of code as long as a specified condition is true.

```python
while condition:
    # Execute this block as long as the condition is True
    statement1
    statement2
    # Update the condition to eventually make it False
    # (or the loop will run indefinitely)
    update_condition
# Code continues here outside the while loop
```

In a `while` loop, `condition` is an expression that is checked before each iteration. If the condition is `True`, the block of code inside the loop is executed. After the block is executed, the condition is checked again. If it is still `True`, the block is executed again, and so on. The loop continues until the condition becomes `False`.

2. **`for` loop**:

The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object in Python.

```python
for item in iterable:
    # Execute this block for each item in the iterable
    statement1
    statement2
# Code continues here outside the for loop
```

In a `for` loop, `iterable` is an object that can be iterated over (e.g., a list, tuple, string, or range object). In each iteration, the loop variable `item` takes on the value of the next item in the iterable, and the block of code inside the loop is executed with `item` set to that value.

For example:
```python
# Example of a for loop
for i in range(5):
    print(i)
```
This loop will print the numbers 0, 1, 2, 3, and 4, because `range(5)` generates a sequence of numbers from 0 to 4 (inclusive).

In summary, `while` loops are used when you want to repeat a block of code based on a condition, and `for` loops are used when you want to iterate over a sequence or any iterable object.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How is Python’s <code>for</code> different from <code>C</code>‘s?</b></summary><br>

Python's `for` loop and C's `for` loop have similarities in their basic functionality but differ in their syntax and some advanced features.

1. **Basic Syntax**:
   - In Python, the `for` loop iterates over items in a sequence (e.g., a list, tuple, string, or any iterable object). The loop variable takes on the value of each item in the sequence.
   - In C, the `for` loop typically uses a counter variable that is initialized, tested against a condition, and updated in each iteration. The loop continues until the condition is false.

2. **Iterable vs. Counter-Based**:
   - Python's `for` loop is primarily used for iteration over iterable objects. It doesn't require an explicit counter variable or index to iterate over a sequence.
   - C's `for` loop is often used with a counter variable that is explicitly incremented or decremented in each iteration. It is typically used for iterating a specific number of times.

3. **Range-Based Iteration**:
   - In Python, the `range()` function is often used with `for` loops to generate a sequence of numbers. This is a common pattern for iterating a specific number of times.
   - C's `for` loop commonly uses a counter variable initialized with a value, tested against a condition, and updated in each iteration. This is the classic use case for a `for` loop in C.

4. **Loop Control Statements**:
   - Both Python and C support loop control statements like `break` and `continue` to modify the flow of the loop.
   - Python's `for` loop also supports an `else` block, which is executed when the loop completes normally (i.e., without encountering a `break` statement). C does not have this feature in its `for` loop.

Here's an example to illustrate the differences:

Python:
```python
# Python for loop iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

C:
```c
// C for loop using a counter variable
int i;
for (i = 0; i < 3; i++) {
    printf("%d\n", i);
}
```

In this example, the Python `for` loop iterates over each item in the `fruits` list, while the C `for` loop uses a counter variable `i` to iterate from 0 to 2.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>break</code> and <code>continue</code> statements</b></summary><br>

In Python, the `break` and `continue` statements are used within loops (such as `for` or `while` loops) to control the flow of the loop.

1. **`break` statement**:

The `break` statement is used to exit the loop prematurely. When Python encounters a `break` statement inside a loop, it immediately exits the loop and continues with the next statement outside the loop.

Example:
```python
for i in range(5):
    if i == 3:
        break  # Exit the loop when i equals 3
    print(i)
# Output: 0, 1, 2
```

2. **`continue` statement**:

The `continue` statement is used to skip the current iteration of the loop and continue with the next iteration. When Python encounters a `continue` statement inside a loop, it skips the remaining code in the current iteration and moves on to the next iteration.

Example:
```python
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop body for i equals 2
    print(i)
# Output: 0, 1, 3, 4
```

In both examples, we used a `for` loop, but `break` and `continue` can also be used with `while` loops. These statements are particularly useful for controlling the flow of loops based on certain conditions.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use <code>else</code> clauses on loops</b></summary><br>

In Python, you can use the `else` clause in conjunction with loops (such as `for` and `while` loops) to execute a block of code when the loop completes normally (i.e., without encountering a `break` statement). Here's how you can use the `else` clause with loops:

1. **`for` loop with `else` clause**:

   In a `for` loop, the `else` block is executed after the loop completes its iterations, unless the loop is terminated by a `break` statement.

   ```python
   for item in iterable:
       # Loop body
       if condition:
           # Do something and break out of the loop
           break
   else:
       # Executed if the loop completes without encountering a break
       # This block will not run if the loop is terminated by a break
       statement
   ```

2. **`while` loop with `else` clause**:

   In a `while` loop, the `else` block is also executed after the loop completes its iterations, unless the loop is terminated by a `break` statement.

   ```python
   while condition:
       # Loop body
       if condition:
           # Do something and break out of the loop
           break
   else:
       # Executed if the loop completes without encountering a break
       # This block will not run if the loop is terminated by a break
       statement
   ```

In both cases, the `else` block is optional and can be used to handle the case when the loop completes without any early termination. If the loop is terminated by a `break` statement, the `else` block will not be executed.

The `else` clause with loops can be useful for scenarios where you want to execute some code after the loop has finished its iterations, but only if the loop completes normally without any interruptions.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What does the <code>pass</code> statement do, and when to use it</b></summary><br>

In Python, the `pass` statement is a null operation. It does nothing when it is executed. It is used as a placeholder where syntactically a statement is required, but no action is needed or desired. Essentially, it is a no-op that serves as a kind of "do nothing" placeholder.

You might use `pass` in situations like:

1. **Placeholder in a Code Structure**: When you're designing a new class, function, or conditional block and you want to define the structure but leave the implementation for later, you can use `pass` to avoid syntax errors.

   ```python
   def my_function():
       # TODO: Implement this function later
       pass
   ```

2. **Empty Loop Body**: In some cases, you might have a loop where the body is intentionally empty, but you need to include it for the loop structure. `pass` can be used to indicate that the loop does nothing.

   ```python
   while condition:
       # No action needed here for now
       pass
   ```

3. **Placeholder in Conditional Statements**: Similar to how it's used in functions, you might use `pass` in conditional statements where you want to acknowledge a condition but don't need to take any action based on it at the moment.

   ```python
   if condition:
       # TODO: Handle this condition later
       pass
   ```

In general, `pass` is a way to handle situations where you need a placeholder in your code structure but don't want to do anything at that point. It's a way to acknowledge that something needs to be done there in the future without causing any errors in the current code.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use <code>range</code></b></summary><br>

In Python, the `range()` function is used to generate a sequence of numbers. It's commonly used in loops to iterate a specific number of times. Here's how you can use the `range()` function:

1. **Using `range()` with one argument:**

   When you provide one argument to `range(n)`, it generates a sequence of numbers from `0` to `n-1`. The syntax is:

   ```python
   for i in range(5):
       print(i)
   ```

   This will output:

   ```
   0
   1
   2
   3
   4
   ```

2. **Using `range()` with two arguments:**

   When you provide two arguments to `range(start, stop)`, it generates a sequence of numbers from `start` to `stop-1`. The syntax is:

   ```python
   for i in range(2, 5):
       print(i)
   ```

   This will output:

   ```
   2
   3
   4
   ```

3. **Using `range()` with three arguments:**

   When you provide three arguments to `range(start, stop, step)`, it generates a sequence of numbers from `start` to `stop-1`, incrementing by `step`. The syntax is:

   ```python
   for i in range(1, 10, 2):
       print(i)
   ```

   This will output:

   ```
   1
   3
   5
   7
   9
   ```

4. **Using `range()` to create a list:**

   You can also use `range()` to create a list of numbers by wrapping it in the `list()` function:

   ```python
   numbers = list(range(5))
   print(numbers)  # Output: [0, 1, 2, 3, 4]
   ```

   This creates a list containing the numbers `0` to `4`.

Remember that in Python 3, `range()` returns a range object which is a generator-like object. If you need a list, you can convert it to a list using the `list()` function as shown in the last example.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a function and how do you use functions</b></summary><br>

In programming, a function is a named block of code that performs a specific task or a set of tasks. Functions are used to organize code into manageable pieces, promote code reuse, and make the code more readable and maintainable.

In Python, you can define a function using the `def` keyword followed by the function name and its parameters (if any). The basic syntax for defining a function in Python is as follows:

```python
def function_name(parameter1, parameter2, ...):
    # Function body
    # Perform some tasks using parameters
    # Optionally return a value using the return statement
```

Here's a breakdown of the parts of a function definition:

- `def`: This keyword is used to define a function.
- `function_name`: This is the name of the function. You can choose any valid identifier as the function name.
- `(parameter1, parameter2, ...)`: These are the parameters (or arguments) that the function takes. They are optional, and you can have zero or more parameters.
- `:`: The colon is used to indicate the beginning of the function body.
- Indented block: This is the body of the function where you write the code that the function will execute. It can contain any valid Python code.
- `return`: This keyword is used to return a value from the function. It's optional, and if omitted, the function returns `None` by default.

Here's an example of a simple function in Python that takes two parameters and returns their sum:

```python
def add_numbers(a, b):
    # Function body
    result = a + b
    return result
```

Once you have defined a function, you can call it by using its name followed by parentheses `()` containing the arguments you want to pass to the function (if any). Here's how you can call the `add_numbers` function from the previous example:

```python
# Call the function and pass arguments
sum_result = add_numbers(5, 3)
print(sum_result)  # Output: 8
```

In this example, `add_numbers(5, 3)` is the function call, and `5` and `3` are the arguments passed to the function. The function returns `8`, which is then printed to the console.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What does return a function that does not use any <code>return</code> statement</b></summary><br>

In Python, if a function does not have a `return` statement, it implicitly returns `None` when the function completes. This means that even if you don't explicitly use a `return` statement in your function, Python will still return a value (`None`) by default. Here's an example to illustrate this:

```python
def my_function():
    print("This function doesn't have a return statement")

result = my_function()
print(result)  # Output: None
```

In this example, `my_function` does not have a `return` statement, so when you call `my_function()`, it prints the message but doesn't explicitly return anything. When you assign the result of `my_function()` to `result`, `result` will contain `None`, indicating that the function did not return a value.

It's important to note that while Python allows functions to have no `return` statement, it's often clearer to include a `return` statement to explicitly indicate the intended return value, even if that value is `None`. This can make the code more readable and help prevent unexpected behavior.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Scope of variables</b></summary><br>

In Python, the scope of a variable refers to the region of the code where the variable is accessible. Python has the following scopes:

1. **Local scope**: Variables defined within a function have local scope. They are accessible only within the function in which they are defined.

```python
def my_function():
    x = 10  # local variable
    print(x)  # accessible here

my_function()
print(x)  # NameError: name 'x' is not defined
```

2. **Enclosing (nonlocal) scope**: If a function is defined inside another function, the inner function has access to variables in the outer (enclosing) function's scope. This is known as the enclosing or nonlocal scope.

```python
def outer_function():
    x = 10  # outer function scope

    def inner_function():
        print(x)  # accessible here

    inner_function()

outer_function()
print(x)  # NameError: name 'x' is not defined
```

3. **Global scope**: Variables defined outside of any function or in the global scope are accessible throughout the entire module.

```python
x = 10  # global variable

def my_function():
    print(x)  # accessible here

my_function()
print(x)  # accessible here
```

4. **Built-in scope**: Python also has a built-in scope that contains names like `print`, `sum`, `len`, etc., which are built-in functions and variables.

When you try to access a variable, Python looks for it in the current scope. If it's not found, it looks in the enclosing scopes, and so on, until it reaches the global scope. If the variable is not found in any of these scopes, a `NameError` is raised.

It's important to understand variable scope in Python because it affects how you can use and modify variables in different parts of your code. Understanding scope helps you write more maintainable and bug-free code.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What’s a traceback</b></summary><br>

In Python, a traceback is a report that displays the function calls made in a program at a specific point in time when an exception occurs. It provides information about the sequence of function calls that led to the point where the exception was raised.

When an exception occurs in Python and is not caught by a try-except block, the interpreter prints a traceback to the console. The traceback includes:

1. The file name and line number where the exception occurred.
2. The sequence of function calls that led to the exception, starting from the innermost function and moving outward.
3. For each function call in the traceback, the file name, line number, and function name are typically displayed.

Here's an example of a simple traceback:

```python
Traceback (most recent call last):
  File "example.py", line 3, in <module>
    result = divide(10, 0)
  File "example.py", line 2, in divide
    return x / y
ZeroDivisionError: division by zero
```

In this example, the traceback shows that the `ZeroDivisionError` occurred in the file `example.py` at line 2, inside the `divide` function, which was called from line 3 of `example.py`. The traceback helps developers identify the cause of the exception by showing the sequence of function calls that led to the error. This information can be valuable for debugging and fixing issues in Python programs.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the arithmetic operators and how to use them</b></summary><br>

In Python, arithmetic operators are used to perform mathematical operations on numeric values. Here are the basic arithmetic operators in Python:

1. **Addition (+)**: Adds two operands.
   ```python
   result = 10 + 5  # result is 15
   ```

2. **Subtraction (-)**: Subtracts the right operand from the left operand.
   ```python
   result = 10 - 5  # result is 5
   ```

3. **Multiplication (*)**: Multiplies two operands.
   ```python
   result = 10 * 5  # result is 50
   ```

4. **Division (/)**: Divides the left operand by the right operand (always results in a float).
   ```python
   result = 10 / 5  # result is 2.0
   ```

5. **Floor Division (//)**: Divides the left operand by the right operand and returns the integer part of the result (discards the fractional part).
   ```python
   result = 10 // 3  # result is 3
   ```

6. **Modulus (%)**: Returns the remainder of the division of the left operand by the right operand.
   ```python
   result = 10 % 3  # result is 1
   ```

7. **Exponentiation (**)**: Raises the left operand to the power of the right operand.
   ```python
   result = 2 ** 3  # result is 8
   ```

These operators can be used with variables, constants, or literal values to perform arithmetic operations and store the result in a variable or use it directly in an expression.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
<details>
<summary><b><a href=" "> </a>Python Scripts</b></summary><br>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>C Scripts</b></summary><br>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/alx-tools/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl)
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<br>

## More Info
***Note***: you do not need to understand lists yet.

<br>

## Quiz questions
<details>
<summary><b>Question 0</b></summary><br>

What do these lines print?
```py
a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun")
else:
    print("School")
```
- [ ] School
- [x] C is fun
- [ ] Holberton

<br>
</details>

<details>
<summary><b>Question 1</b></summary><br>

What do these lines print?
```py
if 12 == 48/4 and False:
    print("Holberton")
else:
    print("School")
```
- [x] School
- [ ] Holberton

<br>
</details>

<details>
<summary><b>Question 2</b></summary><br>

What do these lines print?
```py
if 12 == 48/4:
    print("Holberton")
else:
    print("School")
```
- [ ] School
- [x] Holberton

<br>
</details>

<details>
<summary><b>Question 3</b></summary><br>

What do these lines print?
```py
if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
    print("School")
```
- [ ] School
- [x] Holberton

<br>
</details>

<details>
<summary><b>Question 4</b></summary><br>

What do these lines print?
```py
for i in range(2, 10, 2):
    print(i, end=" ")
```
- [ ] 4 6 8 10 12 14 16 18
- [x] 2 4 6 8
- [ ] 2 3 4 5 6 7 8 9
- [ ] 2 3 4 5 6 7 8 9 10

<br>
</details>

<details>
<summary><b>Question 5</b></summary><br>

What do these lines print?
```py
for i in range(4):
    print(i, end=" ")
```
- [x] 0 1 2 3
- [ ] 0 1 2 3 4
- [ ] 1 2 3
- [ ] 1 2 3 4

<br>
</details>

<details>
<summary><b>Question 6</b></summary><br>

What do these lines print?
```py
for i in range(2, 4):
    print(i, end=" ")
```
- [ ] 2 3 4
- [ ] 3 4
- [x] 2 3
- [ ] 2 4

<br>
</details>

<details>
<summary><b>Question 7</b></summary><br>

What do these lines print?
```py
a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton")
    else:
        print("C is fun")
else:
    print("School")
```
- [ ] School
- [ ] C is fun
- [x] Holberton

<br>
</details>

<details>
<summary><b>Question 8</b></summary><br>


What do these lines print?
```py
if True:
    print("Holberton")
else:
    print("School")
```
- [ ] School
- [x] Holberton

<br>
</details>

<br>

## Tasks
<details>
<summary>

### 0. Positive anything is better than negative nothing
`mandatory`

File: [0-positive_or_negative.py]()
</summary>

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

-You can find the source code [here](https://alx-intranet.hbtn.io/rltoken/rkvoXPA-lS3TAaemM9sChg "here")
-The variable `number` will store a different value every time you will run this program
-You don't have to understand what `import`, `random. randint` do. Please do not touch this code
-The output of the program should be:
-The number, followed by
-if the number is greater than 0: `is positive`
-if the number is 0: `is zero`
-if the number is less than 0: `is negative`
-followed by a new line

```bash
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py
5 is positive
guillaume@ubuntu:~/0x01$

```
</details>

<details>
<summary>

### 1. The last digit
`mandatory`

File: [1-last_digit.py]()
</summary>

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

-   You can find the source code [here](https://alx-intranet.hbtn.io/rltoken/hU682hcMxVchqWAcmh32tA "here")
-   The variable `number` will store a different value every time you will run this program
-   You don't have to understand what `import`, `random.randint` do. **Please do not touch this code**. This line should not change: `number = random.randint(-10000, 10000)`
-   The output of the program should be:
    -   The string `Last digit of`, followed by
    -   the number, followed by
    -   the string `is`, followed by the last digit of `number`, followed by
        -   if the last digit is greater than 5: the string `and is greater than 5`
        -   if the last digit is 0: the string `and is 0`
        -   if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
    -   followed by a new line

```bash
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$

```
</details>

<details>
<summary>

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
`mandatory`

File: [2-print_alphabet.py]()
</summary>

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

-   You can only use one `print` function with string format
-   You can only use one loop in your code
-   You are not allowed to store characters in a variable
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$

```
</details>

<details>
<summary>

### 3. When I was having that alphabet soup, I never thought that it would pay off
`mandatory`

File: [3-print_alphabt.py]()
</summary>

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

-   Print all the letters except `q` and `e`
-   You can only use one `print` function with string format
-   You can only use one loop in your code
-   You are not allowed to store characters in a variable
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$

```
</details>

<details>
<summary>

### 4. Hexadecimal printing
`mandatory`

File: [4-print_hexa.py]()
</summary>

Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)

-   You can only use one `print` function with string format
-   You can only use one loop in your code
-   You are not allowed to store numbers or strings in a variable
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$

```
</details>

<details>
<summary>

### 5. 00...99
`mandatory`

File: [5-print_comb2.py]()
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
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 8. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 9. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 10. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 11. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 12. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 13. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 14. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 15. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 16. 
`#advanced`

File: []()
</summary>


</details>

