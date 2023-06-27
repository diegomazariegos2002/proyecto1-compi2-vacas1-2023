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
	t70, t71, t72, t73, t74, t75, t76, t77, t78, t79,
	t80, t81, t82, t83 float64
)

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
	t6 = SP + 0
	STACK[int(t6)] = t5

	/*INSTRUCCION FOR*/

	/*DECLARACION FOR*/

	/*Declaracion Variable i*/
	t7 = SP + 1
	STACK[int(t7)] = 0.0

	/*CONDICION FOR*/
L2:

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t7 [ < ]*/

	/*Acceso Variable i*/
	t8 = SP + 1
	t7 = STACK[int(t8)]

	/*EXPRESION DERECHA t11 [ < ]*/

	/*EXPRESIONES RESTA*/

	/*FUNCION LENGTH*/

	/*Acceso Variable arreglo*/
	t9 = SP + 0
	t6 = STACK[int(t9)]
	t10 = HEAP[int(t6)]

	/*OPERACION RESTA*/
	t11 = t10 - 1.0
	if t7 < t11 {
		goto L4
	}
	t12 = 0
	goto L5
L4:
	t12 = 1
L5:
	if t12 == 1 {
		goto L1
	}
	goto L3

	/*CUERPO FOR*/
L1:

	/*INSTRUCCION FOR*/

	/*DECLARACION FOR*/

	/*Declaracion Variable j*/
	t13 = SP + 2
	STACK[int(t13)] = 1.0

	/*CONDICION FOR*/
L8:

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t13 [ < ]*/

	/*Acceso Variable j*/
	t14 = SP + 2
	t13 = STACK[int(t14)]

	/*EXPRESION DERECHA t17 [ < ]*/

	/*EXPRESIONES RESTA*/

	/*FUNCION LENGTH*/

	/*Acceso Variable arreglo*/
	t15 = SP + 0
	t6 = STACK[int(t15)]
	t16 = HEAP[int(t6)]

	/*OPERACION RESTA*/
	t17 = t16 - 1.0
	if t13 < t17 {
		goto L10
	}
	t18 = 0
	goto L11
L10:
	t18 = 1
L11:
	if t18 == 1 {
		goto L7
	}
	goto L9

	/*CUERPO FOR*/
L7:

	/*INSTRUCCION IF*/

	/*CONDICION IF*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA t20 [ > ]*/

	/*Acceso Variable j*/
	t19 = SP + 2
	t13 = STACK[int(t19)]

	/*ACCESO A VECTOR*/
	t21 = 0
	t22 = HEAP[int(t6)]
	t23 = t6 + 1
	t24 = 0
L12:
	if t22 > t24 {
		goto L13
	}
	goto L14
L13:
	if t24 == t13 {
		goto L15
	}
	goto L16
L15:
	t26 = t23 + t24
	t21 = 1
	t20 = HEAP[int(t26)]
	goto L14
L16:
	t26 = t23 + t24
	t25 = HEAP[int(t26)]
	t24 = t24 + 1
	goto L12
L14:
	if t21 == 0 {
		goto L17
	}
	goto L18
L17:
	fmt.Printf("%c", int(66))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(110))
	fmt.Printf("%c", int(100))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
L18:

	/*EXPRESION DERECHA t29 [ > ]*/

	/*EXPRESIONES SUMA*/

	/*Acceso Variable j*/
	t27 = SP + 2
	t13 = STACK[int(t27)]

	/*OPERACION SUMA*/
	t28 = t13 + 1.0

	/*ACCESO A VECTOR*/
	t30 = 0
	t31 = HEAP[int(t6)]
	t32 = t6 + 1
	t33 = 0
L19:
	if t31 > t33 {
		goto L20
	}
	goto L21
L20:
	if t33 == t28 {
		goto L22
	}
	goto L23
L22:
	t35 = t32 + t33
	t30 = 1
	t29 = HEAP[int(t35)]
	goto L21
L23:
	t35 = t32 + t33
	t34 = HEAP[int(t35)]
	t33 = t33 + 1
	goto L19
L21:
	if t30 == 0 {
		goto L24
	}
	goto L25
L24:
	fmt.Printf("%c", int(66))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(110))
	fmt.Printf("%c", int(100))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
L25:
	if t20 > t29 {
		goto L26
	}
	t36 = 0
	goto L27
L26:
	t36 = 1
L27:

	/*VALIDACION IF*/
	if t36 == 1 {
		goto L29
	}
	goto L30
L29:

	/*Declaracion Variable temp*/

	/*Acceso Variable i*/
	t37 = SP + 1
	t7 = STACK[int(t37)]

	/*ACCESO A VECTOR*/
	t39 = 0
	t40 = HEAP[int(t6)]
	t41 = t6 + 1
	t42 = 0
L31:
	if t40 > t42 {
		goto L32
	}
	goto L33
L32:
	if t42 == t7 {
		goto L34
	}
	goto L35
