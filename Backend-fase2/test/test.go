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
	t40, t41, t42, t43, t44, t45, t46, t47, t48, t49,
	t50, t51, t52, t53, t54, t55, t56, t57, t58, t59,
	t60, t61 float64
)

func hanoi() {

	/*INSTRUCCION IF*/

	/*CONDICION IF*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t0 [ == ]*/

	/*Acceso Variable discos*/
	t4 = SP + 1
	t0 = STACK[int(t4)]

	/*EXPRESION DERECHA 1.0 [ == ]*/
	if t0 == 1.0 {
		goto L1
	}
	t5 = 0
	goto L2
L1:
	t5 = 1
L2:

	/*VALIDACION IF*/
	if t5 == 1 {
		goto L4
	}
	goto L5
L4:

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t6 = HP
	HEAP[int(HP)] = 77.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 118.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable origen*/
	t9 = SP + 2
	t1 = STACK[int(t9)]

	/*PRIMITIVO -> CADENA*/
	t10 = HP
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable destino*/
	t13 = SP + 4
	t3 = STACK[int(t13)]
	t7 = t6
L6:
	t8 = HEAP[int(t7)]
	if t8 == -1 {
		goto L7
	}
	fmt.Printf("%c", int(t8))
	t7 = t7 + 1
	goto L6
L7:
	fmt.Printf("%f", t1)
	t11 = t10
L8:
	t12 = HEAP[int(t11)]
	if t12 == -1 {
		goto L9
	}
	fmt.Printf("%c", int(t12))
	t11 = t11 + 1
	goto L8
L9:
	fmt.Printf("%f", t3)
	fmt.Printf("%c", int(10))
	goto L3
L5:

	/*ELSE*/

	/*INSTRUCCION DE LLAMADA DE FUNCION hanoi*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS hanoi*/

	/*Declaracion Variable discos*/
	t14 = SP + 6
	STACK[int(t14)] = 0

	/*Asignacion Variable discos*/

	/*EXPRESIONES RESTA*/

	/*Acceso Variable discos*/
	t15 = SP + 1
	t0 = STACK[int(t15)]

	/*OPERACION RESTA*/
	t16 = t0 - 1.0
	STACK[int(t14)] = t16

	/*Declaracion Variable origen*/
	t17 = SP + 7
	STACK[int(t17)] = 0

	/*Asignacion Variable origen*/

	/*Acceso Variable origen*/
	t18 = SP + 2
	t1 = STACK[int(t18)]
	STACK[int(t17)] = t1

	/*Declaracion Variable auxiliar*/
	t19 = SP + 8
	STACK[int(t19)] = 0

	/*Asignacion Variable auxiliar*/

	/*Acceso Variable destino*/
	t20 = SP + 4
	t3 = STACK[int(t20)]
	STACK[int(t19)] = t3

	/*Declaracion Variable destino*/
	t21 = SP + 9
	STACK[int(t21)] = 0

	/*Asignacion Variable destino*/

	/*Acceso Variable auxiliar*/
	t22 = SP + 3
	t2 = STACK[int(t22)]
	STACK[int(t21)] = t2

	/*moviendo puntero al ambito del stack de hanoi*/
	SP = SP + 5
	hanoi()

	/*obteniendo return funcion hanoi*/
	t23 = SP + 0
	t24 = STACK[int(t23)]

	/*restableciendo puntero al ambito anterior de hanoi*/
	SP = SP - 5

	/*reiniciando temporales funcion hanoi*/
	t25 = SP + 1
	t0 = STACK[int(t25)]
	t26 = SP + 2
	t1 = STACK[int(t26)]
	t27 = SP + 3
	t2 = STACK[int(t27)]
	t28 = SP + 4
	t3 = STACK[int(t28)]

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t29 = HP
	HEAP[int(HP)] = 77.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 118.0
	HP = HP + 1
	HEAP[int(HP)] = 101.0
	HP = HP + 1
	HEAP[int(HP)] = 114.0
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

	/*Acceso Variable origen*/
	t32 = SP + 2
	t1 = STACK[int(t32)]

	/*PRIMITIVO -> CADENA*/
	t33 = HP
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*Acceso Variable destino*/
	t36 = SP + 4
	t3 = STACK[int(t36)]
	t30 = t29
L10:
	t31 = HEAP[int(t30)]
	if t31 == -1 {
		goto L11
	}
	fmt.Printf("%c", int(t31))
	t30 = t30 + 1
	goto L10
L11:
	fmt.Printf("%f", t1)
	t34 = t33
L12:
	t35 = HEAP[int(t34)]
	if t35 == -1 {
		goto L13
	}
	fmt.Printf("%c", int(t35))
	t34 = t34 + 1
	goto L12
L13:
	fmt.Printf("%f", t3)
	fmt.Printf("%c", int(10))

	/*INSTRUCCION DE LLAMADA DE FUNCION hanoi*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS hanoi*/

	/*Declaracion Variable discos*/
	t37 = SP + 6
	STACK[int(t37)] = 0

	/*Asignacion Variable discos*/

	/*EXPRESIONES RESTA*/

	/*Acceso Variable discos*/
	t38 = SP + 1
	t0 = STACK[int(t38)]

	/*OPERACION RESTA*/
	t39 = t0 - 1.0
	STACK[int(t37)] = t39

	/*Declaracion Variable origen*/
	t40 = SP + 7
	STACK[int(t40)] = 0

	/*Asignacion Variable origen*/

	/*Acceso Variable auxiliar*/
	t41 = SP + 3
	t2 = STACK[int(t41)]
	STACK[int(t40)] = t2

	/*Declaracion Variable auxiliar*/
	t42 = SP + 8
	STACK[int(t42)] = 0

	/*Asignacion Variable auxiliar*/

	/*Acceso Variable origen*/
	t43 = SP + 2
	t1 = STACK[int(t43)]
	STACK[int(t42)] = t1

	/*Declaracion Variable destino*/
	t44 = SP + 9
	STACK[int(t44)] = 0

	/*Asignacion Variable destino*/

	/*Acceso Variable destino*/
	t45 = SP + 4
	t3 = STACK[int(t45)]
	STACK[int(t44)] = t3

	/*moviendo puntero al ambito del stack de hanoi*/
	SP = SP + 5
	hanoi()

	/*obteniendo return funcion hanoi*/
	t46 = SP + 0
	t47 = STACK[int(t46)]

	/*restableciendo puntero al ambito anterior de hanoi*/
	SP = SP - 5

	/*reiniciando temporales funcion hanoi*/
	t48 = SP + 1
	t0 = STACK[int(t48)]
	t49 = SP + 2
	t1 = STACK[int(t49)]
	t50 = SP + 3
	t2 = STACK[int(t50)]
	t51 = SP + 4
	t3 = STACK[int(t51)]
	goto L3
L3:
	goto L0
L0:
	return
}

