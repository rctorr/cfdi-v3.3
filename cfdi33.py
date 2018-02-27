#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Área de imports

# Área de funciones
def leexml(nombreArchivo):
  """
  Lee el contenido del archivo definido por nombreArchivo y regresa todos los atributos encontrados en
  un diccionario.
  
  Valores de regreso:
  
  {nomAtributo:valor, nomAtributo:valor, ... }
      Si el archivo existe, lee cada uno de los atributos del nodo raíz y se regresan en forma de tuplas
      nomAtributo:valor contenidas en un diccionario.
  Se regresa un diccionario con el código de erro y el mensaje correspondiente según el error sucedido.
      - {noerr:1, err:"El archivo no existe"}
      - {noerr:2, err:"El archivo no corresponde a un xml"}
      - {noerr:3, err:"El archivo no corresponde a un cfd v3.3"}
  """
  pass

# Función principal
def main():
    """
    Esta función se ejecuta sólo cuando el script se ejecuta por separado y puede imprimir la lista de atributos
    por ejemplo.
    """
    pass

if __name__ == "__main__":
    main()
