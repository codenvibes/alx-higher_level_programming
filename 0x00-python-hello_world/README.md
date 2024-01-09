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

Indexing and slicing are techniques used to access elements from sequences (like lists, tuples, and strings) in Python. They allow you to retrieve specific values or sub-sequences from within a larger sequence.

1. **Indexing:**
   Indexing is used to access a single element at a specific position in a sequence. In Python, indexing starts from 0, meaning the first element is at index 0, the second at index 1, and so on.

   ```python
   my_list = [10, 20, 30, 40, 50]
   element = my_list[2]  # Accesses the element at index 2 (which is 30)
   ```

2. **Slicing:**
   Slicing is used to extract a portion (sub-sequence) of a sequence. It involves specifying a start index, an end index, and an optional step value. The slice includes all elements from the start index up to (but not including) the end index.

   ```python
   my_list = [10, 20, 30, 40, 50]
   sub_sequence = my_list[1:4]  # Gets elements at indices 1, 2, and 3 (20, 30, 40)
   ```

   You can also omit the start or end index to slice from the beginning or up to the end:

   ```python
   first_three = my_list[:3]     # Gets elements at indices 0, 1, and 2 (10, 20, 30)
   after_third = my_list[3:]     # Gets elements at indices 3, 4 (40, 50)
   ```

   Using a step value, you can skip elements:

   ```python
   every_second = my_list[::2]   # Gets elements at indices 0, 2, and 4 (10, 30, 50)
   ```

   Negative indices and step values can also be used:

   ```python
   reversed_list = my_list[::-1]  # Reverses the list (50, 40, 30, 20, 10)
   ```

Slicing and indexing are versatile techniques that are not limited to lists; they can also be used with tuples, strings, and other sequence types in Python. Keep in mind that indexing and slicing are subject to bounds, so trying to access an index outside the range of the sequence will result in an error.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the official Python coding style and how to check your code with <code>pycodestyle</code></b></summary><br>


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
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a>Shell Scripts</b></summary><br>

- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l` file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>

<details>
<summary><b><a href=" "> </a>C Scripts</b></summary><br>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using betty-style.pl and betty-doc.pl
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
<details>
<summary><b>Zen</b></summary><br>

> The "Zen of Python" is a collection of guiding principles for writing computer programs in the Python programming language. These principles are meant to capture the design philosophy and values that have shaped the development of Python. The Zen of Python was written by Tim Peters, a long-time contributor to the Python community, and it is included as an "Easter egg" in Python by typing `import this` in the Python interpreter.
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

<br>
</details>

<details>
<summary><b>Pycodestyle</b></summary><br>

`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg">

<br>
</details>


<br>

## Quiz questions
<details>
<summary><b>Question 0</b></summary><br>

What does this command line print?
```py
>>> a = "Python is cool"
>>> print(a[-2])
```
- [x] o
- [ ] Nothing
- [ ] l
- [ ] ol

<br>
</details>

<details>
<summary><b>Question 1</b></summary><br>

What does this command line print?
```py
>>> a = "Python is cool"
>>> print(a[0:6])
```
- [ ] Python is
- [ ] Python is cool
- [ ] Pytho
- [x] Python

<br>
</details>

<details>
<summary><b>Question 2</b></summary><br>

What does this command line print?
```py
>>> print(f"{98} Battery street")
```
- [ ] 9 Battery street
- [ ] 8 Battery street
- [ ] f"98 Battery street"
- [x] 98 Battery street

<br>
</details>

<details>
<summary><b>Question 3</b></summary><br>

What does this command line print?
```py
>>> print("Holberton school")
```
- [x] Holberton school
- [ ] ‘Holberton school’
- [ ] “Holberton school”
- [ ] Holberton

<br>
</details>

<details>
<summary><b>Question 4</b></summary><br>

What does this command line print?
```py
>>> print(f"{98} Battery street, {'San Francisco'}")
```
- [x] 98 Battery street, San Francisco
- [ ] San Francisco Battery street, 98
- [ ] 8 Battery street, San
- [ ] “98 Battery street, San Francisco”

<br>
</details>

<details>
<summary><b>Question 5</b></summary><br>

What does this command line print?
```py
>>> a = "Python is cool"
>>> print(a[7:-5])
```
- [ ] si
- [x] is
- [ ] Python
- [ ] nohtyP
- [ ] on

<br>
</details>

<details>
<summary><b>Question 6</b></summary><br>

What does this command line print?
```py
>>> a = "Python is cool"
>>> print(a[:6])
```
- [ ] Python is
- [ ] is cool
- [x] Python
- [ ] Pytho

<br>
</details>

<details>
<summary><b>Question 7</b></summary><br>

What does this command line print?
```py
>>> a = "Python is cool"
>>> print(a[7:])
```
- [ ] cool
- [x] is cool
- [ ] Python is
- [ ] Python i

<br>
</details>

<details>
<summary><b>Question 8</b></summary><br>

What does this command line print?
```py
>>> a = "Python is cool"
>>> print(a[4])
```
- [x] o
- [ ] h
- [ ] n
- [ ] P

<br>
</details>

<details>
<summary><b>Question 9</b></summary><br>

Who created Python?
- [x] Guido van Rossum
- [ ] Yukihiro Matsumoto
- [ ] Julien Barbier

<br>
</details>

<br>

## Tasks
<details>
<summary>

### 0. Run Python file
`mandatory`

File: [0-run]()
</summary>

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

```
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$

```
</details>

<details>
<summary>

### 1. Run inline
`mandatory`

File: [1-run_inline]()
</summary>

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Best School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline
Best School: 98
guillaume@ubuntu:~/py/0x00$

```
</details>

<details>
<summary>

### 2. Hello, print
`mandatory`

File: [2-print.py]()
</summary>

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

-   Use the function `print`

```
guillaume@ubuntu:~/py/0x00$ ./2-print.py
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$

```
</details>

<details>
<summary>

### 3. Print integer
`mandatory`

File: [3-print_number.py]()
</summary>

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py "source code") in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

-   You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py "here")
-   The output of the script should be:
    -   the number, followed by `Battery street`,
    -   followed by a new line
-   You are not allowed to cast the variable `number` into a string
-   Your code must be 3 lines long
-   You have to use the new print numbers [tips](https://alx-intranet.hbtn.io/rltoken/bKDyX1T7EsKyOMXp_2YzAg "tips") (with `.format(...)`)

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$

```

> C is strongly typed... not in Python! The variable `number` can be assigned to a string, a float, a bool etc... Forcing the type during a string format (`"...".format(...)`) is a way to control the type of a variable
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

