// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"strconv"
// )

// const (
// 	filename = "input.txt"
// )

// func loadData() []string {
// 	data := make([]string, 0)
// 	file, err := os.Open(filename)
// 	if err != nil {
// 		panic(err)
// 	}
// 	defer file.Close()

// 	scanner := bufio.NewScanner(file)
// 	for scanner.Scan() {
// 		data = append(data, scanner.Text())
// 	}

// 	if err := scanner.Err(); err != nil {
// 		panic(err)
// 	}

// 	return data
// }

// func normalize(dial int, counter int) (int, int) {
// 	if dial > 100 {
// 		dial -= 100
// 		counter += 1
// 	}

// 	if dial == 100 {
// 		dial -= 100
// 	}

// 	// if dial == -100{
// 	// 	counter -= 1
// 	// }

// 	if dial < 0 {
// 		dial += 100
// 		counter += 1
// 	}


// 	if dial >= 0 && dial < 100 {
// 		return dial, counter
// 	} else {
// 		return normalize(dial, counter)
// 	}
// }

// func turn(dial int, direction string, value int) (int, int) {
// 	fmt.Printf("%s%d\n", direction, value)
// 	fmt.Printf("dial pos - %d\n", dial)
// 	var dial_orig int
// 	dial_orig = dial
// 	if direction == "L" {
// 		dial -= value
// 	} else {
// 		dial += value
// 	}
// 	fmt.Printf("dial prenorm - %d\n", dial)
// 	dial, counter := normalize(dial, 0)
// 	fmt.Printf("dial_orig - %d\n", dial_orig)
// 	if dial_orig == 0 && counter > 0 {
// 		fmt.Printf("counter--\n")
// 		counter--
// 	}

// 	fmt.Printf("dial postnorm - %d\n", dial)

// 	return dial, counter
// }

// func main() {
// 	data := loadData()
// 	dial := 50
// 	counter := 0
// 	for _, v := range data {
// 		direction := string(v[0])
// 		number, err := strconv.Atoi(v[1:])
// 		if err != nil {
// 			panic(err)
// 		}
// 		var counter2 int
// 		dial, counter2 = turn(dial, direction, number)
// 		fmt.Printf("counter 2 - %d\n", counter2)
// 		counter += counter2
// 		if dial == 0 {
// 			counter++
// 		}
// 		fmt.Println(counter)
// 		fmt.Println()
// 	}

// 	fmt.Println(counter)
// }
