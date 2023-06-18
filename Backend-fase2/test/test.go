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
t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,
t10,t11 float64 
)
func main() {
 HP = 0
 SP = 0

/*Declaracion Variable*/
t0 = SP + 0;
STACK[int (t0)] = 0.0;

/*console.log*/

/*Acceso Variable x*/
t1 = SP + 0;
t2 = STACK[int(t1)];
fmt.Printf("%f", t2)
fmt.Printf("%c", int(10))

/*Declaracion Variable*/

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
HEAP[int(HP)] = 97.0;
HP = HP + 1;
HEAP[int(HP)] = 97.0;
HP = HP + 1;
HEAP[int(HP)] = -1;
HP = HP + 1;
t4 = SP + 1;
STACK[int (t4)] = t3;

/*console.log*/

/*Acceso Variable str*/
t5 = SP + 1;
t6 = STACK[int(t5)];
t7 = t6;
L0:
t8 = HEAP[int(t7)];
if t8 == -1 {goto L1}
fmt.Printf("%c", int(t8))
t7 = t7 + 1;
goto L0;
L1:
fmt.Printf("%c", int(10))

/*Declaracion Variable*/
t9 = SP + 2;
STACK[int (t9)] = 1;

/*console.log*/

/*Acceso Variable bo*/
t10 = SP + 2;
t11 = STACK[int(t10)];
if t11==1 {goto L2}
fmt.Printf("%c", int(102))
fmt.Printf("%c", int(97))
fmt.Printf("%c", int(108))
fmt.Printf("%c", int(115))
fmt.Printf("%c", int(101))
goto L3;
L2:
fmt.Printf("%c", int(116))
fmt.Printf("%c", int(114))
fmt.Printf("%c", int(117))
fmt.Printf("%c", int(101))
L3:
fmt.Printf("%c", int(10))

}