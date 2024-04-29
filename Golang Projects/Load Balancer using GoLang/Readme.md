\# Simple Load Balancer in Go

This is a simple implementation of a load balancer in Go, which distributes incoming HTTP requests among a list of backend servers.

\## Overview

The load balancer consists of two main components:

1. **Server**: Represents a backend server that the load balancer forwards requests to.
2. **LoadBalancer**: Distributes incoming requests among the available backend servers.

\## Installation and Usage

1. Clone the repository:

   \```bash
   git clone https://github.com/your/repo.git
   \```

2. Navigate to the project directory:

   \```bash
   cd your-project-directory
   \```

3. Build and run the Go program:

   \```bash
   go run main.go
   \```

   This will start the load balancer on the specified port (default: 8000) and begin forwarding requests to the backend servers.

\## Configuration

You can configure the load balancer by modifying the `main.go` file:

- `servers`: Define the list of backend servers by creating instances of `simpleServer` with their respective addresses.
- `NewLoadBalancer`: Configure the load balancer by providing the port number and the list of backend servers.
