// Here we will tell where routes are etc etc

package main

import (
	"bookstore_project/package/routes"
	"log"
	"net/http"

	"github.com/gorilla/mux"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

func main() {
	r := mux.NewRouter()
	routes.RegisterBookStoreRoutes(r) // we have function RegisterBookStoreRoutes in routes package (folder) and we are passing
	// router it using "r"
	http.Handle("/", r)
	log.Fatal(http.ListenAndServe(":9010", r))
}
