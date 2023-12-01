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

An HTTP (Hypertext Transfer Protocol) response is a message sent by a server to a client (such as a web browser) in response to an HTTP request. It contains information about the status of the request and may also include the requested data or indicate an error. The response is a crucial part of the request-response cycle that forms the basis of communication on the World Wide Web.

An HTTP response typically includes the following components:

1. **Status Line:** The status line includes the HTTP version, a numeric status code, and a human-readable status message. For example:
   ```
   HTTP/1.1 200 OK
   ```

   - The status code "200" indicates a successful request.
   - The status message "OK" provides a brief description of the status.

2. **Headers:** Headers provide additional information about the server's response, such as content type, content length, server information, caching directives, and more. Examples include:
   ```
   Content-Type: text/html
   Content-Length: 1234
   ```

3. **Body:** The body of the response contains the actual data being sent by the server. For example, if the request was for an HTML page, the body would contain the HTML code. The presence and nature of the body depend on the request method and the specific endpoint on the server.

Here's a basic example of an HTTP response:

```http
HTTP/1.1 200 OK
Date: Tue, 30 Nov 2023 12:00:00 GMT
Content-Type: text/html
Content-Length: 1234

<!DOCTYPE html>
<html>
<head>
  <title>Example Page</title>
</head>
<body>
  <h1>Hello, World!</h1>
</body>
</html>
```

In this example:

- The status line indicates a successful response with a status code of "200 OK."
- Headers provide information about the content type, length, and the date of the response.
- The body contains an HTML document with a simple "Hello, World!" message.

HTTP responses allow the client to understand the outcome of its request and process the received data accordingly. Status codes in the response provide information about whether the request was successful, redirected, or encountered an error.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What HTTP headers are</b></summary><br>

HTTP headers are metadata elements in an HTTP (Hypertext Transfer Protocol) request or response that provide additional information about the communication between the client (typically a web browser) and the server. Headers convey information about the data being sent, the server, the client, the request itself, and other aspects of the communication. Headers are key-value pairs included in the HTTP message, where each header consists of a name and a value separated by a colon.

HTTP headers are divided into two main categories: request headers and response headers.

### Request Headers:

1. **Host:** Specifies the domain name or IP address of the server.
   ```
   Host: www.example.com
   ```

2. **User-Agent:** Identifies the user agent (e.g., web browser) making the request.
   ```
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
   ```

3. **Accept:** Informs the server about the types of content that the client can understand.
   ```
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
   ```

4. **Authorization:** Contains credentials for authenticating the client with the server.
   ```
   Authorization: Basic base64encodedcredentials
   ```

5. **Referer:** Indicates the address of the previous web page from which the link to the currently requested page was followed.
   ```
   Referer: https://www.example.com/previous-page
   ```

### Response Headers:

1. **Content-Type:** Specifies the media type of the resource sent in the response.
   ```
   Content-Type: text/html; charset=utf-8
   ```

2. **Content-Length:** Indicates the size of the response body in octets (8-bit bytes).
   ```
   Content-Length: 1234
   ```

3. **Server:** Identifies the server software used by the origin server.
   ```
   Server: Apache/2.4.38 (Unix) OpenSSL/1.1.1d
   ```

4. **Set-Cookie:** Sets a cookie on the client's browser for tracking or session management.
   ```
   Set-Cookie: user_id=12345; expires=Wed, 30 Nov 2023 12:00:00 GMT; path=/; domain=.example.com
   ```

5. **Location:** Used in redirections or responses that include a new location for the requested resource.
   ```
   Location: https://www.example.com/new-location
   ```

These examples represent just a small subset of the many headers used in HTTP communication. Different headers serve various purposes, and they contribute to the efficiency, security, and functionality of the communication between clients and servers on the web.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What the HTTP message body is</b></summary><br>

The HTTP message body is the part of an HTTP request or response that carries the data being sent between the client and the server. While HTTP headers provide metadata and instructions about the request or response, the message body contains the actual content, which could be HTML, JSON, binary data, or any other format depending on the nature of the communication.

### In an HTTP Request:

For HTTP requests, the message body is used to send data from the client to the server. The presence and format of the body depend on the request method and the specific requirements of the endpoint on the server.

1. **GET Request:** Typically, GET requests do not have a message body. Data is sent through the URL parameters.

   ```http
   GET /path/to/resource?param1=value1&param2=value2 HTTP/1.1
   Host: www.example.com
   ```

