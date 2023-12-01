<h1 align="center"><b>0x11. PYTHON - NETWORK #1</b></h1>
<div align="center"><code>Python</code> <code>Scripting</code> <code>Back-end</code> <code>API</code></div>

<!-- <br>

## Background Context -->

<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/howto/urllib2.html">HOWTO Fetch Internet Resources Using urllib Package</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://requests.readthedocs.io/en/latest/">HOWTO Fetch Internet Resources Using urllib Package</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://pypi.org/project/requests/">Requests package</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!-- **man or help:**
- `` -->

<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>How to fetch internet resources with the Python package <code>urllib</code></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to decode <code>urllib</code> body response</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to use the Python package <code>requests</code> #requestsiswaysimplerthanurllib</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to make HTTP <code>GET</code> request</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to make HTTP <code>POST</code>/<code>PUT</code>/etc. request</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to fetch JSON resources</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to manipulate data from an external service</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

<!-- ## More Info -->

<br>

## Tasks
<details>
<summary>

### 0. What's my status? #0
`mandatory`

File: [0-hbtn_status.py]()
</summary>

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`
- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before `-`)
- You must use a `with` statement
```
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$
```
</details>

<details>
<summary>

### 1. Response header value #0
`mandatory`

File: [1-hbtn_header.py]()
</summary>

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
- You must use the packages `urllib` and `sys`
- You are not allow to import packages other than `urllib` and `sys`
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement
```
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 
```
</details>

<details>
<summary>

### 2. POST an email #0
`mandatory`

File: [2-post_email.py]()
</summary>

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)
- The email must be sent in the `email` variable
- You must use the packages `urllib` and `sys`
- You are not allowed to import packages other than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
```
</details>

<details>
<summary>

### 3. Error code #0
`mandatory`

File: [3-error_code.py]()
</summary>

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).
- You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
- You must use the packages `urllib` and `sys`
- You are not allowed to import other packages than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
```
</details>

<details>
<summary>

### 4. What's my status? #1
`mandatory`

File: [4-hbtn_status.py]()
</summary>

Write a Python script that fetches https://alx-intranet.hbtn.io/status
- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following example (tabulation before -)
```
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
```
</details>

<details>
<summary>

### 5. Response header value #1
`mandatory`

File: [5-hbtn_header.py]()
</summary>


</details>

<details>
<summary>

### 6. POST an email #1
`mandatory`

File: [6-post_email.py]()
</summary>


</details>

<details>
<summary>

### 7. Error code #1
`mandatory`

File: [7-error_code.py]()
</summary>


</details>

<details>
<summary>

### 8. Search API
`mandatory`

File: [8-json_api.py]()
</summary>


</details>

<details>
<summary>

### 9. My GitHub!
`mandatory`

File: [10-my_github.py]()
</summary>


</details>

<details>
<summary>

### 10. Time for an interview!
`#advanced`

File: [100-github_commits.py]()
</summary>


</details>

