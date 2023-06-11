
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftorleftandleftsumarestanonassocmenormayormenorigualmayorigualigualaciondiferenteleftmultiplicaciondivisionmoduloleftpotenciarightnotlefturestaand any boolean break c_Abre c_Cierra cadena coma concat console continue decremento diferente division dosPuntos else false fn for id if igual igualacion incremento let llave_Abre llave_Cierra log mayor mayorigual menor menorigual modulo multiplicacion not null number numero or p_Abre p_Cierra potencia punto puntoYcoma resta return split string suma toExponential toFixed toLowerCase toString toUpperCase true while\n    INICIO : ENTRADAS\n    \n    ENTRADAS : ENTRADAS ENTRADA\n    \n    ENTRADAS : ENTRADA\n    \n    ENTRADA : IMPRIMIR puntoYcoma\n            |   IF puntoYcoma\n            |   WHILE puntoYcoma\n            |   BREAK\n            |   CONTINUE\n            |   FOR puntoYcoma\n            |   INCREMENTO puntoYcoma\n            |   DECREMENTO puntoYcoma\n            |   FUNC puntoYcoma\n            |   LLAMADA_FUNCION puntoYcoma\n    \n   FUNC : fn id p_Abre PARAMETROS_DECLA_FUNC p_Cierra llave_Abre ENTRADAS llave_Cierra\n   \n    FUNC : fn id p_Abre p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    PARAMETROS_DECLA_FUNC : PARAMETROS_DECLA_FUNC coma PARAMETRO_DECLA_FUNC\n                            | PARAMETRO_DECLA_FUNC\n    \n    PARAMETRO_DECLA_FUNC : id dosPuntos TIPO\n    \n    PARAMETRO_DECLA_FUNC : id dosPuntos TIPO c_Abre c_Cierra\n    \n    LLAMADA_FUNCION : id p_Abre PARAMETROS_LLAMA_FUNC p_Cierra\n    \n    LLAMADA_FUNCION : id p_Abre p_Cierra\n    \n    PARAMETROS_LLAMA_FUNC : EXPRESION\n                          | PARAMETROS_LLAMA_FUNC coma EXPRESION\n    \n    FOR : for p_Abre DECLARACION puntoYcoma EXPRESION puntoYcoma FORITERADOR p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    FORITERADOR : ASIGNACION\n                | INCREMENTO\n                | DECREMENTO\n    \n    BREAK : break puntoYcoma\n    \n    CONTINUE : continue puntoYcoma\n    \n    WHILE : while p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    IF : if p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra COMPLEMENTO_IF\n    \n    COMPLEMENTO_IF : else IF\n                    | else llave_Abre ENTRADAS llave_Cierra\n                    | \n    \n    ENTRADA : DECLARACION puntoYcoma\n    \n    DECLARACION : let id igual EXPRESION\n    \n    DECLARACION : let id dosPuntos TIPO igual EXPRESION\n    \n    DECLARACION : let id \n    \n    DECLARACION : let id dosPuntos TIPO\n    \n    DECLARACION : let id dosPuntos TIPO c_Abre c_Cierra igual EXPRESION\n    \n    DECLARACION : let id dosPuntos TIPO c_Abre c_Cierra\n    \n    ENTRADA : ASIGNACION puntoYcoma\n    \n    ASIGNACION : id igual EXPRESION\n    \n    ASIGNACION : id LISTAINDICES igual EXPRESION\n    \n    INCREMENTO : id incremento \n    \n    DECREMENTO : id decremento\n    \n    IMPRIMIR : console punto log p_Abre LISTAEXPRESIONES p_Cierra\n    \n    LISTAEXPRESIONES :  LISTAEXPRESIONES coma EXPRESION\n    \n    LISTAEXPRESIONES : EXPRESION\n    \n    LISTAINDICES :  LISTAINDICES c_Abre EXPRESION c_Cierra\n    \n    LISTAINDICES : c_Abre EXPRESION c_Cierra\n    \n    EXPRESION : EXPRESION suma EXPRESION\n    \n    EXPRESION : EXPRESION resta EXPRESION\n    \n    EXPRESION : EXPRESION multiplicacion EXPRESION\n    \n    EXPRESION : EXPRESION division EXPRESION\n    \n    EXPRESION : EXPRESION potencia EXPRESION\n    \n    EXPRESION : EXPRESION modulo EXPRESION\n    \n    EXPRESION : resta EXPRESION %prec uresta\n    \n    EXPRESION : EXPRESION and EXPRESION\n    \n    EXPRESION : EXPRESION or EXPRESION\n    \n    EXPRESION : not EXPRESION\n    \n    EXPRESION : EXPRESION mayor EXPRESION\n    \n    EXPRESION : EXPRESION mayorigual EXPRESION\n    \n    EXPRESION : EXPRESION menor EXPRESION\n    \n    EXPRESION : EXPRESION menorigual EXPRESION\n    \n    EXPRESION : EXPRESION igualacion EXPRESION\n    \n    EXPRESION : EXPRESION diferente EXPRESION\n    \n    EXPRESION : FUNCION_TOFIXED\n            | FUNCION_TOEXPONENTIAL\n            | FUNCION_TOSTRING\n            | FUNCION_TOLOWERCASE\n            | FUNCION_TOUPPERCASE\n            | FUNCION_SPLIT\n    \n    FUNCION_TOFIXED : id punto toFixed p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOEXPONENTIAL : id punto toExponential p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOSTRING : id punto toString p_Abre p_Cierra\n    \n    FUNCION_TOLOWERCASE : id punto toLowerCase p_Abre p_Cierra\n    \n    FUNCION_TOUPPERCASE : id punto toUpperCase p_Abre p_Cierra\n    \n    FUNCION_SPLIT : id punto split p_Abre EXPRESION p_Cierra\n    \n    EXPRESION : cadena\n    \n    EXPRESION : numero\n    \n    EXPRESION : true\n                | false\n    \n    EXPRESION : null\n    \n    EXPRESION : id\n    \n    EXPRESION : id LISTAINDICES\n    \n    EXPRESION : c_Abre LISTAEXPRESIONES c_Cierra\n    \n    TIPO : number\n    \n    TIPO : string\n    \n    TIPO : boolean\n    \n    TIPO : any\n    '
    
