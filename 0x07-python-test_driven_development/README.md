<h1 align="center"><b>0x07. PYTHON - TEST-DRIVEN DEVELOPMENT</b></h1>
<div align="center"><code>Python</code> <code>UnitTests</code> <code>TDD</code></div>

<br>

## Concepts
<details>
<summary><b><a href="https://intranet.alxswe.com/concepts/47">Never forget a test</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br><img src="https://github.com/codenvibes/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/images/giphy-4.gif">


<br>

## Background Context
### Important notice on intranet checks for Python projects
Starting from today:
- Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. **But not in the implementation of them!**
- **Don’t trust the user**, always think about all possible edge cases


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3.4/library/doctest.html">doctest — Test interactive Python examples</a> <i>(until “26.2.3.7. Warnings” included)</i></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://pymotw.com/3/doctest/">doctest – Testing through documentation</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=1Lfv5tUGsn8">Unit Tests in Python</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=6tNS--WetLI">Unittest module</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/">Interactive and Non-interactive tests</a></b></summary><br>


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
<summary><b><a href=" "> </a>What’s an interactive test</b></summary><br>

An interactive test in Python typically refers to a way of running code interactively and receiving immediate feedback. This is often done using interactive development environments (IDEs), Python shells, or Jupyter notebooks. Interactive testing is a helpful approach for exploring and debugging code, as it allows you to execute small code snippets and see the results without having to write a complete program.

Here are a few common ways to perform interactive testing in Python:

1. **Python REPL (Read-Eval-Print Loop)**: <br> Python comes with a built-in REPL, which allows you to enter Python code line by line and see the output immediately. You can access the Python REPL by running the `python` or `python3` command in your terminal.

   ```python
   $ python
   Python 3.8.2 (default, Feb 24 2020, 17:52:18)
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> print("Hello, world!")
   Hello, world!
   >>> 5 + 3
   8
   >>> exit()
   ```

2. **Jupyter Notebooks**: <br> Jupyter notebooks provide an interactive and web-based environment for writing and running Python code. You can write and execute code in cells, view the output, and add rich text, images, and explanations in between.

3. **Integrated Development Environments (IDEs)**: <br> Many Python IDEs, such as PyCharm, Visual Studio Code, and Spyder, offer interactive modes where you can run code snippets and get immediate feedback. This is often helpful for debugging and exploring code.

4. **Online Python Interpreters**: <br> Various online platforms allow you to run Python code interactively in a web browser without installing any software locally. Examples include Repl.it and Google Colab.

Interactive testing is particularly useful when you want to experiment with new ideas, test functions or algorithms, and quickly check the behavior of specific code snippets without having to create a full-fledged Python script or program. It's an essential part of the development process for many Python developers.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Why tests are important</b></summary><br>

Tests are an integral part of the software development process and play a crucial role in ensuring the reliability, stability, and maintainability of software systems. Here are some key reasons why tests are important in software development:

1. **Bug Detection**: <br> Tests help identify bugs, errors, and issues in the codebase. By systematically testing various parts of the software, developers can catch and fix problems before they become more significant issues in production.

2. **Quality Assurance**: <br> Testing ensures that the software meets the specified requirements and functions correctly. It helps maintain a high level of quality by verifying that the software behaves as expected under various conditions.

3. **Regression Testing**: <br> As software evolves and new features are added, there is a risk of introducing new bugs or breaking existing functionality. Regression testing, which involves re-running tests to check for unintended side effects, helps prevent these issues.

4. **Code Maintenance**: <br> Well-written tests serve as documentation for how the code is supposed to work. They make it easier for developers to understand the codebase, make changes, and refactor without introducing new problems.

5. **Collaboration**: <br> Tests enable collaboration among team members. When one developer writes tests for a particular piece of functionality, other team members can rely on those tests to understand how the code works and build upon it.

6. **Continuous Integration/Continuous Deployment (CI/CD)**: <br> Tests are a critical component of CI/CD pipelines. Automated tests ensure that code changes do not break existing functionality before they are deployed to production, thereby reducing the risk of introducing defects.

7. **Improved Productivity**: <br> While writing tests may require an initial time investment, they can save time in the long run. Bugs caught early in development are often easier and less costly to fix than those discovered later in the development lifecycle.

