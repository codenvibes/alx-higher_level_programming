<h1 align="center"><b>0x12. JAVASCRIPT - WARM UPJAVASCRIPT - WARM UP</b></h1>
<div align="center"><code>JavaScript</code></div>

# Background Context
JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:
- Scripting (same as we did with Python)
- Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

# Resources
<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics">Writing JavaScript Code</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables">Variables</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures">Data Types</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics">Operators</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence">Operator Precedence</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling">Controlling Program Flow</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions">Functions</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects">Objects and Arrays</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects">Intrinsic Objects</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://darrenderidder.github.io/talks/ModulePatterns/#/">Module patterns</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=sjyJBL5fkp8">var, let and const</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://www.youtube.com/watch?v=vZBCTc9zHtI">JavaScript Tutorial</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://github.com/mbeaudru/modern-js-cheatsheet">Modern JS</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!-- **man or help:**
- `` -->

# Learning Objectives
<details>
<summary><b><a href=" "> </a>Why JavaScript programming is amazing</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to run a JavaScript script</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to create variables and constants</b></summary><br>

In JavaScript, you can create variables using the `var`, `let`, or `const` keywords. Variables are used to store and manipulate data. Constants, on the other hand, are created using the `const` keyword and are used for values that should not be reassigned.

### Creating Variables:

#### 1. `var` (Avoid using `var` in modern JavaScript if possible):

```javascript
var myVariable = "Hello, World!";
```

#### 2. `let` (Block-scoped variable):

```javascript
let myVariable = "Hello, World!";
```

#### 3. `const` (Block-scoped constant, cannot be reassigned):

```javascript
const myConstant = 42;
```

### Examples:

```javascript
// Using var
var name = "John";
console.log(name); // Outputs: John

// Using let
let age = 25;
console.log(age); // Outputs: 25

// Using const
const pi = 3.14159;
console.log(pi); // Outputs: 3.14159

// Attempting to reassign a constant will result in an error
// Uncommenting the line below will cause an error
// pi = 3.14;
```

It's generally recommended to use `let` and `const` instead of `var`. `let` is preferable for variables that may be reassigned, while `const` is used for constants that should not be reassigned.

Keep in mind that `const` prevents the reassignment of the variable itself, but it doesn't make the value it holds immutable. For example, if you have a `const` object, you can still modify the properties of that object.

```javascript
const person = {
  name: "Alice",
  age: 30
};

// This is allowed, as it modifies the object property
person.age = 31;
console.log(person); // Outputs: { name: 'Alice', age: 31 }
```

If you want to create an immutable object, you may need to use additional techniques or libraries like Object.freeze().

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are differences between <code>var</code>, <code>const</code> and <code>let</code></b></summary><br>

The `var`, `let`, and `const` are all used for variable declarations in JavaScript, but they have some key differences in terms of scope, reassignment, and hoisting.

### 1. `var`:

- **Function-scoped:** Variables declared with `var` are function-scoped, meaning they are only visible within the function where they are declared. If declared outside any function, they become global.
  
- **Hoisting:** Variables declared with `var` are hoisted to the top of their scope. This means you can use a variable before it's declared, but the value will be `undefined`.

- **Reassignment:** Variables declared with `var` can be redeclared and reassigned.

### 2. `let`:

- **Block-scoped:** Variables declared with `let` are block-scoped, meaning they are only visible within the block (enclosed by curly braces) where they are declared. This includes if statements, for loops, and other block structures.

- **Hoisting:** Like `var`, variables declared with `let` are hoisted, but unlike `var`, they are not initialized. If you try to use the variable before its declaration, you'll get a `ReferenceError`.

- **Reassignment:** Variables declared with `let` can be reassigned, but not redeclared in the same scope.

### 3. `const`:

- **Block-scoped:** Like `let`, variables declared with `const` are block-scoped.

- **Hoisting:** Variables declared with `const` are hoisted, but like `let`, they are not initialized. You'll get a `ReferenceError` if you try to use the variable before its declaration.

- **Reassignment:** Variables declared with `const` cannot be reassigned. They must be assigned a value when declared, and this value cannot be changed.

