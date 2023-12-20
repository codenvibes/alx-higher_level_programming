<h1 align="center"><b>0x14. JAVASCRIPT - WEB SCRAPING</b></h1>
<div align="center"><code>Scripting</code> <code>API</code> <code>JavaScript</code></div>

<!-- <br>

## Background Context -->

<br>

## Resources
<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON">Working with JSON data</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319">The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://github.com/request/request ">request module</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://github.com/mbeaudru/modern-js-cheatsheet">Modern JS</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!-- <br>

**man or help:**
- `` -->

<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>Why JavaScript programming is amazing</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to manipulate JSON data</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use <code>request</code> and fetch API</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to read and write a file using <code>fs</code> module</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

<br>

## More Info

### Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
<br>

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```
<br>

### Install `request` module and use it
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).


<br>

## Tasks
<details>
<summary>

### 0. Readme
`mandatory`

File: [0-readme.js]()
</summary>

Write a script that reads and prints the content of a file.
- The first argument is the file path
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the error object
```
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 
```
</details>

<details>
<summary>

### 1. Write me
`mandatory`

File: [1-writeme.js]()
</summary>

Write a script that writes a string to a file.
- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in `utf-8`
- If an error occurred during while writing, print the error object
```
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$
```
</details>

<details>
<summary>

### 2. Status code
`mandatory`

File: [2-statuscode.js]()
</summary>

Write a script that display the status code of a `GET` request.
- The first argument is the URL to request (`GET`)
- The status code must be printed like this: `code: <status code>`
- You must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
```
</details>

<details>
<summary>

### 3. Star wars movie title
`mandatory`

File: [3-starwars_title.js]()
</summary>

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
- The first argument is the movie ID
- You must use the [Star wars API](https://swapi-api.alx-tools.com/) with the endpoint https://swapi-api.alx-tools.com/api/films/:id
- You must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 
```
</details>

<details>
<summary>

### 4. Star wars Wedge Antilles
`mandatory`

File: [4-starwars_count.js]()
</summary>

Write a script that prints the number of movies where the character “Wedge Antilles” is present.
- The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
- You must use the module request
```
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
guillaume@ubuntu:~/0x14$ 
```
</details>

<details>
<summary>

### 5. Loripsum
`mandatory`

File: [5-request_store.js]()
</summary>


</details>

<details>
<summary>

### 6. How many completed?
`mandatory`

File: [6-completed_tasks.js]()
</summary>


</details>

<details>
<summary>

### 7. Who was playing in this movie?
`#advanced`

File: [100-starwars_characters.js]()
</summary>


</details>

<details>
<summary>

### 8. Right order
`#advanced`

File: [101-starwars_characters.js]()
</summary>


</details>

