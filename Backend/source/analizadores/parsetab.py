
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftorleftandleftsumarestanonassocmenormayormenorigualmayorigualigualaciondiferenteleftmultiplicaciondivisionmoduloleftpotenciarightnotlefturestaand any boolean break c_Abre c_Cierra cadena coma concat console continue decremento diferente division dosPuntos else false fn for id if igual igualacion incremento let llave_Abre llave_Cierra log mayor mayorigual menor menorigual modulo multiplicacion not null number numero or p_Abre p_Cierra potencia punto puntoYcoma resta return split string stringMayus suma toExponential toFixed toLowerCase toString toUpperCase true typeof while\n    INICIO : ENTRADAS\n            | \n    \n    ENTRADAS : ENTRADAS ENTRADA\n    \n    ENTRADAS : ENTRADA\n    \n    ENTRADA : IMPRIMIR puntoYcoma\n            |   IF puntoYcoma\n            |   WHILE puntoYcoma\n            |   BREAK\n            |   CONTINUE\n            |   FOR puntoYcoma\n            |   INCREMENTO puntoYcoma\n            |   DECREMENTO puntoYcoma\n            |   FUNC puntoYcoma\n            |   LLAMADA_FUNCION puntoYcoma\n            |   RETURN\n    \n   FUNC : fn id p_Abre PARAMETROS_DECLA_FUNC p_Cierra llave_Abre ENTRADAS llave_Cierra\n   \n    FUNC : fn id p_Abre p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    PARAMETROS_DECLA_FUNC : PARAMETROS_DECLA_FUNC coma PARAMETRO_DECLA_FUNC\n                            | PARAMETRO_DECLA_FUNC\n    \n    PARAMETRO_DECLA_FUNC : id dosPuntos TIPO\n    \n    PARAMETRO_DECLA_FUNC : id dosPuntos TIPO c_Abre c_Cierra\n    \n    EXPRESION : LLAMADA_FUNCION\n    \n    LLAMADA_FUNCION : id p_Abre PARAMETROS_LLAMA_FUNC p_Cierra\n    \n    LLAMADA_FUNCION : id p_Abre p_Cierra\n    \n    PARAMETROS_LLAMA_FUNC : EXPRESION\n                          | PARAMETROS_LLAMA_FUNC coma EXPRESION\n    \n    FOR : for p_Abre DECLARACION puntoYcoma EXPRESION puntoYcoma FORITERADOR p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    FORITERADOR : ASIGNACION\n                | INCREMENTO\n                | DECREMENTO\n    \n    BREAK : break puntoYcoma\n    \n    CONTINUE : continue puntoYcoma\n    \n    RETURN : return EXPRESION puntoYcoma\n    \n    RETURN : return puntoYcoma\n    \n    WHILE : while p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    IF : if p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra COMPLEMENTO_IF\n    \n    COMPLEMENTO_IF : else IF\n                    | else llave_Abre ENTRADAS llave_Cierra\n                    | \n    \n    ENTRADA : DECLARACION puntoYcoma\n    \n    DECLARACION : let id igual EXPRESION\n    \n    DECLARACION : let id dosPuntos TIPO igual EXPRESION\n    \n    DECLARACION : let id \n    \n    DECLARACION : let id dosPuntos TIPO\n    \n    DECLARACION : let id dosPuntos TIPO c_Abre c_Cierra igual EXPRESION\n    \n    DECLARACION : let id dosPuntos TIPO c_Abre c_Cierra\n    \n    ENTRADA : ASIGNACION puntoYcoma\n    \n    ASIGNACION : id igual EXPRESION\n    \n    ASIGNACION : id LISTAINDICES igual EXPRESION\n    \n    INCREMENTO : id incremento \n    \n    DECREMENTO : id decremento\n    \n    IMPRIMIR : console punto log p_Abre LISTAEXPRESIONES p_Cierra\n    \n    LISTAEXPRESIONES :  LISTAEXPRESIONES coma EXPRESION\n    \n    LISTAEXPRESIONES : EXPRESION\n    \n    LISTAINDICES :  LISTAINDICES c_Abre EXPRESION c_Cierra\n    \n    LISTAINDICES : c_Abre EXPRESION c_Cierra\n    \n    EXPRESION : EXPRESION suma EXPRESION\n    \n    EXPRESION : EXPRESION resta EXPRESION\n    \n    EXPRESION : EXPRESION multiplicacion EXPRESION\n    \n    EXPRESION : EXPRESION division EXPRESION\n    \n    EXPRESION : EXPRESION potencia EXPRESION\n    \n    EXPRESION : EXPRESION modulo EXPRESION\n    \n    EXPRESION : resta EXPRESION %prec uresta\n    \n    EXPRESION : EXPRESION and EXPRESION\n    \n    EXPRESION : EXPRESION or EXPRESION\n    \n    EXPRESION : not EXPRESION\n    \n    EXPRESION : EXPRESION mayor EXPRESION\n    \n    EXPRESION : EXPRESION mayorigual EXPRESION\n    \n    EXPRESION : EXPRESION menor EXPRESION\n    \n    EXPRESION : EXPRESION menorigual EXPRESION\n    \n    EXPRESION : EXPRESION igualacion EXPRESION\n    \n    EXPRESION : EXPRESION diferente EXPRESION\n    \n    EXPRESION : FUNCION_TOFIXED\n            | FUNCION_TOEXPONENTIAL\n            | FUNCION_TOSTRING\n            | FUNCION_TOLOWERCASE\n            | FUNCION_TOUPPERCASE\n            | FUNCION_SPLIT\n            | FUNCION_CONCAT\n            | FUNCION_TYPEOF\n    \n    FUNCION_TOFIXED : id punto toFixed p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOEXPONENTIAL : id punto toExponential p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOSTRING : id punto toString p_Abre p_Cierra\n    \n    FUNCION_TOLOWERCASE : id punto toLowerCase p_Abre p_Cierra\n    \n    FUNCION_TOUPPERCASE : id punto toUpperCase p_Abre p_Cierra\n    \n    FUNCION_SPLIT : id punto split p_Abre EXPRESION p_Cierra\n    \n    FUNCION_CONCAT : id punto concat p_Abre LISTAEXPRESIONES p_Cierra\n    \n    FUNCION_TYPEOF : typeof p_Abre EXPRESION p_Cierra\n    \n    EXPRESION : cadena\n    \n    EXPRESION : numero\n    \n    EXPRESION : true\n                | false\n    \n    EXPRESION : null\n    \n    EXPRESION : id\n    \n    EXPRESION : id LISTAINDICES\n    \n    EXPRESION : c_Abre LISTAEXPRESIONES c_Cierra\n    \n    EXPRESION : TIPO p_Abre EXPRESION p_Cierra\n    \n    TIPO : number\n    \n    TIPO : string\n    \n    TIPO : stringMayus\n    \n    TIPO : boolean\n    \n    TIPO : any\n    '
    
