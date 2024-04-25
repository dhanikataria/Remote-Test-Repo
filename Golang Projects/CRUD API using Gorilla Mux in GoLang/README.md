# CRUD API in GoLang

This is a simple CRUD (Create, Read, Update, Delete) API implementation in GoLang using the Gorilla Mux router.

## Features

- Create, Read, Update, and Delete operations for managing resources.
- RESTful API endpoints for interacting with the resources.
- JSON format for data exchange.
- Error handling for various scenarios.

## Requirements

- GoLang installed on your system.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Run the application:

    ```bash
    go run main.go
    ```

4. The API server should now be running on `http://localhost:8080`.

## Usage

- Use an API client like Postman or curl to interact with the API endpoints.
- Below are the available endpoints:

    - **GET /movies**: Get all movies.
    - **GET /movies/{id}**: Get a movie by ID.
    - **POST /movies**: Create a new movie.
    - **PUT /movies/{id}**: Update a movie by ID.
    - **DELETE /movies/{id}**: Delete a movie by ID.

## Example

- Create a new movie:
  
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title":"New Movie","director":"Director Name","year":2024}' http://localhost:8080/movies
    ```

- Get all movies:

    ```bash
    curl http://localhost:8080/movies
    ```

- Get a movie by ID:

    ```bash
    curl http://localhost:8080/movies/1
    ```

- Update a movie by ID:

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Movie Title","director":"New Director","year":2025}' http://localhost:8080/movies/1
    ```

- Delete a movie by ID:

    ```bash
    curl -X DELETE http://localhost:8080/movies/1
    ```

