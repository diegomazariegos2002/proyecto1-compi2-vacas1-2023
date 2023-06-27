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
	t10, t11, t12, t13, t14, t15, t16, t17, t18, t19,
	t20, t21, t22, t23, t24, t25, t26, t27 float64
)

func factorial() {

	/*INSTRUCCION IF*/

	/*CONDICION IF*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t1 [ == ]*/

	/*Acceso Variable n*/
	t2 = SP + 1
	t1 = STACK[int(t2)]

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if t1 == 0.0 {
		goto L1
	}
	t3 = 0
	goto L2
L1:
	t3 = 1
L2:

	/*VALIDACION IF*/
	if t3 == 1 {
		goto L4
	}
	goto L5
L4:

	/*INSTRUCCION RETURN*/

	/*EXPRESION RETURN*/
	t4 = SP + 0
	STACK[int(t4)] = 1.0
	goto L0
	goto L3
L5:

	/*ELSE*/

	/*INSTRUCCION RETURN*/

	/*EXPRESION RETURN*/

	/*EXPRESIONES MULTIPLICACION*/

	/*Acceso Variable n*/
	t5 = SP + 1
	t1 = STACK[int(t5)]

	/*INSTRUCCION DE LLAMADA DE FUNCION factorial*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS factorial*/

	/*Declaracion Variable n*/
	t6 = SP + 3
	STACK[int(t6)] = 0

	/*Asignacion Variable n*/

	/*EXPRESIONES RESTA*/

	/*Acceso Variable n*/
	t7 = SP + 1
	t1 = STACK[int(t7)]

	/*OPERACION RESTA*/
	t8 = t1 - 1.0
	STACK[int(t6)] = t8

	/*moviendo puntero al ambito del stack de factorial*/
	SP = SP + 2
	factorial()

	/*obteniendo return funcion factorial*/
	t9 = SP + 0
	t10 = STACK[int(t9)]

	/*restableciendo puntero al ambito anterior de factorial*/
	SP = SP - 2

	/*reiniciando temporales funcion factorial*/
	t11 = SP + 1
	t1 = STACK[int(t11)]

	/*OPERACION MULTIPLICACION*/
	t12 = t1 * t10
	t13 = SP + 0
	STACK[int(t13)] = t12
	goto L0
	goto L3
L3:
	goto L0
L0:
	return
}

func main() {
	HP = 0
	SP = 0

	/*Declaracion Variable num*/
	t0 = SP + 1
	STACK[int(t0)] = 5.0

	/*Declaracion Variable resultado*/

	/*INSTRUCCION DE LLAMADA DE FUNCION factorial*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS factorial*/

	/*Declaracion Variable n*/
	t14 = SP + 3
	STACK[int(t14)] = 0

	/*Asignacion Variable n*/

	/*Acceso Variable num*/
	t15 = SP + 1
	t0 = STACK[int(t15)]
	STACK[int(t14)] = t0

	/*moviendo puntero al ambito del stack de factorial*/
	SP = SP + 2
	factorial()

	/*obteniendo return funcion factorial*/
	t16 = SP + 0
	t17 = STACK[int(t16)]

	/*restableciendo puntero al ambito anterior de factorial*/
	SP = SP - 2

	/*reiniciando temporales funcion factorial*/
	t18 = SP + 1
	t1 = STACK[int(t18)]
	t19 = SP + 2
	STACK[int(t19)] = t17

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t20 = HP
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 102.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 99.0
	HP = HP + 1
	HEAP[int(HP)] = 116.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable num*/
	t23 = SP + 1
	t0 = STACK[int(t23)]

	/*PRIMITIVO -> CADENA*/
	t24 = HP
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable resultado*/
	t27 = SP + 2
	t19 = STACK[int(t27)]
	t21 = t20
L6:
	t22 = HEAP[int(t21)]
	if t22 == -1 {
		goto L7
	}
	fmt.Printf("%c", int(t22))
	t21 = t21 + 1
	goto L6
L7:
	fmt.Printf("%f", t0)
	t25 = t24
L8:
	t26 = HEAP[int(t25)]
	if t26 == -1 {
		goto L9
	}
	fmt.Printf("%c", int(t26))
	t25 = t25 + 1
	goto L8
L9:
	fmt.Printf("%f", t19)
	fmt.Printf("%c", int(10))

}
