
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftsumarestaleftmultiplicaciondivisionmodulononassocpotenciaany cadena coma console division false id log modulo multiplicacion null numero p_Abre p_Cierra potencia punto puntoYcoma resta suma true\n    INICIO : ENTRADAS\n    \n    ENTRADAS : ENTRADAS ENTRADA\n    \n    ENTRADAS : ENTRADA\n    \n    ENTRADA : IMPRIMIR puntoYcoma\n    \n    IMPRIMIR : console punto log p_Abre LISTAEXPRESIONES p_Cierra\n    \n    LISTAEXPRESIONES :  LISTAEXPRESIONES coma EXPRESION\n    \n    LISTAEXPRESIONES : EXPRESION\n    \n    EXPRESION : cadena\n    \n    EXPRESION : numero\n    \n    EXPRESION : true\n                | false\n    \n    EXPRESION : null\n    \n    EXPRESION : any\n    '
    
_lr_action_items = {'console':([0,2,3,6,7,],[5,5,-3,-2,-4,]),'$end':([1,2,3,6,7,],[0,-1,-3,-2,-4,]),'puntoYcoma':([4,19,],[7,-5,]),'punto':([5,],[8,]),'log':([8,],[9,]),'p_Abre':([9,],[10,]),'cadena':([10,20,],[13,13,]),'numero':([10,20,],[14,14,]),'true':([10,20,],[15,15,]),'false':([10,20,],[16,16,]),'null':([10,20,],[17,17,]),'any':([10,20,],[18,18,]),'p_Cierra':([11,12,13,14,15,16,17,18,21,],[19,-7,-8,-9,-10,-11,-12,-13,-6,]),'coma':([11,12,13,14,15,16,17,18,21,],[20,-7,-8,-9,-10,-11,-12,-13,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INICIO':([0,],[1,]),'ENTRADAS':([0,],[2,]),'ENTRADA':([0,2,],[3,6,]),'IMPRIMIR':([0,2,],[4,4,]),'LISTAEXPRESIONES':([10,],[11,]),'EXPRESION':([10,20,],[12,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INICIO","S'",1,None,None,None),
  ('INICIO -> ENTRADAS','INICIO',1,'p_INICIO','parser.py',29),
  ('ENTRADAS -> ENTRADAS ENTRADA','ENTRADAS',2,'p_ENTRADAS_PARTE_1','parser.py',35),
  ('ENTRADAS -> ENTRADA','ENTRADAS',1,'p_ENTRADAS_PARTE_2','parser.py',42),
  ('ENTRADA -> IMPRIMIR puntoYcoma','ENTRADA',2,'p_ENTRADA','parser.py',48),
  ('IMPRIMIR -> console punto log p_Abre LISTAEXPRESIONES p_Cierra','IMPRIMIR',6,'p_IMPRIMIR_1','parser.py',55),
  ('LISTAEXPRESIONES -> LISTAEXPRESIONES coma EXPRESION','LISTAEXPRESIONES',3,'p_LISTAEXPRESIONES_1','parser.py',61),
  ('LISTAEXPRESIONES -> EXPRESION','LISTAEXPRESIONES',1,'p_LISTAEXPRESIONES_2','parser.py',69),
  ('EXPRESION -> cadena','EXPRESION',1,'p_EXPRESION_cadena','parser.py',76),
  ('EXPRESION -> numero','EXPRESION',1,'p_EXPRESION_numero','parser.py',83),
  ('EXPRESION -> true','EXPRESION',1,'p_EXPRESION_booleano','parser.py',90),
  ('EXPRESION -> false','EXPRESION',1,'p_EXPRESION_booleano','parser.py',91),
  ('EXPRESION -> null','EXPRESION',1,'p_EXPRESION_null','parser.py',98),
  ('EXPRESION -> any','EXPRESION',1,'p_EXPRESION_any','parser.py',105),
]
