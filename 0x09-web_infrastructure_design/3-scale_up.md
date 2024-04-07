# Infrastructure Readme

## Overview
This setup runs our web application smoothly. It has servers for handling web pages, running the application, and storing data. A load balancer splits traffic between servers to keep everything running smoothly.

## Components

### 1. Web Server
- **Purpose**: Serves web pages to users.
- **Added**: To separate web content for better organization and security.

### 2. Application Server
- **Purpose**: Runs the application's complex processes.
- **Added**: To keep application logic separate from web content for efficiency and security.

### 3. Database Server
- **Purpose**: Stores and manages application data.
- **Added**: To keep data organized and easily scalable.

### 4. Load Balancer (HAProxy)
- **Purpose**: Distributes traffic evenly among servers.
- **Added**: To ensure reliability and responsiveness by avoiding server overload.

## Specifics

### Why Split Components?
- **Efficiency**: Each component can focus on its specific task.
- **Security**: Reduces risk by isolating different parts of the system.

### Why Load Balancer (HAProxy)?
- **Traffic Distribution**: Prevents server overload by evenly distributing traffic.
- **High Availability**: Ensures the system keeps running even if one load balancer fails.
- **Scalability**: Easily handles increased traffic by adding more servers.

### Why Separate Web and Application Servers?
- **Resource Isolation**: Prevents one part from affecting the performance of the other.
- **Flexibility**: Allows scaling each part independently based on demand.
- **Security**: Reduces the risk of security breaches by isolating application logic.

### Why Dedicated Database Server?
- **Performance**: Ensures efficient data storage and management.
- **Data Integrity**: Keeps data safe and organized.
- **Scalability**: Easily scales up storage capacity as the website grows.
