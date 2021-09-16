package main

import "fmt"

func linearSearch(arr []int, target int) int {
	for i := 0; i < len(arr); i++ {
		if arr[i] == target {
			return i
		}
		// continue

	}
	return -1

}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	arr1 := []int{10, 20, 30, 40, 50, 60, 70, 80}
	fmt.Println(linearSearch(arr, 7), linearSearch(arr1, 100))
}
