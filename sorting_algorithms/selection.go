package main

import "fmt"

func selectionSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] > arr[j] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}

	}
	return arr
}
func main() {
	arr := []int{5, 4, 3, 2, 1, 0}
	fmt.Println(selectionSort(arr))
}
