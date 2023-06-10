
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftorleftandleftsumarestanonassocmenormayormenorigualmayorigualigualaciondiferenteleftmultiplicaciondivisionmoduloleftpotenciarightnotlefturestaand any boolean break c_Abre c_Cierra cadena coma concat console continue decremento diferente division dosPuntos else false for id if igual igualacion incremento let llave_Abre llave_Cierra log mayor mayorigual menor menorigual modulo multiplicacion not null number numero or p_Abre p_Cierra potencia punto puntoYcoma resta split string suma toExponential toFixed toLowerCase toString toUpperCase true while\n    INICIO : ENTRADAS\n    \n    ENTRADAS : ENTRADAS ENTRADA\n    \n    ENTRADAS : ENTRADA\n    \n    ENTRADA : IMPRIMIR puntoYcoma\n            |   IF puntoYcoma\n            |   WHILE puntoYcoma\n            |   BREAK\n            |   CONTINUE\n            |   FOR puntoYcoma\n    \n    FOR : for p_Abre DECLARACION puntoYcoma EXPRESION puntoYcoma ASIGNACION p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    BREAK : break puntoYcoma\n    \n    CONTINUE : continue puntoYcoma\n    \n    WHILE : while p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra\n    \n    IF : if p_Abre EXPRESION p_Cierra llave_Abre ENTRADAS llave_Cierra COMPLEMENTO_IF\n    \n    COMPLEMENTO_IF : else IF\n                    | else llave_Abre ENTRADAS llave_Cierra\n                    | \n    \n    ENTRADA : DECLARACION puntoYcoma\n    \n    DECLARACION : let id igual EXPRESION\n    \n    DECLARACION : let id dosPuntos TIPO igual EXPRESION\n    \n    DECLARACION : let id \n    \n    DECLARACION : let id dosPuntos TIPO\n    \n    ENTRADA : ASIGNACION puntoYcoma\n    \n    ASIGNACION : id igual EXPRESION\n    \n    ASIGNACION : id LISTAINDICES igual EXPRESION\n    \n    ASIGNACION : id incremento\n                | id incremento puntoYcoma\n    \n    ASIGNACION : id decremento\n                | id decremento puntoYcoma\n    \n    IMPRIMIR : console punto log p_Abre LISTAEXPRESIONES p_Cierra\n    \n    LISTAEXPRESIONES :  LISTAEXPRESIONES coma EXPRESION\n    \n    LISTAEXPRESIONES : EXPRESION\n    \n    LISTAINDICES :  LISTAINDICES c_Abre EXPRESION c_Cierra\n    \n    LISTAINDICES : c_Abre EXPRESION c_Cierra\n    \n    EXPRESION : EXPRESION suma EXPRESION\n    \n    EXPRESION : EXPRESION resta EXPRESION\n    \n    EXPRESION : EXPRESION multiplicacion EXPRESION\n    \n    EXPRESION : EXPRESION division EXPRESION\n    \n    EXPRESION : EXPRESION potencia EXPRESION\n    \n    EXPRESION : EXPRESION modulo EXPRESION\n    \n    EXPRESION : resta EXPRESION %prec uresta\n    \n    EXPRESION : EXPRESION and EXPRESION\n    \n    EXPRESION : EXPRESION or EXPRESION\n    \n    EXPRESION : not EXPRESION\n    \n    EXPRESION : EXPRESION mayor EXPRESION\n    \n    EXPRESION : EXPRESION mayorigual EXPRESION\n    \n    EXPRESION : EXPRESION menor EXPRESION\n    \n    EXPRESION : EXPRESION menorigual EXPRESION\n    \n    EXPRESION : EXPRESION igualacion EXPRESION\n    \n    EXPRESION : EXPRESION diferente EXPRESION\n    \n    EXPRESION : FUNCION_TOFIXED\n            | FUNCION_TOEXPONENTIAL\n            | FUNCION_TOSTRING\n            | FUNCION_TOLOWERCASE\n            | FUNCION_TOUPPERCASE\n            | FUNCION_SPLIT\n    \n    FUNCION_TOFIXED : id punto toFixed p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOEXPONENTIAL : id punto toExponential p_Abre EXPRESION p_Cierra\n    \n    FUNCION_TOSTRING : id punto toString p_Abre p_Cierra\n    \n    FUNCION_TOLOWERCASE : id punto toLowerCase p_Abre p_Cierra\n    \n    FUNCION_TOUPPERCASE : id punto toUpperCase p_Abre p_Cierra\n    \n    FUNCION_SPLIT : id punto split p_Abre cadena p_Cierra\n    \n    EXPRESION : cadena\n    \n    EXPRESION : numero\n    \n    EXPRESION : true\n                | false\n    \n    EXPRESION : null\n    \n    EXPRESION : id\n    \n    EXPRESION : id LISTAINDICES\n    \n    EXPRESION : c_Abre LISTAEXPRESIONES c_Cierra\n    \n    TIPO : number\n    \n    TIPO : string\n    \n    TIPO : boolean\n    \n    TIPO : any\n    '
    