func main() {
	HP = 0
	SP = 0

	/*INSTRUCCION DE LLAMADA DE FUNCION hanoi*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS hanoi*/

	/*Declaracion Variable discos*/
	t52 = SP + 2
	STACK[int(t52)] = 0

	/*Asignacion Variable discos*/
	STACK[int(t52)] = 3.0

	/*Declaracion Variable origen*/
	t53 = SP + 3
	STACK[int(t53)] = 0

	/*Asignacion Variable origen*/
	STACK[int(t53)] = 1.0

	/*Declaracion Variable auxiliar*/
	t54 = SP + 4
	STACK[int(t54)] = 0

	/*Asignacion Variable auxiliar*/
	STACK[int(t54)] = 2.0

	/*Declaracion Variable destino*/
	t55 = SP + 5
	STACK[int(t55)] = 0

	/*Asignacion Variable destino*/
	STACK[int(t55)] = 3.0

	/*moviendo puntero al ambito del stack de hanoi*/
	SP = SP + 1
	hanoi()

	/*obteniendo return funcion hanoi*/
	t56 = SP + 0
	t57 = STACK[int(t56)]

	/*restableciendo puntero al ambito anterior de hanoi*/
	SP = SP - 1

	/*reiniciando temporales funcion hanoi*/
	t58 = SP + 1
	t0 = STACK[int(t58)]
	t59 = SP + 2
	t1 = STACK[int(t59)]
	t60 = SP + 3
	t2 = STACK[int(t60)]
	t61 = SP + 4
	t3 = STACK[int(t61)]

}
