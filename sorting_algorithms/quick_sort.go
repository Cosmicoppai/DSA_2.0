package main

import "fmt"

// Flight - a struct that
// contains information about flights
type Flight struct {
	Origin      string
	Destination string
	Price       int
}

// SortByPrice sorts flights from highest to lowest
func SortByPrice(flights []Flight) []Flight {
	return sort(flights, 0, len(flights)-1)
}

func sort(flights []Flight, start int, end int) []Flight {
	if start >= end {
		return flights
	}
	pi := partition(flights, start, end)
	sort(flights, pi+1, end)
	sort(flights, start, pi-1)
	return flights
}

func partition(flights []Flight, start int, end int) int {
	i := start
	pep := flights[end].Price
	for j := start; j < end; j++ {
		if flights[j].Price <= pep {
			flights[i], flights[j] = flights[j], flights[i]
			i += 1
		}
	}
	flights[i], flights[end] = flights[end], flights[i]
	return i
}

func printFlights(flights []Flight) {
	for _, flight := range flights {
		fmt.Printf("-> Origin: %s, Destination: %s, Price: %d \n", flight.Origin, flight.Destination, flight.Price)
	}
}

func main() {
	// an empty slice of flights
	var flights []Flight

	var price = 30000
	for i := 0; i < 6; i++ {
		flight := Flight{Origin: "Mumbai", Destination: "Tokyo", Price: price}
		flights = append(flights, flight)
		price += 5000
	}

	sortedList := SortByPrice(flights)
	printFlights(sortedList)
}
