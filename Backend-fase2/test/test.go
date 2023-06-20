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
	t20, t21, t22, t23, t24, t25, t26, t27, t28, t29,
	t30, t31, t32, t33, t34, t35, t36, t37, t38, t39,
	t40, t41 float64
)

func main() {
	HP = 0
	SP = 0

	/*INSTRUCCION FOR*/

	/*DECLARACION FOR*/

	/*Declaracion Variable*/
	t0 = SP + 0
	STACK[int(t0)] = 0.0

	/*CONDICION FOR*/
L2:

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t2 [ < ]*/

	/*Acceso Variable contador*/
	t1 = SP + 0
	t2 = STACK[int(t1)]

	/*EXPRESION DERECHA 5.0 [ < ]*/
	if t2 < 5.0 {
		goto L4
	}
	t3 = 0
	goto L5
L4:
	t3 = 1
L5:
	if t3 == 1 {
		goto L1
	}
	goto L3

	/*CUERPO FOR*/
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
L6:
	t6 = HEAP[int(t5)]
	if t6 == -1 {
		goto L7
	}
	fmt.Printf("%c", int(t6))
	t5 = t5 + 1
	goto L6
L7:
	fmt.Printf("%f", t8)
	fmt.Printf("%c", int(10))

	/*Declaracion Variable*/
	t9 = SP + 1
	STACK[int(t9)] = 0.0

	/*Declaracion Variable*/
	t10 = SP + 2
	STACK[int(t10)] = 0.0

	/*INSTRUCCION WHILE*/
L8:

	/*VALIDANDO CONDICION WHILE*/

	/*EXPRESIONES RELACION  <= */

	/*EXPRESION IZQUIERDA t12 [ <= ]*/

	/*Acceso Variable i*/
	t11 = SP + 2
	t12 = STACK[int(t11)]

	/*EXPRESION DERECHA t14 [ <= ]*/

	/*Acceso Variable contador*/
	t13 = SP + 0
	t14 = STACK[int(t13)]
	if t12 <= t14 {
		goto L11
	}
	t15 = 0
	goto L12
L11:
	t15 = 1
L12:
	if t15 == 1 {
		goto L9
	}
	goto L10

	/*SE CUMPLIO CONDICION WHILE*/
L9:

	/*Asignacion Variable suma*/

	/*EXPRESIONES SUMA*/

	/*Acceso Variable suma*/
	t16 = SP + 1
	t17 = STACK[int(t16)]

	/*Acceso Variable i*/
	t18 = SP + 2
	t19 = STACK[int(t18)]

	/*OPERACION SUMA*/
	t20 = t17 + t19
	STACK[int(t9)] = t20

	/*INSTRUCCION INCREMENTO*/
	t21 = SP + 2
	t22 = STACK[int(t21)]

	/*Asignacion Variable i*/
	t23 = t22 + 1
	STACK[int(t21)] = t23
	goto L8

	/*FIN WHILE*/
L10:

	/*INSTRUCCION IF*/

	/*CONDICION IF*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t25 [ < ]*/

	/*Acceso Variable suma*/
	t24 = SP + 1
	t25 = STACK[int(t24)]

	/*EXPRESION DERECHA 5.0 [ < ]*/
	if t25 < 5.0 {
		goto L13
	}
	t26 = 0
	goto L14
L13:
	t26 = 1
L14:

	/*VALIDACION IF*/
	if t26 == 1 {
		goto L16
	}
	goto L17
L16:

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t27 = HP
	HEAP[int(HP)] = 76.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 109.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 109.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 110.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 113.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 53.0
	HP = HP + 1
	HEAP[int(HP)] = 46.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t28 = t27
L18:
	t29 = HEAP[int(t28)]
	if t29 == -1 {
		goto L19
	}
	fmt.Printf("%c", int(t29))
	t28 = t28 + 1
	goto L18
L19:
	fmt.Printf("%c", int(10))
	goto L15
L17:

	/*ELSE IF*/

	/*INSTRUCCION IF*/

	/*CONDICION IF*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t31 [ == ]*/

	/*Acceso Variable suma*/
	t30 = SP + 1
	t31 = STACK[int(t30)]

	/*EXPRESION DERECHA 5.0 [ == ]*/
	if t31 == 5.0 {
		goto L20
	}
	t32 = 0
	goto L21
L20:
	t32 = 1
L21:

	/*VALIDACION IF*/
	if t32 == 1 {
		goto L22
	}
	goto L23
L22:

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t33 = HP
	HEAP[int(HP)] = 76.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 109.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 103.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 53.0
	HP = HP + 1
	HEAP[int(HP)] = 46.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t34 = t33
L24:
	t35 = HEAP[int(t34)]
	if t35 == -1 {
		goto L25
	}
	fmt.Printf("%c", int(t35))
	t34 = t34 + 1
	goto L24
L25:
	fmt.Printf("%c", int(10))
	goto L15
L23:

	/*ELSE*/

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t36 = HP
	HEAP[int(HP)] = 76.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 109.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 109.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 121.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 113.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 53.0
	HP = HP + 1
	HEAP[int(HP)] = 46.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t37 = t36
L26:
	t38 = HEAP[int(t37)]
	if t38 == -1 {
		goto L27
	}
	fmt.Printf("%c", int(t38))
	t37 = t37 + 1
	goto L26
L27:
	fmt.Printf("%c", int(10))
	goto L15
L15:

	/*ASIGNACION FOR*/
	goto L0
L0:

	/*INSTRUCCION INCREMENTO*/
	t39 = SP + 0
	t40 = STACK[int(t39)]

	/*Asignacion Variable contador*/
	t41 = t40 + 1
	STACK[int(t39)] = t41
	goto L2

	/*FIN FOR*/
L3:
}
