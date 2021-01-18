  
package main

//commented out calls will be uncommented once tinygo is installed

import (
	//need tinygo install for this - will do on personal computer
	//"machine"
	"fmt"
	"time"
)

func main() {

	//led := machine.LED
	//led.Configure(machine.PinConfig{Mode: machine.PinOutput})
	for {
		fmt.Println("changing to low")
		//	led.Low()
		time.Sleep(time.Millisecond * 500)

		fmt.Println("changing to high")
		//	led.High()
		time.Sleep(time.Millisecond * 500)

	}
}
