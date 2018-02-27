# cfdi33.md

Scrip encargado de obtener la información de un cfdi v3.3 a partir del archivo xml

## La sintaxis propuestas es la siguiente:
```
$ python cfdi33.py <nombre del archivo xml del cfdi 3.3>
... se imprime la lista de atributos del nodo raíz del cfdi 3.3
```
Falta actualizar la lista de atributos en base al documento técnico del anexo 20 emitido por el SAT

Para la primera versión beta sólo se imprimirán los atributos del nodo raíz, ya más adelante se obtendrá
e imprimirá la información de cada uno de los nodos contenidos en un cfd v3.3.

## Estructura del script cfdi33.py

Revisar el contenido del archivo [cfdi33.py](cfdi33.py) para ver la estructura
