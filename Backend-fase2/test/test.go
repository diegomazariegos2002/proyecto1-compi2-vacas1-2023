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
	t80, t81, t82, t83, t84, t85, t86, t87, t88, t89,
	t90, t91, t92, t93, t94, t95, t96, t97, t98, t99,
	t100, t101, t102, t103, t104, t105, t106, t107, t108, t109,
	t110, t111, t112, t113, t114, t115, t116, t117, t118, t119,
	t120, t121, t122, t123, t124, t125, t126, t127, t128, t129,
	t130, t131, t132, t133, t134, t135, t136, t137, t138, t139,
	t140, t141, t142, t143, t144, t145, t146, t147, t148, t149,
	t150, t151, t152, t153, t154, t155, t156, t157, t158, t159,
	t160, t161, t162, t163, t164, t165, t166, t167, t168, t169,
	t170, t171, t172, t173, t174, t175, t176, t177, t178, t179,
	t180, t181, t182 float64
)

func main() {
	HP = 0
	SP = 0

	/*console.log*/

	/*CADENAS CONCATENACION*/

	/*CADENAS CONCATENACION*/

	/*PRIMITIVO -> CADENA*/
	t0 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*PRIMITIVO -> CADENA*/
	t1 = HP
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 77.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 110.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*OPERACION CONCATENACION*/
	t2 = HP
	t3 = t0
L0:
	t4 = HEAP[int(t3)]
	if t4 == -1 {
		goto L1
	}
	HEAP[int(HP)] = t4
	HP = HP + 1
	t3 = t3 + 1
	goto L0
L1:
	t3 = t1
L2:
	t4 = HEAP[int(t3)]
	if t4 == -1 {
		goto L3
	}
	HEAP[int(HP)] = t4
	HP = HP + 1
	t3 = t3 + 1
	goto L2
L3:
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*PRIMITIVO -> CADENA*/
	t5 = HP
	HEAP[int(HP)] = 32.0
	HP = HP + 1
	HEAP[int(HP)] = 49.0
	HP = HP + 1
	HEAP[int(HP)] = 50.0
	HP = HP + 1
	HEAP[int(HP)] = 51.0
	HP = HP + 1
	HEAP[int(HP)] = 49.0
	HP = HP + 1
	HEAP[int(HP)] = 50.0
	HP = HP + 1
	HEAP[int(HP)] = 51.0
	HP = HP + 1
	HEAP[int(HP)] = 49.0
	HP = HP + 1
	HEAP[int(HP)] = 50.0
	HP = HP + 1
	HEAP[int(HP)] = 51.0
	HP = HP + 1
	HEAP[int(HP)] = 49.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*OPERACION CONCATENACION*/
	t6 = HP
	t7 = t2
L4:
	t8 = HEAP[int(t7)]
	if t8 == -1 {
		goto L5
	}
	HEAP[int(HP)] = t8
	HP = HP + 1
	t7 = t7 + 1
	goto L4
L5:
	t7 = t5
L6:
	t8 = HEAP[int(t7)]
	if t8 == -1 {
		goto L7
	}
	HEAP[int(HP)] = t8
	HP = HP + 1
	t7 = t7 + 1
	goto L6
L7:
	HEAP[int(HP)] = -1
	HP = HP + 1
	t9 = t6
L8:
	t10 = HEAP[int(t9)]
	if t10 == -1 {
		goto L9
	}
	fmt.Printf("%c", int(t10))
	t9 = t9 + 1
	goto L8
L9:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RESTA*/

	/*EXPRESIONES RESTA*/

	/*EXPRESIONES DIVISION*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t11 = 123.0 * 4.0

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t12 = 2.0 * 2.0

	/*OPERACION SUMA*/
	t13 = 2.0 + t12

	/*OPERACION DIVISION*/
	t14 = t11 / t13

	/*OPERACION RESTA*/
	t15 = 41.0 - t14

	/*EXPRESIONES MULTIPLICACION*/

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MODULO*/

	/*OPERACION MODULO*/
	t16 = math.Mod(125.0, 5.0)

	/*OPERACION SUMA*/
	t17 = 10.0 + t16

	/*EXPRESIONES POTENCIA*/

	/*OPERACION POTENCIA*/
	t18 = math.Pow(2.0, 2.0)

	/*OPERACION MULTIPLICACION*/
	t19 = t17 * t18

	/*OPERACION RESTA*/
	t20 = t15 - t19
	fmt.Printf("%f", t20)
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES SUMA*/

	/*OPERACION SUMA*/
	t21 = 2.0 + 3.0
	fmt.Printf("%f", t21)
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 1 [ == ]*/

	/*EXPRESION DERECHA 0 [ == ]*/
	if 1 == 0 {
		goto L10
	}
	t22 = 0
	goto L11
L10:
	t22 = 1
L11:
	if t22 == 1 {
		goto L12
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L13
L12:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L13:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L14
	}
	t23 = 0
	goto L15
L14:
	t23 = 1
L15:
	if t23 == 1 {
		goto L16
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L17
L16:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L17:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  <= */

	/*EXPRESION IZQUIERDA t24 [ <= ]*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t24 = 7.0 * 7.0

	/*EXPRESION DERECHA t25 [ <= ]*/

	/*EXPRESIONES SUMA*/

	/*OPERACION SUMA*/
	t25 = 15.0 + 555.0
	if t24 <= t25 {
		goto L18
	}
	t26 = 0
	goto L19
L18:
	t26 = 1
L19:
	if t26 == 1 {
		goto L20
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L21
L20:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L21:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA 532.0 [ > ]*/

	/*EXPRESION DERECHA 532.0 [ > ]*/
	if 532.0 > 532.0 {
		goto L22
	}
	t27 = 0
	goto L23
L22:
	t27 = 1
L23:
	if t27 == 1 {
		goto L24
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L25
L24:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L25:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t28 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t28 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t29 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t29 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION IGUALDAD t28 t29*/
	t30 = t28
	t31 = t29
L35:
	t33 = HEAP[int(t30)]
	t34 = HEAP[int(t31)]
	if t33 == -1 {
		goto L32
	}
	t35 = 0
	goto L29
L32:
	t35 = 1
L29:
	if t34 == -1 {
		goto L33
	}
	t36 = 0
	goto L30
L33:
	t36 = 1
L30:
	if t35 == 1 && t36 == 1 {
		goto L34
	}
	t37 = 0
	goto L31
L34:
	t37 = 1
L31:
	if t37 == 1 {
		goto L26
	}
	if t33 != t34 {
		goto L27
	}
	t30 = t30 + 1
	t31 = t31 + 1
	goto L35
L26:
	t32 = 1
	goto L28
L27:
	t32 = 0
L28:
	if t32 == 1 {
		goto L36
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L37
L36:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L37:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t38 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t38 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t39 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t39 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION IGUALDAD t38 t39*/
	t40 = t38
	t41 = t39
L47:
	t43 = HEAP[int(t40)]
	t44 = HEAP[int(t41)]
	if t43 == -1 {
		goto L44
	}
	t45 = 0
	goto L41
L44:
	t45 = 1
L41:
	if t44 == -1 {
		goto L45
	}
	t46 = 0
	goto L42
L45:
	t46 = 1
L42:
	if t45 == 1 && t46 == 1 {
		goto L46
	}
	t47 = 0
	goto L43
L46:
	t47 = 1
L43:
	if t47 == 1 {
		goto L38
	}
	if t43 != t44 {
		goto L39
	}
	t40 = t40 + 1
	t41 = t41 + 1
	goto L47
L38:
	t42 = 1
	goto L40
L39:
	t42 = 0
L40:
	if t42 == 1 {
		goto L48
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L49
L48:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L49:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t48 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t48 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t49 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t49 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION DIFERENCIA t48 t49*/
	t50 = t48
	t51 = t49
L59:
	t53 = HEAP[int(t50)]
	t54 = HEAP[int(t51)]
	if t53 == -1 {
		goto L56
	}
	t55 = 0
	goto L53
L56:
	t55 = 1
L53:
	if t54 == -1 {
		goto L57
	}
	t56 = 0
	goto L54
L57:
	t56 = 1
L54:
	if t55 == 1 && t56 == 1 {
		goto L58
	}
	t57 = 0
	goto L55
L58:
	t57 = 1
L55:
	if t57 == 1 {
		goto L50
	}
	if t53 != t54 {
		goto L51
	}
	t50 = t50 + 1
	t51 = t51 + 1
	goto L59
L50:
	t52 = 1
	goto L52
L51:
	t52 = 0
L52:
	t59 = t52
	if t59 == 1 {
		goto L61
	}
	t60 = 1
	goto L60
L61:
	t60 = 0
L60:
	t58 = t60
	if t58 == 1 {
		goto L62
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L63
L62:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L63:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t61 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t61 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t62 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t62 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION DIFERENCIA t61 t62*/
	t63 = t61
	t64 = t62
L73:
	t66 = HEAP[int(t63)]
	t67 = HEAP[int(t64)]
	if t66 == -1 {
		goto L70
	}
	t68 = 0
	goto L67
L70:
	t68 = 1
L67:
	if t67 == -1 {
		goto L71
	}
	t69 = 0
	goto L68
L71:
	t69 = 1
L68:
	if t68 == 1 && t69 == 1 {
		goto L72
	}
	t70 = 0
	goto L69
L72:
	t70 = 1
L69:
	if t70 == 1 {
		goto L64
	}
	if t66 != t67 {
		goto L65
	}
	t63 = t63 + 1
	t64 = t64 + 1
	goto L73
L64:
	t65 = 1
	goto L66
L65:
	t65 = 0
L66:
	t72 = t65
	if t72 == 1 {
		goto L75
	}
	t73 = 1
	goto L74
L75:
	t73 = 0
L74:
	t71 = t73
	if t71 == 1 {
		goto L76
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L77
L76:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L77:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t74 = HP
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t75 = t74
L78:
	t76 = HEAP[int(t75)]
	if t76 == -1 {
		goto L79
	}
	fmt.Printf("%c", int(t76))
	t75 = t75 + 1
	goto L78
L79:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t77 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t77 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t78 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t78 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION [ < ] t77 t78*/
	t79 = t77
	t80 = t78
	t81 = HEAP[int(t79)]
	t82 = HEAP[int(t80)]
	if t81 < t82 {
		goto L81
	}
	t83 = 0
	goto L80
L81:
	t83 = 1
L80:
	if t83 == 1 {
		goto L82
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L83
L82:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L83:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA t84 [ > ]*/

	/*PRIMITIVO -> CADENA*/
	t84 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t85 [ > ]*/

	/*PRIMITIVO -> CADENA*/
	t85 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION [ > ] t84 t85*/
	t86 = t84
	t87 = t85
	t88 = HEAP[int(t86)]
	t89 = HEAP[int(t87)]
	if t88 > t89 {
		goto L85
	}
	t90 = 0
	goto L84
L85:
	t90 = 1
L84:
	if t90 == 1 {
		goto L86
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L87
L86:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L87:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t91 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t91 = HP
	HEAP[int(HP)] = 77.0
	HP = HP + 1
	HEAP[int(HP)] = 85.0
	HP = HP + 1
	HEAP[int(HP)] = 78.0
	HP = HP + 1
	HEAP[int(HP)] = 68.0
	HP = HP + 1
	HEAP[int(HP)] = 79.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t92 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t92 = HP
	HEAP[int(HP)] = 65.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 110.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION [ < ] t91 t92*/
	t93 = t91
	t94 = t92
	t95 = HEAP[int(t93)]
	t96 = HEAP[int(t94)]
	if t95 < t96 {
		goto L89
	}
	t97 = 0
	goto L88
L89:
	t97 = 1
L88:
	if t97 == 1 {
		goto L90
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L91
L90:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L91:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  <= */

	/*EXPRESION IZQUIERDA t98 [ <= ]*/

	/*PRIMITIVO -> CADENA*/
	t98 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t99 [ <= ]*/

	/*PRIMITIVO -> CADENA*/
	t99 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION [ <= ] t98 t99*/
	t100 = t98
	t101 = t99
	t102 = HEAP[int(t100)]
	t103 = HEAP[int(t101)]
	if t102 <= t103 {
		goto L93
	}
	t104 = 0
	goto L92
L93:
	t104 = 1
L92:
	if t104 == 1 {
		goto L94
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L95
L94:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L95:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  >= */

	/*EXPRESION IZQUIERDA t105 [ >= ]*/

	/*PRIMITIVO -> CADENA*/
	t105 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t106 [ >= ]*/

	/*PRIMITIVO -> CADENA*/
	t106 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 105.0
	HP = HP + 1
	HEAP[int(HP)] = 115.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION [ >= ] t105 t106*/
	t107 = t105
	t108 = t106
	t109 = HEAP[int(t107)]
	t110 = HEAP[int(t108)]
	if t109 >= t110 {
		goto L97
	}
	t111 = 0
	goto L96
L97:
	t111 = 1
L96:
	if t111 == 1 {
		goto L98
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L99
L98:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L99:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t112 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t112 = HP
	HEAP[int(HP)] = 65.0
	HP = HP + 1
	HEAP[int(HP)] = 85.0
	HP = HP + 1
	HEAP[int(HP)] = 78.0
	HP = HP + 1
	HEAP[int(HP)] = 68.0
	HP = HP + 1
	HEAP[int(HP)] = 79.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t113 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t113 = HP
	HEAP[int(HP)] = 77.0
	HP = HP + 1
	HEAP[int(HP)] = 117.0
	HP = HP + 1
	HEAP[int(HP)] = 110.0
	HP = HP + 1
	HEAP[int(HP)] = 100.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION [ < ] t112 t113*/
	t114 = t112
	t115 = t113
	t116 = HEAP[int(t114)]
	t117 = HEAP[int(t115)]
	if t116 < t117 {
		goto L101
	}
	t118 = 0
	goto L100
L101:
	t118 = 1
L100:
	if t118 == 1 {
		goto L102
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L103
L102:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L103:
	fmt.Printf("%c", int(10))

	/*console.log*/
	if 1 == 1 {
		goto L104
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L105
L104:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L105:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t119 = HP
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = 61.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1
	t120 = t119
L106:
	t121 = HEAP[int(t120)]
	if t121 == -1 {
		goto L107
	}
	fmt.Printf("%c", int(t121))
	t120 = t120 + 1
	goto L106
L107:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t122 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L108
	}
	t122 = 0
	goto L109
L108:
	t122 = 1
L109:

	/*EXPRESION DERECHA t123 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 1.0 [ == ]*/

	/*EXPRESION DERECHA 1.0 [ == ]*/
	if 1.0 == 1.0 {
		goto L110
	}
	t123 = 0
	goto L111
L110:
	t123 = 1
L111:

	/*LOGICA AND t122 t123*/
	t124 = t122
	t125 = t123
	if t124 == 1 && t125 == 1 {
		goto L113
	}
	t126 = 0
	goto L112
L113:
	t126 = 1
L112:
	if t126 == 1 {
		goto L114
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L115
L114:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L115:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA t127 [||]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L116
	}
	t127 = 0
	goto L117
L116:
	t127 = 1
L117:

	/*EXPRESION DERECHA t128 [||]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 1.0 [ == ]*/
	if 0.0 == 1.0 {
		goto L118
	}
	t128 = 0
	goto L119
L118:
	t128 = 1
L119:

	/*LOGICA OR t127 t128*/
	t129 = t127
	t130 = t128
	if t129 == 1 || t130 == 1 {
		goto L121
	}
	t131 = 0
	goto L120
L121:
	t131 = 1
L120:
	if t131 == 1 {
		goto L122
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L123
L122:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L123:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA !*/

	/*EXPRESION IZQUIERDA t136 [!]*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t132 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L124
	}
	t132 = 0
	goto L125
L124:
	t132 = 1
L125:

	/*EXPRESION DERECHA t133 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 1.0 [ == ]*/

	/*EXPRESION DERECHA 1.0 [ == ]*/
	if 1.0 == 1.0 {
		goto L126
	}
	t133 = 0
	goto L127
L126:
	t133 = 1
L127:

	/*LOGICA AND t132 t133*/
	t134 = t132
	t135 = t133
	if t134 == 1 && t135 == 1 {
		goto L129
	}
	t136 = 0
	goto L128
L129:
	t136 = 1
L128:

	/*LOGICA NOT t136*/
	t137 = t136
	if t137 == 1 {
		goto L131
	}
	t138 = 1
	goto L130
L131:
	t138 = 0
L130:
	if t138 == 1 {
		goto L132
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L133
L132:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L133:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t152 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t141 [ == ]*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t139 [ != ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L134
	}
	t139 = 0
	goto L135
L134:
	t139 = 1
L135:

	/*EXPRESION DERECHA t140 [ != ]*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA 532.0 [ > ]*/

	/*EXPRESION DERECHA 532.0 [ > ]*/
	if 532.0 > 532.0 {
		goto L136
	}
	t140 = 0
	goto L137
L136:
	t140 = 1
L137:
	if t139 != t140 {
		goto L138
	}
	t141 = 0
	goto L139
L138:
	t141 = 1
L139:

	/*EXPRESION DERECHA t146 [ == ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t142 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t142 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t143 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t143 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION IGUALDAD t142 t143*/
	t144 = t142
	t145 = t143
L149:
	t147 = HEAP[int(t144)]
	t148 = HEAP[int(t145)]
	if t147 == -1 {
		goto L146
	}
	t149 = 0
	goto L143
L146:
	t149 = 1
L143:
	if t148 == -1 {
		goto L147
	}
	t150 = 0
	goto L144
L147:
	t150 = 1
L144:
	if t149 == 1 && t150 == 1 {
		goto L148
	}
	t151 = 0
	goto L145
L148:
	t151 = 1
L145:
	if t151 == 1 {
		goto L140
	}
	if t147 != t148 {
		goto L141
	}
	t144 = t144 + 1
	t145 = t145 + 1
	goto L149
L140:
	t146 = 1
	goto L142
L141:
	t146 = 0
L142:
	if t141 == t146 {
		goto L150
	}
	t152 = 0
	goto L151
L150:
	t152 = 1
L151:

	/*EXPRESION DERECHA t157 [&&]*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA 0 [||]*/

	/*EXPRESION DERECHA t154 [||]*/

	/*EXPRESIONES LOGICA !*/

	/*EXPRESION IZQUIERDA 0 [!]*/

	/*LOGICA NOT 0*/
	t153 = 0
	if t153 == 1 {
		goto L153
	}
	t154 = 1
	goto L152
L153:
	t154 = 0
L152:

	/*LOGICA OR 0 t154*/
	t155 = 0
	t156 = t154
	if t155 == 1 || t156 == 1 {
		goto L155
	}
	t157 = 0
	goto L154
L155:
	t157 = 1
L154:

	/*LOGICA AND t152 t157*/
	t158 = t152
	t159 = t157
	if t158 == 1 && t159 == 1 {
		goto L157
	}
	t160 = 0
	goto L156
L157:
	t160 = 1
L156:
	if t160 == 1 {
		goto L158
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L159
L158:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L159:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t174 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t163 [ == ]*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t161 [ != ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L160
	}
	t161 = 0
	goto L161
L160:
	t161 = 1
L161:

	/*EXPRESION DERECHA t162 [ != ]*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA 1000.0 [ > ]*/

	/*EXPRESION DERECHA 532.0 [ > ]*/
	if 1000.0 > 532.0 {
		goto L162
	}
	t162 = 0
	goto L163
L162:
	t162 = 1
L163:
	if t161 != t162 {
		goto L164
	}
	t163 = 0
	goto L165
L164:
	t163 = 1
L165:

	/*EXPRESION DERECHA t168 [ == ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t164 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t164 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*EXPRESION DERECHA t165 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t165 = HP
	HEAP[int(HP)] = 72.0
	HP = HP + 1
	HEAP[int(HP)] = 111.0
	HP = HP + 1
	HEAP[int(HP)] = 108.0
	HP = HP + 1
	HEAP[int(HP)] = 97.0
	HP = HP + 1
	HEAP[int(HP)] = -1
	HP = HP + 1

	/*COMPARACION IGUALDAD t164 t165*/
	t166 = t164
	t167 = t165
L175:
	t169 = HEAP[int(t166)]
	t170 = HEAP[int(t167)]
	if t169 == -1 {
		goto L172
	}
	t171 = 0
	goto L169
L172:
	t171 = 1
L169:
	if t170 == -1 {
		goto L173
	}
	t172 = 0
	goto L170
L173:
	t172 = 1
L170:
	if t171 == 1 && t172 == 1 {
		goto L174
	}
	t173 = 0
	goto L171
L174:
	t173 = 1
L171:
	if t173 == 1 {
		goto L166
	}
	if t169 != t170 {
		goto L167
	}
	t166 = t166 + 1
	t167 = t167 + 1
	goto L175
L166:
	t168 = 1
	goto L168
L167:
	t168 = 0
L168:
	if t163 == t168 {
		goto L176
	}
	t174 = 0
	goto L177
L176:
	t174 = 1
L177:

	/*EXPRESION DERECHA t179 [&&]*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA 0 [||]*/

	/*EXPRESION DERECHA t176 [||]*/

	/*EXPRESIONES LOGICA !*/

	/*EXPRESION IZQUIERDA 0 [!]*/

	/*LOGICA NOT 0*/
	t175 = 0
	if t175 == 1 {
		goto L179
	}
	t176 = 1
	goto L178
L179:
	t176 = 0
L178:

	/*LOGICA OR 0 t176*/
	t177 = 0
	t178 = t176
	if t177 == 1 || t178 == 1 {
		goto L181
	}
	t179 = 0
	goto L180
L181:
	t179 = 1
L180:

	/*LOGICA AND t174 t179*/
	t180 = t174
	t181 = t179
	if t180 == 1 && t181 == 1 {
		goto L183
	}
	t182 = 0
	goto L182
L183:
	t182 = 1
L182:
	if t182 == 1 {
		goto L184
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L185
L184:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L185:
	fmt.Printf("%c", int(10))

}
