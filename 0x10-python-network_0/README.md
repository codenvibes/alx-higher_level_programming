<h1 align="center"><b>0x10. PYTHON - NETWORK #0</b></h1>
<div align="center"><code>Bash</code> <code>Python</code> <code>Scripting</code> <code>Back-end</code> <code>API</code></div>

<!-- <br>

## Background Context -->

<br>

## Resources
<details>
<summary><b><a href="https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html">HTTP (HyperText Transfer Protocol)</a> (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies">HTTP Cookies</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!-- **man or help:**
- `` -->

<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>What a URL is</b></summary><br>

A URL, or Uniform Resource Locator, is a reference or address used to access resources on the internet. It's a string of characters that provides the means to locate and retrieve a particular resource, such as a web page, a document, an image, or a file. URLs are used in web browsers to navigate the World Wide Web.

A standard URL typically consists of several components:

1. **Scheme:** This specifies the protocol used to access the resource. Common examples include "http," "https," "ftp," etc.

2. **Host:** This identifies the domain or server where the resource is located. For example, in the URL "https://www.example.com," "www.example.com" is the host.

3. **Path:** This indicates the specific location or file on the server. For instance, in the URL "https://www.example.com/page/index.html," "/page/index.html" is the path.

4. **Query Parameters:** These are additional parameters or data that can be appended to the URL to provide information to the server. They are separated from the rest of the URL by a question mark (?).

5. **Fragment Identifier:** This refers to a specific section within the resource. It is indicated by a hash symbol (#) followed by an anchor name.

Here's an example of a URL with all its components:

```
https://www.example.com/path/to/resource?name=value#section
```

In this example:
- **Scheme:** "https"
- **Host:** "www.example.com"
- **Path:** "/path/to/resource"
- **Query Parameters:** "?name=value"
- **Fragment Identifier:** "#section"

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What HTTP is</b></summary><br>

HTTP stands for Hypertext Transfer Protocol. It is the foundation of any data exchange on the Web and is a protocol used for transmitting hypermedia documents, such as HTML. It is an application layer protocol designed within the framework of the Internet Protocol Suite.

Key features and aspects of HTTP include:

1. **Client-Server Model:** HTTP operates in a client-server model, where a client (e.g., a web browser) makes requests for resources and a server provides those resources.

2. **Stateless Protocol:** HTTP is a stateless protocol, meaning each request from a client to a server is independent, and the server does not retain any information about the client's previous requests.

3. **Connectionless:** Each request from the client is processed independently of previous requests, and the connection between the client and server is typically closed after each request/response cycle.

4. **Text-Based:** HTTP messages (requests and responses) are text-based, making them human-readable. These messages consist of headers and, optionally, a message body.

5. **Request Methods:** HTTP defines several request methods or verbs, such as GET, POST, PUT, DELETE, etc., which indicate the action to be performed on the identified resource.

6. **Status Codes:** HTTP responses include status codes indicating the result of the request (e.g., 200 OK for a successful request, 404 Not Found for a resource that could not be found, etc.).

7. **URLs:** HTTP uses URLs to identify resources on the web. URLs, as discussed in the previous answer, specify the location of the resource to be requested.

8. **Versioning:** HTTP has gone through various versions, with HTTP/1.1 being one of the widely used versions. HTTP/2 and HTTP/3 are subsequent versions that aim to improve performance and address certain limitations.

9. **Security:** HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP that uses encryption (TLS/SSL) to secure the data exchanged between the client and server.

HTTP is the protocol that facilitates the communication between web browsers and servers, enabling the retrieval and display of web content. As web technologies have evolved, newer versions of the HTTP protocol have been developed to address performance, security, and other considerations.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to read a URL</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>The scheme for a HTTP URL</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What a domain name is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What a sub-domain is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to define a port number in a URL</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What a query string is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP request is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP response is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What HTTP headers are</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What the HTTP message body is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP request method is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP response status code is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP Cookie is</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to make a request with cURL</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What happens when you type google.com in your browser (Application level)</b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<br>

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (`wc -l file` should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly `#!/bin/bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All `curl` commands must have the option `-s` (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- The first line of all your Python files should be exactly `#!/usr/bin/python3`
- Your code should use the pycodestyle (version `2.8.*`)
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

<!-- ## More Info -->

<br>

## Quiz questions
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

<details>
<summary><h3>Question 14</h3></summary>


</details>

<details>
<summary><h3>Question 15</h3></summary>


</details>

<details>
<summary><h3>Question 16</h3></summary>


</details>

<details>
<summary><h3>Question 17</h3></summary>


</details>

<details>
<summary><h3>Question 18</h3></summary>


</details>

<details>
<summary><h3>Question 19</h3></summary>


</details>

<details>
<summary><h3>Question 20</h3></summary>


</details>

<details>
<summary><h3>Question 21</h3></summary>


</details>

<details>
<summary><h3>Question 22</h3></summary>


</details>

<details>
<summary><h3>Question 23</h3></summary>


</details>

<details>
<summary><h3>Question 24</h3></summary>


</details>

<details>
<summary><h3>Question 25</h3></summary>


</details>

<details>
<summary><h3>Question 26</h3></summary>


</details>

<details>
<summary><h3>Question 27</h3></summary>


</details>

<details>
<summary><h3>Question 28</h3></summary>


</details>

<details>
<summary><h3>Question 29</h3></summary>


</details>

<details>
<summary><h3>Question 30</h3></summary>


</details>

<details>
<summary><h3>Question 31</h3></summary>


</details>

<details>
<summary><h3>Question 32</h3></summary>


</details>

<details>
<summary><h3>Question 33</h3></summary>


</details>

<details>
<summary><h3>Question 34</h3></summary>


</details>

<details>
<summary><h3>Question 35</h3></summary>


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
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 8. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 9. 
`#advanced`

File: []()
</summary>


</details>

