package main

import (
	"fmt"
)

func factorial(number int) int {
	if number == 0 || number == 1 {
		return 1
	}
	if number < 0 {
		fmt.Println("Enter Non Negative Number")
		return -1
	}
	return number * factorial(number-1)
}

func main() {
	numberList := []int{1, 2, 3, 4, 10, 15, 25, 50, -1}
	for i := 0; i < len(numberList); i++ {
		fmt.Println(factorial(numberList[i]))
	}
}
