/* ---- HEADER ----- */
package main

import (
	"fmt"
	"math"
)

var HP, SP float64
var STACK [30101999]float64
var HEAP [30101999]float64

var (
	t0, t1, t2, t3, t4, t5, t6, t7, t8, t9,
	t10, t11, t12, t13, t14, t15, t16, t17, t18, t19,
	t20, t21, t22, t23, t24, t25 float64
)

func bubbleSort() {

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t7 = HP
	HEAP[int(HP)] = 98.0
	HP = HP + 1
	HEAP[int(HP)] = 121.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t8 = t7
L1:
	t9 = HEAP[int(t8)]
	if t9 == -1 {
		goto L2
	}
	fmt.Printf("%c", int(t9))
	t8 = t8 + 1
	goto L1
L2:
	fmt.Printf("%c", int(10))

	/*INSTRUCCION DE LLAMADA DE FUNCION swap*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS swap*/

	/*moviendo puntero al ambito del stack de swap*/
	SP = SP + 1
	swap()

	/*obteniendo return funcion swap*/
	t13 = SP + 0
	t14 = STACK[int(t13)]

	/*restableciendo puntero al ambito anterior de swap*/
	SP = SP - 1

	/*reiniciando temporales funcion swap*/
	goto L0
L0:
	return
}

func swap() {

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t10 = HP
	HEAP[int(HP)] = 98.0
	HP = HP + 1
	HEAP[int(HP)] = 121.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 120.0
	HP = HP + 1
	HEAP[int(HP)] = 50.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t11 = t10
L4:
	t12 = HEAP[int(t11)]
	if t12 == -1 {
		goto L5
	}
	fmt.Printf("%c", int(t12))
	t11 = t11 + 1
	goto L4
L5:
	fmt.Printf("%c", int(10))
	goto L3
L3:
	return
}

func main() {
	HP = 0
	SP = 0

	/*Declaracion Variable arreglo*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t0 = 7.0 * 3.0

	/*EXPRESIONES POTENCIA*/

	/*OPERACION POTENCIA*/
	t1 = math.Pow(9874.0, 0.0)

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t2 = 820.0 * 10.0

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t3 = 8.0 * 0.0

	/*OPERACION SUMA*/
	t4 = t3 + 8.0

	/*----CREACION DE VECTOR----*/
	t5 = HP
	HEAP[int(HP)] = 16
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = t0
	HP = HP + 1
	HEAP[int(HP)] = 7.0
	HP = HP + 1
	HEAP[int(HP)] = 89.0
	HP = HP + 1
	HEAP[int(HP)] = 56.0
	HP = HP + 1
	HEAP[int(HP)] = 909.0
	HP = HP + 1
	HEAP[int(HP)] = 109.0
	HP = HP + 1
	HEAP[int(HP)] = 2.0
	HP = HP + 1
	HEAP[int(HP)] = 9.0
	HP = HP + 1
	HEAP[int(HP)] = t1
	HP = HP + 1
	HEAP[int(HP)] = 44.0
	HP = HP + 1
	HEAP[int(HP)] = 3.0
	HP = HP + 1
	HEAP[int(HP)] = t2
	HP = HP + 1
	HEAP[int(HP)] = 11.0
	HP = HP + 1
	HEAP[int(HP)] = t4
	HP = HP + 1
	HEAP[int(HP)] = 10.0
	HP = HP + 1
	t6 = SP + 3
	STACK[int(t6)] = t5

	/*INSTRUCCION DE LLAMADA DE FUNCION bubbleSort*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS bubbleSort*/

	/*moviendo puntero al ambito del stack de bubbleSort*/
	SP = SP + 4
	bubbleSort()

	/*obteniendo return funcion bubbleSort*/
	t15 = SP + 0
	t16 = STACK[int(t15)]

	/*restableciendo puntero al ambito anterior de bubbleSort*/
	SP = SP - 4

	/*reiniciando temporales funcion bubbleSort*/

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t17 = HP
	HEAP[int(HP)] = 66.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 98.0
	HP = HP + 1
	HEAP[int(HP)] = 98.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 83.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 116.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 62.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable arreglo*/
	t20 = SP + 3
	t6 = STACK[int(t20)]
	t18 = t17
L6:
	t19 = HEAP[int(t18)]
	if t19 == -1 {
		goto L7
	}
	fmt.Printf("%c", int(t19))
	t18 = t18 + 1
	goto L6
L7:
	fmt.Printf("%c", int(91))
	fmt.Printf("%c", int(32))
	t21 = HEAP[int(t6)]
	t22 = t6 + 1
	t23 = 0
L8:
	if t21 > t23 {
		goto L9
	}
	goto L10
L9:
	t25 = t22 + t23
	t24 = HEAP[int(t25)]
	fmt.Printf("%f", t24)
	t23 = t23 + 1
	fmt.Printf("%c", int(32))
	goto L8
L10:
	fmt.Printf("%c", int(93))
	fmt.Printf("%c", int(10))
	fmt.Printf("%c", int(10))

}
