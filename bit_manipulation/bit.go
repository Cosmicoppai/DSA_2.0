package main

import (
	"fmt"
)

// Given a number find if it's odd or even

func oddOrEven(n int) bool { // if the number is even return true else false
	if n&1 == 0 { // the even number have 0 at the last bit, so 00000001 & nnnnnnn0 will give 0 else it'll give 1
		return true
	} else {
		return false
	}

}

// given an array every number appears twice except one, find that number

func findDoutei(arr []int) int {
	n := 0
	for i := 0; i < len(arr); i++ {
		n = n ^ arr[i]
	}
	return n

}
func main() {
	fmt.Println(oddOrEven(3))
	fmt.Println(oddOrEven(6))
	arr := []int{1, 1, 2, 2, 5, 5, 9, 11, 12, 12, 11}
	fmt.Println(findDoutei(arr), findDoutei([]int{1, 1, 0}))
}
