
- **cmd**: Contains the main executable file (`main.go`) responsible for starting the application.
- **package**: Contains various modules for different parts of the application:
  - **config**: Configures the database connection.
  - **controllers**: Defines HTTP handlers for different endpoints.
  - **models**: Defines the data models for performing database operations using GORM tags.
  - **routes**: Registers API routes and associates them with controller functions. This file contains the routes from where the user will hit from the fronthand (Postman)

## Dependencies

- `github.com/jinzhu/gorm`: GORM library for Object-Relational Mapping.
- `github.com/gorilla/mux`: Gorilla Mux router for HTTP routing.

## Database Setup

Ensure that MySQL is installed and running on your system. Update the database connection details (e.g., username, password, database name) in `config/app.go` file.

## Running the Application

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/bookstore_project.git
    ```

2. Navigate to the project directory:

    ```
    cd bookstore_project
    ```

3. Build and run the application:

    ```
    go run cmd/main.go
    ```

## API Endpoints

- `GET /books`: Retrieve all books.
- `GET /books/{id}`: Retrieve a book by ID.
- `POST /books`: Create a new book.
- `DELETE /books/{id}`: Delete a book by ID.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
