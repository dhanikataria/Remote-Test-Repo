package main

import (
	"log"
	"net/http"
)

func python_code_Handler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/python_code" {
		http.Error(w, "404 not found", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "method not supported", http.StatusNotFound)
	}
	http.ServeFile(w, r, "./static/python_code.txt")

}

func CyberAwareness_Game_Handler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/cyberawareness_game" {
		http.Error(w, "404 not found", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "method not supported", http.StatusNotFound)
	}
	http.ServeFile(w, r, "./static/CyberAwareness_Game")
}

func golang_code_Handler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "./static/code.txt")
}

func main() {

	fileserver := http.FileServer(http.Dir("./static"))
	http.Handle("/", fileserver)
	http.HandleFunc("/python_code", python_code_Handler)
	http.HandleFunc("/cyberawareness_game", CyberAwareness_Game_Handler)
	http.HandleFunc("/golang_code", golang_code_Handler)

	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal(err)
	}
}
