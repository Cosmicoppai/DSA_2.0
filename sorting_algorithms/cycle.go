package main

import "fmt"

func cycleSort(arr []int) []int {
	i := 0
	for i < len(arr) {
		indexCurrElem := arr[i]
		if indexCurrElem == i {
			i += 1
			continue
		}
		arr[indexCurrElem], arr[i] = arr[i], arr[indexCurrElem]
	}
	return arr
}

func main() {
	arr := []int{5, 4, 3, 2, 1, 0}
	fmt.Println(cycleSort(arr))
}