_lr_action_items = {'console':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,119,142,149,153,161,164,166,183,196,197,198,199,],[16,16,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,16,16,16,16,16,16,16,16,16,16,16,16,]),'if':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,119,142,149,153,161,164,166,183,187,196,197,198,199,],[17,17,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'while':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,119,142,149,153,161,164,166,183,196,197,198,199,],[18,18,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,18,18,18,18,18,18,18,18,18,18,18,18,]),'break':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,119,142,149,153,161,164,166,183,196,197,198,199,],[19,19,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,19,19,19,19,19,19,19,19,19,19,19,19,]),'continue':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,119,142,149,153,161,164,166,183,196,197,198,199,],[20,20,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,20,20,20,20,20,20,20,20,20,20,20,20,]),'for':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,119,142,149,153,161,164,166,183,196,197,198,199,],[21,21,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,21,21,21,21,21,21,21,21,21,21,21,21,]),'id':([0,2,3,7,8,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,44,45,47,52,53,66,73,74,76,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,119,141,142,148,149,150,153,154,155,159,161,162,164,166,183,185,196,197,198,199,],[22,22,-3,-7,-8,48,49,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,65,65,-28,-29,65,65,65,65,65,65,65,65,108,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,22,65,22,108,22,65,22,65,65,65,22,181,22,22,22,65,22,22,22,22,]),'fn':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,119,142,149,153,161,164,166,183,196,197,198,199,],[23,23,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,23,23,23,23,23,23,23,23,23,23,23,23,]),'let':([0,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,41,119,142,149,153,161,164,166,183,196,197,198,199,],[24,24,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'$end':([1,2,3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,],[0,-1,-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,]),'llave_Cierra':([3,7,8,25,26,27,28,29,30,31,32,33,34,35,39,40,153,161,166,183,198,199,],[-3,-7,-8,-2,-4,-5,-6,-9,-10,-11,-12,-13,-35,-42,-28,-29,169,176,184,193,200,201,]),'puntoYcoma':([4,5,6,9,10,11,12,13,14,15,19,20,42,43,49,54,55,56,57,58,59,60,61,62,63,64,65,68,70,72,95,96,97,103,105,107,112,113,114,115,116,117,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,145,152,167,168,169,172,173,174,176,184,186,188,189,190,193,194,195,200,201,],[26,27,28,29,30,31,32,33,34,35,39,40,-45,-46,-38,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,102,-21,-43,-58,-61,-86,-20,-44,-51,-36,-39,-88,-89,-90,-91,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,-64,-65,-66,-67,-87,162,-50,-47,-37,-41,-34,-76,-77,-78,-30,-15,-31,-74,-75,-79,-14,-40,-32,-33,-24,]),'punto':([16,65,],[36,98,]),'p_Abre':([17,18,21,22,48,50,134,135,136,137,138,139,],[37,38,41,44,76,79,154,155,156,157,158,159,]),'incremento':([22,181,],[42,42,]),'decremento':([22,181,],[43,43,]),'igual':([22,46,49,107,113,114,115,116,117,145,168,181,],[45,73,77,-51,150,-88,-89,-90,-91,-50,185,45,]),'c_Abre':([22,37,38,44,45,46,47,52,53,65,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,102,104,107,113,114,115,116,117,141,145,150,154,155,159,163,181,185,],[47,66,66,66,66,74,66,66,66,47,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,74,66,66,-51,151,-88,-89,-90,-91,66,-50,66,66,66,66,182,47,66,]),'log':([36,],[50,]),'resta':([37,38,44,45,47,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,71,72,73,74,75,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,104,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,141,143,144,145,150,154,155,159,160,167,170,171,172,173,174,175,185,188,189,190,194,],[52,52,52,52,52,82,52,52,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,52,82,82,82,52,52,82,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-58,-61,-86,82,52,52,82,82,-51,82,-52,-53,-54,-55,-56,-57,82,82,-62,-63,-64,-65,-66,-67,-87,52,82,82,-50,52,52,52,52,82,82,82,82,-76,-77,-78,82,52,-74,-75,-79,82,]),'not':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'cadena':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'numero':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'true':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'false':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'null':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'p_Cierra':([42,43,44,51,54,55,56,57,58,59,60,61,62,63,64,65,67,69,71,72,76,95,96,97,100,105,107,109,111,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,144,145,156,157,158,160,163,165,170,171,172,173,174,175,177,178,179,180,188,189,190,192,],[-45,-46,70,80,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,101,103,-22,-43,110,-58,-61,-86,-49,-44,-51,147,-17,-88,-89,-90,-91,152,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,-64,-65,-66,-67,-87,-23,-50,172,173,174,-48,-18,-16,188,189,-76,-77,-78,190,191,-25,-26,-27,-74,-75,-79,-19,]),'dosPuntos':([49,108,],[78,146,]),'suma':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[81,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,81,81,81,81,-58,-61,-86,81,81,81,-51,81,-52,-53,-54,-55,-56,-57,81,81,-62,-63,-64,-65,-66,-67,-87,81,81,-50,81,81,81,81,-76,-77,-78,81,-74,-75,-79,81,]),'multiplicacion':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[83,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,83,83,83,83,-58,-61,-86,83,83,83,-51,83,83,83,-54,-55,-56,-57,83,83,83,83,83,83,83,83,-87,83,83,-50,83,83,83,83,-76,-77,-78,83,-74,-75,-79,83,]),'division':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[84,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,84,84,84,84,-58,-61,-86,84,84,84,-51,84,84,84,-54,-55,-56,-57,84,84,84,84,84,84,84,84,-87,84,84,-50,84,84,84,84,-76,-77,-78,84,-74,-75,-79,84,]),'potencia':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[85,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,85,85,85,85,-58,-61,-86,85,85,85,-51,85,85,85,85,85,-56,85,85,85,85,85,85,85,85,85,-87,85,85,-50,85,85,85,85,-76,-77,-78,85,-74,-75,-79,85,]),'modulo':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[86,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,86,86,86,86,-58,-61,-86,86,86,86,-51,86,86,86,-54,-55,-56,-57,86,86,86,86,86,86,86,86,-87,86,86,-50,86,86,86,86,-76,-77,-78,86,-74,-75,-79,86,]),'and':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[87,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,87,87,87,87,-58,-61,-86,87,87,87,-51,87,-52,-53,-54,-55,-56,-57,-59,87,-62,-63,-64,-65,-66,-67,-87,87,87,-50,87,87,87,87,-76,-77,-78,87,-74,-75,-79,87,]),'or':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[88,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,88,88,88,88,-58,-61,-86,88,88,88,-51,88,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,-64,-65,-66,-67,-87,88,88,-50,88,88,88,88,-76,-77,-78,88,-74,-75,-79,88,]),'mayor':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[89,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,89,89,89,89,-58,-61,-86,89,89,89,-51,89,89,89,-54,-55,-56,-57,89,89,None,None,None,None,None,None,-87,89,89,-50,89,89,89,89,-76,-77,-78,89,-74,-75,-79,89,]),'mayorigual':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[90,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,90,90,90,90,-58,-61,-86,90,90,90,-51,90,90,90,-54,-55,-56,-57,90,90,None,None,None,None,None,None,-87,90,90,-50,90,90,90,90,-76,-77,-78,90,-74,-75,-79,90,]),'menor':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[91,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,91,91,91,91,-58,-61,-86,91,91,91,-51,91,91,91,-54,-55,-56,-57,91,91,None,None,None,None,None,None,-87,91,91,-50,91,91,91,91,-76,-77,-78,91,-74,-75,-79,91,]),'menorigual':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[92,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,92,92,92,92,-58,-61,-86,92,92,92,-51,92,92,92,-54,-55,-56,-57,92,92,None,None,None,None,None,None,-87,92,92,-50,92,92,92,92,-76,-77,-78,92,-74,-75,-79,92,]),'igualacion':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[93,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,93,93,93,93,-58,-61,-86,93,93,93,-51,93,93,93,-54,-55,-56,-57,93,93,None,None,None,None,None,None,-87,93,93,-50,93,93,93,93,-76,-77,-78,93,-74,-75,-79,93,]),'diferente':([51,54,55,56,57,58,59,60,61,62,63,64,65,67,71,72,75,95,96,97,100,105,106,107,112,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,143,144,145,160,167,170,171,172,173,174,175,188,189,190,194,],[94,-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,94,94,94,94,-58,-61,-86,94,94,94,-51,94,94,94,-54,-55,-56,-57,94,94,None,None,None,None,None,None,-87,94,94,-50,94,94,94,94,-76,-77,-78,94,-74,-75,-79,94,]),'coma':([54,55,56,57,58,59,60,61,62,63,64,65,69,71,95,96,97,99,100,107,109,111,114,115,116,117,118,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,144,145,160,163,165,172,173,174,188,189,190,192,],[-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,104,-22,-58,-61,-86,141,-49,-51,148,-17,-88,-89,-90,-91,141,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,-64,-65,-66,-67,-87,-23,-50,-48,-18,-16,-76,-77,-78,-74,-75,-79,-19,]),'c_Cierra':([54,55,56,57,58,59,60,61,62,63,64,65,75,95,96,97,99,100,106,107,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,145,151,160,172,173,174,182,188,189,190,],[-68,-69,-70,-71,-72,-73,-80,-81,-82,-83,-84,-85,107,-58,-61,-86,140,-49,145,-51,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,-64,-65,-66,-67,-87,-50,168,-48,-76,-77,-78,192,-74,-75,-79,]),'number':([78,146,],[114,114,]),'string':([78,146,],[115,115,]),'boolean':([78,146,],[116,116,]),'any':([78,146,],[117,117,]),'llave_Abre':([80,101,110,147,187,191,],[119,142,149,164,196,197,]),'toFixed':([98,],[134,]),'toExponential':([98,],[135,]),'toString':([98,],[136,]),'toLowerCase':([98,],[137,]),'toUpperCase':([98,],[138,]),'split':([98,],[139,]),'else':([169,],[187,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INICIO':([0,],[1,]),'ENTRADAS':([0,119,142,149,164,196,197,],[2,153,161,166,183,198,199,]),'ENTRADA':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[3,25,3,3,3,25,25,3,25,25,3,3,25,25,]),'IMPRIMIR':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'IF':([0,2,119,142,149,153,161,164,166,183,187,196,197,198,199,],[5,5,5,5,5,5,5,5,5,5,195,5,5,5,5,]),'WHILE':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'BREAK':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'CONTINUE':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'FOR':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'INCREMENTO':([0,2,119,142,149,153,161,162,164,166,183,196,197,198,199,],[10,10,10,10,10,10,10,179,10,10,10,10,10,10,10,]),'DECREMENTO':([0,2,119,142,149,153,161,162,164,166,183,196,197,198,199,],[11,11,11,11,11,11,11,180,11,11,11,11,11,11,11,]),'FUNC':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'LLAMADA_FUNCION':([0,2,119,142,149,153,161,164,166,183,196,197,198,199,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'DECLARACION':([0,2,41,119,142,149,153,161,164,166,183,196,197,198,199,],[14,14,68,14,14,14,14,14,14,14,14,14,14,14,14,]),'ASIGNACION':([0,2,119,142,149,153,161,162,164,166,183,196,197,198,199,],[15,15,15,15,15,15,15,178,15,15,15,15,15,15,15,]),'LISTAINDICES':([22,65,181,],[46,97,46,]),'EXPRESION':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[51,67,71,72,75,95,96,100,105,106,112,100,120,121,122,123,124,125,126,127,128,129,130,131,132,133,143,144,160,167,170,171,175,194,]),'FUNCION_TOFIXED':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'FUNCION_TOEXPONENTIAL':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'FUNCION_TOSTRING':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'FUNCION_TOLOWERCASE':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'FUNCION_TOUPPERCASE':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'FUNCION_SPLIT':([37,38,44,45,47,52,53,66,73,74,77,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,102,104,141,150,154,155,159,185,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'PARAMETROS_LLAMA_FUNC':([44,],[69,]),'LISTAEXPRESIONES':([66,79,],[99,118,]),'PARAMETROS_DECLA_FUNC':([76,],[109,]),'PARAMETRO_DECLA_FUNC':([76,148,],[111,165,]),'TIPO':([78,146,],[113,163,]),'FORITERADOR':([162,],[177,]),'COMPLEMENTO_IF':([169,],[186,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INICIO","S'",1,None,None,None),
  ('INICIO -> ENTRADAS','INICIO',1,'p_INICIO','parser.py',61),
  ('ENTRADAS -> ENTRADAS ENTRADA','ENTRADAS',2,'p_ENTRADAS_PARTE_1','parser.py',67),
  ('ENTRADAS -> ENTRADA','ENTRADAS',1,'p_ENTRADAS_PARTE_2','parser.py',74),
  ('ENTRADA -> IMPRIMIR puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',80),
  ('ENTRADA -> IF puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',81),
  ('ENTRADA -> WHILE puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',82),
  ('ENTRADA -> BREAK','ENTRADA',1,'p_ENTRADA','parser.py',83),
  ('ENTRADA -> CONTINUE','ENTRADA',1,'p_ENTRADA','parser.py',84),
  ('ENTRADA -> FOR puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',85),
  ('ENTRADA -> INCREMENTO puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',86),
  ('ENTRADA -> DECREMENTO puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',87),
  ('ENTRADA -> FUNC puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',88),
  ('ENTRADA -> LLAMADA_FUNCION puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',89),
  ('FUNC -> fn id p_Abre PARAMETROS_DECLA_FUNC p_Cierra llave_Abre ENTRADAS llave_Cierra','FUNC',8,'p_FUNC_1','parser.py',107),
  ('FUNC -> fn id p_Abre p_Cierra llave_Abre ENTRADAS llave_Cierra','FUNC',7,'p_FUNC_2','parser.py',114),
  ('PARAMETROS_DECLA_FUNC -> PARAMETROS_DECLA_FUNC coma PARAMETRO_DECLA_FUNC','PARAMETROS_DECLA_FUNC',3,'p_PARAMETROS_DECLA_FUNC','parser.py',121),
  ('PARAMETROS_DECLA_FUNC -> PARAMETRO_DECLA_FUNC','PARAMETROS_DECLA_FUNC',1,'p_PARAMETROS_DECLA_FUNC','parser.py',122),
  ('PARAMETRO_DECLA_FUNC -> id dosPuntos TIPO','PARAMETRO_DECLA_FUNC',3,'p_PARAMETRO_DECLA_FUNC_1','parser.py',131),
  ('PARAMETRO_DECLA_FUNC -> id dosPuntos TIPO c_Abre c_Cierra','PARAMETRO_DECLA_FUNC',5,'p_PARAMETRO_DECLA_FUNC_2','parser.py',137),
  ('LLAMADA_FUNCION -> id p_Abre PARAMETROS_LLAMA_FUNC p_Cierra','LLAMADA_FUNCION',4,'p_LLAMADA_FUNCION_1','parser.py',144),
  ('LLAMADA_FUNCION -> id p_Abre p_Cierra','LLAMADA_FUNCION',3,'p_LLAMADA_FUNCION_2','parser.py',150),
  ('PARAMETROS_LLAMA_FUNC -> EXPRESION','PARAMETROS_LLAMA_FUNC',1,'p_PARAMETROS_LLAMA_FUNC','parser.py',156),
  ('PARAMETROS_LLAMA_FUNC -> PARAMETROS_LLAMA_FUNC coma EXPRESION','PARAMETROS_LLAMA_FUNC',3,'p_PARAMETROS_LLAMA_FUNC','parser.py',157),
  ('FOR -> for p_Abre DECLARACION puntoYcoma EXPRESION puntoYcoma FORITERADOR p_Cierra llave_Abre ENTRADAS llave_Cierra','FOR',11,'p_FOR','parser.py',167),
  ('FORITERADOR -> ASIGNACION','FORITERADOR',1,'p_FORITERADOR','parser.py',173),
  ('FORITERADOR -> INCREMENTO','FORITERADOR',1,'p_FORITERADOR','parser.py',174),
  ('FORITERADOR -> DECREMENTO','FORITERADOR',1,'p_FORITERADOR','parser.py',175),
  ('BREAK -> break puntoYcoma','BREAK',2,'p_BREAK','parser.py',182),
  ('CONTINUE -> continue puntoYcoma','CONTINUE',2,'p_CONTINUE','parser.py',188),
  ('WHILE -> while p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra','WHILE',7,'p_WHILE','parser.py',195),
  ('IF -> if p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra COMPLEMENTO_IF','IF',8,'p_IF','parser.py',202),
  ('COMPLEMENTO_IF -> else IF','COMPLEMENTO_IF',2,'p_COMPLEMENTO_IF','parser.py',208),
  ('COMPLEMENTO_IF -> else llave_Abre ENTRADAS llave_Cierra','COMPLEMENTO_IF',4,'p_COMPLEMENTO_IF','parser.py',209),
  ('COMPLEMENTO_IF -> <empty>','COMPLEMENTO_IF',0,'p_COMPLEMENTO_IF','parser.py',210),
  ('ENTRADA -> DECLARACION puntoYcoma','ENTRADA',2,'p_ENTRADA_Declaracion','parser.py',223),
  ('DECLARACION -> let id igual EXPRESION','DECLARACION',4,'p_DECLARACION_NoTipada','parser.py',229),
  ('DECLARACION -> let id dosPuntos TIPO igual EXPRESION','DECLARACION',6,'p_DECLARACION_Tipada','parser.py',236),
  ('DECLARACION -> let id','DECLARACION',2,'p_DECLARACION_SinExpresion_SinTipado','parser.py',242),
  ('DECLARACION -> let id dosPuntos TIPO','DECLARACION',4,'p_DECLARACION_SinExpresion_Tipado','parser.py',248),
  ('DECLARACION -> let id dosPuntos TIPO c_Abre c_Cierra igual EXPRESION','DECLARACION',8,'p_DECLARACION_Tipada_VECTOR','parser.py',254),
  ('DECLARACION -> let id dosPuntos TIPO c_Abre c_Cierra','DECLARACION',6,'p_DECLARACION_SinExpresion_Tipado_VECTOR','parser.py',260),
  ('ENTRADA -> ASIGNACION puntoYcoma','ENTRADA',2,'p_ENTRADA_Asignacion','parser.py',269),
  ('ASIGNACION -> id igual EXPRESION','ASIGNACION',3,'p_ASIGNACION','parser.py',275),
  ('ASIGNACION -> id LISTAINDICES igual EXPRESION','ASIGNACION',4,'p_ASIGNACION_VEC','parser.py',281),
  ('INCREMENTO -> id incremento','INCREMENTO',2,'p_INCREMENTO','parser.py',289),
  ('DECREMENTO -> id decremento','DECREMENTO',2,'p_DECREMENTO','parser.py',295),
  ('IMPRIMIR -> console punto log p_Abre LISTAEXPRESIONES p_Cierra','IMPRIMIR',6,'p_IMPRIMIR_1','parser.py',302),
  ('LISTAEXPRESIONES -> LISTAEXPRESIONES coma EXPRESION','LISTAEXPRESIONES',3,'p_LISTAEXPRESIONES_1','parser.py',308),
  ('LISTAEXPRESIONES -> EXPRESION','LISTAEXPRESIONES',1,'p_LISTAEXPRESIONES_2','parser.py',315),
  ('LISTAINDICES -> LISTAINDICES c_Abre EXPRESION c_Cierra','LISTAINDICES',4,'p_LISTAEXPRESIONES_Indices','parser.py',321),
  ('LISTAINDICES -> c_Abre EXPRESION c_Cierra','LISTAINDICES',3,'p_LISTAEXPRESIONES_Indices_2','parser.py',328),
  ('EXPRESION -> EXPRESION suma EXPRESION','EXPRESION',3,'p_EXPRESION_suma','parser.py',336),
  ('EXPRESION -> EXPRESION resta EXPRESION','EXPRESION',3,'p_EXPRESION_resta','parser.py',343),
  ('EXPRESION -> EXPRESION multiplicacion EXPRESION','EXPRESION',3,'p_EXPRESION_multiplicacion','parser.py',350),
  ('EXPRESION -> EXPRESION division EXPRESION','EXPRESION',3,'p_EXPRESION_division','parser.py',357),
  ('EXPRESION -> EXPRESION potencia EXPRESION','EXPRESION',3,'p_EXPRESION_potencia','parser.py',364),
  ('EXPRESION -> EXPRESION modulo EXPRESION','EXPRESION',3,'p_EXPRESION_modulo','parser.py',371),
  ('EXPRESION -> resta EXPRESION','EXPRESION',2,'p_EXPRESION_negativo','parser.py',378),
  ('EXPRESION -> EXPRESION and EXPRESION','EXPRESION',3,'p_EXPRESION_and','parser.py',387),
  ('EXPRESION -> EXPRESION or EXPRESION','EXPRESION',3,'p_EXPRESION_or','parser.py',394),
  ('EXPRESION -> not EXPRESION','EXPRESION',2,'p_EXPRESION_not','parser.py',401),
  ('EXPRESION -> EXPRESION mayor EXPRESION','EXPRESION',3,'p_EXPRESION_mayor','parser.py',410),
  ('EXPRESION -> EXPRESION mayorigual EXPRESION','EXPRESION',3,'p_EXPRESION_mayorigual','parser.py',417),
  ('EXPRESION -> EXPRESION menor EXPRESION','EXPRESION',3,'p_EXPRESION_menor','parser.py',424),
  ('EXPRESION -> EXPRESION menorigual EXPRESION','EXPRESION',3,'p_EXPRESION_menorigual','parser.py',431),
  ('EXPRESION -> EXPRESION igualacion EXPRESION','EXPRESION',3,'p_EXPRESION_igualacion','parser.py',438),
  ('EXPRESION -> EXPRESION diferente EXPRESION','EXPRESION',3,'p_EXPRESION_diferente','parser.py',445),
  ('EXPRESION -> FUNCION_TOFIXED','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',454),
  ('EXPRESION -> FUNCION_TOEXPONENTIAL','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',455),
  ('EXPRESION -> FUNCION_TOSTRING','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',456),
  ('EXPRESION -> FUNCION_TOLOWERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',457),
  ('EXPRESION -> FUNCION_TOUPPERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',458),
  ('EXPRESION -> FUNCION_SPLIT','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',459),
  ('FUNCION_TOFIXED -> id punto toFixed p_Abre EXPRESION p_Cierra','FUNCION_TOFIXED',6,'p_FUNCION_TOFIXED','parser.py',465),
  ('FUNCION_TOEXPONENTIAL -> id punto toExponential p_Abre EXPRESION p_Cierra','FUNCION_TOEXPONENTIAL',6,'p_FUNCION_TOEXPONENTIAL','parser.py',472),
  ('FUNCION_TOSTRING -> id punto toString p_Abre p_Cierra','FUNCION_TOSTRING',5,'p_FUNCION_TOSTRING','parser.py',479),
  ('FUNCION_TOLOWERCASE -> id punto toLowerCase p_Abre p_Cierra','FUNCION_TOLOWERCASE',5,'p_FUNCION_TOLOWERCASE','parser.py',486),
  ('FUNCION_TOUPPERCASE -> id punto toUpperCase p_Abre p_Cierra','FUNCION_TOUPPERCASE',5,'p_FUNCION_TOUPPERCASE','parser.py',493),
  ('FUNCION_SPLIT -> id punto split p_Abre EXPRESION p_Cierra','FUNCION_SPLIT',6,'p_FUNCION_SPLIT','parser.py',500),
  ('EXPRESION -> cadena','EXPRESION',1,'p_EXPRESION_cadena','parser.py',510),
  ('EXPRESION -> numero','EXPRESION',1,'p_EXPRESION_numero','parser.py',517),
  ('EXPRESION -> true','EXPRESION',1,'p_EXPRESION_booleano','parser.py',524),
  ('EXPRESION -> false','EXPRESION',1,'p_EXPRESION_booleano','parser.py',525),
  ('EXPRESION -> null','EXPRESION',1,'p_EXPRESION_null','parser.py',532),
  ('EXPRESION -> id','EXPRESION',1,'p_EXPRESION_Acceso','parser.py',539),
  ('EXPRESION -> id LISTAINDICES','EXPRESION',2,'p_EXPRESION_Acceso_Vector','parser.py',546),
  ('EXPRESION -> c_Abre LISTAEXPRESIONES c_Cierra','EXPRESION',3,'p_EXPRESION_Vector','parser.py',553),
  ('TIPO -> number','TIPO',1,'p_TIPO_NUMBER','parser.py',561),
  ('TIPO -> string','TIPO',1,'p_TIPO_STRING','parser.py',567),
  ('TIPO -> boolean','TIPO',1,'p_TIPO_BOOLEAN','parser.py',573),
  ('TIPO -> any','TIPO',1,'p_TIPO_ANY','parser.py',579),
]
