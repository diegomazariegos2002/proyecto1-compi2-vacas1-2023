/* ---- HEADER ----- */
package main

import (
	"fmt"
)

var HP, SP float64
var STACK [30101999]float64
var HEAP [30101999]float64

var (
	t0, t1, t2, t3, t4, t5, t6, t7, t8, t9,
	t10, t11 float64
)

func main() {
	HP = 0
	SP = 0

	/*Declaracion Variable*/
	t0 = SP + 0
	STACK[int(t0)] = 0.0

	/*INSTRUCCION WHILE*/
L0:

	/*VALIDANDO CONDICION WHILE*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t2 [ < ]*/

	/*Acceso Variable contador*/
	t1 = SP + 0
	t2 = STACK[int(t1)]

	/*EXPRESION DERECHA 5.0 [ < ]*/
	if t2 < 5.0 {
		goto L3
	}
	t3 = 0
	goto L4
L3:
	t3 = 1
L4:
	if t3 == 1 {
		goto L1
	}
	goto L2

	/*SE CUMPLIO CONDICION WHILE*/
L1:

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t4 = HP
	HEAP[int(HP)] = 69.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 99.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 110.0
	HP = HP + 1
	HEAP[int(HP)] = 116.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 58.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable contador*/
	t7 = SP + 0
	t8 = STACK[int(t7)]
	t5 = t4
L5:
	t6 = HEAP[int(t5)]
	if t6 == -1 {
		goto L6
	}
	fmt.Printf("%c", int(t6))
	t5 = t5 + 1
	goto L5
L6:
	fmt.Printf("%f", t8)
	fmt.Printf("%c", int(10))

	/*Asignacion Variable contador*/

	/*EXPRESIONES SUMA*/

	/*Acceso Variable contador*/
	t9 = SP + 0
	t10 = STACK[int(t9)]

	/*OPERACION SUMA*/
	t11 = t10 + 1.0
	STACK[int(t0)] = t11
	goto L0

	/*FIN WHILE*/
L2:
}