8. **Confidence**: <br> Having a comprehensive test suite gives developers and stakeholders confidence that the software behaves as intended. This confidence is essential for making informed decisions about releasing the software to end-users.

9. **Documentation**: <br> Tests serve as executable documentation. They provide clear examples of how various parts of the codebase are intended to be used and can help new developers understand the system faster.

10. **User Satisfaction**: <br> Thorough testing leads to a more stable and reliable software product. Users are more satisfied when they experience fewer crashes, errors, and unexpected behavior.

11. **Security**: <br> Security vulnerabilities can have severe consequences. Tests can be used to identify security issues early and ensure that security measures are effective.

In summary, tests are essential for delivering high-quality software that meets user requirements, is maintainable, and can evolve over time. They provide a safety net for developers, reduce the risk of defects in production, and contribute to overall software reliability and robustness.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to write Docstrings to create tests</b></summary><br>

Docstrings are used to document Python code, providing information about a module, class, function, or method. While docstrings themselves are not used to create tests directly, they can be helpful in generating tests or ensuring that your code is testable. Here's how you can write docstrings to support testing in your Python code:

1. **Describe the Function or Method**: <br> Begin your docstring with a brief description of what the function or method does. This helps both developers and testing frameworks understand the purpose of the code.

   ```python
   def add(a, b):
       """
       Adds two numbers and returns the result.

       Parameters:
           a (int): The first number.
           b (int): The second number.

       Returns:
           int: The sum of a and b.
       """
       return a + b
   ```

2. **Document Parameters**: <br> Clearly document the function or method parameters, including their data types and any constraints or requirements. This information can help testers understand how to provide valid inputs.

3. **Document Return Values**: <br> Explain what the function or method returns and the data type of the return value. This helps testers understand what to expect from the function.

4. **Include Examples**: <br> Provide usage examples within the docstring. These examples can serve as test cases for your code.

   ```python
   def add(a, b):
       """
       Adds two numbers and returns the result.

       Parameters:
           a (int): The first number.
           b (int): The second number.

       Returns:
           int: The sum of a and b.

       Examples:
           >>> add(2, 3)
           5
           >>> add(-1, 1)
           0
       """
       return a + b
   ```

5. **Include Edge Cases**: <br> If applicable, include information about edge cases or corner cases that need to be tested.

6. **Mention Side Effects**: <br> If the function has any side effects (e.g., modifying global variables), document them in the docstring.

7. **Use Docstring Formats**: <br> There are various docstring formats, such as reStructuredText (reST) and Google-style docstrings. Pick a format that's commonly used in your project or organization.

While docstrings themselves don't create tests, they serve as valuable documentation for your code, making it easier to write tests. You can use tools like Sphinx to generate documentation from your docstrings, and testing frameworks like `doctest` can extract and execute code examples from docstrings as tests.

Here's an example of how you can use `doctest` to test code based on the examples in the docstring:

```python
import doctest

def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b

if __name__ == "__main__":
    doctest.testmod()
```

Running this script will execute the examples in the docstring as tests and report any failures.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to write documentation for each module and function</b></summary><br>

Writing documentation for each module and function in your Python code is essential for making your codebase understandable, maintainable, and usable by others (including your future self). Python has a standard way of documenting code using docstrings, and tools like Sphinx can help generate documentation in various formats (HTML, PDF, etc.). Here's how you can write documentation for modules and functions:

<br>
<p align="center">※※※※※※※※※※※※</p>
<h3>Writing Module Documentation:</h3>

1. **Module-Level Docstring**: <br> At the top of your module (Python file), include a module-level docstring. This docstring should describe the purpose and contents of the module. Use triple double-quotes (`"""`) for multi-line docstrings.

   ```python
   """This module provides utility functions for working with strings."""
   ```

2. **Module-level Imports**: <br> If your module imports other modules or has any global variables, include a section at the beginning of the module that lists these imports and variables, along with explanations if necessary.

<br>
<p align="center">※※※※※※※※※※※※</p>
<h3>Writing Function Documentation:</h3>

1. **Function-Level Docstring**: <br> For each function, include a docstring just below the function definition. The docstring should describe what the function does, its parameters (arguments), return values, and any exceptions it may raise. Use triple double-quotes for multi-line docstrings.

   ```python
   def add(a, b):
       """
       Adds two numbers.

       Args:
           a (int): The first number.
           b (int): The second number.

       Returns:
           int: The sum of a and b.
       """
       return a + b
   ```