_lr_action_items = {'$end':([0,1,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,],[-2,0,-1,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,]),'console':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[17,17,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,17,17,17,17,17,17,17,17,17,17,17,17,]),'if':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,211,217,218,219,220,],[18,18,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'while':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[19,19,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,19,19,19,19,19,19,19,19,19,19,19,19,]),'break':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[20,20,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,20,20,20,20,20,20,20,20,20,20,20,20,]),'continue':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[21,21,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,21,21,21,21,21,21,21,21,21,21,21,21,]),'for':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[22,22,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,22,22,22,22,22,22,22,22,22,22,22,22,]),'id':([0,2,3,7,8,14,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,46,47,49,52,54,55,70,87,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,157,158,164,165,166,167,171,172,176,179,180,181,183,185,203,209,217,218,219,220,],[23,23,-4,-8,-9,-15,50,69,78,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,69,69,-31,-32,69,69,69,-34,69,69,69,69,69,125,-33,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,23,23,125,23,69,69,69,69,69,23,23,201,23,23,23,69,23,23,23,23,]),'fn':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[24,24,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,24,24,24,24,24,24,24,24,24,24,24,24,]),'return':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[25,25,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,25,25,25,25,25,25,25,25,25,25,25,25,]),'let':([0,2,3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,43,52,91,157,158,165,179,180,183,185,203,217,218,219,220,],[26,26,-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,26,-34,-33,26,26,26,26,26,26,26,26,26,26,26,26,]),'llave_Cierra':([3,7,8,14,27,28,29,30,31,32,33,34,35,36,37,41,42,52,91,179,180,185,203,219,220,],[-4,-8,-9,-15,-3,-5,-6,-7,-10,-11,-12,-13,-14,-40,-47,-31,-32,-34,-33,195,196,204,214,221,222,]),'puntoYcoma':([4,5,6,9,10,11,12,13,15,16,20,21,25,44,45,51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,73,74,75,76,77,78,82,84,86,106,107,108,120,122,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,154,155,159,161,174,175,178,188,189,190,193,194,195,196,204,205,206,207,208,210,214,215,216,221,222,],[28,29,30,31,32,33,34,35,36,37,41,42,52,-50,-51,91,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,-98,-99,-100,-101,-102,-43,119,-24,-48,-63,-66,-95,-23,-49,-56,-57,-58,-59,-60,-61,-62,-64,-65,-67,-68,-69,-70,-71,-72,-96,-41,-44,181,-55,-97,-88,-52,-83,-84,-85,-42,-46,-39,-35,-17,-81,-82,-86,-87,-36,-16,-45,-37,-38,-27,]),'punto':([17,69,],[38,109,]),'p_Abre':([18,19,22,23,50,69,71,72,73,74,75,76,77,79,143,144,145,146,147,148,149,],[39,40,43,46,90,46,112,113,-98,-99,-100,-101,-102,116,166,167,168,169,170,171,172,]),'incremento':([23,201,],[44,44,]),'decremento':([23,201,],[45,45,]),'igual':([23,48,73,74,75,76,77,78,124,155,161,194,201,],[47,87,-98,-99,-100,-101,-102,114,-56,176,-55,209,47,]),'c_Abre':([23,25,39,40,46,47,48,49,54,55,69,70,73,74,75,76,77,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,108,112,113,114,116,119,121,124,151,155,161,166,167,171,172,176,182,201,209,],[49,70,70,70,70,70,88,70,70,70,49,70,-98,-99,-100,-101,-102,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,88,70,70,70,70,70,70,-56,70,177,-55,70,70,70,70,70,202,49,70,]),'resta':([25,39,40,46,47,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,80,81,84,85,86,87,88,89,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,111,112,113,114,116,119,120,121,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,151,152,153,154,159,160,161,166,167,171,172,173,174,175,176,186,187,188,189,190,191,193,205,206,207,208,209,215,],[54,54,54,54,54,54,93,-22,54,54,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,54,93,93,-24,93,93,54,54,93,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-63,-66,-95,93,54,54,54,54,54,-23,54,93,93,-56,-57,-58,-59,-60,-61,-62,93,93,-67,-68,-69,-70,-71,-72,-96,54,93,93,93,93,93,-55,54,54,54,54,93,-97,-88,54,93,93,-83,-84,-85,93,93,-81,-82,-86,-87,54,93,]),'not':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'cadena':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'numero':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'true':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'false':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'null':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'typeof':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'number':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,115,116,119,121,151,162,166,167,171,172,176,209,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'string':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,115,116,119,121,151,162,166,167,171,172,176,209,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'stringMayus':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,115,116,119,121,151,162,166,167,171,172,176,209,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'boolean':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,115,116,119,121,151,162,166,167,171,172,176,209,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'any':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,115,116,119,121,151,162,166,167,171,172,176,209,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'log':([38,],[79,]),'p_Cierra':([44,45,46,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,73,74,75,76,77,80,81,83,84,85,86,90,106,107,108,111,120,122,124,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,156,160,161,168,169,170,173,174,175,182,184,186,187,188,189,190,191,192,197,198,199,200,205,206,207,208,213,],[-50,-51,84,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,-98,-99,-100,-101,-102,117,118,120,-24,-25,-48,127,-63,-66,-95,-54,-23,-49,-56,163,-19,-57,-58,-59,-60,-61,-62,-64,-65,-67,-68,-69,-70,-71,-72,-96,174,175,178,-26,-55,188,189,190,-53,-97,-88,-20,-18,205,206,-83,-84,-85,207,208,212,-28,-29,-30,-81,-82,-86,-87,-21,]),'suma':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[92,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,92,92,-24,92,92,92,-63,-66,-95,92,-23,92,92,-56,-57,-58,-59,-60,-61,-62,92,92,-67,-68,-69,-70,-71,-72,-96,92,92,92,92,92,-55,92,-97,-88,92,92,-83,-84,-85,92,92,-81,-82,-86,-87,92,]),'multiplicacion':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[94,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,94,94,-24,94,94,94,-63,-66,-95,94,-23,94,94,-56,94,94,-59,-60,-61,-62,94,94,94,94,94,94,94,94,-96,94,94,94,94,94,-55,94,-97,-88,94,94,-83,-84,-85,94,94,-81,-82,-86,-87,94,]),'division':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[95,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,95,95,-24,95,95,95,-63,-66,-95,95,-23,95,95,-56,95,95,-59,-60,-61,-62,95,95,95,95,95,95,95,95,-96,95,95,95,95,95,-55,95,-97,-88,95,95,-83,-84,-85,95,95,-81,-82,-86,-87,95,]),'potencia':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[96,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,96,96,-24,96,96,96,-63,-66,-95,96,-23,96,96,-56,96,96,96,96,-61,96,96,96,96,96,96,96,96,96,-96,96,96,96,96,96,-55,96,-97,-88,96,96,-83,-84,-85,96,96,-81,-82,-86,-87,96,]),'modulo':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[97,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,97,97,-24,97,97,97,-63,-66,-95,97,-23,97,97,-56,97,97,-59,-60,-61,-62,97,97,97,97,97,97,97,97,-96,97,97,97,97,97,-55,97,-97,-88,97,97,-83,-84,-85,97,97,-81,-82,-86,-87,97,]),'and':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[98,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,98,98,-24,98,98,98,-63,-66,-95,98,-23,98,98,-56,-57,-58,-59,-60,-61,-62,-64,98,-67,-68,-69,-70,-71,-72,-96,98,98,98,98,98,-55,98,-97,-88,98,98,-83,-84,-85,98,98,-81,-82,-86,-87,98,]),'or':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[99,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,99,99,-24,99,99,99,-63,-66,-95,99,-23,99,99,-56,-57,-58,-59,-60,-61,-62,-64,-65,-67,-68,-69,-70,-71,-72,-96,99,99,99,99,99,-55,99,-97,-88,99,99,-83,-84,-85,99,99,-81,-82,-86,-87,99,]),'mayor':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[100,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,100,100,-24,100,100,100,-63,-66,-95,100,-23,100,100,-56,100,100,-59,-60,-61,-62,100,100,None,None,None,None,None,None,-96,100,100,100,100,100,-55,100,-97,-88,100,100,-83,-84,-85,100,100,-81,-82,-86,-87,100,]),'mayorigual':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[101,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,101,101,-24,101,101,101,-63,-66,-95,101,-23,101,101,-56,101,101,-59,-60,-61,-62,101,101,None,None,None,None,None,None,-96,101,101,101,101,101,-55,101,-97,-88,101,101,-83,-84,-85,101,101,-81,-82,-86,-87,101,]),'menor':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[102,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,102,102,-24,102,102,102,-63,-66,-95,102,-23,102,102,-56,102,102,-59,-60,-61,-62,102,102,None,None,None,None,None,None,-96,102,102,102,102,102,-55,102,-97,-88,102,102,-83,-84,-85,102,102,-81,-82,-86,-87,102,]),'menorigual':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[103,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,103,103,-24,103,103,103,-63,-66,-95,103,-23,103,103,-56,103,103,-59,-60,-61,-62,103,103,None,None,None,None,None,None,-96,103,103,103,103,103,-55,103,-97,-88,103,103,-83,-84,-85,103,103,-81,-82,-86,-87,103,]),'igualacion':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[104,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,104,104,-24,104,104,104,-63,-66,-95,104,-23,104,104,-56,104,104,-59,-60,-61,-62,104,104,None,None,None,None,None,None,-96,104,104,104,104,104,-55,104,-97,-88,104,104,-83,-84,-85,104,104,-81,-82,-86,-87,104,]),'diferente':([51,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,80,81,84,85,86,89,106,107,108,111,120,122,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,152,153,154,159,160,161,173,174,175,186,187,188,189,190,191,193,205,206,207,208,215,],[105,-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,105,105,-24,105,105,105,-63,-66,-95,105,-23,105,105,-56,105,105,-59,-60,-61,-62,105,105,None,None,None,None,None,None,-96,105,105,105,105,105,-55,105,-97,-88,105,105,-83,-84,-85,105,105,-81,-82,-86,-87,105,]),'coma':([53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,73,74,75,76,77,83,84,85,106,107,108,110,111,120,124,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,156,160,161,173,174,175,182,184,188,189,190,192,205,206,207,208,213,],[-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,-98,-99,-100,-101,-102,121,-24,-25,-63,-66,-95,151,-54,-23,-56,164,-19,-57,-58,-59,-60,-61,-62,-64,-65,-67,-68,-69,-70,-71,-72,-96,151,-26,-55,-53,-97,-88,-20,-18,-83,-84,-85,151,-81,-82,-86,-87,-21,]),'c_Cierra':([53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,84,89,106,107,108,110,111,120,123,124,129,130,131,132,133,134,135,136,137,138,139,140,141,142,150,161,173,174,175,177,188,189,190,202,205,206,207,208,],[-22,-73,-74,-75,-76,-77,-78,-79,-80,-89,-90,-91,-92,-93,-94,-24,124,-63,-66,-95,150,-54,-23,161,-56,-57,-58,-59,-60,-61,-62,-64,-65,-67,-68,-69,-70,-71,-72,-96,-55,-53,-97,-88,194,-83,-84,-85,213,-81,-82,-86,-87,]),'dosPuntos':([78,125,],[115,162,]),'toFixed':([109,],[143,]),'toExponential':([109,],[144,]),'toString':([109,],[145,]),'toLowerCase':([109,],[146,]),'toUpperCase':([109,],[147,]),'split':([109,],[148,]),'concat':([109,],[149,]),'llave_Abre':([117,118,127,163,211,212,],[157,158,165,183,217,218,]),'else':([195,],[211,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INICIO':([0,],[1,]),'ENTRADAS':([0,157,158,165,183,217,218,],[2,179,180,185,203,219,220,]),'ENTRADA':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[3,27,3,3,3,27,27,3,27,27,3,3,27,27,]),'IMPRIMIR':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'IF':([0,2,157,158,165,179,180,183,185,203,211,217,218,219,220,],[5,5,5,5,5,5,5,5,5,5,216,5,5,5,5,]),'WHILE':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'BREAK':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'CONTINUE':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'FOR':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'INCREMENTO':([0,2,157,158,165,179,180,181,183,185,203,217,218,219,220,],[10,10,10,10,10,10,10,199,10,10,10,10,10,10,10,]),'DECREMENTO':([0,2,157,158,165,179,180,181,183,185,203,217,218,219,220,],[11,11,11,11,11,11,11,200,11,11,11,11,11,11,11,]),'FUNC':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'LLAMADA_FUNCION':([0,2,25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,157,158,165,166,167,171,172,176,179,180,183,185,203,209,217,218,219,220,],[13,13,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,13,13,13,53,53,53,53,53,13,13,13,13,13,53,13,13,13,13,]),'RETURN':([0,2,157,158,165,179,180,183,185,203,217,218,219,220,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'DECLARACION':([0,2,43,157,158,165,179,180,183,185,203,217,218,219,220,],[15,15,82,15,15,15,15,15,15,15,15,15,15,15,15,]),'ASIGNACION':([0,2,157,158,165,179,180,181,183,185,203,217,218,219,220,],[16,16,16,16,16,16,16,198,16,16,16,16,16,16,16,]),'LISTAINDICES':([23,69,201,],[48,108,48,]),'EXPRESION':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[51,80,81,85,86,89,106,107,111,122,123,129,130,131,132,133,134,135,136,137,138,139,140,141,142,152,153,154,111,159,160,173,186,187,191,111,193,215,]),'FUNCION_TOFIXED':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'FUNCION_TOEXPONENTIAL':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'FUNCION_TOSTRING':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'FUNCION_TOLOWERCASE':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'FUNCION_TOUPPERCASE':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'FUNCION_SPLIT':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'FUNCION_CONCAT':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'FUNCION_TYPEOF':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,116,119,121,151,166,167,171,172,176,209,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'TIPO':([25,39,40,46,47,49,54,55,70,87,88,92,93,94,95,96,97,98,99,100,101,102,103,104,105,112,113,114,115,116,119,121,151,162,166,167,171,172,176,209,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,155,71,71,71,71,182,71,71,71,71,71,71,]),'PARAMETROS_LLAMA_FUNC':([46,],[83,]),'LISTAEXPRESIONES':([70,116,172,],[110,156,192,]),'PARAMETROS_DECLA_FUNC':([90,],[126,]),'PARAMETRO_DECLA_FUNC':([90,164,],[128,184,]),'FORITERADOR':([181,],[197,]),'COMPLEMENTO_IF':([195,],[210,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INICIO","S'",1,None,None,None),
  ('INICIO -> ENTRADAS','INICIO',1,'p_INICIO','parser.py',67),
  ('INICIO -> <empty>','INICIO',0,'p_INICIO','parser.py',68),
  ('ENTRADAS -> ENTRADAS ENTRADA','ENTRADAS',2,'p_ENTRADAS_PARTE_1','parser.py',77),
  ('ENTRADAS -> ENTRADA','ENTRADAS',1,'p_ENTRADAS_PARTE_2','parser.py',84),
  ('ENTRADA -> IMPRIMIR puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',90),
  ('ENTRADA -> IF puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',91),
  ('ENTRADA -> WHILE puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',92),
  ('ENTRADA -> BREAK','ENTRADA',1,'p_ENTRADA','parser.py',93),
  ('ENTRADA -> CONTINUE','ENTRADA',1,'p_ENTRADA','parser.py',94),
  ('ENTRADA -> FOR puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',95),
  ('ENTRADA -> INCREMENTO puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',96),
  ('ENTRADA -> DECREMENTO puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',97),
  ('ENTRADA -> FUNC puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',98),
  ('ENTRADA -> LLAMADA_FUNCION puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',99),
  ('ENTRADA -> RETURN','ENTRADA',1,'p_ENTRADA','parser.py',100),
  ('FUNC -> fn id p_Abre PARAMETROS_DECLA_FUNC p_Cierra llave_Abre ENTRADAS llave_Cierra','FUNC',8,'p_FUNC_1','parser.py',118),
  ('FUNC -> fn id p_Abre p_Cierra llave_Abre ENTRADAS llave_Cierra','FUNC',7,'p_FUNC_2','parser.py',125),
  ('PARAMETROS_DECLA_FUNC -> PARAMETROS_DECLA_FUNC coma PARAMETRO_DECLA_FUNC','PARAMETROS_DECLA_FUNC',3,'p_PARAMETROS_DECLA_FUNC','parser.py',132),
  ('PARAMETROS_DECLA_FUNC -> PARAMETRO_DECLA_FUNC','PARAMETROS_DECLA_FUNC',1,'p_PARAMETROS_DECLA_FUNC','parser.py',133),
  ('PARAMETRO_DECLA_FUNC -> id dosPuntos TIPO','PARAMETRO_DECLA_FUNC',3,'p_PARAMETRO_DECLA_FUNC_1','parser.py',143),
  ('PARAMETRO_DECLA_FUNC -> id dosPuntos TIPO c_Abre c_Cierra','PARAMETRO_DECLA_FUNC',5,'p_PARAMETRO_DECLA_FUNC_2','parser.py',149),
  ('EXPRESION -> LLAMADA_FUNCION','EXPRESION',1,'p_EXPRESION_LLAMA_FUNC','parser.py',156),
  ('LLAMADA_FUNCION -> id p_Abre PARAMETROS_LLAMA_FUNC p_Cierra','LLAMADA_FUNCION',4,'p_LLAMADA_FUNCION_1','parser.py',163),
  ('LLAMADA_FUNCION -> id p_Abre p_Cierra','LLAMADA_FUNCION',3,'p_LLAMADA_FUNCION_2','parser.py',169),
  ('PARAMETROS_LLAMA_FUNC -> EXPRESION','PARAMETROS_LLAMA_FUNC',1,'p_PARAMETROS_LLAMA_FUNC','parser.py',175),
  ('PARAMETROS_LLAMA_FUNC -> PARAMETROS_LLAMA_FUNC coma EXPRESION','PARAMETROS_LLAMA_FUNC',3,'p_PARAMETROS_LLAMA_FUNC','parser.py',176),
  ('FOR -> for p_Abre DECLARACION puntoYcoma EXPRESION puntoYcoma FORITERADOR p_Cierra llave_Abre ENTRADAS llave_Cierra','FOR',11,'p_FOR','parser.py',187),
  ('FORITERADOR -> ASIGNACION','FORITERADOR',1,'p_FORITERADOR','parser.py',193),
  ('FORITERADOR -> INCREMENTO','FORITERADOR',1,'p_FORITERADOR','parser.py',194),
  ('FORITERADOR -> DECREMENTO','FORITERADOR',1,'p_FORITERADOR','parser.py',195),
  ('BREAK -> break puntoYcoma','BREAK',2,'p_BREAK','parser.py',202),
  ('CONTINUE -> continue puntoYcoma','CONTINUE',2,'p_CONTINUE','parser.py',208),
  ('RETURN -> return EXPRESION puntoYcoma','RETURN',3,'p_RETURN_1','parser.py',214),
  ('RETURN -> return puntoYcoma','RETURN',2,'p_RETURN_2','parser.py',220),
  ('WHILE -> while p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra','WHILE',7,'p_WHILE','parser.py',229),
  ('IF -> if p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra COMPLEMENTO_IF','IF',8,'p_IF','parser.py',236),
  ('COMPLEMENTO_IF -> else IF','COMPLEMENTO_IF',2,'p_COMPLEMENTO_IF','parser.py',242),
  ('COMPLEMENTO_IF -> else llave_Abre ENTRADAS llave_Cierra','COMPLEMENTO_IF',4,'p_COMPLEMENTO_IF','parser.py',243),
  ('COMPLEMENTO_IF -> <empty>','COMPLEMENTO_IF',0,'p_COMPLEMENTO_IF','parser.py',244),
  ('ENTRADA -> DECLARACION puntoYcoma','ENTRADA',2,'p_ENTRADA_Declaracion','parser.py',257),
  ('DECLARACION -> let id igual EXPRESION','DECLARACION',4,'p_DECLARACION_NoTipada','parser.py',263),
  ('DECLARACION -> let id dosPuntos TIPO igual EXPRESION','DECLARACION',6,'p_DECLARACION_Tipada','parser.py',270),
  ('DECLARACION -> let id','DECLARACION',2,'p_DECLARACION_SinExpresion_SinTipado','parser.py',276),
  ('DECLARACION -> let id dosPuntos TIPO','DECLARACION',4,'p_DECLARACION_SinExpresion_Tipado','parser.py',282),
  ('DECLARACION -> let id dosPuntos TIPO c_Abre c_Cierra igual EXPRESION','DECLARACION',8,'p_DECLARACION_Tipada_VECTOR','parser.py',288),
  ('DECLARACION -> let id dosPuntos TIPO c_Abre c_Cierra','DECLARACION',6,'p_DECLARACION_SinExpresion_Tipado_VECTOR','parser.py',294),
  ('ENTRADA -> ASIGNACION puntoYcoma','ENTRADA',2,'p_ENTRADA_Asignacion','parser.py',303),
  ('ASIGNACION -> id igual EXPRESION','ASIGNACION',3,'p_ASIGNACION','parser.py',309),
  ('ASIGNACION -> id LISTAINDICES igual EXPRESION','ASIGNACION',4,'p_ASIGNACION_VEC','parser.py',315),
  ('INCREMENTO -> id incremento','INCREMENTO',2,'p_INCREMENTO','parser.py',323),
  ('DECREMENTO -> id decremento','DECREMENTO',2,'p_DECREMENTO','parser.py',329),
  ('IMPRIMIR -> console punto log p_Abre LISTAEXPRESIONES p_Cierra','IMPRIMIR',6,'p_IMPRIMIR_1','parser.py',336),
  ('LISTAEXPRESIONES -> LISTAEXPRESIONES coma EXPRESION','LISTAEXPRESIONES',3,'p_LISTAEXPRESIONES_1','parser.py',342),
  ('LISTAEXPRESIONES -> EXPRESION','LISTAEXPRESIONES',1,'p_LISTAEXPRESIONES_2','parser.py',349),
  ('LISTAINDICES -> LISTAINDICES c_Abre EXPRESION c_Cierra','LISTAINDICES',4,'p_LISTAEXPRESIONES_Indices','parser.py',355),
  ('LISTAINDICES -> c_Abre EXPRESION c_Cierra','LISTAINDICES',3,'p_LISTAEXPRESIONES_Indices_2','parser.py',362),
  ('EXPRESION -> EXPRESION suma EXPRESION','EXPRESION',3,'p_EXPRESION_suma','parser.py',370),
  ('EXPRESION -> EXPRESION resta EXPRESION','EXPRESION',3,'p_EXPRESION_resta','parser.py',377),
  ('EXPRESION -> EXPRESION multiplicacion EXPRESION','EXPRESION',3,'p_EXPRESION_multiplicacion','parser.py',384),
  ('EXPRESION -> EXPRESION division EXPRESION','EXPRESION',3,'p_EXPRESION_division','parser.py',391),
  ('EXPRESION -> EXPRESION potencia EXPRESION','EXPRESION',3,'p_EXPRESION_potencia','parser.py',398),
  ('EXPRESION -> EXPRESION modulo EXPRESION','EXPRESION',3,'p_EXPRESION_modulo','parser.py',405),
  ('EXPRESION -> resta EXPRESION','EXPRESION',2,'p_EXPRESION_negativo','parser.py',412),
  ('EXPRESION -> EXPRESION and EXPRESION','EXPRESION',3,'p_EXPRESION_and','parser.py',421),
  ('EXPRESION -> EXPRESION or EXPRESION','EXPRESION',3,'p_EXPRESION_or','parser.py',428),
  ('EXPRESION -> not EXPRESION','EXPRESION',2,'p_EXPRESION_not','parser.py',435),
  ('EXPRESION -> EXPRESION mayor EXPRESION','EXPRESION',3,'p_EXPRESION_mayor','parser.py',444),
  ('EXPRESION -> EXPRESION mayorigual EXPRESION','EXPRESION',3,'p_EXPRESION_mayorigual','parser.py',451),
  ('EXPRESION -> EXPRESION menor EXPRESION','EXPRESION',3,'p_EXPRESION_menor','parser.py',458),
  ('EXPRESION -> EXPRESION menorigual EXPRESION','EXPRESION',3,'p_EXPRESION_menorigual','parser.py',465),
  ('EXPRESION -> EXPRESION igualacion EXPRESION','EXPRESION',3,'p_EXPRESION_igualacion','parser.py',472),
  ('EXPRESION -> EXPRESION diferente EXPRESION','EXPRESION',3,'p_EXPRESION_diferente','parser.py',479),
  ('EXPRESION -> FUNCION_TOFIXED','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',488),
  ('EXPRESION -> FUNCION_TOEXPONENTIAL','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',489),
  ('EXPRESION -> FUNCION_TOSTRING','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',490),
  ('EXPRESION -> FUNCION_TOLOWERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',491),
  ('EXPRESION -> FUNCION_TOUPPERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',492),
  ('EXPRESION -> FUNCION_SPLIT','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',493),
  ('EXPRESION -> FUNCION_CONCAT','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',494),
  ('EXPRESION -> FUNCION_TYPEOF','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',495),
  ('FUNCION_TOFIXED -> id punto toFixed p_Abre EXPRESION p_Cierra','FUNCION_TOFIXED',6,'p_FUNCION_TOFIXED','parser.py',501),
  ('FUNCION_TOEXPONENTIAL -> id punto toExponential p_Abre EXPRESION p_Cierra','FUNCION_TOEXPONENTIAL',6,'p_FUNCION_TOEXPONENTIAL','parser.py',508),
  ('FUNCION_TOSTRING -> id punto toString p_Abre p_Cierra','FUNCION_TOSTRING',5,'p_FUNCION_TOSTRING','parser.py',515),
  ('FUNCION_TOLOWERCASE -> id punto toLowerCase p_Abre p_Cierra','FUNCION_TOLOWERCASE',5,'p_FUNCION_TOLOWERCASE','parser.py',522),
  ('FUNCION_TOUPPERCASE -> id punto toUpperCase p_Abre p_Cierra','FUNCION_TOUPPERCASE',5,'p_FUNCION_TOUPPERCASE','parser.py',529),
  ('FUNCION_SPLIT -> id punto split p_Abre EXPRESION p_Cierra','FUNCION_SPLIT',6,'p_FUNCION_SPLIT','parser.py',536),
  ('FUNCION_CONCAT -> id punto concat p_Abre LISTAEXPRESIONES p_Cierra','FUNCION_CONCAT',6,'p_FUNCION_CONCAT','parser.py',543),
  ('FUNCION_TYPEOF -> typeof p_Abre EXPRESION p_Cierra','FUNCION_TYPEOF',4,'p_FUNCION_TYPEOF','parser.py',550),
  ('EXPRESION -> cadena','EXPRESION',1,'p_EXPRESION_cadena','parser.py',558),
  ('EXPRESION -> numero','EXPRESION',1,'p_EXPRESION_numero','parser.py',565),
  ('EXPRESION -> true','EXPRESION',1,'p_EXPRESION_booleano','parser.py',572),
  ('EXPRESION -> false','EXPRESION',1,'p_EXPRESION_booleano','parser.py',573),
  ('EXPRESION -> null','EXPRESION',1,'p_EXPRESION_null','parser.py',580),
  ('EXPRESION -> id','EXPRESION',1,'p_EXPRESION_Acceso','parser.py',587),
  ('EXPRESION -> id LISTAINDICES','EXPRESION',2,'p_EXPRESION_Acceso_Vector','parser.py',594),
  ('EXPRESION -> c_Abre LISTAEXPRESIONES c_Cierra','EXPRESION',3,'p_EXPRESION_Vector','parser.py',601),
  ('EXPRESION -> TIPO p_Abre EXPRESION p_Cierra','EXPRESION',4,'p_EXPRESION_Casteo','parser.py',608),
  ('TIPO -> number','TIPO',1,'p_TIPO_NUMBER','parser.py',616),
  ('TIPO -> string','TIPO',1,'p_TIPO_STRING','parser.py',622),
  ('TIPO -> stringMayus','TIPO',1,'p_TIPO_STRINGMayus','parser.py',628),
  ('TIPO -> boolean','TIPO',1,'p_TIPO_BOOLEAN','parser.py',634),
  ('TIPO -> any','TIPO',1,'p_TIPO_ANY','parser.py',640),
]
