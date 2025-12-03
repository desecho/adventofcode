package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	filename = "input.txt"
)

func loadData() []string {
	data := make([]string, 0)
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	return data
}

func normalize(dial int) int {
	if dial > 99 {
		dial -= 100
	}

	if dial < 0 {
		dial += 100
	}

	if dial >= 0 && dial < 100 {
		return dial
	} else {
		return normalize(dial)
	}
}

func turn(dial int, direction string, value int) int {
	if direction == "L" {
		dial -= value
	} else {
		dial += value
	}

	dial = normalize(dial)

	return dial
}

func main() {
	data := loadData()
	dial := 50
	counter := 0
	for _, v := range data {
		direction := string(v[0])
		number, err := strconv.Atoi(v[1:])
		if err != nil {
			panic(err)
		}
		dial = turn(dial, direction, number)
		if dial == 0 {
			counter++
		}
	}

	fmt.Println(counter)
}