2. **Parameters**: <br> List all parameters with their types and descriptions in the docstring. Mention whether they are required or optional.

3. **Return Values**: <br> Specify the type and description of the return value. If the function doesn't return anything (returns `None`), mention that explicitly.

4. **Raises (if applicable)**: <br> If the function can raise exceptions, list them in a "Raises" section and provide explanations.

5. **Examples**: <br> Provide usage examples of the function in the docstring. Show how to call the function and what to expect as output.

6. **Notes and Additional Information (if needed)**: <br> Include any additional information, notes, or caveats that may be helpful for users of the function.

<br>
<p align="center">※※※※※※※※※※※※</p>

<h3>Using Sphinx for Documentation Generation:</h3>

While docstrings are essential for documenting code, you can use tools like Sphinx to generate user-friendly documentation from your docstrings. Sphinx allows you to create documentation in various formats, including HTML, PDF, and more.

Here's a brief overview of how to use Sphinx:

1. Install Sphinx:

   ```
   pip install sphinx
   ```

2. Create a Sphinx Project: <br> Use the `sphinx-quickstart` command to set up a new Sphinx documentation project. This command will generate the necessary configuration files and directory structure.

3. Write ReStructuredText (RST): <br> Sphinx uses ReStructuredText (RST) as its markup language. Write your documentation in `.rst` files using RST syntax.

4. Include Python Docstrings: <br> Sphinx can automatically extract documentation from your Python docstrings. Use the `autodoc` extension to enable this feature.

5. Build Documentation: <br> Use Sphinx's `make` commands (e.g., `make html` or `make pdf`) to build the documentation in the desired format.

6. Publish: <br> Once you've built the documentation, you can publish it online or distribute it with your code.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the basic option flags to create tests</b></summary><br>

