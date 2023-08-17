# **0x03. PYTHON - DATA STRUCTURES: LISTS, TUPLES**
`Python`

# Resources
- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (*until `5.3. Tuples and Sequences` included*)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

# Learning Objectives
<details>
<summary><h3><a href="https://docs.python.org/3/tutorial/datastructures.html?highlight=sequence">Data Structures</a></h3></summary>
</details>

<details>

<details>
<summary><h3>What are lists and how to use them</h3></summary>
</details>

<details>
<summary><h3>What are the differences and similarities between strings and lists</h3></summary>

**Differences:**

1. **Mutability:**
   - Strings are immutable, meaning their individual characters cannot be changed after they are created. You can create a new string by modifying or concatenating existing ones.
   - Lists are mutable, so you can modify, add, or remove elements within the list after it's created.

2. **Element Type:**
   - Strings are sequences of characters. Each character is a Unicode code point, and you can access individual characters using indexing (e.g., `"hello"[0]` gives `'h'`).
   - Lists can contain elements of any type, including other lists. Elements in a list are accessed using indexing as well (e.g., `my_list[0]`).

3. **Concatenation and Joining:**
   - Strings can be concatenated using the `+` operator, and you can join a list of strings using the `join()` method (e.g., `' '.join(my_list)`).
   - Lists can be concatenated using the `+` operator as well, and you can create a new string by joining a list of characters using `join()` (e.g., `"".join(my_list)`).

**Similarities:**

1. **Indexing and Slicing:**
   - Both strings and lists support indexing to access individual elements. For strings, it's individual characters; for lists, it's the elements.
   - Both strings and lists support slicing to extract sub-portions of the sequence. For example, `my_string[1:4]` or `my_list[1:4]` extracts a portion of the sequence.

2. **Iteration:**
   - Both strings and lists can be iterated over using loops. You can use a `for` loop to iterate through each character in a string or each element in a list.

3. **Length:**
   - Both strings and lists have a length, which can be obtained using the `len()` function (e.g., `len(my_string)` or `len(my_list)`).

4. **In Membership:**
   - You can use the `in` operator to check if an element exists within both strings and lists (e.g., `'a' in my_string` or `3 in my_list`).

5. **Methods:**
   - Both strings and lists have various built-in methods. While the methods themselves might be different, the idea of using methods to manipulate and interact with the data is common to both.
</details>

<details>
<summary><h3>What are the most common methods of lists and how to use them</h3></summary>

1. **`append()`**: Adds an element to the end of the list.
   ```python
   my_list = [1, 2, 3]
   my_list.append(4)
   # my_list is now [1, 2, 3, 4]
   ```

2. **`extend()`**: Extends the list by appending elements from another iterable.
   ```python
   my_list = [1, 2, 3]
   my_list.extend([4, 5, 6])
   # my_list is now [1, 2, 3, 4, 5, 6]
   ```

3. **`insert()`**: Inserts an element at a specified index.
   ```python
   my_list = [1, 2, 3]
   my_list.insert(1, 4)
   # my_list is now [1, 4, 2, 3]
   ```

4. **`remove()`**: Removes the first occurrence of a specific value.
   ```python
   my_list = [1, 2, 3, 2, 4]
   my_list.remove(2)
   # my_list is now [1, 3, 2, 4]
   ```

5. **`pop()`**: Removes and returns an element at a specified index. If no index is provided, it removes and returns the last element.
   ```python
   my_list = [1, 2, 3, 4]
   removed_element = my_list.pop(1)
   # my_list is now [1, 3, 4], removed_element is 2
   ```

6. **`index()`**: Returns the index of the first occurrence of a specified value.
   ```python
   my_list = [1, 2, 3, 4]
   index_of_3 = my_list.index(3)
   # index_of_3 is 2
   ```

7. **`count()`**: Returns the number of occurrences of a specific value in the list.
   ```python
   my_list = [1, 2, 2, 3, 2]
   count_of_2 = my_list.count(2)
   # count_of_2 is 3
   ```

