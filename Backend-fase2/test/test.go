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
t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,
t40,t41,t42,t43,t44,t45,t46,t47,t48,t49,
t50,t51,t52,t53,t54,t55,t56,t57,t58,t59,
t60,t61,t62,t63,t64,t65,t66,t67,t68,t69,
t70,t71,t72,t73,t74,t75,t76,t77,t78,t79,
t80,t81,t82,t83,t84,t85,t86,t87,t88,t89,
t90,t91,t92,t93,t94,t95,t96,t97,t98,t99,
t100,t101,t102,t103,t104,t105 float64 
)
func bubbleSort(){
func swap(){

/*Declaracion Variable temp*/

/*Acceso Variable i*/
t41 = SP + 1;
t38 = STACK[int(t41)];

/*ACCESO A VECTOR*/
t43 = 0;
t44 = HEAP[int(t40)];
t45 = t40 + 1;
t46 = 0;
L33:
if t44 > t46 {goto L34}
goto L35;
L34:
if t46 == t38 {goto L36}
goto L37;
L36:
t48 = t45 + t46;
t43 = 1;
t42 = HEAP[int(t48)];
goto L35;
L37:
t48 = t45 + t46;
t47 = HEAP[int(t48)];
t46 = t46 + 1;
goto L33;
L35:
if t43 == 0 {goto L38}
goto L39;
L38:
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
L39:
t49 = SP + 4;
STACK[int (t49)] = t42;

/*Acceso Variable i*/
t58 = SP + 1;
t38 = STACK[int(t58)];

/*ASIGNACION EN VECTOR*/
t59 = 0;
t60 = HEAP[int(t40)];
t61 = t40 + 1;
t62 = 0;
L47:
if t60 > t62 {goto L48}
goto L49;
L48:
if t62 == t38 {goto L50}
goto L51;
L50:
t64 = t61 + t62;
t59 = 1;
HEAP[int(t64)] = t51;
goto L49;
L51:
t64 = t61 + t62;
t63 = HEAP[int(t64)];
t62 = t62 + 1;
goto L47;
L49:
if t59 == 0 {goto L52}
goto L53;
L52:
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
L53:

/*Acceso Variable j*/
t66 = SP + 2;
t39 = STACK[int(t66)];

/*ASIGNACION EN VECTOR*/
t67 = 0;
t68 = HEAP[int(t40)];
t69 = t40 + 1;
t70 = 0;
L54:
if t68 > t70 {goto L55}
goto L56;
L55:
if t70 == t39 {goto L57}
goto L58;
L57:
t72 = t69 + t70;
t67 = 1;
HEAP[int(t72)] = t49;
goto L56;
L58:
t72 = t69 + t70;
t71 = HEAP[int(t72)];
t70 = t70 + 1;
goto L54;
L56:
if t67 == 0 {goto L59}
goto L60;
L59:
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
L60:
goto L32;
L32:
return;
}


/*INSTRUCCION FOR*/

/*DECLARACION FOR*/

/*Declaracion Variable i*/
t8 = SP + 2;
STACK[int (t8)] = 0.0;

/*CONDICION FOR*/
L3:

/*EXPRESIONES RELACION  < */

/*EXPRESION IZQUIERDA t8 [ < ]*/

/*Acceso Variable i*/
t9 = SP + 2;
t8 = STACK[int(t9)];

/*EXPRESION DERECHA t12 [ < ]*/

/*EXPRESIONES RESTA*/

/*FUNCION LENGTH*/

/*Acceso Variable arr*/
t10 = SP + 1;
t7 = STACK[int(t10)];
t11 = HEAP[int(t7)];

/*OPERACION RESTA*/
t12 = t11 - 1.0
if t8 < t12 {goto L5}
t13 = 0;
goto L6;
L5:
t13 = 1;
L6:
if t13==1 {goto L2}
goto L4;

/*CUERPO FOR*/
L2:

/*INSTRUCCION FOR*/

/*DECLARACION FOR*/

/*Declaracion Variable j*/
t14 = SP + 3;
STACK[int (t14)] = 1.0;

/*CONDICION FOR*/
L9:

/*EXPRESIONES RELACION  < */

/*EXPRESION IZQUIERDA t14 [ < ]*/

/*Acceso Variable j*/
t15 = SP + 3;
t14 = STACK[int(t15)];

/*EXPRESION DERECHA t18 [ < ]*/

/*EXPRESIONES RESTA*/

/*FUNCION LENGTH*/

/*Acceso Variable arr*/
t16 = SP + 1;
t7 = STACK[int(t16)];
t17 = HEAP[int(t7)];

/*OPERACION RESTA*/
t18 = t17 - 1.0
if t14 < t18 {goto L11}
t19 = 0;
goto L12;
L11:
t19 = 1;
L12:
if t19==1 {goto L8}
goto L10;

/*CUERPO FOR*/
L8:

/*INSTRUCCION IF*/

/*CONDICION IF*/

/*EXPRESIONES RELACION  > */

/*EXPRESION IZQUIERDA t21 [ > ]*/

/*Acceso Variable j*/
t20 = SP + 3;
t14 = STACK[int(t20)];

/*ACCESO A VECTOR*/
t22 = 0;
t23 = HEAP[int(t7)];
t24 = t7 + 1;
t25 = 0;
L13:
if t23 > t25 {goto L14}
goto L15;
L14:
if t25 == t14 {goto L16}
goto L17;
L16:
t27 = t24 + t25;
t22 = 1;
t21 = HEAP[int(t27)];
goto L15;
L17:
t27 = t24 + t25;
t26 = HEAP[int(t27)];
t25 = t25 + 1;
goto L13;
L15:
if t22 == 0 {goto L18}
goto L19;
L18:
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
L19:

/*EXPRESION DERECHA t30 [ > ]*/

/*EXPRESIONES SUMA*/

/*Acceso Variable j*/
t28 = SP + 3;
t14 = STACK[int(t28)];

/*OPERACION SUMA*/
t29 = t14 + 1.0

/*ACCESO A VECTOR*/
t31 = 0;
t32 = HEAP[int(t7)];
t33 = t7 + 1;
t34 = 0;
L20:
if t32 > t34 {goto L21}
goto L22;
L21:
if t34 == t29 {goto L23}
goto L24;
L23:
t36 = t33 + t34;
t31 = 1;
t30 = HEAP[int(t36)];
goto L22;
L24:
t36 = t33 + t34;
t35 = HEAP[int(t36)];
t34 = t34 + 1;
goto L20;
L22:
if t31 == 0 {goto L25}
goto L26;
L25:
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
L26:
if t21 > t30 {goto L27}
t37 = 0;
goto L28;
L27:
t37 = 1;
L28:

/*VALIDACION IF*/
if t37==1 {goto L30}
goto L31;
L30: 

/*INSTRUCCION DE LLAMADA DE FUNCION swap*/

/*DECLARACION Y ASIGNACION DE PARAMETROS swap*/

/*Declaracion Variable i*/
t73 = SP + 5;
STACK[int (t73)] = 0;

/*Asignacion Variable i*/

/*Acceso Variable j*/
t74 = SP + 3;
t14 = STACK[int(t74)];
STACK[int(t73)] = t14;

/*Declaracion Variable j*/
t75 = SP + 6;
STACK[int (t75)] = 0;

/*Asignacion Variable j*/

/*EXPRESIONES SUMA*/

/*Acceso Variable j*/
t76 = SP + 3;
t14 = STACK[int(t76)];

/*OPERACION SUMA*/
t77 = t14 + 1.0
STACK[int(t75)] = t77;

/*Declaracion Variable arr*/
t78 = SP + 7;
STACK[int (t78)] = 0;

/*Asignacion Variable arr*/

/*Acceso Variable arr*/
t79 = SP + 1;
t7 = STACK[int(t79)];
STACK[int(t78)] = t7;

/*moviendo puntero al ambito del stack de swap*/
SP = SP + 4;
swap();

/*obteniendo return funcion swap*/
t80 = SP + 0;
t81 = STACK[int(t80)];

/*restableciendo puntero al ambito anterior de swap*/
SP = SP - 4;

/*reiniciando temporales funcion swap*/
t82 = SP + 1;
t38 = STACK[int(t82)];
t83 = SP + 2;
t39 = STACK[int(t83)];
t84 = SP + 3;
t40 = STACK[int(t84)];
t85 = SP + 4;
t49 = STACK[int(t85)];
goto L29;
L31: 
goto L29;
L29: 

/*ASIGNACION FOR*/
goto L7;
L7:

/*INSTRUCCION INCREMENTO*/
t86 = SP + 3;
t87 = STACK[int(t86)];

/*Asignacion Variable j*/
t88 = t87+1;
STACK[int(t86)] = t88;
goto L9;

/*FIN FOR*/
L10:

/*ASIGNACION FOR*/
goto L1;
L1:

/*INSTRUCCION INCREMENTO*/
t89 = SP + 2;
t90 = STACK[int(t89)];

/*Asignacion Variable i*/
t91 = t90+1;
STACK[int(t89)] = t91;
goto L3;

/*FIN FOR*/
L4:
goto L0;
L0:
return;
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
t1 = math.Pow(9874.0 , 0.0)

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
t5 = HP;
HEAP[int(HP)] = 16;
HP = HP + 1;
HEAP[int(HP)] = 32.0;
HP = HP + 1;
HEAP[int(HP)] = t0;
HP = HP + 1;
HEAP[int(HP)] = 7.0;
HP = HP + 1;
HEAP[int(HP)] = 89.0;
HP = HP + 1;
HEAP[int(HP)] = 56.0;
HP = HP + 1;
HEAP[int(HP)] = 909.0;
HP = HP + 1;
HEAP[int(HP)] = 109.0;
HP = HP + 1;
HEAP[int(HP)] = 2.0;
HP = HP + 1;
HEAP[int(HP)] = 9.0;
HP = HP + 1;
HEAP[int(HP)] = t1;
HP = HP + 1;
HEAP[int(HP)] = 44.0;
HP = HP + 1;
HEAP[int(HP)] = 3.0;
HP = HP + 1;
HEAP[int(HP)] = t2;
HP = HP + 1;
HEAP[int(HP)] = 11.0;
HP = HP + 1;
HEAP[int(HP)] = t4;
HP = HP + 1;
HEAP[int(HP)] = 10.0;
HP = HP + 1;
t6 = SP + 3;
STACK[int (t6)] = t5;

/*INSTRUCCION DE LLAMADA DE FUNCION bubbleSort*/

/*DECLARACION Y ASIGNACION DE PARAMETROS bubbleSort*/

/*Declaracion Variable arr*/
t92 = SP + 5;
STACK[int (t92)] = 0;

/*Asignacion Variable arr*/

/*Acceso Variable arreglo*/
t93 = SP + 3;
t6 = STACK[int(t93)];
STACK[int(t92)] = t6;

/*moviendo puntero al ambito del stack de bubbleSort*/
SP = SP + 4;
bubbleSort();

/*obteniendo return funcion bubbleSort*/
t94 = SP + 0;
t95 = STACK[int(t94)];

/*restableciendo puntero al ambito anterior de bubbleSort*/
SP = SP - 4;

/*reiniciando temporales funcion bubbleSort*/
t96 = SP + 1;
t7 = STACK[int(t96)];

/*console.log*/

/*PRIMITIVO -> CADENA*/
t97 = HP;
HEAP[int(HP)] = 66.0;
HP = HP + 1;
HEAP[int(HP)] = 117.0;
HP = HP + 1;
HEAP[int(HP)] = 98.0;
HP = HP + 1;
HEAP[int(HP)] = 98.0;
HP = HP + 1;
HEAP[int(HP)] = 108.0;
HP = HP + 1;
HEAP[int(HP)] = 101.0;
HP = HP + 1;
HEAP[int(HP)] = 83.0;
HP = HP + 1;
HEAP[int(HP)] = 111.0;
HP = HP + 1;
HEAP[int(HP)] = 114.0;
HP = HP + 1;
HEAP[int(HP)] = 116.0;
HP = HP + 1;
HEAP[int(HP)] = 32.0;
HP = HP + 1;
HEAP[int(HP)] = 61.0;
HP = HP + 1;
HEAP[int(HP)] = 62.0;
HP = HP + 1;
HEAP[int(HP)] = 32.0;
HP = HP + 1;
HEAP[int(HP)] = -1;
HP = HP + 1;

/*Acceso Variable arreglo*/
t100 = SP + 3;
t6 = STACK[int(t100)];
t98 = t97;
L61:
t99 = HEAP[int(t98)];
if t99 == -1 {goto L62}
fmt.Printf("%c", int(t99))
t98 = t98 + 1;
goto L61;
L62:
fmt.Printf("%c", int(91))
fmt.Printf("%c", int(32))
t101 = HEAP[int(t6)];
t102 = t6 + 1;
t103 = 0;
L63:
if t101 > t103 {goto L64}
goto L65;
L64:
t105 = t102 + t103;
t104 = HEAP[int (t105)];
fmt.Printf("%f", t104)
t103 = t103 + 1;
fmt.Printf("%c", int(32))
goto L63;
L65:
fmt.Printf("%c", int(93))
fmt.Printf("%c", int(10))
fmt.Printf("%c", int(10))

}