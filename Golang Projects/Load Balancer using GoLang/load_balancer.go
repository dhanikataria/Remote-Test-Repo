package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
	"net/url"
	"os"
)

type simpleServer struct {
	addr  string
	proxy *httputil.ReverseProxy
}

type Server interface {
	Address() string
	IsAlive() bool
	Serve(rw http.ResponseWriter, r *http.Request)
}

func newSimpleServer(addr string) *simpleServer { // initialize a new server

	serverUrl, err := url.Parse(addr) // Parse strings are used to parse strings which are url.
	handleErr(err)

	return &simpleServer{
		addr:  addr,
		proxy: httputil.NewSingleHostReverseProxy(serverUrl), /*  This function creates a new reverse proxy that forwards HTTP requests
		to the URL specified in serverUrl */
	}
}

type LoadBalancer struct {
	port            string
	roundRobinCount int
	servers         []Server
}

func NewLoadBalancer(port string, servers []Server) *LoadBalancer {
	return &LoadBalancer{
		port:            port,
		roundRobinCount: 0,
		servers:         servers,
	}

}
func handleErr(err error) {
	if err != nil {
		fmt.Printf("error: %v\n", err)
		os.Exit(1)
	}
}

func (s *simpleServer) Address() string { return s.addr }

func (s *simpleServer) IsAlive() bool { return true }

func (s *simpleServer) Serve(rw http.ResponseWriter, req *http.Request) {
	s.proxy.ServeHTTP(rw, req)
}

func (lb *LoadBalancer) getNextAvailabelServer() Server {
	server := lb.servers[lb.roundRobinCount%len(lb.servers)]
	for !server.IsAlive() {
		lb.roundRobinCount++
		server = lb.servers[lb.roundRobinCount%len(lb.servers)]

	}
	lb.roundRobinCount++
	return server
}

func (lb *LoadBalancer) serveProxy(rw http.ResponseWriter, req *http.Request) {
	targetServer := lb.getNextAvailabelServer()
	fmt.Println("forwarding request to ", targetServer.Address())
	targetServer.Serve(rw, req)
}

func main() {
	servers := []Server{
		newSimpleServer("https://www.facebook.com"),
		newSimpleServer("http://www.bing.com"),
		newSimpleServer("http://www.duckduckgo.com"),
	}
	lb := NewLoadBalancer("8000", servers)
	handleRedirect := func(rw http.ResponseWriter, req *http.Request) {
		lb.serveProxy(rw, req)
	}
	http.HandleFunc("/", handleRedirect)
	fmt.Print("serving reqs")
	http.ListenAndServe(":"+lb.port, nil)
}
