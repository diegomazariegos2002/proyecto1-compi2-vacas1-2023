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
	t180, t181, t182, t183, t184, t185, t186, t187, t188, t189,
	t190, t191, t192, t193, t194, t195, t196, t197, t198, t199,
	t200, t201, t202, t203, t204, t205, t206, t207, t208, t209,
	t210, t211, t212, t213, t214, t215, t216, t217, t218, t219,
	t220, t221, t222, t223, t224, t225, t226, t227, t228, t229,
	t230, t231, t232, t233, t234, t235, t236, t237, t238, t239,
	t240, t241, t242, t243, t244, t245, t246, t247, t248, t249,
	t250, t251, t252, t253, t254, t255, t256, t257, t258, t259,
	t260, t261, t262, t263, t264, t265, t266, t267, t268, t269,
	t270, t271, t272, t273, t274, t275, t276, t277, t278, t279,
	t280, t281, t282, t283, t284, t285, t286, t287, t288, t289,
	t290, t291, t292, t293, t294, t295, t296, t297, t298, t299,
	t300, t301, t302, t303, t304, t305, t306, t307, t308, t309,
	t310, t311, t312, t313, t314, t315, t316, t317, t318, t319,
	t320, t321, t322, t323, t324, t325, t326, t327, t328, t329,
	t330, t331, t332, t333, t334, t335, t336, t337, t338, t339,
	t340, t341, t342, t343 float64
)

func main() {
	HP = 0
	SP = 0

	/*console.log*/

	/*EXPRESIONES RESTA*/

	/*EXPRESIONES RESTA*/

	/*EXPRESIONES DIVISION*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t10 = 123.0 * 4.0

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t11 = 2.0 * 2.0

	/*OPERACION SUMA*/
	t12 = 2.0 + t11

	/*OPERACION DIVISION*/
	t13 = t10 / t12

	/*OPERACION RESTA*/
	t14 = 41.0 - t13

	/*EXPRESIONES MULTIPLICACION*/

	/*EXPRESIONES SUMA*/

	/*EXPRESIONES MODULO*/

	/*OPERACION MODULO*/
	t15 = math.Mod(125.0, 5.0)

	/*OPERACION SUMA*/
	t16 = 10.0 + t15

	/*EXPRESIONES POTENCIA*/

	/*OPERACION POTENCIA*/
	t17 = math.Pow(2.0, 2.0)

	/*OPERACION MULTIPLICACION*/
	t18 = t16 * t17

	/*OPERACION RESTA*/
	t19 = t14 - t18
	fmt.Printf("%f", t19)
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
		goto L4
	}
	t23 = 0
	goto L5
L4:
	t23 = 1
L5:
	if t23 == 1 {
		goto L6
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L7
L6:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L7:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L12
	}
	t25 = 0
	goto L13
L12:
	t25 = 1