2. **POST Request:** POST requests often include a message body, used to send data to the server. This is common when submitting forms or uploading files.

   ```http
   POST /submit-form HTTP/1.1
   Host: www.example.com
   Content-Type: application/x-www-form-urlencoded

   username=user123&password=pass456
   ```

### In an HTTP Response:

For HTTP responses, the message body contains the actual content that the server is sending back to the client in response to a request.

1. **HTML Response:**

   ```http
   HTTP/1.1 200 OK
   Content-Type: text/html
   Content-Length: 1234

   <!DOCTYPE html>
   <html>
   <head>
     <title>Example Page</title>
   </head>
   <body>
     <h1>Hello, World!</h1>
   </body>
   </html>
   ```

2. **JSON Response:**

   ```http
   HTTP/1.1 200 OK
   Content-Type: application/json
   Content-Length: 45

   {"message": "Data successfully retrieved", "status": "success"}
   ```

3. **Binary Data Response:**

   ```http
   HTTP/1.1 200 OK
   Content-Type: image/jpeg
   Content-Length: 56789

   [binary data]
   ```

The content type and length are often specified in the headers to help the client understand how to interpret and process the message body. The structure and format of the message body depend on the media type specified in the `Content-Type` header.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP request method is</b></summary><br>

An HTTP request method is a verb or command used by a client (such as a web browser) to indicate the desired action to be performed on a resource identified by a given URI (Uniform Resource Identifier). The HTTP request method defines the nature of the operation that the client is requesting from the server. Each HTTP request method corresponds to a specific set of actions, and the server processes the request based on the indicated method.

Common HTTP request methods include:

1. **GET:** The GET method is used to retrieve information from the server. It requests a representation of a specified resource without altering the state of the server or the resource.

   ```http
   GET /path/to/resource HTTP/1.1
   Host: www.example.com
   ```

2. **POST:** The POST method is used to submit data to be processed to a specified resource. It is often used when submitting forms or uploading files.

   ```http
   POST /submit-form HTTP/1.1
   Host: www.example.com
   Content-Type: application/x-www-form-urlencoded

   username=user123&password=pass456
   ```

3. **PUT:** The PUT method is used to update a resource or create a new resource if it does not exist at the specified URI.

   ```http
   PUT /update-resource HTTP/1.1
   Host: www.example.com
   Content-Type: application/json

   {"newData": "updated content"}
   ```

4. **DELETE:** The DELETE method is used to request the removal of a resource identified by the URI.

   ```http
   DELETE /delete-resource HTTP/1.1
   Host: www.example.com
   ```

5. **HEAD:** The HEAD method is similar to GET but is used to retrieve the headers of a resource without the actual body content. It is often used to check the status of a resource.

   ```http
   HEAD /check-resource HTTP/1.1
   Host: www.example.com
   ```

6. **OPTIONS:** The OPTIONS method is used to describe the communication options for the target resource.

   ```http
   OPTIONS /options-resource HTTP/1.1
   Host: www.example.com
   ```

These are just a few examples of HTTP request methods. Each method serves a specific purpose and is designed to perform a particular type of action on the identified resource. The method is an essential part of the HTTP request and plays a key role in determining how the server should process the client's request.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP response status code is</b></summary><br>

An HTTP response status code is a three-digit numeric code returned by a web server in response to an HTTP request made by a client (typically a web browser or other user agent). The status code is a part of the HTTP response and provides information about the success, failure, or other conditions of the requested operation. The status code is included in the first line of the HTTP response and is followed by a brief, human-readable status message.

HTTP status codes are grouped into five classes, each represented by the first digit of the status code:

1. **1xx (Informational):** The request was received, continuing process.
   - Example: `100 Continue` (The server has received the request headers and the client should proceed to send the request body.)

2. **2xx (Successful):** The request was successfully received, understood, and accepted.
   - Example: `200 OK` (The request was successful.)

3. **3xx (Redirection):** Further action needs to be taken to complete the request.
   - Example: `301 Moved Permanently` (The requested resource has been permanently moved to a new location.)

4. **4xx (Client Error):** The request contains bad syntax or cannot be fulfilled by the server.
   - Example: `404 Not Found` (The server cannot find the requested resource.)

