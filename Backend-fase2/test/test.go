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
	t20, t21, t22, t23, t24, t25, t26, t27, t28, t29,
	t30, t31, t32, t33, t34, t35, t36, t37, t38, t39,
	t40, t41, t42, t43, t44, t45, t46, t47, t48, t49,
	t50, t51, t52, t53, t54, t55, t56, t57, t58, t59,
	t60, t61, t62, t63, t64, t65, t66, t67, t68, t69,
	t70, t71, t72 float64
)

func main() {
	HP = 0
	SP = 0

	/*Declaracion Variable val1*/
	t0 = SP + 0
	STACK[int(t0)] = 1.0

	/*Declaracion Variable val2*/
	t1 = SP + 1
	STACK[int(t1)] = 10.0

	/*Declaracion Variable val3*/
	t2 = SP + 2
	STACK[int(t2)] = 2021.202

	/*Asignacion Variable val1*/

	/*EXPRESIONES RESTA*/

	/*EXPRESIONES RESTA*/

	/*EXPRESIONES SUMA*/

	/*Acceso Variable val1*/
	t3 = SP + 0
	t0 = STACK[int(t3)]

	/*OPERACION SUMA*/
	t4 = t0 + 41.0

	/*EXPRESIONES DIVISION*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t5 = 123.0 * 4.0

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t6 = 2.0 * 2.0

	/*OPERACION SUMA*/
	t7 = 2.0 + t6

	/*OPERACION DIVISION*/
	t8 = t5 / t7

	/*OPERACION RESTA*/
	t9 = t4 - t8

	/*EXPRESIONES MULTIPLICACION*/

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MODULO*/

	/*OPERACION MODULO*/
	t10 = math.Mod(125.0, 5.0)

	/*OPERACION SUMA*/
	t11 = 10.0 + t10

	/*EXPRESIONES POTENCIA*/

	/*OPERACION POTENCIA*/
	t12 = math.Pow(2.0, 2.0)

	/*OPERACION MULTIPLICACION*/
	t13 = t11 * t12

	/*OPERACION RESTA*/
	t14 = t9 - t13
	STACK[int(t0)] = t14

	/*Asignacion Variable val2*/

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MULTIPLICACION*/

	/*EXPRESIONES MODULO*/

	/*EXPRESIONES SUMA*/

	/*EXPRESION NEGATIVO*/

	/*OPERACION NEGATIVO*/
	t15 = 10.0 * (-1)

	/*OPERACION SUMA*/
	t16 = 12.0 + t15

	/*OPERACION MODULO*/
	t17 = math.Mod(11.0, t16)

	/*OPERACION MULTIPLICACION*/
	t18 = 11.0 * t17

	/*EXPRESIONES DIVISION*/

	/*OPERACION DIVISION*/
	t19 = 22.0 / 2.0

	/*OPERACION SUMA*/
	t20 = t18 + t19
	STACK[int(t1)] = t20

	/*Declaracion Variable rel1*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA t34 [||]*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t24 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t23 [ == ]*/

	/*EXPRESIONES RESTA*/

	/*Acceso Variable val1*/
	t21 = SP + 0
	t14 = STACK[int(t21)]

	/*Acceso Variable val2*/
	t22 = SP + 1
	t20 = STACK[int(t22)]

	/*OPERACION RESTA*/
	t23 = t14 - t20

	/*EXPRESION DERECHA 24.0 [ == ]*/
	if t23 == 24.0 {
		goto L0
	}
	t24 = 0
	goto L1
L0:
	t24 = 1
L1:

	/*EXPRESION DERECHA t31 [&&]*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA 1 [&&]*/

	/*EXPRESION DERECHA t28 [&&]*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA 0 [||]*/

	/*EXPRESION DERECHA t25 [||]*/

	/*EXPRESIONES RELACION  >= */

	/*EXPRESION IZQUIERDA 5.0 [ >= ]*/

	/*EXPRESION DERECHA 5.0 [ >= ]*/
	if 5.0 >= 5.0 {
		goto L2
	}
	t25 = 0
	goto L3
L2:
	t25 = 1
L3:

	/*LOGICA OR 0 t25*/
	t26 = 0
	t27 = t25
	if t26 == 1 || t27 == 1 {
		goto L5
	}
	t28 = 0
	goto L4
L5:
	t28 = 1
L4:

	/*LOGICA AND 1 t28*/
	t29 = 1
	t30 = t28
	if t29 == 1 && t30 == 1 {
		goto L7
	}
	t31 = 0
	goto L6
L7:
	t31 = 1
L6:

	/*LOGICA AND t24 t31*/
	t32 = t24
	t33 = t31
	if t32 == 1 && t33 == 1 {
		goto L9
	}
	t34 = 0
	goto L8
L9:
	t34 = 1
L8:

	/*EXPRESION DERECHA t42 [||]*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA t37 [||]*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t35 [ != ]*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t35 = 7.0 * 7.0

	/*EXPRESION DERECHA t36 [ != ]*/

	/*EXPRESIONES SUMA*/

	/*OPERACION SUMA*/
	t36 = 15.0 + 555.0
	if t35 != t36 {
		goto L10
	}
	t37 = 0
	goto L11
L10:
	t37 = 1
L11:

	/*EXPRESION DERECHA t39 [||]*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA t38 [ > ]*/

	/*EXPRESION NEGATIVO*/

	/*OPERACION NEGATIVO*/
	t38 = 61.0 * (-1)

	/*EXPRESION DERECHA 51.0 [ > ]*/
	if t38 > 51.0 {
		goto L12
	}
	t39 = 0
	goto L13
L12:
	t39 = 1
L13:

	/*LOGICA OR t37 t39*/
	t40 = t37
	t41 = t39
	if t40 == 1 || t41 == 1 {
		goto L15
	}
	t42 = 0
	goto L14
L15:
	t42 = 1
L14:

	/*LOGICA OR t34 t42*/
	t43 = t34
	t44 = t42
	if t43 == 1 || t44 == 1 {
		goto L17
	}
	t45 = 0
	goto L16
L17:
	t45 = 1
L16:
	t46 = SP + 3
	STACK[int(t46)] = t45

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t47 = HP
	HEAP[int(HP)] = 80.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 98.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 110.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 99.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 99.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 110.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 118.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 98.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 10.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t48 = t47
L18:
	t49 = HEAP[int(t48)]
	if t49 == -1 {
		goto L19
	}
	fmt.Printf("%c", int(t49))
	t48 = t48 + 1
	goto L18
L19:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*Acceso Variable val1*/
	t50 = SP + 0
	t14 = STACK[int(t50)]

	/*PRIMITIVO -> CADENA*/
	t51 = HP
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable val2*/
	t54 = SP + 1
	t20 = STACK[int(t54)]

	/*PRIMITIVO -> CADENA*/
	t55 = HP
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable val3*/
	t58 = SP + 2
	t2 = STACK[int(t58)]
	fmt.Printf("%f", t14)
	t52 = t51
L20:
	t53 = HEAP[int(t52)]
	if t53 == -1 {
		goto L21
	}
	fmt.Printf("%c", int(t53))
	t52 = t52 + 1
	goto L20
L21:
	fmt.Printf("%f", t20)
	t56 = t55
L22:
	t57 = HEAP[int(t56)]
	if t57 == -1 {
		goto L23
	}
	fmt.Printf("%c", int(t57))
	t56 = t56 + 1
	goto L22
L23:
	fmt.Printf("%f", t2)
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t59 = HP
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = 45.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t60 = t59
L24:
	t61 = HEAP[int(t60)]
	if t61 == -1 {
		goto L25
	}
	fmt.Printf("%c", int(t61))
	t60 = t60 + 1
	goto L24
L25:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*Acceso Variable val1*/
	t62 = SP + 0
	t14 = STACK[int(t62)]

	/*Guardando en el Heap TYPEOF*/
	t63 = HP
	HEAP[int(HP)] = 78
	HP = HP + 1
	HEAP[int(HP)] = 85
	HP = HP + 1
	HEAP[int(HP)] = 77
	HP = HP + 1
	HEAP[int(HP)] = 66
	HP = HP + 1
	HEAP[int(HP)] = 69
	HP = HP + 1
	HEAP[int(HP)] = 82
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*PRIMITIVO -> CADENA*/
	t66 = HP
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable rel1*/
	t69 = SP + 3
	t46 = STACK[int(t69)]

	/*Guardando en el Heap TYPEOF*/
	t70 = HP
	HEAP[int(HP)] = 66
	HP = HP + 1
	HEAP[int(HP)] = 79
	HP = HP + 1
	HEAP[int(HP)] = 79
	HP = HP + 1
	HEAP[int(HP)] = 76
	HP = HP + 1
	HEAP[int(HP)] = 69
	HP = HP + 1
	HEAP[int(HP)] = 65
	HP = HP + 1
	HEAP[int(HP)] = 78
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t64 = t63
L26:
	t65 = HEAP[int(t64)]
	if t65 == -1 {
		goto L27
	}
	fmt.Printf("%c", int(t65))
	t64 = t64 + 1
	goto L26
L27:
	t67 = t66
L28:
	t68 = HEAP[int(t67)]
	if t68 == -1 {
		goto L29
	}
	fmt.Printf("%c", int(t68))
	t67 = t67 + 1
	goto L28
L29:
	t71 = t70
L30:
	t72 = HEAP[int(t71)]
	if t72 == -1 {
		goto L31
	}
	fmt.Printf("%c", int(t72))
	t71 = t71 + 1
	goto L30
L31:
	fmt.Printf("%c", int(10))

}