In Python, you can create tests using various testing frameworks, with the two most popular ones being **unittest** (inspired by Java's JUnit) and **pytest**. When creating tests using these frameworks, you can use different options or flags to control the behavior of the test runner or customize the test execution. Below, I'll provide some basic option flags for both unittest and pytest:

<br>
<p align="center">※※※※※※※※※※※※</p>
<h3>unittest:</h3>

1. **-v or --verbose**: <br> This flag increases the verbosity of test output, providing more details about each test case.

   ```bash
   python -m unittest -v my_test_module
   ```

2. **-f or --failfast**: <br> When this flag is used, the test runner stops as soon as one test case fails, rather than running all the tests.

   ```bash
   python -m unittest -f my_test_module
   ```

3. **-k PATTERN**: <br> This flag allows you to run only the test methods whose names match the given pattern.

   ```bash
   python -m unittest -k test_feature my_test_module
   ```

4. **--start-directory**: <br> Specifies the starting directory for test discovery. Useful when you want to run tests from a specific directory.

   ```bash
   python -m unittest --start-directory tests/
   ```

<br>
<p align="center">※※※※※※※※※※※※</p>
<h3>pytest:</h3>

1. **-v or --verbose**: <br> Similar to unittest, this flag increases the verbosity of test output, providing more details about each test case.

   ```bash
   pytest -v my_test_module.py
   ```

2. **-k EXPRESSION**: <br> Run only the test functions and classes whose names match the given expression.

   ```bash
   pytest -k test_feature my_test_module.py
   ```

3. **-x or --exitfirst**: <br> Stops the test run after the first failure, just like the failfast option in unittest.

   ```bash
   pytest -x my_test_module.py
   ```

4. **--maxfail=num**: <br> Specifies the maximum number of allowed test failures before pytest stops the test run.

   ```bash
   pytest --maxfail=2 my_test_module.py
   ```

5. **-m MARKEXPR**: <br> Run only tests marked with specific markers. Markers are used to group and select tests with certain characteristics.

   ```bash
   pytest -m slow my_test_module.py
   ```

6. **-k and -m can be combined**: <br> You can combine the -k and -m flags to filter tests based on their names and markers simultaneously.

   ```bash
   pytest -k test_feature -m slow my_test_module.py
   ```

These are some of the basic option flags you can use when running tests with unittest and pytest. Depending on your specific testing needs and the features provided by these frameworks, you may find additional flags and options to further customize your test runs.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to find edge cases</b></summary><br>

Edge cases are the scenarios in which a program is expected to behave differently or where it is most likely to fail. By identifying and testing these edge cases, you can improve the robustness and reliability of your software. Here's how you can find edge cases with examples:

1. **Understand the Problem Domain**:
   - Start by thoroughly understanding the problem or requirements of the software you are testing.
   - Identify the boundaries and constraints of the problem domain. These boundaries are often where edge cases reside.

2. **Identify Input Boundaries**:
   - Consider the input variables and parameters that the software takes.
   - Identify the boundary values for these inputs. For example, if a function accepts integers, consider values like 0, 1, -1, the largest possible positive integer, and the smallest possible negative integer.

3. **Consider Special Values**:
   - Think about special values or exceptional cases that might lead to different program behavior. For example, if your program handles file paths, consider edge cases like empty strings or paths with special characters.

4. **Account for Limits and Constraints**:
   - If your program has specific constraints or limits, make sure to test scenarios that approach or exceed these limits. For instance, if your program can only handle a certain number of concurrent users, test it with both the maximum and minimum number of users.

5. **Examine Boundary Conditions**:
   - Focus on the boundaries where different behaviors may occur. For example, if you're testing a sorting algorithm, consider lists that are already sorted, reverse-sorted, or have identical elements.

6. **Think About Error Handling**:
   - Consider scenarios where errors or exceptions are likely to occur. For example, if your code interacts with a database, test what happens when the database is down or when a query returns no results.

7. **Review the Code and Specifications**:
   - Carefully review the code and specifications for any hints or mentions of edge cases. Often, developers or documentation will explicitly highlight potential edge cases.

8. **Consult Stakeholders or Users**:
   - If possible, consult with stakeholders, users, or domain experts to gain insights into potential edge cases. They may provide valuable input based on their experience.

9. **Document and Test**:
   - Once you've identified potential edge cases, document them and create test cases that cover these scenarios.
   - Develop test inputs and expected outcomes for each edge case.
   - Execute these tests to ensure that the software behaves correctly in all identified edge cases.

10. **Automate Testing if Possible**:
    - If you have a set of identified edge cases, consider automating the testing process to ensure these cases are repeatedly tested in the future.

Finding and testing edge cases with examples is a systematic approach to improving the quality of your software. It helps uncover hidden issues and ensures that your software is more robust and reliable, especially under challenging or unexpected conditions.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`


### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!


<!-- <br>

## More Info -->

<br>

## Quiz questions
<details>
<summary><b>Question 0</b></summary><br>

Is this module correctly commented?
```py
#!/usr/bin/python3
import sys

""" 
    My calculation module
"""
...
```
- [x] No
- [ ] Yes

> Tips:<br>
Docstring must be before import statements

<br>
</details>

<details>
<summary><b>Question 1</b></summary><br>

Is this a standardized way to comment a function in Python?
```py
##########
# Addition function
##########
def add(a, b):
    return a + b
```
- [x] No
- [ ] Yes

<br>
</details>

<details>
<summary><b>Question 2</b></summary><br>

Is this a standardized way to comment a function in Python?
```py
"""" Addition function """
def add(a, b):
    return a + b
```
- [x] No
- [ ] Yes

<br>
</details>

<details>
<summary><b>Question 3</b></summary><br>

Is this a standardized way to comment a function in Python?
```py
def add(a, b):
    """ Addition function """
    return a + b
```
- [ ] No
- [x] Yes

<br>
</details>

<details>
<summary><b>Question 4</b></summary><br>

Based on this code, what should all the test cases be? (select multiple)
```py
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
```
- [x] list with one element (any type)
- [x] not a list argument (ex: passing a dictionary to the method)
- [x] list with twice the same element (same type)
- [x] list with more than 2 times the same element (same type)
- [x] list with 2 different element (same type)
- [x] list with multiple types (integer, string, etc…)
- [x] empty list

<br>
</details>

<details>
<summary><b>Question 5</b></summary><br>

Is this module correctly commented?
```py
#!/usr/bin/python3
""" 
    My calculation module
"""
import sys
...
```
- [ ] No
- [x] Yes

<br>
</details>

<details>
<summary><b>Question 6</b></summary><br>

Is this a standardized way to comment a function in Python?
```py
/* Addition function */
def add(a, b):
    return a + b
```
- [x] No
- [ ] Yes

<br>
</details>

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