### Example:

```javascript
// Example with var
function exampleVar() {
  if (true) {
    var x = 10;
  }
  console.log(x); // Outputs: 10
}

// Example with let
function exampleLet() {
  if (true) {
    let y = 20;
    console.log(y); // Outputs: 20
  }
  // Uncommenting the line below would result in a ReferenceError
  // console.log(y);
}

// Example with const
function exampleConst() {
  const z = 30;
  // Uncommenting the line below would result in a TypeError
  // z = 40;
  console.log(z); // Outputs: 30
}

// Example of hoisting with var
function hoistingExample() {
  console.log(a); // Outputs: undefined
  var a = 5;
  console.log(a); // Outputs: 5
}

// Example of hoisting with let/const
function hoistingExampleLetConst() {
  // Uncommenting the line below would result in a ReferenceError
  // console.log(b);
  let b = 10;
  console.log(b); // Outputs: 10
}
```

In modern JavaScript, it's generally recommended to use `let` and `const` over `var` due to their block-scoping behavior and fewer unexpected issues. Use `const` when you know the variable value should not be reassigned. Use `let` for variables that may be reassigned.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are all the data types available in JavaScript</b></summary><br>

JavaScript has several built-in data types, which can be categorized into two main groups: primitive data types and object types.

### Primitive Data Types:

1. **Undefined:**
   - Represents the absence of a value or an uninitialized variable.

   ```javascript
   let undefinedVar;
   console.log(undefinedVar); // Outputs: undefined
   ```

2. **Null:**
   - Represents the intentional absence of any object value.

   ```javascript
   let nullVar = null;
   console.log(nullVar); // Outputs: null
   ```

3. **Boolean:**
   - Represents a logical entity and can have two values: `true` or `false`.

   ```javascript
   let isTrue = true;
   let isFalse = false;
   ```

4. **Number:**
   - Represents numeric values, including integers and floating-point numbers.

   ```javascript
   let num = 42;
   let pi = 3.14;
   ```

5. **String:**
   - Represents sequences of characters and is enclosed in single or double quotes.

   ```javascript
   let str = "Hello, World!";
   ```

6. **Symbol (ES6 and later):**
   - Represents a unique identifier.

   ```javascript
   let sym = Symbol("uniqueSymbol");
   ```

### Object Types:

7. **Object:**
   - Represents a collection of key-value pairs and is a fundamental data structure in JavaScript.

   ```javascript
   let person = {
     name: "John",
     age: 30,
   };
   ```

8. **Array:**
   - Represents an ordered list of values and is a special type of object.

   ```javascript
   let colors = ["red", "green", "blue"];
   ```

9. **Function:**
   - Represents a reusable block of code.

   ```javascript
   function greet(name) {
     console.log("Hello, " + name + "!");
   }
   ```

### Special Data Types:

10. **BigInt (ES2020 and later):**
    - Represents integers of arbitrary precision.

    ```javascript
    let bigIntNum = BigInt(9007199254740991); // Note the "n" suffix is also possible.
    ```

11. **NaN (Not a Number):**
    - Represents a value that is not a legal number.

    ```javascript
    let notANumber = "hello" / 5;
    console.log(notANumber); // Outputs: NaN
    ```

12. **Infinity and -Infinity:**
    - Represents positive and negative infinity, respectively.

    ```javascript
    let positiveInfinity = Infinity;
    let negativeInfinity = -Infinity;
    ```

These are the fundamental data types in JavaScript. Keep in mind that JavaScript is a dynamically typed language, meaning variables can change their type at runtime. Understanding these data types is crucial for effective JavaScript programming.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the <code>if</code>, <code>if ... else</code> statements</b></summary><br>

In JavaScript, the `if` statement is used for conditional execution of code. It allows you to run a block of code only if a specified condition is true. The `if...else` statement extends this by allowing you to specify an alternative block of code to be executed if the condition is false.

### Using `if` Statement:

```javascript
let x = 10;

if (x > 5) {
  console.log("x is greater than 5");
}
```

