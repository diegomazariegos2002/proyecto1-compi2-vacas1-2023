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
	t40, t41, t42, t43, t44, t45, t46, t47, t48 float64
)

func ackermann() {

	/*INSTRUCCION IF*/

	/*CONDICION IF*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t0 [ == ]*/

	/*Acceso Variable m*/
	t2 = SP + 1
	t0 = STACK[int(t2)]

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if t0 == 0.0 {
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

	/*EXPRESIONES SUMA*/

	/*Acceso Variable n*/
	t4 = SP + 2
	t1 = STACK[int(t4)]

	/*OPERACION SUMA*/
	t5 = t1 + 1.0
	t6 = SP + 0
	STACK[int(t6)] = t5
	goto L3
L5:

	/*ELSE IF*/

	/*INSTRUCCION IF*/

	/*CONDICION IF*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t8 [&&]*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA t0 [ > ]*/

	/*Acceso Variable m*/
	t7 = SP + 1
	t0 = STACK[int(t7)]

	/*EXPRESION DERECHA 0.0 [ > ]*/
	if t0 > 0.0 {
		goto L6
	}
	t8 = 0
	goto L7
L6:
	t8 = 1
L7:

	/*EXPRESION DERECHA t10 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t1 [ == ]*/

	/*Acceso Variable n*/
	t9 = SP + 2
	t1 = STACK[int(t9)]

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if t1 == 0.0 {
		goto L8
	}
	t10 = 0
	goto L9
L8:
	t10 = 1
L9:

	/*LOGICA AND t8 t10*/
	t11 = t8
	t12 = t10
	if t11 == 1 && t12 == 1 {
		goto L11
	}
	t13 = 0
	goto L10
L11:
	t13 = 1
L10:

	/*VALIDACION IF*/
	if t13 == 1 {
		goto L12
	}
	goto L13
L12:

	/*INSTRUCCION RETURN*/

	/*EXPRESION RETURN*/

	/*INSTRUCCION DE LLAMADA DE FUNCION ackermann*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS ackermann*/

	/*Declaracion Variable m*/
	t14 = SP + 4
	STACK[int(t14)] = 0

	/*Asignacion Variable m*/

	/*EXPRESIONES RESTA*/

	/*Acceso Variable m*/
	t15 = SP + 1
	t0 = STACK[int(t15)]

	/*OPERACION RESTA*/
	t16 = t0 - 1.0
	STACK[int(t14)] = t16

	/*Declaracion Variable n*/
	t17 = SP + 5
	STACK[int(t17)] = 0

	/*Asignacion Variable n*/
	STACK[int(t17)] = 1.0

	/*moviendo puntero al ambito del stack de ackermann*/
	SP = SP + 3
	ackermann()

	/*obteniendo return funcion ackermann*/
	t18 = SP + 0
	t19 = STACK[int(t18)]

	/*restableciendo puntero al ambito anterior de ackermann*/
	SP = SP - 3

	/*reiniciando temporales funcion ackermann*/
	t20 = SP + 1
	t0 = STACK[int(t20)]
	t21 = SP + 2
	t1 = STACK[int(t21)]
	t22 = SP + 0
	STACK[int(t22)] = t19
	goto L3
L13:

	/*ELSE*/

	/*INSTRUCCION RETURN*/

	/*EXPRESION RETURN*/

	/*INSTRUCCION DE LLAMADA DE FUNCION ackermann*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS ackermann*/

	/*Declaracion Variable m*/
	t23 = SP + 4
	STACK[int(t23)] = 0

	/*Asignacion Variable m*/

	/*EXPRESIONES RESTA*/

	/*Acceso Variable m*/
	t24 = SP + 1
	t0 = STACK[int(t24)]

	/*OPERACION RESTA*/
	t25 = t0 - 1.0
	STACK[int(t23)] = t25

	/*Declaracion Variable n*/
	t26 = SP + 5
	STACK[int(t26)] = 0

	/*Asignacion Variable n*/

	/*INSTRUCCION DE LLAMADA DE FUNCION ackermann*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS ackermann*/

	/*Declaracion Variable m*/
	t27 = SP + 6
	STACK[int(t27)] = 0

	/*Asignacion Variable m*/

	/*Acceso Variable m*/
	t28 = SP + 1
	t0 = STACK[int(t28)]
	STACK[int(t27)] = t0

	/*Declaracion Variable n*/
	t29 = SP + 7
	STACK[int(t29)] = 0

	/*Asignacion Variable n*/

	/*EXPRESIONES RESTA*/

	/*Acceso Variable n*/
	t30 = SP + 2
	t1 = STACK[int(t30)]

	/*OPERACION RESTA*/
	t31 = t1 - 1.0
	STACK[int(t29)] = t31

	/*moviendo puntero al ambito del stack de ackermann*/
	SP = SP + 5
	ackermann()

	/*obteniendo return funcion ackermann*/
	t32 = SP + 0
	t33 = STACK[int(t32)]

	/*restableciendo puntero al ambito anterior de ackermann*/
	SP = SP - 5

	/*reiniciando temporales funcion ackermann*/
	t34 = SP + 1
	t0 = STACK[int(t34)]
	t35 = SP + 2
	t1 = STACK[int(t35)]
	STACK[int(t26)] = t33

	/*moviendo puntero al ambito del stack de ackermann*/
	SP = SP + 3
	ackermann()

	/*obteniendo return funcion ackermann*/
	t36 = SP + 0
	t37 = STACK[int(t36)]

	/*restableciendo puntero al ambito anterior de ackermann*/
	SP = SP - 3

	/*reiniciando temporales funcion ackermann*/
	t38 = SP + 1
	t0 = STACK[int(t38)]
	t39 = SP + 2
	t1 = STACK[int(t39)]
	t40 = SP + 0
	STACK[int(t40)] = t37
	goto L3
L3:
	goto L0
L0:
	return
}

func main() {
	HP = 0
	SP = 0

	/*Declaracion Variable result*/

	/*INSTRUCCION DE LLAMADA DE FUNCION ackermann*/

	/*DECLARACION Y ASIGNACION DE PARAMETROS ackermann*/

	/*Declaracion Variable m*/
	t41 = SP + 2
	STACK[int(t41)] = 0

	/*Asignacion Variable m*/
	STACK[int(t41)] = 3.0

	/*Declaracion Variable n*/
	t42 = SP + 3
	STACK[int(t42)] = 0

	/*Asignacion Variable n*/
	STACK[int(t42)] = 2.0

	/*moviendo puntero al ambito del stack de ackermann*/
	SP = SP + 1
	ackermann()

	/*obteniendo return funcion ackermann*/
	t43 = SP + 0
	t44 = STACK[int(t43)]

	/*restableciendo puntero al ambito anterior de ackermann*/
	SP = SP - 1

	/*reiniciando temporales funcion ackermann*/
	t45 = SP + 1
	t0 = STACK[int(t45)]
	t46 = SP + 2
	t1 = STACK[int(t46)]
	t47 = SP + 1
	STACK[int(t47)] = t44

	/*console.log*/

	/*Acceso Variable result*/
	t48 = SP + 1
	t47 = STACK[int(t48)]
	fmt.Printf("%f", t47)
	fmt.Printf("%c", int(10))

}