8. **`sort()`**: Sorts the list in place (modifies the original list).
   ```python
   my_list = [4, 2, 1, 3]
   my_list.sort()
   # my_list is now [1, 2, 3, 4]
   ```

9. **`reverse()`**: Reverses the order of elements in the list in place.
   ```python
   my_list = [1, 2, 3]
   my_list.reverse()
   # my_list is now [3, 2, 1]
   ```

10. **`copy()`** (or `list()` constructor): Creates a shallow copy of the list.
    ```python
    my_list = [1, 2, 3]
    new_list = my_list.copy()
    # new_list is [1, 2, 3]
    ```

11. **`clear()`**: Removes all elements from the list, making it empty.
    ```python
    my_list = [1, 2, 3]
    my_list.clear()
    # my_list is now []
    ```

These are just a subset of the available list methods. Each of these methods can be very useful depending on your specific use case. Remember that you can access information about these methods using Python's built-in help system, like `help(list)` or by using `dir(list)` to see a list of all available methods for lists.
</details>

<details>
<summary><h3>How to use lists as stacks and queues</h3></summary>

You can use Python lists to implement both stacks and queues, two common data structures for managing collections of items with specific behavior. Here's how you can use lists to implement stacks and queues:

**Using Lists as Stacks:**

A stack is a last-in, first-out (LIFO) data structure, where elements are added and removed from the top (or end) of the stack.

To use a list as a stack, you can utilize the `append()` method to add elements to the end of the list and the `pop()` method to remove and return the last element.

```python
stack = []
stack.append(1)    # Push 1
stack.append(2)    # Push 2
stack.append(3)    # Push 3

top_element = stack.pop()  # Pop the top element (3)
print(top_element)         # Output: 3

print(stack)       # Remaining stack: [1, 2]
```

**Using Lists as Queues:**

A queue is a first-in, first-out (FIFO) data structure, where elements are added at the back and removed from the front of the queue.

To use a list as a queue, you can use the `append()` method to add elements to the end of the list, and the `pop(0)` method to remove and return the first element. However, it's worth noting that using `pop(0)` on a large list can be inefficient because it requires shifting all the remaining elements to fill the gap.
```py
queue = []

# Enqueue elements using append()
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeue elements using pop(0)
front_element = queue.pop(0)  # Dequeue the front element (1)
print(front_element)          # Output: 1

print(queue)      # Remaining queue: [2, 3]
```

A more efficient way to implement a queue using a list is to use the `collections.deque` class, which is designed to efficiently support both ends of the queue.

```python
from collections import deque

queue = deque()
queue.append(1)   # Enqueue 1
queue.append(2)   # Enqueue 2
queue.append(3)   # Enqueue 3

front_element = queue.popleft()  # Dequeue the front element (1)
print(front_element)             # Output: 1

print(queue)      # Remaining queue: deque([2, 3])
```

Using `collections.deque` is more efficient for populating and dequeuing elements from both ends of the queue compared to using a regular list.

Remember that Python's `list` type is quite versatile, so you can use it to implement a wide range of data structures, including stacks and queues. However, for certain applications, specialized data structure classes like `collections.deque` might offer better performance and more convenient methods for these purposes.
</details>

<details>
<summary><h3>What are list comprehensions and how to use them</h3></summary>
List comprehensions are a concise and expressive way to create lists in Python. They provide a compact syntax for generating new lists by applying an expression to each item in an iterable (such as a list, tuple, or range) and optionally filtering items based on a condition.

The basic syntax of a list comprehension is as follows:
```
new_list = [expression for item in iterable if condition]
```

Here's a breakdown of the components:
- `expression`: The operation or value you want to include in the new list for each item in the iterable.
- `item`: Represents each element in the iterable that you're iterating over.
- `iterable`: The collection of items you're iterating over.
- `condition`: An optional condition that filters which items are included in the new list.

