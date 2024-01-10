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


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to affect values to variables</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>while</code> and for <code>loops</code></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How is Python’s <code>for</code> different from <code>C</code>‘s?</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>break</code> and <code>continue</code> statements</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use <code>else</code> clauses on loops</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What does the <code>pass</code> statement do, and when to use it</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use <code>range</code></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a function and how do you use functions</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What does return a function that does not use any <code>return</code> statement</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Scope of variables</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What’s a traceback</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the arithmetic operators and how to use them</b></summary><br>


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


<br>
</details>

<details>
<summary><b>Question 1</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 2</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 3</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 4</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 5</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 6</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 7</b></summary><br>


<br>
</details>

<details>
<summary><b>Question 8</b></summary><br>


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

