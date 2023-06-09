
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftorleftandleftsumarestanonassocmenormayormenorigualmayorigualigualaciondiferenteleftmultiplicaciondivisionmoduloleftpotenciarightnotlefturestaand any boolean break c_Abre c_Cierra cadena coma concat console continue diferente division dosPuntos else false for id if igual igualacion let llave_Abre llave_Cierra log mayor mayorigual menor menorigual modulo multiplicacion not null number numero or p_Abre p_Cierra potencia punto puntoYcoma resta split string suma toExponential toFixed toLowerCase toString toUpperCase true while\n    INICIO : ENTRADAS\n    \n    ENTRADAS : ENTRADAS ENTRADA\n    \n    ENTRADAS : ENTRADA\n    \n    ENTRADA : IMPRIMIR puntoYcoma\n            |   IF puntoYcoma\n            |   WHILE puntoYcoma\n            |   BREAK\n            |   CONTINUE\n            |   FOR puntoYcoma\n    \n    FOR : for p_Abre DECLARACION puntoYcoma EXPRESION puntoYcoma ASIGNACION p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    BREAK : break puntoYcoma\n    \n    CONTINUE : continue puntoYcoma\n    \n    WHILE : while p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    IF : if p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra COMPLEMENTO_IF\n    \n    COMPLEMENTO_IF : else IF\n                    | else llave_Abre ENTRADAS llave_Cierra\n                    | \n    \n    ENTRADA : DECLARACION puntoYcoma\n    \n    DECLARACION : let id igual EXPRESION\n    \n    DECLARACION : let id dosPuntos TIPO igual EXPRESION\n    \n    DECLARACION : let id \n    \n    DECLARACION : let id dosPuntos TIPO\n    \n    ENTRADA : ASIGNACION puntoYcoma\n    \n    ASIGNACION : id igual EXPRESION\n    \n    ASIGNACION : id LISTAINDICES igual EXPRESION\n    \n    IMPRIMIR : console punto log p_Abre LISTAEXPRESIONES p_Cierra\n    \n    LISTAEXPRESIONES :  LISTAEXPRESIONES coma EXPRESION\n    \n    LISTAEXPRESIONES : EXPRESION\n    \n    LISTAINDICES :  LISTAINDICES c_Abre EXPRESION c_Cierra\n    \n    LISTAINDICES : c_Abre EXPRESION c_Cierra\n    \n    EXPRESION : EXPRESION suma EXPRESION\n    \n    EXPRESION : EXPRESION resta EXPRESION\n    \n    EXPRESION : EXPRESION multiplicacion EXPRESION\n    \n    EXPRESION : EXPRESION division EXPRESION\n    \n    EXPRESION : EXPRESION potencia EXPRESION\n    \n    EXPRESION : EXPRESION modulo EXPRESION\n    \n    EXPRESION : resta EXPRESION %prec uresta\n    \n    EXPRESION : EXPRESION and EXPRESION\n    \n    EXPRESION : EXPRESION or EXPRESION\n    \n    EXPRESION : not EXPRESION\n    \n    EXPRESION : EXPRESION mayor EXPRESION\n    \n    EXPRESION : EXPRESION mayorigual EXPRESION\n    \n    EXPRESION : EXPRESION menor EXPRESION\n    \n    EXPRESION : EXPRESION menorigual EXPRESION\n    \n    EXPRESION : EXPRESION igualacion EXPRESION\n    \n    EXPRESION : EXPRESION diferente EXPRESION\n    \n    EXPRESION : FUNCION_TOFIXED\n            | FUNCION_TOEXPONENTIAL\n            | FUNCION_TOSTRING\n            | FUNCION_TOLOWERCASE\n            | FUNCION_TOUPPERCASE\n            | FUNCION_SPLIT\n    \n    FUNCION_TOFIXED : id punto toFixed p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOEXPONENTIAL : id punto toExponential p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOSTRING : id punto toString p_Abre p_Cierra\n    \n    FUNCION_TOLOWERCASE : id punto toLowerCase p_Abre p_Cierra\n    \n    FUNCION_TOUPPERCASE : id punto toUpperCase p_Abre p_Cierra\n    \n    FUNCION_SPLIT : id punto split p_Abre cadena p_Cierra\n    \n    EXPRESION : cadena\n    \n    EXPRESION : numero\n    \n    EXPRESION : true\n                | false\n    \n    EXPRESION : null\n    \n    EXPRESION : id\n    \n    EXPRESION : id LISTAINDICES\n    \n    EXPRESION : c_Abre LISTAEXPRESIONES c_Cierra\n    \n    TIPO : number\n    \n    TIPO : string\n    \n    TIPO : boolean\n    \n    TIPO : any\n    '
    
