### Description
Design of Three-Server Web Infrastructure for www.foobar.com:**

1. **Server 1: Web Server (Nginx)**
   - Purpose: Handles incoming HTTP requests and serves static content efficiently.
   - Configuration: Nginx is optimized for high concurrency and can handle a large number of simultaneous connections, making it suitable for serving web content.

2. **Server 2: Application Server**
   - Purpose: Executes dynamic code, processes requests, and generates dynamic content for the website.
   - Configuration: Hosts the application codebase (e.g., Python Django, Node.js, etc.) responsible for generating dynamic pages and handling user interactions.

3. **Server 3: Load Balancer (HAproxy)**
   - Purpose: Distributes incoming traffic across multiple servers to ensure high availability and scalability.
   - Configuration: HAproxy is configured with round-robin distribution algorithm, ensuring that each server receives an equal share of incoming requests. This algorithm works by sequentially distributing requests to each server in turn.

4. **Application Files**
   - Purpose: Contains the codebase responsible for generating dynamic content and processing user requests.
   - Configuration: Hosted on the application server, these files include scripts, templates, stylesheets, and other assets required to run the website.

5. **Database (MySQL)**
   - Purpose: Stores website data, including user accounts, content, and configurations.
   - Configuration: MySQL is configured as a Primary-Replica (Master-Slave) cluster, where the Primary node handles all write operations and replicates data to one or more Replica nodes for read operations.

**Explanation of Specifics:**

- **Load Balancer Distribution Algorithm:** Round-robin distribution ensures that each server receives an equal share of incoming requests, distributing the load evenly across the infrastructure.

- **Active-Active vs. Active-Passive Setup:** In an Active-Active setup, all servers actively handle incoming requests simultaneously, providing redundancy and load distribution. In contrast, an Active-Passive setup designates one server as active while others remain passive, ready to take over in case of failure. Our infrastructure employs Active-Active setup to maximize resource utilization and minimize downtime.

- **Database Primary-Replica Cluster:** In this setup, the Primary node manages write operations, ensuring data consistency and integrity. Replica nodes replicate data from the Primary node and handle read operations, distributing the load and improving read performance.

- **Difference Between Primary and Replica Nodes:** The Primary node is responsible for handling write operations, ensuring that data modifications are consistent across the database cluster. Replica nodes, on the other hand, serve read requests, providing scalable read access to the database without impacting the Primary node's performance.

**Issues with the Infrastructure:**

1. **Single Points of Failure (SPOF):**
   - The absence of redundant components (e.g., single load balancer, single database) poses a risk of downtime if any of these components fail.

2. **Security Issues:**
   - Lack of firewall protection exposes servers to potential attacks and unauthorized access.
   - Absence of HTTPS encryption leaves data transmitted between clients and servers vulnerable to interception and manipulation.

3. **No Monitoring:**
   - Without monitoring tools, it's challenging to detect and address performance issues, security breaches, or system failures proactively. Monitoring solutions are essential for maintaining the health and security of the infrastructure.
