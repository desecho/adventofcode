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

func turn(dial int, direction string, value int, counter int) (int, int) {
	// fmt.Printf("%s%d\n", direction, value)
	if direction == "L" {
		if dial == 0 {
			dial = 99
		} else {
			dial--
		}

		value--
	} else {
		if dial == 99 {
			dial = 0
		} else {
			dial++
		}
		value--
	}
	// fmt.Printf("dial pos - %d\n", dial)

	if dial == 0 {
		counter++
	}
	// fmt.Printf("counter - %d\n", counter)

	if value > 0 {
		return turn(dial, direction, value, counter)
	}

	return dial, counter
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
		var counter2 int
		dial, counter2 = turn(dial, direction, number, 0)
		counter += counter2
		// fmt.Println(counter)
		// fmt.Println()
	}

	fmt.Println(counter)
}
