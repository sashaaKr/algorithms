package main

import (
	"fmt"
	"os"
	"strconv"
)

func gcd(m int, n int) int {
	if m < n {
		return gcd(n, m)
	}
	if n == 0 {
		return m
	}
	return gcd(n, m%n)
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide an integer argument m and n.")
		return
	}

	m, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Invalid integer argument for m", err)
		return
	}

	n, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println("Invalid integer argument for n", err)
		return
	}

	fmt.Printf("gcd(%d, %d) = %d\n", m, n, gcd(m, n))
}