L13:
	if t25 == 1 {
		goto L14
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L15
L14:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L15:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  <= */

	/*EXPRESION IZQUIERDA t29 [ <= ]*/

	/*EXPRESIONES MULTIPLICACION*/

	/*OPERACION MULTIPLICACION*/
	t29 = 7.0 * 7.0

	/*EXPRESION DERECHA t30 [ <= ]*/

	/*EXPRESIONES SUMA*/

	/*OPERACION SUMA*/
	t30 = 15.0 + 555.0
	if t29 <= t30 {
		goto L20
	}
	t31 = 0
	goto L21
L20:
	t31 = 1
L21:
	if t31 == 1 {
		goto L22
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L23
L22:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L23:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA 532.0 [ > ]*/

	/*EXPRESION DERECHA 532.0 [ > ]*/
	if 532.0 > 532.0 {
		goto L28
	}
	t33 = 0
	goto L29
L28:
	t33 = 1
L29:
	if t33 == 1 {
		goto L30
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L31
L30:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L31:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t44 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t44 = HP
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

	/*EXPRESION DERECHA t45 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t45 = HP
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

	/*COMPARACION IGUALDAD t44 t45*/
	t46 = t44
	t47 = t45
L53:
	t49 = HEAP[int(t46)]
	t50 = HEAP[int(t47)]
	if t49 == -1 {
		goto L50
	}
	t51 = 0
	goto L47
L50:
	t51 = 1
L47:
	if t50 == -1 {
		goto L51
	}
	t52 = 0
	goto L48
L51:
	t52 = 1
L48:
	if t51 == 1 && t52 == 1 {
		goto L52
	}
	t53 = 0
	goto L49
L52:
	t53 = 1
L49:
	if t53 == 1 {
		goto L44
	}
	if t49 != t50 {
		goto L45
	}
	t46 = t46 + 1
	t47 = t47 + 1
	goto L53
L44:
	t48 = 1
	goto L46
L45:
	t48 = 0
L46:
	if t48 == 1 {
		goto L54
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L55
L54:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L55:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t64 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t64 = HP
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

	/*EXPRESION DERECHA t65 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t65 = HP
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

	/*COMPARACION IGUALDAD t64 t65*/
	t66 = t64
	t67 = t65
L77:
	t69 = HEAP[int(t66)]
	t70 = HEAP[int(t67)]
	if t69 == -1 {
		goto L74
	}
	t71 = 0
	goto L71
L74:
	t71 = 1
L71:
	if t70 == -1 {
		goto L75
	}
	t72 = 0
	goto L72
L75:
	t72 = 1
L72:
	if t71 == 1 && t72 == 1 {
		goto L76
	}
	t73 = 0
	goto L73
L76:
	t73 = 1
L73:
	if t73 == 1 {
		goto L68
	}
	if t69 != t70 {
		goto L69
	}
	t66 = t66 + 1
	t67 = t67 + 1
	goto L77
L68:
	t68 = 1
	goto L70
L69:
	t68 = 0
L70:
	if t68 == 1 {
		goto L78
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L79
L78:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L79:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t87 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t87 = HP
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

	/*EXPRESION DERECHA t88 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t88 = HP
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

	/*COMPARACION DIFERENCIA t87 t88*/
	t89 = t87
	t90 = t88
L103:
	t92 = HEAP[int(t89)]
	t93 = HEAP[int(t90)]
	if t92 == -1 {
		goto L100
	}
	t94 = 0
	goto L97
L100:
	t94 = 1
L97:
	if t93 == -1 {
		goto L101
	}
	t95 = 0
	goto L98
L101:
	t95 = 1
L98:
	if t94 == 1 && t95 == 1 {
		goto L102
	}
	t96 = 0
	goto L99
L102:
	t96 = 1
L99:
	if t96 == 1 {
		goto L94
	}
	if t92 != t93 {
		goto L95
	}
	t89 = t89 + 1
	t90 = t90 + 1
	goto L103
L94:
	t91 = 1
	goto L96
L95:
	t91 = 0
L96:
	t98 = t91
	if t98 == 1 {
		goto L105
	}
	t99 = 1
	goto L104
L105:
	t99 = 0
L104:
	t97 = t99
	if t97 == 1 {
		goto L106
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L107
L106:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L107:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t113 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t113 = HP
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

	/*EXPRESION DERECHA t114 [ != ]*/

	/*PRIMITIVO -> CADENA*/
	t114 = HP
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

	/*COMPARACION DIFERENCIA t113 t114*/
	t115 = t113
	t116 = t114
L131:
	t118 = HEAP[int(t115)]
	t119 = HEAP[int(t116)]
	if t118 == -1 {
		goto L128
	}
	t120 = 0
	goto L125
L128:
	t120 = 1
L125:
	if t119 == -1 {
		goto L129
	}
	t121 = 0
	goto L126
L129:
	t121 = 1
L126:
	if t120 == 1 && t121 == 1 {
		goto L130
	}
	t122 = 0
	goto L127
L130:
	t122 = 1
L127:
	if t122 == 1 {
		goto L122
	}
	if t118 != t119 {
		goto L123
	}
	t115 = t115 + 1
	t116 = t116 + 1
	goto L131
L122:
	t117 = 1
	goto L124
L123:
	t117 = 0
L124:
	t124 = t117
	if t124 == 1 {
		goto L133
	}
	t125 = 1
	goto L132
L133:
	t125 = 0
L132:
	t123 = t125
	if t123 == 1 {
		goto L134
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L135
L134:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L135:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t129 = HP
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
	t130 = t129
L138:
	t131 = HEAP[int(t130)]
	if t131 == -1 {
		goto L139
	}
	fmt.Printf("%c", int(t131))
	t130 = t130 + 1
	goto L138
L139:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t139 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t139 = HP
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

	/*EXPRESION DERECHA t140 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t140 = HP
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

	/*COMPARACION [ < ] t139 t140*/
	t141 = t139
	t142 = t140
	t143 = HEAP[int(t141)]
	t144 = HEAP[int(t142)]
	if t143 < t144 {
		goto L145
	}
	t145 = 0
	goto L144
L145:
	t145 = 1
L144:
	if t145 == 1 {
		goto L146
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L147
L146:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L147:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA t153 [ > ]*/

	/*PRIMITIVO -> CADENA*/
	t153 = HP
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

	/*EXPRESION DERECHA t154 [ > ]*/

	/*PRIMITIVO -> CADENA*/
	t154 = HP
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

	/*COMPARACION [ > ] t153 t154*/
	t155 = t153
	t156 = t154
	t157 = HEAP[int(t155)]
	t158 = HEAP[int(t156)]
	if t157 > t158 {
		goto L153
	}
	t159 = 0
	goto L152
L153:
	t159 = 1
L152:
	if t159 == 1 {
		goto L154
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L155
L154:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L155:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t167 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t167 = HP
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

	/*EXPRESION DERECHA t168 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t168 = HP
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

	/*COMPARACION [ < ] t167 t168*/
	t169 = t167
	t170 = t168
	t171 = HEAP[int(t169)]
	t172 = HEAP[int(t170)]
	if t171 < t172 {
		goto L161
	}
	t173 = 0
	goto L160
L161:
	t173 = 1
L160:
	if t173 == 1 {
		goto L162
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L163
L162:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L163:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  <= */

	/*EXPRESION IZQUIERDA t181 [ <= ]*/

	/*PRIMITIVO -> CADENA*/
	t181 = HP
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

	/*EXPRESION DERECHA t182 [ <= ]*/

	/*PRIMITIVO -> CADENA*/
	t182 = HP
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

	/*COMPARACION [ <= ] t181 t182*/
	t183 = t181
	t184 = t182
	t185 = HEAP[int(t183)]
	t186 = HEAP[int(t184)]
	if t185 <= t186 {
		goto L169
	}
	t187 = 0
	goto L168
L169:
	t187 = 1
L168:
	if t187 == 1 {
		goto L170
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L171
L170:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L171:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  >= */

	/*EXPRESION IZQUIERDA t195 [ >= ]*/

	/*PRIMITIVO -> CADENA*/
	t195 = HP
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

	/*EXPRESION DERECHA t196 [ >= ]*/

	/*PRIMITIVO -> CADENA*/
	t196 = HP
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

	/*COMPARACION [ >= ] t195 t196*/
	t197 = t195
	t198 = t196
	t199 = HEAP[int(t197)]
	t200 = HEAP[int(t198)]
	if t199 >= t200 {
		goto L177
	}
	t201 = 0
	goto L176
L177:
	t201 = 1
L176:
	if t201 == 1 {
		goto L178
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L179
L178:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L179:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES RELACION  < */

	/*EXPRESION IZQUIERDA t209 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t209 = HP
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

	/*EXPRESION DERECHA t210 [ < ]*/

	/*PRIMITIVO -> CADENA*/
	t210 = HP
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

	/*COMPARACION [ < ] t209 t210*/
	t211 = t209
	t212 = t210
	t213 = HEAP[int(t211)]
	t214 = HEAP[int(t212)]
	if t213 < t214 {
		goto L185
	}
	t215 = 0
	goto L184
L185:
	t215 = 1
L184:
	if t215 == 1 {
		goto L186
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L187
L186:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L187:
	fmt.Printf("%c", int(10))

	/*console.log*/
	if 1 == 1 {
		goto L190
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L191
L190:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L191:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*PRIMITIVO -> CADENA*/
	t219 = HP
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
	t220 = t219
L194:
	t221 = HEAP[int(t220)]
	if t221 == -1 {
		goto L195
	}
	fmt.Printf("%c", int(t221))
	t220 = t220 + 1
	goto L194
L195:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t227 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L204
	}
	t227 = 0
	goto L205
L204:
	t227 = 1
L205:

	/*EXPRESION DERECHA t228 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 1.0 [ == ]*/

	/*EXPRESION DERECHA 1.0 [ == ]*/
	if 1.0 == 1.0 {
		goto L206
	}
	t228 = 0
	goto L207
L206:
	t228 = 1
L207:

	/*LOGICA AND t227 t228*/
	t229 = t227
	t230 = t228
	if t229 == 1 && t230 == 1 {
		goto L209
	}
	t231 = 0
	goto L208
L209:
	t231 = 1
L208:
	if t231 == 1 {
		goto L210
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L211
L210:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L211:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA t237 [||]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L220
	}
	t237 = 0
	goto L221
L220:
	t237 = 1
L221:

	/*EXPRESION DERECHA t238 [||]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 1.0 [ == ]*/
	if 0.0 == 1.0 {
		goto L222
	}
	t238 = 0
	goto L223
L222:
	t238 = 1
L223:

	/*LOGICA OR t237 t238*/
	t239 = t237
	t240 = t238
	if t239 == 1 || t240 == 1 {
		goto L225
	}
	t241 = 0
	goto L224
L225:
	t241 = 1
L224:
	if t241 == 1 {
		goto L226
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L227
L226:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L227:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA !*/

	/*EXPRESION IZQUIERDA t253 [!]*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t249 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L238
	}
	t249 = 0
	goto L239
L238:
	t249 = 1
L239:

	/*EXPRESION DERECHA t250 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 1.0 [ == ]*/

	/*EXPRESION DERECHA 1.0 [ == ]*/
	if 1.0 == 1.0 {
		goto L240
	}
	t250 = 0
	goto L241
L240:
	t250 = 1
L241:

	/*LOGICA AND t249 t250*/
	t251 = t249
	t252 = t250
	if t251 == 1 && t252 == 1 {
		goto L243
	}
	t253 = 0
	goto L242
L243:
	t253 = 1
L242:

	/*LOGICA NOT t253*/
	t254 = t253
	if t254 == 1 {
		goto L245
	}
	t255 = 1
	goto L244
L245:
	t255 = 0
L244:
	if t255 == 1 {
		goto L246
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L247
L246:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L247:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t291 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t280 [ == ]*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t278 [ != ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L274
	}
	t278 = 0
	goto L275
L274:
	t278 = 1
L275:

	/*EXPRESION DERECHA t279 [ != ]*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA 532.0 [ > ]*/

	/*EXPRESION DERECHA 532.0 [ > ]*/
	if 532.0 > 532.0 {
		goto L276
	}
	t279 = 0
	goto L277
L276:
	t279 = 1
L277:
	if t278 != t279 {
		goto L278
	}
	t280 = 0
	goto L279
L278:
	t280 = 1
L279:

	/*EXPRESION DERECHA t285 [ == ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t281 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t281 = HP
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

	/*EXPRESION DERECHA t282 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t282 = HP
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

	/*COMPARACION IGUALDAD t281 t282*/
	t283 = t281
	t284 = t282
L289:
	t286 = HEAP[int(t283)]
	t287 = HEAP[int(t284)]
	if t286 == -1 {
		goto L286
	}
	t288 = 0
	goto L283
L286:
	t288 = 1
L283:
	if t287 == -1 {
		goto L287
	}
	t289 = 0
	goto L284
L287:
	t289 = 1
L284:
	if t288 == 1 && t289 == 1 {
		goto L288
	}
	t290 = 0
	goto L285
L288:
	t290 = 1
L285:
	if t290 == 1 {
		goto L280
	}
	if t286 != t287 {
		goto L281
	}
	t283 = t283 + 1
	t284 = t284 + 1
	goto L289
L280:
	t285 = 1
	goto L282
L281:
	t285 = 0
L282:
	if t280 == t285 {
		goto L290
	}
	t291 = 0
	goto L291
L290:
	t291 = 1
L291:

	/*EXPRESION DERECHA t296 [&&]*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA 0 [||]*/

	/*EXPRESION DERECHA t293 [||]*/

	/*EXPRESIONES LOGICA !*/

	/*EXPRESION IZQUIERDA 0 [!]*/

	/*LOGICA NOT 0*/
	t292 = 0
	if t292 == 1 {
		goto L293
	}
	t293 = 1
	goto L292
L293:
	t293 = 0
L292:

	/*LOGICA OR 0 t293*/
	t294 = 0
	t295 = t293
	if t294 == 1 || t295 == 1 {
		goto L295
	}
	t296 = 0
	goto L294
L295:
	t296 = 1
L294:

	/*LOGICA AND t291 t296*/
	t297 = t291
	t298 = t296
	if t297 == 1 && t298 == 1 {
		goto L297
	}
	t299 = 0
	goto L296
L297:
	t299 = 1
L296:
	if t299 == 1 {
		goto L298
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L299
L298:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L299:
	fmt.Printf("%c", int(10))

	/*console.log*/

	/*EXPRESIONES LOGICA &&*/

	/*EXPRESION IZQUIERDA t335 [&&]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t324 [ == ]*/

	/*EXPRESIONES RELACION  != */

	/*EXPRESION IZQUIERDA t322 [ != ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA 0.0 [ == ]*/

	/*EXPRESION DERECHA 0.0 [ == ]*/
	if 0.0 == 0.0 {
		goto L326
	}
	t322 = 0
	goto L327
L326:
	t322 = 1
L327:

	/*EXPRESION DERECHA t323 [ != ]*/

	/*EXPRESIONES RELACION  > */

	/*EXPRESION IZQUIERDA 1000.0 [ > ]*/

	/*EXPRESION DERECHA 532.0 [ > ]*/
	if 1000.0 > 532.0 {
		goto L328
	}
	t323 = 0
	goto L329
L328:
	t323 = 1
L329:
	if t322 != t323 {
		goto L330
	}
	t324 = 0
	goto L331
L330:
	t324 = 1
L331:

	/*EXPRESION DERECHA t329 [ == ]*/

	/*EXPRESIONES RELACION  == */

	/*EXPRESION IZQUIERDA t325 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t325 = HP
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

	/*EXPRESION DERECHA t326 [ == ]*/

	/*PRIMITIVO -> CADENA*/
	t326 = HP
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

	/*COMPARACION IGUALDAD t325 t326*/
	t327 = t325
	t328 = t326
L341:
	t330 = HEAP[int(t327)]
	t331 = HEAP[int(t328)]
	if t330 == -1 {
		goto L338
	}
	t332 = 0
	goto L335
L338:
	t332 = 1
L335:
	if t331 == -1 {
		goto L339
	}
	t333 = 0
	goto L336
L339:
	t333 = 1
L336:
	if t332 == 1 && t333 == 1 {
		goto L340
	}
	t334 = 0
	goto L337
L340:
	t334 = 1
L337:
	if t334 == 1 {
		goto L332
	}
	if t330 != t331 {
		goto L333
	}
	t327 = t327 + 1
	t328 = t328 + 1
	goto L341
L332:
	t329 = 1
	goto L334
L333:
	t329 = 0
L334:
	if t324 == t329 {
		goto L342
	}
	t335 = 0
	goto L343
L342:
	t335 = 1
L343:

	/*EXPRESION DERECHA t340 [&&]*/

	/*EXPRESIONES LOGICA ||*/

	/*EXPRESION IZQUIERDA 0 [||]*/

	/*EXPRESION DERECHA t337 [||]*/

	/*EXPRESIONES LOGICA !*/

	/*EXPRESION IZQUIERDA 0 [!]*/

	/*LOGICA NOT 0*/
	t336 = 0
	if t336 == 1 {
		goto L345
	}
	t337 = 1
	goto L344
L345:
	t337 = 0
L344:

	/*LOGICA OR 0 t337*/
	t338 = 0
	t339 = t337
	if t338 == 1 || t339 == 1 {
		goto L347
	}
	t340 = 0
	goto L346
L347:
	t340 = 1
L346:

	/*LOGICA AND t335 t340*/
	t341 = t335
	t342 = t340
	if t341 == 1 && t342 == 1 {
		goto L349
	}
	t343 = 0
	goto L348
L349:
	t343 = 1
L348:
	if t343 == 1 {
		goto L350
	}
	fmt.Printf("%c", int(102))
	fmt.Printf("%c", int(97))
	fmt.Printf("%c", int(108))
	fmt.Printf("%c", int(115))
	fmt.Printf("%c", int(101))
	goto L351
L350:
	fmt.Printf("%c", int(116))
	fmt.Printf("%c", int(114))
	fmt.Printf("%c", int(117))
	fmt.Printf("%c", int(101))
L351:
	fmt.Printf("%c", int(10))

}
