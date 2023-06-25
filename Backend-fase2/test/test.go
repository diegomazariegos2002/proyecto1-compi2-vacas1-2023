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
t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,
t20,t21 float64 
)
func main() {
 HP = 0
 SP = 0

/*console.log*/

/*----CREACION DE VECTOR----*/
t0 = HP;
HEAP[int(HP)] = 2;
HP = HP + 1;
HEAP[int(HP)] = 1.0;
HP = HP + 1;
HEAP[int(HP)] = 2.0;
HP = HP + 1;

/*----CREACION DE VECTOR----*/
t1 = HP;
HEAP[int(HP)] = 2;
HP = HP + 1;
HEAP[int(HP)] = 3.0;
HP = HP + 1;
HEAP[int(HP)] = 4.0;
HP = HP + 1;

/*----CREACION DE VECTOR----*/
t2 = HP;
HEAP[int(HP)] = 2;
HP = HP + 1;
HEAP[int(HP)] = t0;
HP = HP + 1;
HEAP[int(HP)] = t1;
HP = HP + 1;

/*----CREACION DE VECTOR----*/
t3 = HP;
HEAP[int(HP)] = 2;
HP = HP + 1;
HEAP[int(HP)] = 5.0;
HP = HP + 1;
HEAP[int(HP)] = 6.0;
HP = HP + 1;

/*----CREACION DE VECTOR----*/
t4 = HP;
HEAP[int(HP)] = 2;
HP = HP + 1;
HEAP[int(HP)] = 7.0;
HP = HP + 1;
HEAP[int(HP)] = 8.0;
HP = HP + 1;

/*----CREACION DE VECTOR----*/
t5 = HP;
HEAP[int(HP)] = 2;
HP = HP + 1;
HEAP[int(HP)] = t3;
HP = HP + 1;
HEAP[int(HP)] = t4;
HP = HP + 1;

/*----CREACION DE VECTOR----*/
t6 = HP;
HEAP[int(HP)] = 2;
HP = HP + 1;
HEAP[int(HP)] = t2;
HP = HP + 1;
HEAP[int(HP)] = t5;
HP = HP + 1;
fmt.Printf("%c", int(91))
fmt.Printf("%c", int(32))
t7 = HEAP[int(t6)];
t8 = t6 + 1;
t9 = 0;
L0:
if t7 > t9 {goto L1}
goto L2;
L1:
t11 = t8 + t9;
t10 = HEAP[int(t11)];
fmt.Printf("%c", int(91))
fmt.Printf("%c", int(32))
t12 = HEAP[int(t10)];
t13 = t10 + 1;
t14 = 0;
L3:
if t12 > t14 {goto L4}
goto L5;
L4:
t16 = t13 + t14;
t15 = HEAP[int(t16)];
fmt.Printf("%c", int(91))
fmt.Printf("%c", int(32))
t17 = HEAP[int(t15)];
t18 = t15 + 1;
t19 = 0;
L6:
if t17 > t19 {goto L7}
goto L8;
L7:
t21 = t18 + t19;
t20 = HEAP[int (t21)];
fmt.Printf("%f", t20)
t19 = t19 + 1;
fmt.Printf("%c", int(32))
goto L6;
L8:
fmt.Printf("%c", int(93))
t14 = t14 + 1;
fmt.Printf("%c", int(32))
goto L3;
L5:
fmt.Printf("%c", int(93))
t9 = t9 + 1;
fmt.Printf("%c", int(32))
goto L0;
L2:
fmt.Printf("%c", int(93))
fmt.Printf("%c", int(10))
fmt.Printf("%c", int(10))

}