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
t0,t1,t2,t3 float64 
)
func main() {
 HP = 0
 SP = 0

/*console.log*/

/*FUNCION LENGTH*/

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
HEAP[int(HP)] = 32.0;
HP = HP + 1;
HEAP[int(HP)] = 110.0;
HP = HP + 1;
HEAP[int(HP)] = 111.0;
HP = HP + 1;
HEAP[int(HP)] = 32.0;
HP = HP + 1;
HEAP[int(HP)] = 115.0;
HP = HP + 1;
HEAP[int(HP)] = 101.0;
HP = HP + 1;
HEAP[int(HP)] = -1;
HP = HP + 1;
t1 = t0;
L0:
t2 = HEAP[int(t1)];
if t2 == -1 {goto L1}
t1 = t1 + 1;
t3 = t3 + 1;
goto L0;
L1:
fmt.Printf("%f", t3)
fmt.Printf("%c", int(10))

}