Here are some examples to illustrate how to use list comprehensions:

**Example 1: Generating a list of squares of numbers from 0 to 9:**
```python
squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Example 2: Filtering even numbers from a list:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
# Result: [2, 4, 6, 8, 10]
```

**Example 3: Creating a list of tuples with values and their squares:**
```python
values = [1, 2, 3, 4, 5]
value_squares = [(x, x**2) for x in values]
# Result: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

**Example 4: Flattening a list of lists:**
```python
nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [x for sublist in nested_lists for x in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List comprehensions can be a powerful tool for creating and transforming lists in a concise and readable manner. However, it's important to strike a balance between readability and complexity. For more complex operations, using regular loops might be more appropriate.
</details>

<details>
<summary><h3>What are tuples and how to use them</h3></summary>

A tuple in Python is an ordered collection of elements, similar to a list. However, tuples are immutable, which means once they are created, their elements cannot be changed, added, or removed. Tuples are typically used to group related data together, and they are often used when you want to create a collection of items that should not be modified after creation.

Tuples are defined by enclosing elements in parentheses `()`, separated by commas. Here's a basic example:

```python
my_tuple = (1, 2, 3)
```

You can also create a tuple without parentheses by using commas:

```python
another_tuple = 4, 5, 6
```

Here are some key characteristics of tuples and how to use them:

1. **Accessing Elements:**
   Elements in a tuple can be accessed using indexing, just like lists.
   
   ```python
   my_tuple = (10, 20, 30, 40)
   print(my_tuple[1])  # Output: 20
   ```

2. **Unpacking Tuples:**
   You can unpack the elements of a tuple into variables. This is particularly useful when you have functions returning multiple values.

   ```python
   my_tuple = (3.14, "hello", 42)
   pi, greeting, answer = my_tuple
   ```

3. **Tuple Concatenation:**
   Tuples can be concatenated using the `+` operator.

   ```python
   tuple1 = (1, 2, 3)
   tuple2 = (4, 5, 6)
   combined_tuple = tuple1 + tuple2
   ```

4. **Nested Tuples:**
   Tuples can contain other tuples as elements, allowing you to create nested structures.

   ```python
   nested_tuple = ((1, 2), (3, 4), (5, 6))
   ```

5. **Iteration:**
   You can iterate over the elements of a tuple using a `for` loop.

   ```python
   my_tuple = (10, 20, 30)
   for item in my_tuple:
       print(item)
   ```

6. **Immutability:**
   As mentioned earlier, tuples are immutable. Once a tuple is created, you cannot modify its elements.

7. **Methods:**
   Tuples have fewer built-in methods compared to lists, as they can't be modified. However, they have methods like `count()` and `index()` for basic operations.

8. **Advantages:**
   Tuples are useful when you want to ensure that a collection of items remains unchanged throughout your program's execution. They can also be used as keys in dictionaries due to their immutability.

Overall, tuples provide a way to group related data in an ordered and immutable way. They are often used in situations where you need to store a set of values that shouldn't be modified, such as coordinates, configuration settings, or data that you want to pass around safely without the risk of accidental modification.
</details>

<details>
<summary><h3>When to use tuples versus lists</h3></summary>
</details>

<details>
<summary><h3>What is a sequence</h3></summary>

In programming, a sequence refers to an ordered collection of elements. These elements can be of any data type, such as numbers, characters, strings, or even other sequences. Sequences are fundamental data structures used to store and manipulate collections of items in a specific order.

Python provides several built-in sequence types that you can use:

1. **Lists**: Ordered collections of items, where each item can be of any data type. Lists are mutable, meaning you can add, remove, and modify elements after creation.

2. **Tuples**: Similar to lists, but tuples are immutable, meaning their elements cannot be changed once they are created.

3. **Strings**: Sequences of characters. Strings are also immutable, like tuples.

4. **Ranges**: Represent a sequence of numbers, typically used in loops to iterate over a range of values.

5. **Bytes and Bytearrays**: Sequences of bytes, used to represent binary data.

6. **Lists of Lists (Nested Lists)**: Lists can also contain other lists, creating a nested structure.

7. **Tuples of Tuples (Nested Tuples)**: Similar to nested lists, but with tuples.

8. **Strings of Strings (Nested Strings)**: A string containing other strings, often used in text processing.

You can perform common sequence operations on these types, such as indexing to access individual elements, slicing to extract sub-sequences, iteration through loops, and more. Understanding sequences is crucial as they are a fundamental concept in programming and are widely used in various applications, from data manipulation to algorithms and beyond.
</details>

<details>
<summary><h3>What is tuple packing</h3></summary>
</details>

<details>
<summary><h3>What is sequence unpacking</h3></summary>
</details>

<details>
<summary><h3>What is the <code>del</code> statement and how to use it</h3></summary>
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

Write a function that prints all integers of a list.

-   Prototype: `def print_list_integer(my_list=[]):`
-   Format: one integer per line. See example
-   You are not allowed to import any module
-   You can assume that the list only contains integers
-   You are not allowed to cast integers into strings
-   You have to use `str.format()` to print integers

```bash
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 1. Secure access to an element in a list
`mandatory`

File: [1-element_at.py]()
</summary>

Write a function that retrieves an element from a list like in C.

-   Prototype: `def element_at(my_list, idx):`
-   If `idx` is negative, the function should return `None`
-   If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
-   You are not allowed to import any module
-   You are not allowed to use `try/except`

```bash
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 2. Replace element
`mandatory`

File: [2-replace_in_list.py]()
</summary>

Write a function that replaces an element of a list at a specific position (like in C).

-   Prototype: `def replace_in_list(my_list, idx, element):`
-   If `idx` is negative, the function should not modify anything, and returns the original list
-   If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
-   You are not allowed to import any module
-   You are not allowed to use `try/except`

```bash
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 3. Print a list of integers... in reverse!
`mandatory`

File: [3-print_reversed_list_integer.py]()
</summary>

Write a function that prints all integers of a list, in reverse order.

-   Prototype: `def print_reversed_list_integer(my_list=[]):`
-   Format: one integer per line. See example
-   You are not allowed to import any module
-   You can assume that the list only contains integers
-   You are not allowed to cast integers into strings
-   You have to use `str.format()` to print integers

```bash
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 4. Replace in a copy
`mandatory`

File: [4-new_in_list.py]()
</summary>

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

-   Prototype: `def new_in_list(my_list, idx, element):`
-   If `idx` is negative, the function should return a copy of the original `list`
-   If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
-   You are not allowed to import any module
-   You are not allowed to use `try/except`

```bash
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 5. Can you C me now?
`mandatory`

File: [5-no_c.py]()
</summary>

Write a function that removes all characters `c` and `C` from a string.

-   Prototype: `def no_c(my_string):`
-   The function should return the new string
-   You are not allowed to import any module
-   You are not allowed to use `str.replace()`

```bash
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 6. Lists of lists = Matrix
`mandatory`

File: [6-print_matrix_integer.py]()
</summary>

Write a function that prints a matrix of integers.

-   Prototype: `def print_matrix_integer(matrix=[[]]):`
-   Format: see example
-   You are not allowed to import any module
-   You can assume that the list only contains integers
-   You are not allowed to cast integers into strings
-   You have to use `str.format()` to print integers

```bash
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 7. Tuples addition
`mandatory`

File: [7-add_tuple.py]()
</summary>

Write a function that adds 2 tuples.

-   Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
-   Returns a tuple with 2 integers:
    -   The first element should be the addition of the first element of each argument
    -   The second element should be the addition of the second element of each argument
-   You are not allowed to import any module
-   You can assume that the two tuples will only contain integers
-   If a tuple is smaller than 2, use the value `0` for each missing integer
-   If a tuple is bigger than 2, use only the first 2 integers

```bash
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 8. More returns!
`mandatory`

File: [8-multiple_returns.py]()
</summary>

Write a function that returns a tuple with the length of a string and its first character.

-   Prototype: `def multiple_returns(sentence):`
-   If the sentence is empty, the first character should be equal to `None`
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 9. Find the max
`mandatory`

File: [9-max_integer.py]()
</summary>

Write a function that finds the biggest integer of a list.

-   Prototype: `def max_integer(my_list=[]):`
-   If the list is empty, return `None`
-   You can assume that the list only contains integers
-   You are not allowed to import any module
-   You are not allowed to use the builtin `max()`

```bash
guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 10. Only by 2
`mandatory`

File: [10-divisible_by_2.py]()
</summary>

Write a function that finds all multiples of 2 in a list.

-   Prototype: `def divisible_by_2(my_list=[]):`
-   Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
-   The new list should have the same size as the original list
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 11. Delete at
`mandatory`

File: [11-delete_at.py]()
</summary>

Write a function that deletes the item at a specific position in a list.

-   Prototype: `def delete_at(my_list=[], idx=0):`
-   If `idx` is negative or out of range, nothing change (returns the same list)
-   You are not allowed to use `pop()`
-   You are not allowed to import any module

```bash
guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$

```
</details>

<details>
<summary>

### 12. Switch
`mandatory`

File: [12-switch.py]()
</summary>

Complete the source code in order to switch value of `a` and `b`

-   You can find the source code [here](https://alx-intranet.hbtn.io/rltoken/Iwhtw8ZaGLN7TIzodKGnYA "here")
-   Your code should be inserted where the comment is (line 4)
-   Your program should be exactly 5 lines long

```bash
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$

```
</details>

<details>
<summary>

### 13. Linked list palindrome
`mandatory`

File: [13-is_palindrome.c](), [lists.h]()
</summary>

**Technical interview preparation**:

-   You are not allowed to google anything
-   Whiteboard first

Write a function in C that checks if a singly linked list is a palindrome.

-   Prototype: `int is_palindrome(listint_t **head);`
-   Return: `0` if it is not a palindrome, `1` if it is a palindrome
-   An empty list is considered a palindrome

```bash
carrie@ubuntu:0x03$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
carrie@ubuntu:0x03$

```

```bash
carrie@ubuntu:0x03$ cat linked_lists.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
carrie@ubuntu:0x03$

```

```bash
carrie@ubuntu:0x03$ cat 13-main.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
carrie@ubuntu:0x03$

```

```bash
carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
carrie@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
carrie@ubuntu:0x03$

```
</details>


<details>
<summary>

### 14. CPython #0: Python lists
`#advanced`

File: [100-print_python_list_info.c]()
</summary>

CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.\
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let's have fun with Python and C, and let's look at what makes Python so easy to use.

-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/7e7834b535261d05532fb80a9304f7051c4ad7ac.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20211121%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211121T180457Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=665e724d14ace604a30295cda2420ee7685b2123a40ff31d766039451a58447b)

Create a C function that prints some basic info about Python lists.

-   Prototype: `void print_python_list_info(PyObject *p);`
-   Format: see example
-   Python version: 3.4
-   Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
-   OS: `Ubuntu 14.04 LTS`
-   Start by reading:
    -   listobject.h
    -   object.h
    -   [Common Object Structures](https://alx-intranet.hbtn.io/rltoken/jmRTk4m1VSzjsu3QTGaC6w "Common Object Structures")
    -   [List Objects](https://alx-intranet.hbtn.io/rltoken/7V1HlQRESjCqrKrw_O_Urw "List Objects")

```bash
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
julien@ubuntu:~/CPython$ cat 100-test_lists.py
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
julien@CPython:~/CPython$

```
</details>