L34:
	t44 = t41 + t42
	t39 = 1
	t38 = HEAP[int(t44)]
	goto L33
L35:
	t44 = t41 + t42
	t43 = HEAP[int(t44)]
	t42 = t42 + 1
	goto L31
L33:
	if t39 == 0 {
		goto L36
	}
	goto L37
L36:
	fmt.Printf("%c", int(66))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(110))
	fmt.Printf("%c", int(100))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
L37:
	t45 = SP + 3
	STACK[int(t45)] = t38

	/*Acceso Variable i*/
	t54 = SP + 1
	t7 = STACK[int(t54)]

	/*Acceso Variable j*/
	t46 = SP + 2
	t13 = STACK[int(t46)]

	/*ACCESO A VECTOR*/
	t48 = 0
	t49 = HEAP[int(t6)]
	t50 = t6 + 1
	t51 = 0
L38:
	if t49 > t51 {
		goto L39
	}
	goto L40
L39:
	if t51 == t13 {
		goto L41
	}
	goto L42
L41:
	t53 = t50 + t51
	t48 = 1
	t47 = HEAP[int(t53)]
	goto L40
L42:
	t53 = t50 + t51
	t52 = HEAP[int(t53)]
	t51 = t51 + 1
	goto L38
L40:
	if t48 == 0 {
		goto L43
	}
	goto L44
L43:
	fmt.Printf("%c", int(66))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(110))
	fmt.Printf("%c", int(100))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
L44:

	/*ASIGNACION EN VECTOR*/
	t55 = 0
	t56 = HEAP[int(t6)]
	t57 = t6 + 1
	t58 = 0
L45:
	if t56 > t58 {
		goto L46
	}
	goto L47
L46:
	if t58 == t7 {
		goto L48
	}
	goto L49
L48:
	t60 = t57 + t58
	t55 = 1
	HEAP[int(t60)] = t47
	goto L47
L49:
	t60 = t57 + t58
	t59 = HEAP[int(t60)]
	t58 = t58 + 1
	goto L45
L47:
	if t55 == 0 {
		goto L50
	}
	goto L51
L50:
	fmt.Printf("%c", int(66))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(110))
	fmt.Printf("%c", int(100))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
L51:

	/*Acceso Variable j*/
	t62 = SP + 2
	t13 = STACK[int(t62)]

	/*Acceso Variable temp*/
	t61 = SP + 3
	t45 = STACK[int(t61)]

	/*ASIGNACION EN VECTOR*/
	t63 = 0
	t64 = HEAP[int(t6)]
	t65 = t6 + 1
	t66 = 0
L52:
	if t64 > t66 {
		goto L53
	}
	goto L54
L53:
	if t66 == t13 {
		goto L55
	}
	goto L56
L55:
	t68 = t65 + t66
	t63 = 1
	HEAP[int(t68)] = t45
	goto L54
L56:
	t68 = t65 + t66
	t67 = HEAP[int(t68)]
	t66 = t66 + 1
	goto L52
L54:
	if t63 == 0 {
		goto L57
	}
	goto L58
L57:
	fmt.Printf("%c", int(66))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(110))
	fmt.Printf("%c", int(100))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(32))
	fmt.Printf("%c", int(69))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(111))
	fmt.Printf("%c", int(114))
L58:
	goto L28
L30:
	goto L28
L28:

	/*ASIGNACION FOR*/
	goto L6
L6:

	/*INSTRUCCION INCREMENTO*/
	t69 = SP + 2
	t70 = STACK[int(t69)]

	/*Asignacion Variable j*/
	t71 = t70 + 1
	STACK[int(t69)] = t71
	goto L8

	/*FIN FOR*/
L9:

	/*ASIGNACION FOR*/
	goto L0
L0:

	/*INSTRUCCION INCREMENTO*/
	t72 = SP + 1
	t73 = STACK[int(t72)]

	/*Asignacion Variable i*/
	t74 = t73 + 1
	STACK[int(t72)] = t74
	goto L2

	/*FIN FOR*/
L3:

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t75 = HP
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
	t78 = SP + 0
	t6 = STACK[int(t78)]
	t76 = t75
L59:
	t77 = HEAP[int(t76)]
	if t77 == -1 {
		goto L60
	}
	fmt.Printf("%c", int(t77))
	t76 = t76 + 1
	goto L59
L60:
	fmt.Printf("%c", int(91))
	fmt.Printf("%c", int(32))
	t79 = HEAP[int(t6)]
	t80 = t6 + 1
	t81 = 0
L61:
	if t79 > t81 {
		goto L62
	}
	goto L63
L62:
	t83 = t80 + t81
	t82 = HEAP[int(t83)]
	fmt.Printf("%f", t82)
	t81 = t81 + 1
	fmt.Printf("%c", int(32))
	goto L61
L63:
	fmt.Printf("%c", int(93))
	fmt.Printf("%c", int(10))
	fmt.Printf("%c", int(10))

}
