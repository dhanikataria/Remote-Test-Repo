package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"github.com/gorilla/mux"
)

type movie struct {
	ID    string `json:"id"`
	Isbn  string `json:"isbn"`
	Title string `json:"title"`
}

func getmovies(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(movies)
}

func deletemovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)

	for index, value := range movies {
		if value.ID == params["id"] {
			movies = append(movies[:index], movies[index+1:]...) //deleting the movie at index
		}

	}
	json.NewEncoder(w).Encode(movies)
}

func getmovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	for _, value := range movies {
		if value.ID == params["id"] {
			json.NewEncoder(w).Encode(value)
			return
		}
	}
}

func createmovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	bodybytes, _ := io.ReadAll(r.Body)
	var temp movie
	json.Unmarshal(bodybytes, &temp) //Json sent from POSTMAN is decoded here and value is stored in movie
	fmt.Printf("%+v", temp)
	movies = append(movies, temp)
	json.NewEncoder(w).Encode(temp)
}

var movies []movie

func main() {

	movies = append(movies, movie{ID: "1", Isbn: "abc", Title: "Terminator"})
	movies = append(movies, movie{ID: "2", Isbn: "123", Title: "Pulp Fiction"})

	r := mux.NewRouter()
	r.HandleFunc("/movies", getmovies).Methods("GET")
	r.HandleFunc("/movies/{id}", getmovie).Methods("GET") // in Gorilla Mux, URL Parameters are defined in {}
	r.HandleFunc("/movies", createmovie).Methods("POST")

	r.HandleFunc("/movies/{id}", deletemovie).Methods("DELETE")

	http.ListenAndServe(":8080", r)

}