In this example, the code inside the curly braces will only be executed if the condition `(x > 5)` is true.

### Using `if...else` Statement:

```javascript
let y = 3;

if (y > 5) {
  console.log("y is greater than 5");
} else {
  console.log("y is not greater than 5");
}
```

In this example, if the condition `(y > 5)` is true, the first block of code will be executed; otherwise, the block of code inside the `else` statement will be executed.

### Using `if...else if...else` Statement:

You can also chain multiple conditions using `else if` statements:

```javascript
let z = 7;

if (z < 5) {
  console.log("z is less than 5");
} else if (z === 5) {
  console.log("z is equal to 5");
} else {
  console.log("z is greater than 5");
}
```

In this example, the first condition checks if `z` is less than 5, the second condition checks if `z` is equal to 5, and the last block is executed if none of the previous conditions is true.

### Nesting `if` Statements:

You can also nest `if` statements within each other to create more complex conditional logic:

```javascript
let a = 10;
let b = 5;

if (a > 5) {
  if (b > 2) {
    console.log("Both conditions are true");
  } else {
    console.log("Inner condition is false");
  }
} else {
  console.log("Outer condition is false");
}
```

In this example, the inner `if` statement is nested within the outer `if` statement.

Remember that proper indentation is crucial for code readability, especially when dealing with nested `if` statements or other control structures.

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
<summary><b><a href=" "> </a>How to use while and for loops</b></summary><br>

In JavaScript, `while` and `for` loops are used for repetitive execution of a block of code. They allow you to iterate over a sequence of values or perform a task until a certain condition is met.

### `while` Loop:

The `while` loop repeats a block of code as long as a specified condition is true.

```javascript
let i = 0;

while (i < 5) {
  console.log(i);
  i++; // Increment the loop variable
}
```

In this example, the code inside the `while` loop will be executed repeatedly as long as the condition `(i < 5)` is true.

### `for` Loop:

The `for` loop provides a more concise way to write loops and includes the initialization, condition, and iteration in one line.

```javascript
for (let j = 0; j < 5; j++) {
  console.log(j);
}
```

The `for` loop has three parts:
- Initialization (`let j = 0`): Initializes the loop variable.
- Condition (`j < 5`): Specifies the condition for continuing the loop.
- Iteration (`j++`): Updates the loop variable after each iteration.

### Looping Through Arrays:

Both `while` and `for` loops can be used to iterate through arrays.

```javascript
let colors = ["red", "green", "blue"];

// Using while loop
let index = 0;
while (index < colors.length) {
  console.log(colors[index]);
  index++;
}

// Using for loop
for (let k = 0; k < colors.length; k++) {
  console.log(colors[k]);
}
```

### `for...of` Loop:

ES6 introduced the `for...of` loop, which is a more concise way to iterate over values in an iterable object, such as an array.

```javascript
let fruits = ["apple", "orange", "banana"];

for (let fruit of fruits) {
  console.log(fruit);
}
```

This loop directly iterates over the values of the array without the need for an index.

### `for...in` Loop:

The `for...in` loop is used to iterate over the properties of an object. However, it's generally not recommended for arrays due to potential issues with inherited properties.

```javascript
let person = { name: "John", age: 30 };

for (let key in person) {
  console.log(key + ": " + person[key]);
}
```

Be cautious with `for...in` when working with arrays, and consider using `for...of` instead.

Choose the appropriate loop based on your specific needs and the structure of the data you're working with.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use <code>break</code> and <code>continue</code> statements</b></summary><br>

In JavaScript, the `break` and `continue` statements are used within loops (such as `for` and `while` loops) to control the flow of the program.

### `break` Statement:

The `break` statement is used to exit a loop prematurely. When a `break` statement is encountered inside a loop, the loop is immediately terminated, and the program continues with the next statement after the loop.

Here's an example of using `break` in a `for` loop:

```javascript
for (let i = 0; i < 5; i++) {
    if (i === 3) {
        break; // exit the loop when i is 3
    }
    console.log(i);
}
```

In this example, the loop will print values `0`, `1`, and `2` to the console, but when `i` becomes `3`, the `break` statement is encountered, and the loop is terminated.

