### Description
Designing a Single Server Web Infrastructure for www.foobar.com. this is an unsecure infrastructure with no scaling and load balancing.

#### Scenario
A user wants to access www.foobar.com.

#### Infrastructure Components:

1. **Server:**
   - A physical or virtual machine where all components of the web infrastructure reside.
   - It has an IP address 8.8.8.8.

2. **Web Server (Nginx):**
   - Receives and responds to HTTP requests from users' browsers.
   - Serves static content and forwards dynamic requests to the application server.
   - Nginx is commonly used for its high performance and efficiency in serving static content.

3. **Application Server:**
   - Executes the application logic and generates dynamic content based on user requests.
   - Interfaces with the web server to process requests and deliver responses.
   - Common choices include Apache with mod_php or uWSGI with Django or Flask for Python applications.

4. **Application Files (Code Base):**
   - The actual codebase of the website/application.
   - Contains scripts, stylesheets, templates, and other assets necessary for the functioning of the website.

5. **Database (MySQL):**
   - Stores and manages data required by the application.
   - MySQL is a popular choice for relational databases due to its reliability, scalability, and robust feature set.

#### Specifics Explanation:

- **Server:**
  - The server is the physical or virtual machine that hosts the entire web infrastructure. It's where all software components and data reside.

- **Domain Name:**
  - The domain name (foobar.com) is a human-readable alias for the server's IP address (8.8.8.8). It allows users to access the website using a memorable name instead of an IP address.

- **DNS Record for www:**
  - The "www" in www.foobar.com is a subdomain, and the DNS record for it is typically a CNAME (Canonical Name) record pointing to the main domain (foobar.com) or an A record pointing directly to the server's IP address.

- **Web Server:**
  - The web server (Nginx) handles incoming HTTP requests from users' browsers, serves static content directly, and forwards dynamic requests to the application server for processing.

- **Application Server:**
  - The application server executes the actual codebase, generating dynamic content based on user requests. It communicates with the web server to receive and respond to requests.

- **Database:**
  - The database (MySQL) stores and manages structured data required by the application. It allows for efficient storage, retrieval, and manipulation of data needed by the website.

- **Communication with Users' Computers:**
  - The server communicates with users' computers over the internet using the HTTP protocol. When a user requests www.foobar.com, their browser sends an HTTP request to the server, which then processes the request and sends back an HTTP response with the requested content.

#### Issues with the Infrastructure:

1. **Single Point of Failure (SPOF):**
   - Since all components are hosted on a single server, if the server goes down for any reason (hardware failure, software issue, etc.), the entire website becomes inaccessible.

2. **Downtime during Maintenance:**
   - When maintenance tasks, such as deploying new code or updating server configurations, are required, the web server typically needs to be restarted. During this time, the website may experience downtime, causing inconvenience to users.

3. **Limited Scalability:**
   - With only one server hosting the entire infrastructure, it's challenging to scale the website to handle a significant increase in incoming traffic. As traffic grows, the server may become overloaded, leading to performance issues or downtime.
