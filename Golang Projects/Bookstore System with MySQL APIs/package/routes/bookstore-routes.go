// Includes the routes where the user will hit from frontend such as POSTMAN

package routes

import (
	"bookstore_project/package/controllers" //

	"github.com/gorilla/mux"
)

var RegisterBookStoreRoutes = func(r *mux.Router) { // var RegisterBooksStoreRoutes is assigned an anonymous function which received
	// "r" router from main.go in cmd folder/package

	r.HandleFunc("/book", controllers.GetBook).Methods("GET") //controllers.getbooks -> because my handlers are in controllers package
	r.HandleFunc("/book", controllers.CreateBook).Methods("POST")
	r.HandleFunc("/book/{bookid}", controllers.GetBookById).Methods("GET")
	r.HandleFunc("/book/{bookid}", controllers.DeleteBook).Methods("DELETE")

}
