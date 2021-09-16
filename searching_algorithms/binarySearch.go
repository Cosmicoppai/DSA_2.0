package main

import "fmt"

func binarySearch(arr []int, target int) int {
	var start = 0
	var end = len(arr) - 1
	for start <= end {
		var mid = start + (end - start) //2
		if arr[mid] == target {
			return mid
		}
		if arr[mid] > target {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return -1

}
func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
	fmt.Println(binarySearch(arr, 9))
	fmt.Println(binarySearch(arr, 15))
}
