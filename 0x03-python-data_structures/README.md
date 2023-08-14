# **0x03. PYTHON - DATA STRUCTURES: LISTS, TUPLES**
`Python`

# Resources
- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (*until `5.3. Tuples and Sequences` included*)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

# Learning Objectives
<details>
<summary>What are lists and how to use them</summary>
</details>

<details>
<summary>What are the differences and similarities between strings and lists</summary>
</details>

<details>
<summary>What are the most common methods of lists and how to use them</summary>
</details>

<details>
<summary>How to use lists as stacks and queues</summary>
</details>

<details>
<summary>What are list comprehensions and how to use them</summary>
</details>

<details>
<summary>What are tuples and how to use them</summary>
</details>

<details>
<summary>When to use tuples versus lists</summary>
</details>

<details>
<summary>What is a sequence</summary>
</details>

<details>
<summary>What is tuple packing</summary>
</details>

<details>
<summary>What is sequence unpacking</summary>
</details>

<details>
<summary>What is the <code>del</code> statement and how to use it</summary>
</details>

# Requirements
<details>
<summary>

### Python Scripts
</summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
</details>

<details>
<summary>

### C
</summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded
</details>

# Quiz questions
<details>
<summary>

### Question #0
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> b
```
- [ ] a
- [ ] b
- [ ] [1, 2, 3, 4]
- [x] [1, 2, 10, 4]
- [ ] [1]
</details>

<details>
<summary>

### Question #1
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> a[1:3]
```
- [x] [2, 3]
- [ ] [1, 2]
- [ ] [1, 2, 3]

<details><summary>Explanation:</summary>

The index before the colon (`:`) is the start index (inclusive), and the index after the colon is the end index (exclusive). Therefore, `a[1:3]` will include elements at indices 1 and 2, but not the element at index 3.</details>
</details>

<details>
<summary>

### Question #2
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> a[-3]
```
- [x] 2
- [ ] [4, 3]
- [ ] -3
</details>

<details>
<summary>

### Question #3
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> a[-1]
```
- [x] 4
- [ ] [4, 3, 2, 1]
- [ ] 2
- [ ] -1
</details>

<details>
<summary>

### Question #4
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> len(a)
```
- [ ] 6
- [ ] 8
- [x] 4
- [ ] 2
</details>

<details>
<summary>

### Question #5
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> a
```
- [ ] a
- [ ] b
- [ ] [1, 2, 3, 4]
- [x] [1, 2, 10, 4]
- [ ] [1]
</details>

<details>
<summary>

### Question #6
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> a[2] = 10
>>> a
```
- [x] [1, 2, 10, 4]
- [ ] [1, 2, 10, 10]
- [ ] [1, 10, 3, 4]
- [ ] [1, 2, 3, 4]
</details>

<details>
<summary>

### Question #7
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> b = a
>>> b
```
- [ ] 1
- [ ] a
- [ ] [1]
- [x] [1, 2, 3, 4]
</details>

<details>
<summary>

### Question #8
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> len(a)
```
- [ ] 6
- [x] 5
- [ ] 2
</details>

<details>
<summary>

### Question #9
</summary>

What do these lines print?
```py
>>> a = [1, 2, 3, 4]
>>> a[0]
```
- [ ] [1, 2]
- [ ] [1, 2, 3, 4]
- [ ] [1]
- [ ] 2
- [x] 1
</details>

# Tasks
<details>
<summary>

### 0. Print a list of integers
`mandatory`

File: [0-print_list_integer.py]()
</summary>
</details>

<details>
<summary>

### 1. Secure access to an element in a list
`mandatory`

File: [1-element_at.py]()
</summary>
</details>

<details>
<summary>

### 2. Replace element
`mandatory`

File: [2-replace_in_list.py]()
</summary>
</details>

<details>
<summary>

### 3. Print a list of integers... in reverse!
`mandatory`

File: [3-print_reversed_list_integer.py]()
</summary>
</details>

<details>
<summary>

### 4. Replace in a copy
`mandatory`

File: [4-new_in_list.py]()
</summary>
</details>

<details>
<summary>

### 5. Can you C me now?
`mandatory`

File: [5-no_c.py]()
</summary>
</details>

<details>
<summary>

### 6. Lists of lists = Matrix
`mandatory`

File: [6-print_matrix_integer.py]()
</summary>
</details>

<details>
<summary>

### 7. Tuples addition
`mandatory`

File: [7-add_tuple.py]()
</summary>
</details>

<details>
<summary>

### 8. More returns!
`mandatory`

File: [8-multiple_returns.py]()
</summary>
</details>

<details>
<summary>

### 9. Find the max
`mandatory`

File: [9-max_integer.py]()
</summary>
</details>

<details>
<summary>

### 10. Only by 2
`mandatory`

File: [10-divisible_by_2.py]()
</summary>
</details>

<details>
<summary>

### 11. Delete at
`mandatory`

File: [11-delete_at.py]()
</summary>
</details>