5. **5xx (Server Error):** The server failed to fulfill a valid request.
   - Example: `500 Internal Server Error` (A generic error message indicating that the server has encountered a situation it doesn't know how to handle.)

Common HTTP status codes include:

- `200 OK`: The request was successful.
- `201 Created`: The request has been fulfilled, resulting in the creation of a new resource.
- `204 No Content`: The server successfully processed the request but there is no additional content to send in the response.
- `400 Bad Request`: The request cannot be fulfilled due to bad syntax or other client-side errors.
- `401 Unauthorized`: The client must authenticate itself to get the requested response.
- `403 Forbidden`: The client does not have the necessary permission to access the requested resource.
- `404 Not Found`: The server cannot find the requested resource.
- `500 Internal Server Error`: A generic error message indicating that the server has encountered a situation it doesn't know how to handle.

Status codes provide valuable information about the outcome of an HTTP request, allowing the client to understand whether the request was successful, if redirection is needed, or if an error occurred. They are crucial for troubleshooting and diagnosing issues in web communication.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What an HTTP Cookie is</b></summary><br>

An HTTP cookie (often just called a "cookie") is a small piece of data stored by a user's web browser on their device, which is sent between the client (browser) and the server in the HTTP header of a request and response. Cookies serve various purposes, including session management, personalization, tracking, and maintaining stateful information between HTTP transactions.

Here are some key characteristics and uses of HTTP cookies:

1. **State Management:** Cookies are commonly used to maintain stateful information across multiple requests from the same client. This is particularly useful for tracking user sessions on a website.

2. **Session Cookies:** These cookies are temporary and are stored only during a user's session. They are deleted when the user closes their browser.

3. **Persistent Cookies:** Persistent cookies are stored on a user's device for a specified duration, even after the browser is closed. They are useful for retaining user preferences or login information across multiple sessions.

4. **Authentication:** Cookies can be used to authenticate users. When a user logs in, a server may issue a session cookie to keep the user logged in until they log out or the session expires.

5. **Personalization:** Cookies can store information about a user's preferences, language, and other personalized settings to enhance the user experience.

6. **Tracking and Analytics:** Cookies are often used for tracking user behavior and collecting analytics data. This information can be used to analyze website traffic and improve content and services.

7. **Cross-Site Request Forgery (CSRF) Protection:** Cookies can be configured with security attributes to mitigate CSRF attacks by ensuring that requests originate from the same site.

8. **Cross-Site Scripting (XSS) Protection:** Properly implemented cookie attributes can enhance protection against certain types of XSS attacks.

A typical HTTP response header that sets a cookie might look like this:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: user_id=12345; expires=Wed, 30 Nov 2023 12:00:00 GMT; path=/; domain=.example.com
```

In this example, a cookie named "user_id" is set with a value of "12345." It will expire on a specific date, has a specified path, and is valid for a specific domain.

It's important to note that while cookies are widely used for legitimate purposes, they also raise privacy concerns. Browsers often provide settings for users to control cookie storage and may implement mechanisms such as SameSite attributes to enhance user privacy and security. Additionally, web developers need to be mindful of how they handle and secure cookies to prevent potential vulnerabilities.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>How to make a request with cURL</b></summary><br>

cURL (short for Client for URLs) is a command-line tool and library for making HTTP requests and working with URLs. It supports a wide range of protocols, including HTTP, HTTPS, FTP, FTPS, SCP, LDAP, and more. Here's a basic example of how to make an HTTP GET request using cURL:

```bash
curl https://www.example.com
```

This command sends a GET request to `https://www.example.com` and outputs the response to the terminal.

Here are some common options you might use with cURL:

- **Specify Request Method:**
  ```bash
  curl -X POST https://www.example.com
  ```

- **Include Headers:**
  ```bash
  curl -H "Content-Type: application/json" https://www.example.com
  ```

- **Pass Data in the Request Body:**
  ```bash
  curl -X POST -d '{"key":"value"}' -H "Content-Type: application/json" https://www.example.com
  ```

- **Follow Redirects:**
  ```bash
  curl -L https://www.example.com
  ```

- **Save Response to a File:**
  ```bash
  curl -o output.html https://www.example.com
  ```

- **Include Verbose Output:**
  ```bash
  curl -v https://www.example.com
  ```

These are just a few examples. The `curl` command is highly versatile, and you can customize it based on your specific needs.

cURL is available on various operating systems, including Linux, macOS, and Windows (using tools like Git Bash or Windows Subsystem for Linux). Make sure you have cURL installed on your system before using these commands.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>What happens when you type google.com in your browser (Application level)</b></summary><br>

1. **Browser Processes Request:**
   - When you press Enter, your browser starts processing the request. It checks if the requested URL is valid and then proceeds to parse the URL.

2. **DNS Resolution:**
   - The browser checks its DNS cache for the IP address associated with "google.com." If not found or if the cache has expired, the browser queries a DNS server to obtain the IP address.

3. **Establishing a TCP Connection:**
   - Using the obtained IP address, the browser initiates a TCP connection to the Google server. This involves a three-way handshake: SYN, SYN-ACK, and ACK.

4. **HTTP Request:**
   - The browser constructs an HTTP GET request for the "/" resource on the Google server. The request may include additional headers, such as user-agent information, to inform the server about the type of client making the request.

5. **Server Receives Request:**
   - The Google server receives the HTTP request and processes it. It identifies the requested resource ("/" in this case) and begins preparing the response.

6. **Server Generates HTTP Response:**
   - The server generates an HTTP response containing the requested resource (HTML content for the Google homepage). It includes headers such as Content-Type, Content-Length, and others.

7. **Sending HTTP Response:**
   - The server sends the HTTP response back to the browser over the established TCP connection.

8. **Browser Receives Response:**
   - The browser receives the HTTP response. It begins processing the response headers to determine the content type and length.

9. **HTML Parsing:**
   - The browser parses the HTML content received in the response. It identifies additional resources (stylesheets, scripts, images) referenced in the HTML and initiates requests for these resources.

10. **Fetching Additional Resources:**
    - The browser makes separate HTTP requests for the additional resources identified in the HTML. These requests happen concurrently for performance optimization.

11. **Rendering the Page:**
    - As resources are fetched, the browser starts rendering the Google homepage. It constructs the Document Object Model (DOM) and renders the visual representation of the page.

12. **Displaying the Page:**
    - The rendered page is displayed in the browser window, showing the Google homepage with its search bar and other elements.

Throughout this process, various optimizations, such as caching and compression, may be employed to enhance performance. Additionally, if Google is using HTTPS, the communication between the browser and server is encrypted, adding a layer of security to the data exchange.

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

In the following URL, what’s the resource path?
```
https://api.google.com/v1/auth/new
```
- [x] v1/auth/new
- [ ] v1/auth/new/index.html
- [ ] v1/auth
- [ ] v1
</details>

<details>
<summary><h3>Question 1</h3></summary>

What is the `curl` option to follow all redirects?
- [x] -L
- [ ] -X
- [ ] -s
</details>

<details>
<summary><h3>Question 2</h3></summary>

What’s the status code number for an invalid HTTP request (server can’t understand it)?
- [x] 400
- [ ] 404
- [ ] 500
</details>

<details>
<summary><h3>Question 3</h3></summary>

In the following URL, what’s the name of the parameter in the query string?
```
https://www.google.com/apply?batch=89
```
- [ ] 89
- [ ] apply
- [x] batch
</details>

<details>
<summary><h3>Question 4</h3></summary>

In this following HTML code, which HTTP verb will be used when you will submit this form?
```
<FORM action="/12/update.php" method="put">
    <INPUT type="text" name="first_name" value="Bob"/>
    <INPUT type="text" name="last_name" value="Dylan"/>
    <INPUT type="submit" name="update" value="Update" />
<FORM>
```
- [ ] POST
- [x] PUT
- [ ] UPDATE
- [ ] GET
</details>

<details>
<summary><h3>Question 5</h3></summary>

What is the first digit of status codes that indicate a server error?
- [ ] 4xx
- [x] 5xx
- [ ] 3xx
- [ ] 2xx
- [ ] 1xx
</details>

<details>
<summary><h3>Question 6</h3></summary>

What is the name of the HTTP response header used to define the size, in bytes, of the body of the response?
- [ ] Length
- [x] Content-Length
- [ ] Content-Size
- [ ] Body-Size
</details>

<details>
<summary><h3>Question 7</h3></summary>

What is the name of the HTTP response header used to define the formatting of the body? (This header gives details to the client on how to interpret the data received.)
- [ ] Format
- [x] Content-Type
- [ ] Content-Format
- [ ] Type
</details>

<details>
<summary><h3>Question 8</h3></summary>

In the following URL, what’s the sub domain?
```
https://api.google.com/v1/auth
```
- [x] api
- [ ] api.google
- [ ] .com
</details>

<details>
<summary><h3>Question 9</h3></summary>

What is the `curl` option to save the body of the resulting response to a file?
- [ ] -r
- [x] -o
- [ ] -b
- [ ] -d
</details>

<details>
<summary><h3>Question 10</h3></summary>

What is the `curl` option that defines the HTTP method used?
- [ ] -s
- [x] -X
- [ ] -d
</details>

<details>
<summary><h3>Question 11</h3></summary>

What’s the status code number for a web page that can’t be found?
- [ ] 500
- [ ] 405
- [x] 404
</details>

<details>
<summary><h3>Question 12</h3></summary>

Which `curl` option is used to set an HTTP header to a specific value?
- [ ] -s
- [ ] -X
- [x] -H
</details>

<details>
<summary><h3>Question 13</h3></summary>

What will be the port number requested by this URL?
```
https://www.google.com:8080/apply
```
- [ ] 8888
- [x] 8080
- [ ] 80
</details>

<details>
<summary><h3>Question 14</h3></summary>

Which HTTP request header indicates the browser used by the client sending the request?
- [ ] I-Am
- [ ] Browser-Name
- [x] User-Agent
- [ ] Origin
</details>

<details>
<summary><h3>Question 15</h3></summary>

In the following URL, what’s the protocol?
```
http://www.google.com
```
- [ ] ftp
- [ ] https
- [x] http
</details>

<details>
<summary><h3>Question 16</h3></summary>

What’s the status code number for a permanent redirection (moved permanently)?
- [ ] 302
- [ ] 304
- [x] 301
- [ ] 300
- [ ] 201
</details>

<details>
<summary><h3>Question 17</h3></summary>

In the following URL, how many parameters are in the query string?
```
https://www.google.com/apply?batch=89&location=SF
```
- [ ] 1
- [ ] 3
- [x] 2
</details>

<details>
<summary><h3>Question 18</h3></summary>

What is the name of the HTTP request header used to send cookies from the client?
- [x] Cookie
- [ ] Cookies
- [ ] Send-Cookie
- [ ] Set-Cookie
</details>

<details>
<summary><h3>Question 19</h3></summary>

What is the name of the HTTP request header that defines the size (in bytes) of the message body?
- [ ] Content-Size
- [ ] Size
- [ ] Length
- [x] Content-Length
</details>

<details>
<summary><h3>Question 20</h3></summary>

When you are typing `https://intranet.hbtn.io` in your browser, which HTTP verb is used?
- [x] GET
- [ ] PUT
- [ ] DELETE
- [ ] POST
</details>

<details>
<summary><h3>Question 21</h3></summary>

What is the `curl` option to set a body key-value parameter?
- [x] -d
- [ ] -X
- [ ] -b
</details>

<details>
<summary><h3>Question 22</h3></summary>

What will be the port number requested by this URL?
```
http://www.google.com/apply
```
- [ ] 443
- [ ] 22
- [x] 80
- [ ] 8080
</details>

<details>
<summary><h3>Question 23</h3></summary>

In the following URL, what’s the resource path?
```
https://www.google.com/assets/scripts/main.js
```
- [ ] assets/scripts
- [ ] main.js
- [x] assets/scripts/main.js
</details>

<details>
<summary><h3>Question 24</h3></summary>

In the following URL, what’s the sub domain?
```
https://api-dev.google.com/v1/auth/new
```
- [ ] /v1
- [ ] /v1/auth/new
- [x] api-dev
</details>

<details>
<summary><h3>Question 25</h3></summary>

When an HTTP response indicates a redirection, which header defines the URL the client should be redirected to?
- [ ] Redirect-Location
- [ ] Redirect
- [ ] Next-Location
- [x] Location
- [ ] Redirect-URI
</details>

<details>
<summary><h3>Question 26</h3></summary>

What is the name of the HTTP response header used to send cookies to the client from the server?
- [ ] Cookie-Setter
- [x] Set-Cookie
- [ ] Send-Cookies
</details>

<details>
<summary><h3>Question 27</h3></summary>

What is the `curl` option to set a cookie with a key-value pair?
- [ ] -a
- [ ] -c
- [x] -b
- [ ] -d
</details>

<details>
<summary><h3>Question 28</h3></summary>

In the following URL, what’s the resource path?
```
https://www.google.com/index.html
```
- [ ] www.google.com/index.html
- [x] index.html
- [ ] /
</details>

<details>
<summary><h3>Question 29</h3></summary>

What is the name of the HTTP response header used to define the status code of the response?
- [ ] Code
- [ ] Http-Status
- [ ] Status-Code
- [x] Status
</details>

<details>
<summary><h3>Question 30</h3></summary>

In this following HTML code, which HTTP verb will be used when you will submit this form?
```
<FORM action="/login.php" method="post">
    <INPUT type="email" name="email" placeholder="Email" required/>
    <INPUT type="password" name="password" placeholder="Password" required/>
    <INPUT type="submit" name="submit" value="Login" />
<FORM>
```
- [ ] ENTER
- [ ] GET
- [ ] SUBMIT
- [ ] FORM
- [x] POST
</details>

<details>
<summary><h3>Question 31</h3></summary>

What will be the port number requested by this URL?
```
afp://www.google.com/access_in_port_543
```
- [x] 548
- [ ] 80
- [ ] 543
</details>

<details>
<summary><h3>Question 32</h3></summary>

What is the name of the HTTP response header that defines a list of available HTTP methods for this URL?
- [ ] Verbs-Allowed
- [x] Allow
- [ ] Verbs
</details>

<details>
<summary><h3>Question 33</h3></summary>

What is the `curl` option to disable the progression display?
- [ ] -b
- [ ] -p
- [ ] -c
- [x] -s
</details>

<details>
<summary><h3>Question 34</h3></summary>

In the following URL, what’s the hostname?
```
http://www.google.com
```
- [x] www.google.com
- [ ] www.google
- [ ] google.com
- [ ] google
</details>

<details>
<summary><h3>Question 35</h3></summary>

In the following URL, how many parameters are in the query string?
```
https://www.google.com/apply?batch=89&location=SF&name=John%20do%20is%20the%20best%20%3D%20c%20is%20fun
```
- [ ] 4
- [ ] 5
- [ ] 1
- [ ] 2
- [x] 3
</details>

<br>

## Tasks
<details>
<summary>

### 0. cURL body size
`mandatory`

File: [0-body_size.sh]()
</summary>

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 1. cURL to the end
`mandatory`

File: [1-body.sh]()
</summary>

Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
- Display only body of a `200` status code response
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 2. cURL Method
`mandatory`

File: [2-delete.sh]()
</summary>

Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 3. cURL only methods
`mandatory`

File: [3-methods.sh]()
</summary>

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 4. cURL headers
`mandatory`

File: [4-header.sh]()
</summary>

Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
- A header variable `X-School-User-Id` must be sent with the value 98
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 5. cURL POST parameters
`mandatory`

File: [5-post_params.sh]()
</summary>

Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
- A variable `email` must be sent with the value `test@gmail.com`
- A variable `subject` must be sent with the value `I will always be here for PLD`
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 6. Find a peak
`mandatory`

File: [6-peak.py](), [6-peak.txt]()
</summary>

**Technical interview preparation:**
- You are not allowed to google anything
- Whiteboard first

Write a function that finds a **peak** in a list of unsorted integers.
- Prototype: `def find_peak(list_of_integers):`
- You are not allowed to import any module
- Your algorithm must have the lowest complexity *(hint: you don’t need to go through all numbers to find a peak)*
- `6-peak.py` must contain the function
- `6-peak.txt` must contain the complexity of your algorithm: `O(log(n)), O(n), O(nlog(n))` or `O(n2)`
- **Note**: there may be more than one peak in the list
```
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 7. Only status code
`#advanced`

File: [100-status_code.sh]()
</summary>

Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
- You are not allowed to use any pipe, redirection, etc.
- You are not allowed to use `;` and `&&`
- You have to use `curl`

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 8. cURL a JSON file
`#advanced`

File: [101-post_json.sh]()
</summary>

Write a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.

- Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
- You have to use `curl`

Please test your scripts in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_1
I'm a JSON! really!
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
```
</details>

<details>
<summary>

### 9. Catch me if you can!
`#advanced`

File: [102-catch_me.sh]()
</summary>

Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.

- You have to use `curl`
- You are not allow to use `echo`, `cat`, etc. to display the final result

Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./102-catch_me.sh ; echo ""
You got me!
guillaume@ubuntu:~/0x10$ 
```
</details>

