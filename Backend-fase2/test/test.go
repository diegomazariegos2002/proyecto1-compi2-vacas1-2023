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
t10,t11 float64 
)
func bubbleSort(){

/*console.log*/

/*Acceso Variable arr*/
t1 = SP + 1;
t0 = STACK[int(t1)];
fmt.Printf("%f", t0)
fmt.Printf("%c", int(10))
func swap(){

/*console.log*/

/*Acceso Variable i*/
t3 = SP + 1;
t2 = STACK[int(t3)];
fmt.Printf("%f", t2)
fmt.Printf("%c", int(10))
goto L1;
L1:
return;
}


/*INSTRUCCION DE LLAMADA DE FUNCION swap*/

/*DECLARACION Y ASIGNACION DE PARAMETROS swap*/

/*Declaracion Variable i*/
t4 = SP + 3;
STACK[int (t4)] = 0;

/*Asignacion Variable i*/
STACK[int(t4)] = 3.0;

/*moviendo puntero al ambito del stack de swap*/
SP = SP + 2;
swap();

/*obteniendo return funcion swap*/
t5 = SP + 0;
t6 = STACK[int(t5)];

/*restableciendo puntero al ambito anterior de swap*/
SP = SP - 2;

/*reiniciando temporales funcion swap*/
t7 = SP + 1;
t2 = STACK[int(t7)];
goto L0;
L0:
return;
}

func main() {
 HP = 0
 SP = 0

/*INSTRUCCION DE LLAMADA DE FUNCION bubbleSort*/

/*DECLARACION Y ASIGNACION DE PARAMETROS bubbleSort*/

/*Declaracion Variable arr*/
t8 = SP + 3;
STACK[int (t8)] = 0;

/*Asignacion Variable arr*/
STACK[int(t8)] = 4.0;

/*moviendo puntero al ambito del stack de bubbleSort*/
SP = SP + 2;
bubbleSort();

/*obteniendo return funcion bubbleSort*/
t9 = SP + 0;
t10 = STACK[int(t9)];

/*restableciendo puntero al ambito anterior de bubbleSort*/
SP = SP - 2;

/*reiniciando temporales funcion bubbleSort*/
t11 = SP + 1;
t0 = STACK[int(t11)];

}