_lr_action_items = {'console':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,96,119,124,132,151,152,153,154,],[12,12,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,12,12,12,12,12,12,12,12,]),'if':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,96,119,124,132,145,151,152,153,154,],[13,13,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,13,13,13,13,13,13,13,13,13,]),'while':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,96,119,124,132,151,152,153,154,],[14,14,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,14,14,14,14,14,14,14,14,]),'break':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,96,119,124,132,151,152,153,154,],[15,15,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,15,15,15,15,15,15,15,15,]),'continue':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,96,119,124,132,151,152,153,154,],[16,16,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,16,16,16,16,16,16,16,16,]),'for':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,96,119,124,132,151,152,153,154,],[17,17,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,17,17,17,17,17,17,17,17,]),'let':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,32,96,119,124,132,151,152,153,154,],[18,18,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,18,18,18,18,18,18,18,18,18,]),'id':([0,2,3,7,8,18,20,21,22,23,24,25,26,28,29,30,31,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,96,118,119,121,124,125,126,132,133,151,152,153,154,],[19,19,-3,-7,-8,33,-2,-4,-5,-6,-9,-18,-23,52,52,-11,-12,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,19,52,19,52,19,52,52,19,19,19,19,19,19,]),'$end':([1,2,3,7,8,20,21,22,23,24,25,26,30,31,],[0,-1,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,]),'llave_Cierra':([3,7,8,20,21,22,23,24,25,26,30,31,124,132,153,154,],[-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,135,142,155,156,]),'puntoYcoma':([4,5,6,9,10,11,15,16,33,41,42,43,44,45,46,47,48,49,50,51,52,55,58,78,79,80,86,87,88,89,90,91,92,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,123,134,135,138,139,140,142,144,146,147,148,150,155,156,],[21,22,23,24,25,26,30,31,-21,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,85,-24,-37,-40,-65,-19,-22,-67,-68,-69,-70,-25,-30,-31,-32,-33,-34,-35,-36,-38,-39,-41,-42,-43,-44,-45,-46,-66,133,-29,-26,-20,-17,-55,-56,-57,-13,-14,-53,-54,-58,-15,-16,-10,]),'punto':([12,52,],[27,81,]),'p_Abre':([13,14,17,37,111,112,113,114,115,116,],[28,29,32,62,125,126,127,128,129,130,]),'igual':([19,33,35,87,88,89,90,91,94,122,],[34,56,59,121,-67,-68,-69,-70,-30,-29,]),'c_Abre':([19,28,29,34,35,36,39,40,52,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,85,94,118,121,122,125,126,],[36,53,53,53,60,53,53,53,36,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,60,53,-30,53,53,-29,53,53,]),'log':([27,],[37,]),'resta':([28,29,34,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,85,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,120,121,122,125,126,131,134,136,137,138,139,140,146,147,148,],[39,39,39,39,65,39,39,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,39,65,39,65,39,39,65,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-37,-40,-65,65,39,65,65,65,-30,-31,-32,-33,-34,-35,-36,65,65,-41,-42,-43,-44,-45,-46,-66,39,65,39,-29,39,39,65,65,65,65,-55,-56,-57,-53,-54,-58,]),'not':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'cadena':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,130,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,141,]),'numero':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'true':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'false':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'null':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'dosPuntos':([33,],[57,]),'p_Cierra':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,78,79,80,83,92,94,95,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,122,127,128,129,131,136,137,138,139,140,141,143,146,147,148,],[63,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,84,-24,-37,-40,-65,-28,-25,-30,123,-31,-32,-33,-34,-35,-36,-38,-39,-41,-42,-43,-44,-45,-46,-66,-29,138,139,140,-27,146,147,-55,-56,-57,148,149,-53,-54,-58,]),'suma':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[64,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,64,64,64,-37,-40,-65,64,64,64,64,-30,-31,-32,-33,-34,-35,-36,64,64,-41,-42,-43,-44,-45,-46,-66,64,-29,64,64,64,64,-55,-56,-57,-53,-54,-58,]),'multiplicacion':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[66,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,66,66,66,-37,-40,-65,66,66,66,66,-30,66,66,-33,-34,-35,-36,66,66,66,66,66,66,66,66,-66,66,-29,66,66,66,66,-55,-56,-57,-53,-54,-58,]),'division':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[67,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,67,67,67,-37,-40,-65,67,67,67,67,-30,67,67,-33,-34,-35,-36,67,67,67,67,67,67,67,67,-66,67,-29,67,67,67,67,-55,-56,-57,-53,-54,-58,]),'potencia':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[68,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,68,68,68,-37,-40,-65,68,68,68,68,-30,68,68,68,68,-35,68,68,68,68,68,68,68,68,68,-66,68,-29,68,68,68,68,-55,-56,-57,-53,-54,-58,]),'modulo':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[69,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,69,69,69,-37,-40,-65,69,69,69,69,-30,69,69,-33,-34,-35,-36,69,69,69,69,69,69,69,69,-66,69,-29,69,69,69,69,-55,-56,-57,-53,-54,-58,]),'and':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[70,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,70,70,70,-37,-40,-65,70,70,70,70,-30,-31,-32,-33,-34,-35,-36,-38,70,-41,-42,-43,-44,-45,-46,-66,70,-29,70,70,70,70,-55,-56,-57,-53,-54,-58,]),'or':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[71,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,71,71,71,-37,-40,-65,71,71,71,71,-30,-31,-32,-33,-34,-35,-36,-38,-39,-41,-42,-43,-44,-45,-46,-66,71,-29,71,71,71,71,-55,-56,-57,-53,-54,-58,]),'mayor':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[72,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,72,72,72,-37,-40,-65,72,72,72,72,-30,72,72,-33,-34,-35,-36,72,72,None,None,None,None,None,None,-66,72,-29,72,72,72,72,-55,-56,-57,-53,-54,-58,]),'mayorigual':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[73,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,73,73,73,-37,-40,-65,73,73,73,73,-30,73,73,-33,-34,-35,-36,73,73,None,None,None,None,None,None,-66,73,-29,73,73,73,73,-55,-56,-57,-53,-54,-58,]),'menor':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[74,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,74,74,74,-37,-40,-65,74,74,74,74,-30,74,74,-33,-34,-35,-36,74,74,None,None,None,None,None,None,-66,74,-29,74,74,74,74,-55,-56,-57,-53,-54,-58,]),'menorigual':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[75,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,75,75,75,-37,-40,-65,75,75,75,75,-30,75,75,-33,-34,-35,-36,75,75,None,None,None,None,None,None,-66,75,-29,75,75,75,75,-55,-56,-57,-53,-54,-58,]),'igualacion':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[76,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,76,76,76,-37,-40,-65,76,76,76,76,-30,76,76,-33,-34,-35,-36,76,76,None,None,None,None,None,None,-66,76,-29,76,76,76,76,-55,-56,-57,-53,-54,-58,]),'diferente':([38,41,42,43,44,45,46,47,48,49,50,51,52,54,58,61,78,79,80,83,86,92,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,120,122,131,134,136,137,138,139,140,146,147,148,],[77,-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,77,77,77,-37,-40,-65,77,77,77,77,-30,77,77,-33,-34,-35,-36,77,77,None,None,None,None,None,None,-66,77,-29,77,77,77,77,-55,-56,-57,-53,-54,-58,]),'c_Cierra':([41,42,43,44,45,46,47,48,49,50,51,52,61,78,79,80,82,83,93,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,122,131,138,139,140,146,147,148,],[-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,94,-37,-40,-65,117,-28,122,-30,-31,-32,-33,-34,-35,-36,-38,-39,-41,-42,-43,-44,-45,-46,-66,-29,-27,-55,-56,-57,-53,-54,-58,]),'coma':([41,42,43,44,45,46,47,48,49,50,51,52,78,79,80,82,83,94,95,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,122,131,138,139,140,146,147,148,],[-47,-48,-49,-50,-51,-52,-59,-60,-61,-62,-63,-64,-37,-40,-65,118,-28,-30,118,-31,-32,-33,-34,-35,-36,-38,-39,-41,-42,-43,-44,-45,-46,-66,-29,-27,-55,-56,-57,-53,-54,-58,]),'number':([57,],[88,]),'string':([57,],[89,]),'boolean':([57,],[90,]),'any':([57,],[91,]),'llave_Abre':([63,84,145,149,],[96,119,151,152,]),'toFixed':([81,],[111,]),'toExponential':([81,],[112,]),'toString':([81,],[113,]),'toLowerCase':([81,],[114,]),'toUpperCase':([81,],[115,]),'split':([81,],[116,]),'else':([135,],[145,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INICIO':([0,],[1,]),'ENTRADAS':([0,96,119,151,152,],[2,124,132,153,154,]),'ENTRADA':([0,2,96,119,124,132,151,152,153,154,],[3,20,3,3,20,20,3,3,20,20,]),'IMPRIMIR':([0,2,96,119,124,132,151,152,153,154,],[4,4,4,4,4,4,4,4,4,4,]),'IF':([0,2,96,119,124,132,145,151,152,153,154,],[5,5,5,5,5,5,150,5,5,5,5,]),'WHILE':([0,2,96,119,124,132,151,152,153,154,],[6,6,6,6,6,6,6,6,6,6,]),'BREAK':([0,2,96,119,124,132,151,152,153,154,],[7,7,7,7,7,7,7,7,7,7,]),'CONTINUE':([0,2,96,119,124,132,151,152,153,154,],[8,8,8,8,8,8,8,8,8,8,]),'FOR':([0,2,96,119,124,132,151,152,153,154,],[9,9,9,9,9,9,9,9,9,9,]),'DECLARACION':([0,2,32,96,119,124,132,151,152,153,154,],[10,10,55,10,10,10,10,10,10,10,10,]),'ASIGNACION':([0,2,96,119,124,132,133,151,152,153,154,],[11,11,11,11,11,11,143,11,11,11,11,]),'LISTAINDICES':([19,52,],[35,80,]),'EXPRESION':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[38,54,58,61,78,79,83,86,92,93,83,97,98,99,100,101,102,103,104,105,106,107,108,109,110,120,131,134,136,137,]),'FUNCION_TOFIXED':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'FUNCION_TOEXPONENTIAL':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'FUNCION_TOSTRING':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'FUNCION_TOLOWERCASE':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'FUNCION_TOUPPERCASE':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'FUNCION_SPLIT':([28,29,34,36,39,40,53,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,85,118,121,125,126,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'LISTAEXPRESIONES':([53,62,],[82,95,]),'TIPO':([57,],[87,]),'COMPLEMENTO_IF':([135,],[144,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INICIO","S'",1,None,None,None),
  ('INICIO -> ENTRADAS','INICIO',1,'p_INICIO','parser.py',58),
  ('ENTRADAS -> ENTRADAS ENTRADA','ENTRADAS',2,'p_ENTRADAS_PARTE_1','parser.py',64),
  ('ENTRADAS -> ENTRADA','ENTRADAS',1,'p_ENTRADAS_PARTE_2','parser.py',71),
  ('ENTRADA -> IMPRIMIR puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',77),
  ('ENTRADA -> IF puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',78),
  ('ENTRADA -> WHILE puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',79),
  ('ENTRADA -> BREAK','ENTRADA',1,'p_ENTRADA','parser.py',80),
  ('ENTRADA -> CONTINUE','ENTRADA',1,'p_ENTRADA','parser.py',81),
  ('ENTRADA -> FOR puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',82),
  ('FOR -> for p_Abre DECLARACION puntoYcoma EXPRESION puntoYcoma ASIGNACION p_Cierra llave_Abre ENTRADAS llave_Cierra','FOR',11,'p_FOR','parser.py',100),
  ('BREAK -> break puntoYcoma','BREAK',2,'p_BREAK','parser.py',107),
  ('CONTINUE -> continue puntoYcoma','CONTINUE',2,'p_CONTINUE','parser.py',113),
  ('WHILE -> while p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra','WHILE',7,'p_WHILE','parser.py',120),
  ('IF -> if p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra COMPLEMENTO_IF','IF',8,'p_IF','parser.py',127),
  ('COMPLEMENTO_IF -> else IF','COMPLEMENTO_IF',2,'p_COMPLEMENTO_IF','parser.py',133),
  ('COMPLEMENTO_IF -> else llave_Abre ENTRADAS llave_Cierra','COMPLEMENTO_IF',4,'p_COMPLEMENTO_IF','parser.py',134),
  ('COMPLEMENTO_IF -> <empty>','COMPLEMENTO_IF',0,'p_COMPLEMENTO_IF','parser.py',135),
  ('ENTRADA -> DECLARACION puntoYcoma','ENTRADA',2,'p_ENTRADA_Declaracion','parser.py',148),
  ('DECLARACION -> let id igual EXPRESION','DECLARACION',4,'p_DECLARACION_NoTipada','parser.py',154),
  ('DECLARACION -> let id dosPuntos TIPO igual EXPRESION','DECLARACION',6,'p_DECLARACION_Tipada','parser.py',161),
  ('DECLARACION -> let id','DECLARACION',2,'p_DECLARACION_SinExpresion_SinTipado','parser.py',167),
  ('DECLARACION -> let id dosPuntos TIPO','DECLARACION',4,'p_DECLARACION_SinExpresion_Tipado','parser.py',173),
  ('ENTRADA -> ASIGNACION puntoYcoma','ENTRADA',2,'p_ENTRADA_Asignacion','parser.py',181),
  ('ASIGNACION -> id igual EXPRESION','ASIGNACION',3,'p_ASIGNACION','parser.py',187),
  ('ASIGNACION -> id LISTAINDICES igual EXPRESION','ASIGNACION',4,'p_ASIGNACION_VEC','parser.py',193),
  ('IMPRIMIR -> console punto log p_Abre LISTAEXPRESIONES p_Cierra','IMPRIMIR',6,'p_IMPRIMIR_1','parser.py',200),
  ('LISTAEXPRESIONES -> LISTAEXPRESIONES coma EXPRESION','LISTAEXPRESIONES',3,'p_LISTAEXPRESIONES_1','parser.py',206),
  ('LISTAEXPRESIONES -> EXPRESION','LISTAEXPRESIONES',1,'p_LISTAEXPRESIONES_2','parser.py',214),
  ('LISTAINDICES -> LISTAINDICES c_Abre EXPRESION c_Cierra','LISTAINDICES',4,'p_LISTAEXPRESIONES_Indices','parser.py',220),
  ('LISTAINDICES -> c_Abre EXPRESION c_Cierra','LISTAINDICES',3,'p_LISTAEXPRESIONES_Indices_2','parser.py',227),
  ('EXPRESION -> EXPRESION suma EXPRESION','EXPRESION',3,'p_EXPRESION_suma','parser.py',235),
  ('EXPRESION -> EXPRESION resta EXPRESION','EXPRESION',3,'p_EXPRESION_resta','parser.py',242),
  ('EXPRESION -> EXPRESION multiplicacion EXPRESION','EXPRESION',3,'p_EXPRESION_multiplicacion','parser.py',249),
  ('EXPRESION -> EXPRESION division EXPRESION','EXPRESION',3,'p_EXPRESION_division','parser.py',256),
  ('EXPRESION -> EXPRESION potencia EXPRESION','EXPRESION',3,'p_EXPRESION_potencia','parser.py',263),
  ('EXPRESION -> EXPRESION modulo EXPRESION','EXPRESION',3,'p_EXPRESION_modulo','parser.py',270),
  ('EXPRESION -> resta EXPRESION','EXPRESION',2,'p_EXPRESION_negativo','parser.py',277),
  ('EXPRESION -> EXPRESION and EXPRESION','EXPRESION',3,'p_EXPRESION_and','parser.py',286),
  ('EXPRESION -> EXPRESION or EXPRESION','EXPRESION',3,'p_EXPRESION_or','parser.py',293),
  ('EXPRESION -> not EXPRESION','EXPRESION',2,'p_EXPRESION_not','parser.py',300),
  ('EXPRESION -> EXPRESION mayor EXPRESION','EXPRESION',3,'p_EXPRESION_mayor','parser.py',309),
  ('EXPRESION -> EXPRESION mayorigual EXPRESION','EXPRESION',3,'p_EXPRESION_mayorigual','parser.py',316),
  ('EXPRESION -> EXPRESION menor EXPRESION','EXPRESION',3,'p_EXPRESION_menor','parser.py',323),
  ('EXPRESION -> EXPRESION menorigual EXPRESION','EXPRESION',3,'p_EXPRESION_menorigual','parser.py',330),
  ('EXPRESION -> EXPRESION igualacion EXPRESION','EXPRESION',3,'p_EXPRESION_igualacion','parser.py',337),
  ('EXPRESION -> EXPRESION diferente EXPRESION','EXPRESION',3,'p_EXPRESION_diferente','parser.py',344),
  ('EXPRESION -> FUNCION_TOFIXED','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',353),
  ('EXPRESION -> FUNCION_TOEXPONENTIAL','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',354),
  ('EXPRESION -> FUNCION_TOSTRING','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',355),
  ('EXPRESION -> FUNCION_TOLOWERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',356),
  ('EXPRESION -> FUNCION_TOUPPERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',357),
  ('EXPRESION -> FUNCION_SPLIT','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',358),
  ('FUNCION_TOFIXED -> id punto toFixed p_Abre EXPRESION p_Cierra','FUNCION_TOFIXED',6,'p_FUNCION_TOFIXED','parser.py',364),
  ('FUNCION_TOEXPONENTIAL -> id punto toExponential p_Abre EXPRESION p_Cierra','FUNCION_TOEXPONENTIAL',6,'p_FUNCION_TOEXPONENTIAL','parser.py',371),
  ('FUNCION_TOSTRING -> id punto toString p_Abre p_Cierra','FUNCION_TOSTRING',5,'p_FUNCION_TOSTRING','parser.py',378),
  ('FUNCION_TOLOWERCASE -> id punto toLowerCase p_Abre p_Cierra','FUNCION_TOLOWERCASE',5,'p_FUNCION_TOLOWERCASE','parser.py',385),
  ('FUNCION_TOUPPERCASE -> id punto toUpperCase p_Abre p_Cierra','FUNCION_TOUPPERCASE',5,'p_FUNCION_TOUPPERCASE','parser.py',392),
  ('FUNCION_SPLIT -> id punto split p_Abre cadena p_Cierra','FUNCION_SPLIT',6,'p_FUNCION_SPLIT','parser.py',399),
  ('EXPRESION -> cadena','EXPRESION',1,'p_EXPRESION_cadena','parser.py',408),
  ('EXPRESION -> numero','EXPRESION',1,'p_EXPRESION_numero','parser.py',415),
  ('EXPRESION -> true','EXPRESION',1,'p_EXPRESION_booleano','parser.py',422),
  ('EXPRESION -> false','EXPRESION',1,'p_EXPRESION_booleano','parser.py',423),
  ('EXPRESION -> null','EXPRESION',1,'p_EXPRESION_null','parser.py',430),
  ('EXPRESION -> id','EXPRESION',1,'p_EXPRESION_Acceso','parser.py',437),
  ('EXPRESION -> id LISTAINDICES','EXPRESION',2,'p_EXPRESION_Acceso_Vector','parser.py',444),
  ('EXPRESION -> c_Abre LISTAEXPRESIONES c_Cierra','EXPRESION',3,'p_EXPRESION_Vector','parser.py',451),
  ('TIPO -> number','TIPO',1,'p_TIPO_NUMBER','parser.py',459),
  ('TIPO -> string','TIPO',1,'p_TIPO_STRING','parser.py',465),
  ('TIPO -> boolean','TIPO',1,'p_TIPO_BOOLEAN','parser.py',471),
  ('TIPO -> any','TIPO',1,'p_TIPO_ANY','parser.py',477),
]
