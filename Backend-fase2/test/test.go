/* ---- HEADER ----- */
package main;

import(
	"fmt"
	"math"
	"strconv"

)

var HP, SP float64;
var STACK[30101999] float64;
var HEAP[30101999] float64;

var (
t0,t1,t2,t3,t4,t5,t6 float64 
)
func main() {
 HP = 0
 SP = 0

/*console.log*/

/*PRIMITIVO -> CADENA*/
t0 = HP;
HEAP[int(HP)] = 104.0;
HP = HP + 1;
HEAP[int(HP)] = 111.0;
HP = HP + 1;
HEAP[int(HP)] = 108.0;
HP = HP + 1;
HEAP[int(HP)] = 97.0;
HP = HP + 1;
HEAP[int(HP)] = -1;
HP = HP + 1;
t1 = HP;
t2 = HP;
t2 = t2 + 2;
HEAP[int(t1)] = t2;
HEAP[int(HP)] = 2.0;
HP = HP + 1;
HEAP[int(HP)] = t0;
HP = HP + 1;
t3 = HP;
t4 = HP;
t4 = t4 + 3;
HEAP[int(t3)] = t4;
HEAP[int(HP)] = 1.0;
HP = HP + 1;
HEAP[int(HP)] = t1;
HP = HP + 1;
HEAP[int(HP)] = 3.0;
HP = HP + 1;

/*PRIMITIVO -> CADENA*/
t0 = HP;
HEAP[int(HP)] = 104.0;
HP = HP + 1;
HEAP[int(HP)] = 111.0;
HP = HP + 1;
HEAP[int(HP)] = 108.0;
HP = HP + 1;
HEAP[int(HP)] = 97.0;
HP = HP + 1;
HEAP[int(HP)] = -1;
HP = HP + 1;
t1 = HP;
t2 = HP;
t2 = t2 + 2;
HEAP[int(t1)] = t2;
HEAP[int(HP)] = 2.0;
HP = HP + 1;
HEAP[int(HP)] = t0;
HP = HP + 1;
fmt.Printf("%c", int(10))
fmt.Printf("%c", int(91))
fmt.Printf("%f", 1.0)
fmt.Printf("%c", int(44))
fmt.Printf("%c", int(91))
fmt.Printf("%f", 2.0)
fmt.Printf("%c", int(44))
t5 = t0;
L0:
t6 = HEAP[int(t5)];
if t6 == -1 {goto L1}
fmt.Printf("%c", int(t6))
t5 = t5 + 1;
goto L0;
L1:
fmt.Printf("%c", int(93))
fmt.Printf("%c", int(44))
fmt.Printf("%f", 3.0)
fmt.Printf("%c", int(93))
fmt.Printf("%c", int(10))

}