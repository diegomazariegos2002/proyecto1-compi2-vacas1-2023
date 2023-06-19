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
t0,t1,t2,t3,t4,t5,t6,t7 float64 
)
func main() {
 HP = 0
 SP = 0

/*Declaracion Variable*/
t0 = SP + 0;
STACK[int (t0)] = 1;

/*console.log*/

/*Acceso Variable x*/
t1 = SP + 0;
t2 = STACK[int(t1)];
if t2==1 {goto L0}
fmt.Printf("%c", int(102))
fmt.Printf("%c", int(97))
fmt.Printf("%c", int(108))
fmt.Printf("%c", int(115))
fmt.Printf("%c", int(101))
goto L1;
L0:
fmt.Printf("%c", int(116))
fmt.Printf("%c", int(114))
fmt.Printf("%c", int(117))
fmt.Printf("%c", int(101))
L1:
fmt.Printf("%c", int(10))

/*Asignacion Variable x*/

/*PRIMITIVO -> CADENA*/
t3 = HP;
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
STACK[int(t0)] = t3;

/*console.log*/

/*Acceso Variable x*/
t4 = SP + 0;
t5 = STACK[int(t4)];
t6 = t5;
L2:
t7 = HEAP[int(t6)];
if t7 == -1 {goto L3}
fmt.Printf("%c", int(t7))
t6 = t6 + 1;
goto L2;
L3:
fmt.Printf("%c", int(10))

}