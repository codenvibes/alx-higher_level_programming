# **0x08. PYTHON - MORE CLASSES AND OBJECTS**
`Python` `OOP`

<!-- # Background Context -->

# Resources
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” (excluded))
- [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The `__init__` Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “`__str__`- and `__repr__`-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (Mainly the last part “Public instead of Private Attributes”)
- [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

<!-- man or help:
- `` -->

# Learning Objectives
<details>
<summary><h3>Why Python programming is awesome</h3></summary>
</details>

<details>
<summary><h3>What is OOP</h3></summary>
</details>

<details>
<summary><h3>“first-class everything”</h3></summary>
</details>

<details>
<summary><h3>What is a class</h3></summary>
</details>

<details>
<summary><h3>What is an object and an instance</h3></summary>
</details>

<details>
<summary><h3>What is the difference between a class and an object or instance</h3></summary>
</details>

<details>
<summary><h3>What is an attribute</h3></summary>
</details>

<details>
<summary><h3>What are and how to use public, protected and private attributes</h3></summary>
</details>

<details>
<summary><h3>What is <code>self</code></h3></summary>
</details>

<details>
<summary><h3>What is a method</h3></summary>
</details>

<details>
<summary><h3>What is the special <code>__init__</code> method and how to use it</h3></summary>
</details>

<details>
<summary><h3>What is Data Abstraction, Data Encapsulation, and Information Hiding</h3></summary>
</details>

<details>
<summary><h3>What is a property</h3></summary>
</details>

<details>
<summary><h3>What is the difference between an attribute and a property in Python</h3></summary>
</details>

<details>
<summary><h3>What is the Pythonic way to write getters and setters in Python</h3></summary>
</details>

<details>
<summary><h3>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</h3></summary>
</details>

<details>
<summary><h3>What is the difference between <code>__str__</code> and <code>__repr__</code></h3></summary>
</details>

<details>
<summary><h3>What is a class attribute</h3></summary>
</details>

<details>
<summary><h3>What is the difference between a object attribute and a class attribute</h3></summary>
</details>

<details>
<summary><h3>What is a class method</h3></summary>
</details>

<details>
<summary><h3>What is a static method</h3></summary>
</details>

<details>
<summary><h3>How to dynamically create arbitrary new attributes for existing instances of a class</h3></summary>
</details>

<details>
<summary><h3>How to bind attributes to object and classes</h3></summary>
</details>

<details>
<summary><h3>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</h3></summary>
</details>

<details>
<summary><h3>How does Python find the attributes of an object or class</h3></summary>
</details>

<details>
<summary><h3>How to use the <code>getattr</code> function</h3></summary>
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

# Quiz questions
<details>
<summary><h3>Question 0</h3></summary>


</details>

<details>
<summary><h3>Question 1</h3></summary>


</details>

<details>
<summary><h3>Question 2</h3></summary>


</details>

<details>
<summary><h3>Question 3</h3></summary>


</details>

<details>
<summary><h3>Question 4</h3></summary>


</details>

<details>
<summary><h3>Question 5</h3></summary>


</details>

<details>
<summary><h3>Question 6</h3></summary>


</details>

<details>
<summary><h3>Question 7</h3></summary>


</details>

<details>
<summary><h3>Question 8</h3></summary>


</details>

<details>
<summary><h3>Question 9</h3></summary>


</details>

<details>
<summary><h3>Question 10</h3></summary>


</details>

<details>
<summary><h3>Question 11</h3></summary>


</details>

<details>
<summary><h3>Question 12</h3></summary>


</details>

<details>
<summary><h3>Question 13</h3></summary>


</details>

# Tasks
<details>
<summary>

### 0. Simple rectangle
`mandatory`

File: [0-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 1. Real definition of a rectangle
`mandatory`

File: [1-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 2. Area and Perimeter
`mandatory`

File: [2-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 3. String representation
`mandatory`

File: [3-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 4. Eval is magic
`mandatory`

File: [4-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 5. Detect instance deletion
`mandatory`

File: [5-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 6. How many instances
`mandatory`

File: [6-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 7. Change representation
`mandatory`

File: [7-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 8. Compare rectangles
`mandatory`

File: [8-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 9. A square is a rectangle
`mandatory`

File: [9-rectangle.py]()
</summary>


</details>

<details>
<summary>

### 10. N queens
`#advanced`

File: [101-nqueens.py]()
</summary>


</details>