### `continue` Statement:

The `continue` statement is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration of the loop.

Here's an example of using `continue` in a `for` loop:

```javascript
for (let i = 0; i < 5; i++) {
    if (i === 2) {
        continue; // skip the rest of the loop body for i = 2
    }
    console.log(i);
}
```

In this example, the loop will print values `0`, `1`, `3`, and `4` to the console. When `i` is `2`, the `continue` statement is encountered, and the loop proceeds to the next iteration without executing the remaining code inside the loop body for that iteration.

Both `break` and `continue` statements can be used with `while` loops and other loop structures in a similar way. They provide flexibility in controlling the flow of your loops based on certain conditions.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What is a function and how do you use functions</b></summary><br>

In programming, a function is a reusable block of code that performs a specific task or set of tasks. Functions allow you to organize your code, make it more modular, and avoid duplicating code. In most programming languages, including JavaScript, functions are a fundamental building block.

Here's a basic overview of how functions work and how to use them in JavaScript:

### Function Declaration:

You can declare a function using the `function` keyword, followed by the function name and a pair of parentheses. If the function takes parameters, they are listed inside the parentheses. The function body is enclosed in curly braces `{}`.

```javascript
function greet(name) {
    console.log("Hello, " + name + "!");
}
```

In this example, `greet` is the function name, and it takes one parameter `name`.

### Function Invocation (Calling a Function):

To use a function, you "call" or "invoke" it. You do this by using the function name followed by parentheses. If the function takes parameters, you provide values for those parameters inside the parentheses.

```javascript
greet("John"); // Output: Hello, John!
```

### Return Statement:

Functions can also return values using the `return` statement. The `return` statement ends the execution of the function and specifies the value to be returned to the caller.

```javascript
function add(a, b) {
    return a + b;
}

let result = add(3, 5);
console.log(result); // Output: 8
```

### Function Expression:

Another way to create functions is through function expressions, where you assign a function to a variable.

```javascript
let multiply = function(x, y) {
    return x * y;
};

console.log(multiply(4, 7)); // Output: 28
```

### Arrow Functions (ES6+):

With ECMAScript 6 (ES6) and later versions, arrow functions provide a more concise syntax for creating functions.

```javascript
const square = (x) => {
    return x * x;
};

console.log(square(5)); // Output: 25
```

### Anonymous Functions:

Functions can also be anonymous, meaning they don't have a name. This is often used in situations like passing a function as an argument to another function.

```javascript
let printMessage = function() {
    console.log("This is an anonymous function.");
};

printMessage(); // Output: This is an anonymous function.
```

