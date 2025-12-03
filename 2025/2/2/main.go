package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const filename = "input.txt"

func loadData() string {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return string(data)
}

func findInvalidIDs(n1 int, n2 int) []int {
	var invalidIDs []int
	for i := n1; i <= n2; i++ {
		x := strconv.Itoa(i)
		if len(x) % 2 == 0 {
			z := len(x) / 2
			m1 := x[0:z]
			m2 := x[z:]
			if m1 == m2 {
				invalidIDs = append(invalidIDs, i)
			}
		}
	}
	return invalidIDs
}

func trim(ranges []string) []string {
	var output []string
	for _, v := range ranges {
		output = append(output, strings.TrimSpace(v))
	}

	return output
}

func getAnswer(ids []int) int {
	sum := 0
	for _,v := range ids {
		sum += v
	}
	return sum
}

func main() {
	data := loadData()
	ranges := strings.Split(data, ",")
	ranges = trim(ranges)
	var invalidIDs []int
	for _, r := range ranges {
		x := strings.Split(r, "-")
		n1, err := strconv.Atoi(x[0])
		if err != nil {
			panic(err)
		}

		n2, err := strconv.Atoi(x[1])
		if err != nil {
			panic(err)
		}
		newInvalidIDs := findInvalidIDs(n1, n2)
		invalidIDs = append(invalidIDs, newInvalidIDs...)
	}
	result := getAnswer(invalidIDs)
	fmt.Println(result)
}
