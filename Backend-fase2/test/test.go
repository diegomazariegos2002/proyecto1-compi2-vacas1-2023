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
t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,
t30,t31 float64 
)
func impar(){

/*INSTRUCCION IF*/

/*CONDICION IF*/

/*EXPRESIONES RELACION  == */

/*EXPRESION IZQUIERDA t0 [ == ]*/

/*Acceso Variable num*/
t1 = SP + 1;
t0 = STACK[int(t1)];

/*EXPRESION DERECHA 0.0 [ == ]*/
if t0 == 0.0 {goto L1}
t2 = 0;
goto L2;
L1:
t2 = 1;
L2:

/*VALIDACION IF*/
if t2==1 {goto L4}
goto L5;
L4: 

/*INSTRUCCION RETURN*/

/*EXPRESION RETURN*/
t3 = SP + 0;
STACK[int(t3)] = 0;
goto L3;
L5: 
goto L3;
L3: 

/*Declaracion Variable a*/

/*INSTRUCCION DE LLAMADA DE FUNCION par*/

/*DECLARACION Y ASIGNACION DE PARAMETROS par*/

/*Declaracion Variable num*/
t17 = SP + 3;
STACK[int (t17)] = 0;

/*Asignacion Variable num*/

/*EXPRESIONES RESTA*/

/*Acceso Variable num*/
t18 = SP + 1;
t0 = STACK[int(t18)];

/*OPERACION RESTA*/
t19 = t0 - 1.0
STACK[int(t17)] = t19;

/*moviendo puntero al ambito del stack de par*/
SP = SP + 2;
par();

/*obteniendo return funcion par*/
t20 = SP + 0;
t21 = STACK[int(t20)];

/*restableciendo puntero al ambito anterior de par*/
SP = SP - 2;

/*reiniciando temporales funcion par*/
t22 = SP + 1;
t4 = STACK[int(t22)];
t23 = SP + 2;
t14 = STACK[int(t23)];
t24 = SP + 2;
STACK[int (t24)] = t21;

/*INSTRUCCION RETURN*/

/*EXPRESION RETURN*/

/*Acceso Variable a*/
t25 = SP + 2;
t24 = STACK[int(t25)];
t26 = SP + 0;
STACK[int(t26)] = t24;
goto L0;
L0:
return;
}

func par(){

/*INSTRUCCION IF*/

/*CONDICION IF*/

/*EXPRESIONES RELACION  == */

/*EXPRESION IZQUIERDA t4 [ == ]*/

/*Acceso Variable num*/
t5 = SP + 1;
t4 = STACK[int(t5)];

/*EXPRESION DERECHA 0.0 [ == ]*/
if t4 == 0.0 {goto L7}
t6 = 0;
goto L8;
L7:
t6 = 1;
L8:

/*VALIDACION IF*/
if t6==1 {goto L10}
goto L11;
L10: 

/*INSTRUCCION RETURN*/

/*EXPRESION RETURN*/
t7 = SP + 0;
STACK[int(t7)] = 1;
goto L9;
L11: 
goto L9;
L9: 

/*Declaracion Variable a*/

/*INSTRUCCION DE LLAMADA DE FUNCION impar*/

/*DECLARACION Y ASIGNACION DE PARAMETROS impar*/

/*Declaracion Variable num*/
t8 = SP + 3;
STACK[int (t8)] = 0;

/*Asignacion Variable num*/

/*EXPRESIONES RESTA*/

/*Acceso Variable num*/
t9 = SP + 1;
t4 = STACK[int(t9)];

/*OPERACION RESTA*/
t10 = t4 - 1.0
STACK[int(t8)] = t10;

/*moviendo puntero al ambito del stack de impar*/
SP = SP + 2;
impar();

/*obteniendo return funcion impar*/
t11 = SP + 0;
t12 = STACK[int(t11)];

/*restableciendo puntero al ambito anterior de impar*/
SP = SP - 2;

/*reiniciando temporales funcion impar*/
t13 = SP + 1;
t0 = STACK[int(t13)];
t14 = SP + 2;
STACK[int (t14)] = t12;

/*INSTRUCCION RETURN*/

/*EXPRESION RETURN*/

/*Acceso Variable a*/
t15 = SP + 2;
t14 = STACK[int(t15)];
t16 = SP + 0;
STACK[int(t16)] = t14;
goto L6;
L6:
return;
}

func main() {
 HP = 0
 SP = 0

/*console.log*/

/*INSTRUCCION DE LLAMADA DE FUNCION impar*/

/*DECLARACION Y ASIGNACION DE PARAMETROS impar*/

/*Declaracion Variable num*/
t27 = SP + 3;
STACK[int (t27)] = 0;

/*Asignacion Variable num*/
STACK[int(t27)] = 251.0;

/*moviendo puntero al ambito del stack de impar*/
SP = SP + 2;
impar();

/*obteniendo return funcion impar*/
t28 = SP + 0;
t29 = STACK[int(t28)];

/*restableciendo puntero al ambito anterior de impar*/
SP = SP - 2;

/*reiniciando temporales funcion impar*/
t30 = SP + 1;
t0 = STACK[int(t30)];
t31 = SP + 2;
t24 = STACK[int(t31)];
if t29==1 {goto L12}
fmt.Printf("%c", int(102))
fmt.Printf("%c", int(97))
fmt.Printf("%c", int(108))
fmt.Printf("%c", int(115))
fmt.Printf("%c", int(101))
goto L13;
L12:
fmt.Printf("%c", int(116))
fmt.Printf("%c", int(114))
fmt.Printf("%c", int(117))
fmt.Printf("%c", int(101))
L13:
fmt.Printf("%c", int(10))

}