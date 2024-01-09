<h1 align="center"><b>0x00. PYTHON - HELLO, WORLD</b></h1>
<div align="center"><code>Python</code></div>

<br>

## Concepts
<details>
<summary><b><a href="https://intranet.alxswe.com/concepts/550">Python programming</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<br><div align="center"><img src="https://github.com/codenvibes/alx-higher_level_programming/blob/master/0x00-python-hello_world/images/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg"></div>


## Author’s disclaimer
```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.

Enjoy!

- Guillaume
```

<!-- <br>

## Background Context -->


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/tutorial/index.html">The Python tutorial</a> (only the first three chapters below)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/tutorial/appetite.html">Whetting Your Appetite</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/tutorial/interpreter.html">Using the Python Interpreter</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/tutorial/introduction.html">An Informal Introduction to Python</a> (Read up until “3.1.2. Strings” included)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://realpython.com/python-f-strings/">How To Use String Formatters in Python 3</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt">Learn to Program</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://pypi.org/project/pycodestyle/">Pycodestyle – Style Guide for Python Code</a></b></summary><br>


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
<summary><b><a href=" "> </a>Who created Python</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Who is Guido van Rossum</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Where does the name ‘Python’ come from</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the Zen of Python
</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the Python interpreter</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to print text and variables using <code>print</code></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use strings</b></summary><br>

Strings in Python are used to represent textual data. They can be used to store and manipulate text, such as words, sentences, and even characters. Here's how you can work with strings in Python:

1. **Creating Strings:**
   You can create strings using either single quotes `'`, double quotes `"`, or triple quotes `'''` or `"""` for multi-line strings.

   ```python
   single_quoted = 'Hello, single quotes!'
   double_quoted = "Hello, double quotes!"
   multi_line = '''This is a
   multi-line string.'''
   ```

2. **Accessing Characters:**
   Strings are sequences of characters, and you can access individual characters using indexing.

   ```python
   my_string = "Hello, World!"
   first_character = my_string[0]   # Access the first character 'H'
   ```

3. **String Methods:**
   Strings have many built-in methods for manipulation. Some examples include:

   ```python
   my_string = "Hello, World!"
   length = len(my_string)           # Get the length of the string
   uppercase = my_string.upper()     # Convert to uppercase: "HELLO, WORLD!"
   lowercase = my_string.lower()     # Convert to lowercase: "hello, world!"
   replaced = my_string.replace("Hello", "Hi")  # Replace text: "Hi, World!"
   ```

4. **String Concatenation:**
   You can concatenate (combine) strings using the `+` operator.

   ```python
   greeting = "Hello"
   name = "Alice"
   full_greeting = greeting + ", " + name  # "Hello, Alice"
   ```

5. **String Formatting:**
   String formatting allows you to insert variables or values into a string. Python offers different methods for string formatting, including the `%` operator and the `.format()` method.

   ```python
   age = 25
   message = "I am %d years old." % age   # "I am 25 years old."
   ```

   ```python
   name = "Bob"
   age = 30
   message = "My name is {} and I am {} years old.".format(name, age)
   ```

   In modern Python (3.6 and above), you can use f-strings for a more concise and readable way of formatting strings:

   ```python
   name = "Charlie"
   age = 22
   message = f"My name is {name} and I am {age} years old."
   ```

6. **String Slicing:**
   You can extract substrings from a string using slicing.

   ```python
   my_string = "Hello, World!"
   substring = my_string[7:12]   # "World"
   ```

7. **Escape Sequences:**
   You can use escape sequences to include special characters within strings.

   ```python
   escaped_string = "This is a \"quote\" inside a string."
   ```

These are just some basic operations you can perform with strings in Python. Strings are versatile and widely used for various text-based operations in programming.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are indexing and slicing in Python</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the official Python coding style and how to check your code with <code>pycodestyle</code></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
<!-- Add your requirements here -->

<!-- <br>

## More Info -->

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

<details>
<summary><b>Question 9</b></summary><br>


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
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 12. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 13. 
`#advanced`

File: []()
</summary>


</details>

