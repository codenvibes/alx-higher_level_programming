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

A domain name is a human-readable label or address that is used to identify and locate resources on the internet. It serves as a more user-friendly alternative to the numeric IP addresses that computers use to communicate with each other. Domain names are an integral part of the Domain Name System (DNS), which is a hierarchical and decentralized naming system for computers, services, or other resources connected to the internet.

Here are key components and characteristics of a domain name:

1. **Top-Level Domain (TLD):** This is the last part of a domain name, such as ".com," ".org," ".net," or country code TLDs like ".uk," ".ca," etc. TLDs categorize and provide some context to the website's purpose or origin.

2. **Second-Level Domain (SLD):** This is the part of the domain name that comes before the TLD. For example, in the domain name "example.com," "example" is the second-level domain.

3. **Subdomain:** A subdomain is a domain that is part of a larger domain. For instance, in "blog.example.com," "blog" is a subdomain of "example.com."

4. **Fully Qualified Domain Name (FQDN):** This is the complete domain name, including all levels and the TLD. For example, "www.example.com" is a fully qualified domain name.

5. **Domain Registration:** To use a specific domain name, individuals or organizations must register it through accredited domain registrars. Registration is typically done on an annual basis, and domain owners have the option to renew their registration.

6. **Domain Name System (DNS):** The DNS translates human-readable domain names into IP addresses that computers use to identify each other on the internet. When you type a domain name into a web browser, the DNS resolves it to the corresponding IP address, allowing your browser to connect to the desired server.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What a sub-domain is</b></summary><br>

A subdomain is a domain that is part of a larger domain. In a hierarchical domain structure, a subdomain is created by adding a prefix to the main or root domain. The main purpose of subdomains is to organize and structure websites into distinct sections or categories.

For example, consider the URL: `https://blog.example.com`

In this case:
- The main domain is `example.com`.
- The subdomain is `blog`, and it is prefixed to the main domain.

Here are some key points about subdomains:

1. **Organization:** Subdomains are often used to organize and categorize content within a larger website. For instance, a company might use subdomains for different departments or services, such as `sales.example.com` or `support.example.com`.

2. **Technical Separation:** Subdomains can be associated with different servers or server configurations, allowing for technical separation of content and functionality. This can be useful for scaling and managing different parts of a website independently.

3. **Distinct Content:** Each subdomain can have its own unique content and resources. For example, a blog hosted on `blog.example.com` might have different content than the main website hosted on `www.example.com`.

4. **Common Subdomains:**
   - **www:** Historically used to denote the 'World Wide Web' and often used as the default for websites (e.g., `www.example.com`).
   - **blog:** Used for blogs (e.g., `blog.example.com`).
   - **shop:** Used for online stores (e.g., `shop.example.com`).
   - **mail:** Used for email services (e.g., `mail.example.com`).

5. **DNS Configuration:** Subdomains are configured through DNS (Domain Name System) settings. The DNS records for a subdomain are typically set up to point to the same or a different IP address than the main domain.

It's important to note that while subdomains share the same root domain, they are considered separate entities in terms of configuration and content.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to define a port number in a URL</b></summary><br>

In a URL, the port number is specified using a colon followed by the port number after the domain or IP address. The general syntax is:

```
protocol://domain:port/path
```

Here's a breakdown of the components:

- **Protocol:** This is typically "http" or "https" for web URLs.
- **Domain:** This is the domain name or IP address of the server.
- **Port:** This is the port number to use for the connection.
- **Path:** This is the specific resource or location on the server.

For example, if you have a web server running on port 8080, the URL might look like this:

```
http://example.com:8080/path/to/resource
```

In this example:

- **Protocol:** "http"
- **Domain:** "example.com"
- **Port:** "8080"
- **Path:** "/path/to/resource"

If the port is not specified in the URL, the browser will default to using the standard port for the given protocol (e.g., 80 for HTTP, 443 for HTTPS). If a different port is used, it needs to be explicitly mentioned in the URL.

It's worth noting that certain ports are associated with specific protocols by default. For example:

- HTTP typically uses port 80.
- HTTPS typically uses port 443.

When accessing a resource on the web, most URLs omit the port number if the default port for the protocol is being used. If a non-default port is used, it must be specified in the URL to ensure that the client connects to the correct port on the server.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What a query string is</b></summary><br>

A query string is a part of a URL (Uniform Resource Locator) that is used to pass and transmit data between a web browser and a web server. It is located after the path of the URL and is preceded by a question mark "?". The query string is a set of key-value pairs, where each pair is separated by an ampersand "&".

The general structure of a URL with a query string looks like this:

```
https://www.example.com/path/to/resource?name1=value1&name2=value2&name3=value3
```

In this example:

- The URL is `https://www.example.com/path/to/resource`.
- The query string starts with a question mark and includes key-value pairs separated by ampersands.

Each key-value pair in the query string represents a parameter and its corresponding value. These parameters are typically used to provide additional information to the server, such as search terms, filters, or any other data relevant to the request.

For instance, in the URL `https://www.example.com/search?query=web&page=1`, the query string includes two parameters:

- `query`: This parameter has the value "web," indicating a search query.
- `page`: This parameter has the value "1," indicating the page number of the search results.

On the server side, web applications and scripts can parse the query string to extract and process these parameters, enabling dynamic and customized content based on user input.

It's important to note that while the query string is a convenient way to transmit data, sensitive information, such as passwords, should not be included in the query string for security reasons. Instead, sensitive data is typically transmitted using other methods, such as through the request body in a POST request.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP request is</b></summary><br>

An HTTP (Hypertext Transfer Protocol) request is a message sent by a client (typically a web browser) to a server, requesting a specific action or resource. HTTP is the protocol used for communication on the World Wide Web, and it operates as a request-response protocol. When you type a URL into your web browser and press Enter, or when you click a link, your browser generates an HTTP request to the server hosting the requested resource.

An HTTP request consists of several components:

1. **Request Method:** The request method or verb indicates the action to be performed by the server. Common HTTP methods include:
   - **GET:** Retrieve data from the server (typically used for fetching web pages).
   - **POST:** Submit data to be processed to a specified resource.
   - **PUT:** Update a resource on the server.
   - **DELETE:** Request the removal of a resource.
   - And others like HEAD, OPTIONS, PATCH, etc.

2. **URL (Uniform Resource Locator):** The URL specifies the address of the resource the client is requesting.

3. **Headers:** Headers provide additional information about the request or the client making the request. Examples include information about the client's capabilities, preferred content types, authentication credentials, and more.

4. **Body (for some methods):** The request body contains data that is sent to the server, usually with methods like POST or PUT. For example, when submitting a form on a website, the form data is included in the request body.

Here's a basic example of an HTTP request:

```http
GET /path/to/resource HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
```

In this example:

- The method is `GET`.
- The URL is `/path/to/resource`.
- Headers include the host, user-agent information, and accepted content types.

Once the server receives this request, it processes it and sends back an HTTP response, which contains the requested resource or information about the outcome of the request. The interaction between HTTP clients and servers is fundamental to how information is exchanged on the web.

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