Functions are a crucial concept in programming, enabling you to structure your code, make it more readable, and reuse logic throughout your program. They help in achieving the DRY (Don't Repeat Yourself) principle by encapsulating reusable code into modular units.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What does a function that does not use any <code>return</code> statement return</b></summary><br>

In JavaScript, if a function does not explicitly use the `return` statement or if it ends without executing a `return` statement, it will return a special value called `undefined`. This is the default return value for functions that do not specify a return value.

Here's an example:

```javascript
function noReturn() {
    // This function does not have a return statement
}

let result = noReturn();
console.log(result); // Output: undefined
```

In this example, the function `noReturn` does not have a `return` statement, so when it is called and assigned to the variable `result`, the value of `result` becomes `undefined`.

It's important to note that even if a function doesn't explicitly use `return`, it still performs any side effects that might be present in the function body. Side effects could include modifying variables, printing to the console, or interacting with the DOM, among other things. The absence of a `return` statement doesn't mean the function does nothing; it just means it doesn't produce a specific value for the caller.

```javascript
function sideEffectFunction() {
    console.log("This function has a side effect");
}

let result = sideEffectFunction(); // Output: This function has a side effect
console.log(result); // Output: undefined
```

In this example, the function `sideEffectFunction` has a side effect (printing to the console), but it still returns `undefined` because there is no explicit `return` statement.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Scope of variables</b></summary><br>

JavaScript has two main types of scope for variables: global scope and local scope.

1. **Global Scope:**
   - Variables declared outside of any function or block have global scope.
   - They can be accessed from any part of the code, including functions.
   - Example:

     ```javascript
     var globalVariable = "I am global";

     function exampleFunction() {
         console.log(globalVariable); // Accessible within the function
     }

     exampleFunction();
     console.log(globalVariable); // Accessible outside the function
     ```

2. **Local Scope:**
   - Variables declared within a function have local scope.
   - They are only accessible within that function.
   - Example:

     ```javascript
     function exampleFunction() {
         var localVariable = "I am local";
         console.log(localVariable); // Accessible within the function
     }

     exampleFunction();
     // console.log(localVariable); // This would result in an error - not accessible outside the function
     ```

   - Variables declared using `let` and `const` within a block (inside curly braces `{}`) also have block scope. This means they are only accessible within that block.
  
     ```javascript
     if (true) {
         let blockVariable = "I am in a block";
         console.log(blockVariable); // Accessible within the block
     }

     // console.log(blockVariable); // This would result in an error - not accessible outside the block
     ```

3. **Function Scope (pre-ES6):**
   - Before ECMAScript 6 (ES6), JavaScript only had function scope.
   - Variables declared using `var` within a function are hoisted to the top of the function, meaning they can be accessed throughout the entire function, even before they are declared.
   - Example:

     ```javascript
     function exampleFunction() {
         console.log(variableBeforeDeclaration); // Outputs: undefined (due to hoisting)
         var variableBeforeDeclaration = "I am hoisted";
         console.log(variableBeforeDeclaration); // Outputs: I am hoisted
     }
     ```

   - It's important to note that `let` and `const` declarations have block scope and are not hoisted in the same way as `var`.

In modern JavaScript, it's recommended to use `let` and `const` for variable declarations to benefit from block scoping and to avoid unexpected behavior associated with hoisting in the case of `var`.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What are the arithmetic operators and how to use them</b></summary><br>

Arithmetic operators in JavaScript perform mathematical operations on numeric values. Here are the main arithmetic operators and how to use them:

1. **Addition (+):**
   - Adds two numbers.
   - Example:

     ```javascript
     let sum = 5 + 3; // sum is now 8
     ```

2. **Subtraction (-):**
   - Subtracts the right operand from the left operand.
   - Example:

     ```javascript
     let difference = 10 - 4; // difference is now 6
     ```

3. **Multiplication (*):**
   - Multiplies two numbers.
   - Example:

     ```javascript
     let product = 3 * 7; // product is now 21
     ```

4. **Division (/):**
   - Divides the left operand by the right operand.
   - Example:

     ```javascript
     let quotient = 15 / 3; // quotient is now 5
     ```

5. **Modulus (%):**
   - Returns the remainder of the division of the left operand by the right operand.
   - Example:

     ```javascript
     let remainder = 17 % 5; // remainder is now 2
     ```

6. **Exponentiation (**):**
   - Raises the left operand to the power of the right operand.
   - Example:

     ```javascript
     let result = 2 ** 3; // result is now 8
     ```

7. **Increment (++) and Decrement (--):**
   - Increment (++) adds 1 to a variable.
   - Decrement (--) subtracts 1 from a variable.
   - These can be used as either prefix or postfix operators.
   - Example:

     ```javascript
     let x = 5;
     x++; // x is now 6
     ```

     ```javascript
     let y = 8;
     y--; // y is now 7
     ```

   - When used as postfix, the original value is returned before the increment or decrement.

     ```javascript
     let a = 3;
     let b = a++; // a is now 4, b is 3
     ```

     ```javascript
     let c = 7;
     let d = c--; // c is now 6, d is 7
     ```

These arithmetic operators can be used in combination to create complex expressions. It's important to understand the order of operations (precedence) and use parentheses to control the order of evaluation when necessary. For example, `2 + 3 * 4` will result in 14 because multiplication has a higher precedence than addition. If you want the addition to be performed first, you can use parentheses: `(2 + 3) * 4`.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to manipulate dictionary</b></summary><br>

In JavaScript, there isn't a built-in "dictionary" type. Instead, you typically use objects to represent key-value pairs. Objects in JavaScript can be used as dictionaries because they allow you to associate keys with values. Here's how you can manipulate a dictionary-like object in JavaScript:

### Creating a Dictionary:

You can create a dictionary (object) by using curly braces `{}` and defining key-value pairs:

```javascript
let myDictionary = {
    key1: "value1",
    key2: "value2",
    key3: "value3"
};
```

### Accessing Values:

You can access the values in the dictionary using the keys:

```javascript
console.log(myDictionary.key1); // Output: value1
```

### Modifying Values:

You can modify the values associated with keys:

```javascript
myDictionary.key2 = "new value";
console.log(myDictionary.key2); // Output: new value
```

### Adding New Key-Value Pairs:

You can add new key-value pairs to the dictionary:

```javascript
myDictionary.key4 = "value4";
console.log(myDictionary.key4); // Output: value4
```

### Removing Key-Value Pairs:

You can remove key-value pairs using the `delete` keyword:

```javascript
delete myDictionary.key3;
console.log(myDictionary.key3); // Output: undefined
```

### Checking if a Key Exists:

You can check if a key exists in the dictionary:

```javascript
if ("key2" in myDictionary) {
    console.log("Key2 exists!");
} else {
    console.log("Key2 does not exist.");
}
```

### Iterating Over Keys:

You can iterate over the keys of the dictionary using a `for...in` loop:

```javascript
for (let key in myDictionary) {
    console.log(key + ": " + myDictionary[key]);
}
```

### Object Methods:

JavaScript objects come with some built-in methods that can be used to manipulate keys and values:

- `Object.keys(obj)`: Returns an array of a given object's own enumerable property names.
- `Object.values(obj)`: Returns an array of a given object's own enumerable property values.
- `Object.entries(obj)`: Returns an array of a given object's own enumerable property `[key, value]` pairs.

```javascript
let keys = Object.keys(myDictionary);
let values = Object.values(myDictionary);
let entries = Object.entries(myDictionary);

console.log(keys);    // Output: ["key1", "key2", "key4"]
console.log(values);  // Output: ["value1", "new value", "value4"]
console.log(entries); // Output: [["key1", "value1"], ["key2", "new value"], ["key4", "value4"]]
```

These methods can be helpful for more advanced manipulation and analysis of dictionaries (objects) in JavaScript. Keep in mind that the order of keys in an object is not guaranteed, so if order matters, you might need an additional data structure or a Map.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to import a file</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


# Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)

    [![JavaScript Style Guide](https://cdn.rawgit.com/standard/standard/master/badge.svg)](https://github.com/standard/standard)

- All your files must be executable
- The length of your files will be tested using `wc`

# More Info
### Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```bash
$ sudo npm install semistandard --global
```

# Quiz questions
<details>
<summary><h3>Question 0</h3></summary>

What does `const` mean? (please check all true answers)
- [x] It’s the keyword to define a constant variable
- [ ] It’s the keyword to define a variable that can be re-assign during the execution
- [ ] It’s the keyword to define a variable with optionally initializing it to a value
- [ ] It’s the keyword to define a global variable
- [x] It’s the keyword to define a variable in the local scope
</details>

<details>
<summary><h3>Question 1</h3></summary>

Does Javascript have `Set` as a native datatype?
- [x] No
- [ ] Yes
</details>

<details>
<summary><h3>Question 2</h3></summary>

Does Javascript have `Array` as a native datatype?
- [ ] No
- [x] Yes
</details>

<details>
<summary><h3>Question 3</h3></summary>

Does Javascript have Dictionary as a native datatype?
- [x] No
- [ ] Yes

> **Tips**: <br>Everything is `Object` and `Object` type in Javascript is powerful.
</details>

<details>
<summary><h3>Question 4</h3></summary>

What does let mean? (please check all true answers)
- [ ] It’s the keyword to define a constant variable
- [x] It’s the keyword to define a variable that can be re-assign during the execution
- [x] It’s the keyword to define a variable with optionally initializing it to a value
- [ ] It’s the keyword to define a global variable
- [x] It’s the keyword to define a variable in the local scope
</details>

<details>
<summary><h3>Question 5</h3></summary>

Does Javascript have `String` as a native datatype?
- [ ] No
- [x] Yes
</details>

# Tasks
<details>
<summary>

### 0. First constant, first print
`mandatory`

File: [0-javascript_is_amazing.js]()
</summary>

Write a script that prints "JavaScript is amazing":

- You must create a constant variable called `myVar` with the value "JavaScript is amazing"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
JavaScript is amazing
guillaume@ubuntu:~/0x12$
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 1. 3 languages
`mandatory`

File: [1-multi_languages.js]()
</summary>

Write a script that prints 3 lines:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 2. Arguments
`mandatory`

File: [2-arguments.js]()
</summary>

Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print "No argument"
- If only one argument is passed to the script, print "Argument found"
- Otherwise, print "Arguments found"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv)

```
guillaume@ubuntu:~/0x12$ ./2-arguments.js
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$

```

</details>

<details>
<summary>

### 3. Value of my argument
`mandatory`

File: [3-value_argument.js]()
</summary>

Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print "No argument"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`

```
guillaume@ubuntu:~/0x12$ ./3-value_argument.js
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 4. Create a sentence
`mandatory`

File: [4-concat.js]()
</summary>

Write a script that prints two arguments passed to it, in the following format: " is "

- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 5. An Integer
`mandatory`

File: [5-to_integer.js]()
</summary>

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can't be converted to an integer, print "Not a number"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

```
guillaume@ubuntu:~/0x12$ ./5-to_integer.js
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 6. Loop to languages
`mandatory`

File: [6-multi_languages_loop.js]()
</summary>

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop (`while`, `for`, etc.)

```
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 7. I love C
`mandatory`

File: [7-multi_c.js]()
</summary>

Write a script that prints `x` times "C is fun"

- Where `x` is the first argument of the script
- If the first argument can't be converted to an integer, print "Missing number of occurrences"
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (`while`, `for`, etc.)

```
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 8. Square
`mandatory`

File: [8-square.js]()
</summary>

Write a script that prints a square

- The first argument is the size of the square
- If the first argument can't be converted to an integer, print "Missing size"
- You must use the character `X` to print the square
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop (`while`, `for`, etc.)

```
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 9. Add
`mandatory`

File: [9-add.js]()
</summary>

Write a script that prints the addition of 2 integers

- The first argument is the first integer
- The second argument is the second integer
- You have to define a function with this prototype: `function add(a, b)`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ ./9-add.js
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 10. Factorial
`mandatory`

File: [10-factorial.js]()
</summary>

Write a script that computes and prints a factorial

- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- You must do it recursively
- You must use a function
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ ./10-factorial.js
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 11. Second biggest!
`mandatory`

File: [11-second_biggest.js]()
</summary>

Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer
- If no argument passed, print `0`
- If the number of arguments is 1, print `0`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 12. Object
`mandatory`

File: [12-object.js]()
</summary>

Update this script to replace the value `12` with `89`:

- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 13. Add file
`mandatory`

File: [13-add.js]()
</summary>

Write a function that returns the addition of 2 integers.

- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`

[Tip](https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

```
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 14. Const or not const
`#advanced`

File: [100-let_me_const.js]()
</summary>

Write a file that modifies the value of `myVar` to `333`

```
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$
```

Do you get it? Tweet! Post! Talk about it!

Hint: Scope

**This exercise doesn't pass `semistandard`** so don't worry about it.
</details>

<details>
<summary>

### 15. Call me Moby
`#advanced`

File: [101-call_me_moby.js]()
</summary>

Write a function that executes `x` times a function.

- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 16. Add me maybe
`#advanced`

File: [102-add_me_maybe.js]()
</summary>

Write a function that increments and calls a function.

- The function must be visible from outside
- Prototype: `function (number, theFunction)`
- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$

```
</details>

<details>
<summary>

### 17. Increment object
`#advanced`

File: [103-object_fct.js]()
</summary>

Update this script by adding a new function `incr` that increments the integer `value`.

- You are not allowed to use `var`

```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$

```
</details>