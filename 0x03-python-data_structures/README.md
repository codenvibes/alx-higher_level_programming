<h1 align="center"><b>0x03. PYTHON - DATA STRUCTURES: LISTS, TUPLES</b></h1>
<div align="center"><code>Python</code></div>

<!-- <br>

## Background Context -->


<!-- <br>
<hr>
<h3><a href=>Notes</a></h3>
<hr> -->

<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/tutorial/introduction.html#lists">3.1.3. Lists</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/tutorial/datastructures.html">Data structures</a> <em>(*until `5.3. Tuples and Sequences` included*)</em></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=A1HUzrvS-Pw">Learn to Program 6 : Lists</a></b></summary><br>


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
<summary><b><a href=" "> </a>What are lists and how to use them</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the differences and similarities between strings and lists</b></summary><br>

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

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the most common methods of lists and how to use them</b></summary><br>

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

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use lists as stacks and queues</b></summary><br>

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

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are list comprehensions and how to use them</b></summary><br>

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

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are tuples and how to use them</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>When to use tuples versus lists</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a sequence</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is tuple packing</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is sequence unpacking</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is the <code>del</code> statement and how to use it</b></summary><br>


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