_lr_action_items = {'console':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,100,123,128,136,155,156,157,158,],[12,12,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,12,12,12,12,12,12,12,12,]),'if':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,100,123,128,136,149,155,156,157,158,],[13,13,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,13,13,13,13,13,13,13,13,13,]),'while':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,100,123,128,136,155,156,157,158,],[14,14,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,14,14,14,14,14,14,14,14,]),'break':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,100,123,128,136,155,156,157,158,],[15,15,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,15,15,15,15,15,15,15,15,]),'continue':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,100,123,128,136,155,156,157,158,],[16,16,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,16,16,16,16,16,16,16,16,]),'for':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,100,123,128,136,155,156,157,158,],[17,17,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,17,17,17,17,17,17,17,17,]),'let':([0,2,3,7,8,20,21,22,23,24,25,26,30,31,32,100,123,128,136,155,156,157,158,],[18,18,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,18,18,18,18,18,18,18,18,18,]),'id':([0,2,3,7,8,18,20,21,22,23,24,25,26,28,29,30,31,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,100,122,123,125,128,129,130,136,137,155,156,157,158,],[19,19,-3,-7,-8,33,-2,-4,-5,-6,-9,-18,-23,54,54,-11,-12,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,19,54,19,54,19,54,54,19,19,19,19,19,19,]),'$end':([1,2,3,7,8,20,21,22,23,24,25,26,30,31,],[0,-1,-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,]),'llave_Cierra':([3,7,8,20,21,22,23,24,25,26,30,31,128,136,157,158,],[-3,-7,-8,-2,-4,-5,-6,-9,-18,-23,-11,-12,139,146,159,160,]),'puntoYcoma':([4,5,6,9,10,11,15,16,33,36,37,43,44,45,46,47,48,49,50,51,52,53,54,57,60,63,64,82,83,84,90,91,92,93,94,95,96,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,127,138,139,142,143,144,146,148,150,151,152,154,159,160,],[21,22,23,24,25,26,30,31,-21,63,64,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,89,-24,-27,-29,-41,-44,-69,-19,-22,-71,-72,-73,-74,-25,-34,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-47,-48,-49,-50,-70,137,-33,-30,-20,-17,-59,-60,-61,-13,-14,-57,-58,-62,-15,-16,-10,]),'punto':([12,54,],[27,85,]),'p_Abre':([13,14,17,39,115,116,117,118,119,120,],[28,29,32,66,129,130,131,132,133,134,]),'igual':([19,33,35,91,92,93,94,95,98,126,],[34,58,61,125,-71,-72,-73,-74,-34,-33,]),'incremento':([19,],[36,]),'decremento':([19,],[37,]),'c_Abre':([19,28,29,34,35,38,41,42,54,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,84,89,98,122,125,126,129,130,],[38,55,55,55,62,55,55,55,38,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,62,55,-34,55,55,-33,55,55,]),'log':([27,],[39,]),'resta':([28,29,34,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,89,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,122,124,125,126,129,130,135,138,140,141,142,143,144,150,151,152,],[41,41,41,41,69,41,41,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,41,69,41,69,41,41,69,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-41,-44,-69,69,41,69,69,69,-34,-35,-36,-37,-38,-39,-40,69,69,-45,-46,-47,-48,-49,-50,-70,41,69,41,-33,41,41,69,69,69,69,-59,-60,-61,-57,-58,-62,]),'not':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'cadena':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,134,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,145,]),'numero':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'true':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'false':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'null':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'dosPuntos':([33,],[59,]),'p_Cierra':([36,37,40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,63,64,82,83,84,87,96,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,126,131,132,133,135,140,141,142,143,144,145,147,150,151,152,],[-26,-28,67,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,88,-24,-27,-29,-41,-44,-69,-32,-25,-34,127,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-47,-48,-49,-50,-70,-33,142,143,144,-31,150,151,-59,-60,-61,152,153,-57,-58,-62,]),'suma':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[68,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,68,68,68,-41,-44,-69,68,68,68,68,-34,-35,-36,-37,-38,-39,-40,68,68,-45,-46,-47,-48,-49,-50,-70,68,-33,68,68,68,68,-59,-60,-61,-57,-58,-62,]),'multiplicacion':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[70,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,70,70,70,-41,-44,-69,70,70,70,70,-34,70,70,-37,-38,-39,-40,70,70,70,70,70,70,70,70,-70,70,-33,70,70,70,70,-59,-60,-61,-57,-58,-62,]),'division':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[71,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,71,71,71,-41,-44,-69,71,71,71,71,-34,71,71,-37,-38,-39,-40,71,71,71,71,71,71,71,71,-70,71,-33,71,71,71,71,-59,-60,-61,-57,-58,-62,]),'potencia':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[72,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,72,72,72,-41,-44,-69,72,72,72,72,-34,72,72,72,72,-39,72,72,72,72,72,72,72,72,72,-70,72,-33,72,72,72,72,-59,-60,-61,-57,-58,-62,]),'modulo':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[73,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,73,73,73,-41,-44,-69,73,73,73,73,-34,73,73,-37,-38,-39,-40,73,73,73,73,73,73,73,73,-70,73,-33,73,73,73,73,-59,-60,-61,-57,-58,-62,]),'and':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[74,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,74,74,74,-41,-44,-69,74,74,74,74,-34,-35,-36,-37,-38,-39,-40,-42,74,-45,-46,-47,-48,-49,-50,-70,74,-33,74,74,74,74,-59,-60,-61,-57,-58,-62,]),'or':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[75,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,75,75,75,-41,-44,-69,75,75,75,75,-34,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-47,-48,-49,-50,-70,75,-33,75,75,75,75,-59,-60,-61,-57,-58,-62,]),'mayor':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[76,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,76,76,76,-41,-44,-69,76,76,76,76,-34,76,76,-37,-38,-39,-40,76,76,None,None,None,None,None,None,-70,76,-33,76,76,76,76,-59,-60,-61,-57,-58,-62,]),'mayorigual':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[77,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,77,77,77,-41,-44,-69,77,77,77,77,-34,77,77,-37,-38,-39,-40,77,77,None,None,None,None,None,None,-70,77,-33,77,77,77,77,-59,-60,-61,-57,-58,-62,]),'menor':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[78,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,78,78,78,-41,-44,-69,78,78,78,78,-34,78,78,-37,-38,-39,-40,78,78,None,None,None,None,None,None,-70,78,-33,78,78,78,78,-59,-60,-61,-57,-58,-62,]),'menorigual':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[79,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,79,79,79,-41,-44,-69,79,79,79,79,-34,79,79,-37,-38,-39,-40,79,79,None,None,None,None,None,None,-70,79,-33,79,79,79,79,-59,-60,-61,-57,-58,-62,]),'igualacion':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[80,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,80,80,80,-41,-44,-69,80,80,80,80,-34,80,80,-37,-38,-39,-40,80,80,None,None,None,None,None,None,-70,80,-33,80,80,80,80,-59,-60,-61,-57,-58,-62,]),'diferente':([40,43,44,45,46,47,48,49,50,51,52,53,54,56,60,65,82,83,84,87,90,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,124,126,135,138,140,141,142,143,144,150,151,152,],[81,-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,81,81,81,-41,-44,-69,81,81,81,81,-34,81,81,-37,-38,-39,-40,81,81,None,None,None,None,None,None,-70,81,-33,81,81,81,81,-59,-60,-61,-57,-58,-62,]),'c_Cierra':([43,44,45,46,47,48,49,50,51,52,53,54,65,82,83,84,86,87,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,126,135,142,143,144,150,151,152,],[-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,98,-41,-44,-69,121,-32,126,-34,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-47,-48,-49,-50,-70,-33,-31,-59,-60,-61,-57,-58,-62,]),'coma':([43,44,45,46,47,48,49,50,51,52,53,54,82,83,84,86,87,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,121,126,135,142,143,144,150,151,152,],[-51,-52,-53,-54,-55,-56,-63,-64,-65,-66,-67,-68,-41,-44,-69,122,-32,-34,122,-35,-36,-37,-38,-39,-40,-42,-43,-45,-46,-47,-48,-49,-50,-70,-33,-31,-59,-60,-61,-57,-58,-62,]),'number':([59,],[92,]),'string':([59,],[93,]),'boolean':([59,],[94,]),'any':([59,],[95,]),'llave_Abre':([67,88,149,153,],[100,123,155,156,]),'toFixed':([85,],[115,]),'toExponential':([85,],[116,]),'toString':([85,],[117,]),'toLowerCase':([85,],[118,]),'toUpperCase':([85,],[119,]),'split':([85,],[120,]),'else':([139,],[149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INICIO':([0,],[1,]),'ENTRADAS':([0,100,123,155,156,],[2,128,136,157,158,]),'ENTRADA':([0,2,100,123,128,136,155,156,157,158,],[3,20,3,3,20,20,3,3,20,20,]),'IMPRIMIR':([0,2,100,123,128,136,155,156,157,158,],[4,4,4,4,4,4,4,4,4,4,]),'IF':([0,2,100,123,128,136,149,155,156,157,158,],[5,5,5,5,5,5,154,5,5,5,5,]),'WHILE':([0,2,100,123,128,136,155,156,157,158,],[6,6,6,6,6,6,6,6,6,6,]),'BREAK':([0,2,100,123,128,136,155,156,157,158,],[7,7,7,7,7,7,7,7,7,7,]),'CONTINUE':([0,2,100,123,128,136,155,156,157,158,],[8,8,8,8,8,8,8,8,8,8,]),'FOR':([0,2,100,123,128,136,155,156,157,158,],[9,9,9,9,9,9,9,9,9,9,]),'DECLARACION':([0,2,32,100,123,128,136,155,156,157,158,],[10,10,57,10,10,10,10,10,10,10,10,]),'ASIGNACION':([0,2,100,123,128,136,137,155,156,157,158,],[11,11,11,11,11,11,147,11,11,11,11,]),'LISTAINDICES':([19,54,],[35,84,]),'EXPRESION':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[40,56,60,65,82,83,87,90,96,97,87,101,102,103,104,105,106,107,108,109,110,111,112,113,114,124,135,138,140,141,]),'FUNCION_TOFIXED':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'FUNCION_TOEXPONENTIAL':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'FUNCION_TOSTRING':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'FUNCION_TOLOWERCASE':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FUNCION_TOUPPERCASE':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'FUNCION_SPLIT':([28,29,34,38,41,42,55,58,61,62,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,89,122,125,129,130,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'LISTAEXPRESIONES':([55,66,],[86,99,]),'TIPO':([59,],[91,]),'COMPLEMENTO_IF':([139,],[148,]),}

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
  ('ASIGNACION -> id incremento','ASIGNACION',2,'p_ASIGNACION_INC','parser.py',199),
  ('ASIGNACION -> id incremento puntoYcoma','ASIGNACION',3,'p_ASIGNACION_INC','parser.py',200),
  ('ASIGNACION -> id decremento','ASIGNACION',2,'p_ASIGNACION_DEC','parser.py',206),
  ('ASIGNACION -> id decremento puntoYcoma','ASIGNACION',3,'p_ASIGNACION_DEC','parser.py',207),
  ('IMPRIMIR -> console punto log p_Abre LISTAEXPRESIONES p_Cierra','IMPRIMIR',6,'p_IMPRIMIR_1','parser.py',214),
  ('LISTAEXPRESIONES -> LISTAEXPRESIONES coma EXPRESION','LISTAEXPRESIONES',3,'p_LISTAEXPRESIONES_1','parser.py',220),
  ('LISTAEXPRESIONES -> EXPRESION','LISTAEXPRESIONES',1,'p_LISTAEXPRESIONES_2','parser.py',228),
  ('LISTAINDICES -> LISTAINDICES c_Abre EXPRESION c_Cierra','LISTAINDICES',4,'p_LISTAEXPRESIONES_Indices','parser.py',234),
  ('LISTAINDICES -> c_Abre EXPRESION c_Cierra','LISTAINDICES',3,'p_LISTAEXPRESIONES_Indices_2','parser.py',241),
  ('EXPRESION -> EXPRESION suma EXPRESION','EXPRESION',3,'p_EXPRESION_suma','parser.py',249),
  ('EXPRESION -> EXPRESION resta EXPRESION','EXPRESION',3,'p_EXPRESION_resta','parser.py',256),
  ('EXPRESION -> EXPRESION multiplicacion EXPRESION','EXPRESION',3,'p_EXPRESION_multiplicacion','parser.py',263),
  ('EXPRESION -> EXPRESION division EXPRESION','EXPRESION',3,'p_EXPRESION_division','parser.py',270),
  ('EXPRESION -> EXPRESION potencia EXPRESION','EXPRESION',3,'p_EXPRESION_potencia','parser.py',277),
  ('EXPRESION -> EXPRESION modulo EXPRESION','EXPRESION',3,'p_EXPRESION_modulo','parser.py',284),
  ('EXPRESION -> resta EXPRESION','EXPRESION',2,'p_EXPRESION_negativo','parser.py',291),
  ('EXPRESION -> EXPRESION and EXPRESION','EXPRESION',3,'p_EXPRESION_and','parser.py',300),
  ('EXPRESION -> EXPRESION or EXPRESION','EXPRESION',3,'p_EXPRESION_or','parser.py',307),
  ('EXPRESION -> not EXPRESION','EXPRESION',2,'p_EXPRESION_not','parser.py',314),
  ('EXPRESION -> EXPRESION mayor EXPRESION','EXPRESION',3,'p_EXPRESION_mayor','parser.py',323),
  ('EXPRESION -> EXPRESION mayorigual EXPRESION','EXPRESION',3,'p_EXPRESION_mayorigual','parser.py',330),
  ('EXPRESION -> EXPRESION menor EXPRESION','EXPRESION',3,'p_EXPRESION_menor','parser.py',337),
  ('EXPRESION -> EXPRESION menorigual EXPRESION','EXPRESION',3,'p_EXPRESION_menorigual','parser.py',344),
  ('EXPRESION -> EXPRESION igualacion EXPRESION','EXPRESION',3,'p_EXPRESION_igualacion','parser.py',351),
  ('EXPRESION -> EXPRESION diferente EXPRESION','EXPRESION',3,'p_EXPRESION_diferente','parser.py',358),
  ('EXPRESION -> FUNCION_TOFIXED','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',367),
  ('EXPRESION -> FUNCION_TOEXPONENTIAL','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',368),
  ('EXPRESION -> FUNCION_TOSTRING','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',369),
  ('EXPRESION -> FUNCION_TOLOWERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',370),
  ('EXPRESION -> FUNCION_TOUPPERCASE','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',371),
  ('EXPRESION -> FUNCION_SPLIT','EXPRESION',1,'p_EXPRESION_funcionesnativas','parser.py',372),
  ('FUNCION_TOFIXED -> id punto toFixed p_Abre EXPRESION p_Cierra','FUNCION_TOFIXED',6,'p_FUNCION_TOFIXED','parser.py',378),
  ('FUNCION_TOEXPONENTIAL -> id punto toExponential p_Abre EXPRESION p_Cierra','FUNCION_TOEXPONENTIAL',6,'p_FUNCION_TOEXPONENTIAL','parser.py',385),
  ('FUNCION_TOSTRING -> id punto toString p_Abre p_Cierra','FUNCION_TOSTRING',5,'p_FUNCION_TOSTRING','parser.py',392),
  ('FUNCION_TOLOWERCASE -> id punto toLowerCase p_Abre p_Cierra','FUNCION_TOLOWERCASE',5,'p_FUNCION_TOLOWERCASE','parser.py',399),
  ('FUNCION_TOUPPERCASE -> id punto toUpperCase p_Abre p_Cierra','FUNCION_TOUPPERCASE',5,'p_FUNCION_TOUPPERCASE','parser.py',406),
  ('FUNCION_SPLIT -> id punto split p_Abre cadena p_Cierra','FUNCION_SPLIT',6,'p_FUNCION_SPLIT','parser.py',413),
  ('EXPRESION -> cadena','EXPRESION',1,'p_EXPRESION_cadena','parser.py',422),
  ('EXPRESION -> numero','EXPRESION',1,'p_EXPRESION_numero','parser.py',429),
  ('EXPRESION -> true','EXPRESION',1,'p_EXPRESION_booleano','parser.py',436),
  ('EXPRESION -> false','EXPRESION',1,'p_EXPRESION_booleano','parser.py',437),
  ('EXPRESION -> null','EXPRESION',1,'p_EXPRESION_null','parser.py',444),
  ('EXPRESION -> id','EXPRESION',1,'p_EXPRESION_Acceso','parser.py',451),
  ('EXPRESION -> id LISTAINDICES','EXPRESION',2,'p_EXPRESION_Acceso_Vector','parser.py',458),
  ('EXPRESION -> c_Abre LISTAEXPRESIONES c_Cierra','EXPRESION',3,'p_EXPRESION_Vector','parser.py',465),
  ('TIPO -> number','TIPO',1,'p_TIPO_NUMBER','parser.py',473),
  ('TIPO -> string','TIPO',1,'p_TIPO_STRING','parser.py',479),
  ('TIPO -> boolean','TIPO',1,'p_TIPO_BOOLEAN','parser.py',485),
  ('TIPO -> any','TIPO',1,'p_TIPO_ANY','parser.py',491),
]
