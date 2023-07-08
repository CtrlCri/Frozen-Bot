# Frozen Bot

## Descripción del proyecto
El proyecto Frozen Bot consiste en la construcción de un bot para la toma de pedidos de Heladerías Frozen SRL. Se requiere el desarrollo de funciones auxiliares que permitan al bot interactuar en la conversación con los clientes.

## Las funciones a desarrollar son las siguientes:

### 1. Función is_hot_in_pehuajo en GeoAPI
Esta función debe consultar la información del clima y devolver True si la temperatura actual en Pehuajó supera los 28 grados Celsius. Si ocurre cualquier excepción HTTP, debe devolver False.

### 2. Función is_product_available
En esta función, se busca en un DataFrame de pandas y se debe devolver True si hay stock disponible para el producto y la cantidad especificados. Se debe evitar un posible loop infinito cuando el usuario ingrese productos inválidos o sin stock.

### 3. Función validate_discount_code
El objetivo de esta función es validar un código de descuento mencionado por el cliente en comparación con una lista de códigos de descuento vigentes. Si la diferencia entre el código mencionado y los códigos vigentes es menor a tres caracteres en al menos uno de los casos, se debe devolver True.

Estas funciones son fundamentales para que el bot de pedidos pueda tomar decisiones basadas en la información del clima, la disponibilidad de productos y los códigos de descuento. El proyecto busca desarrollar estas funcionalidades y asegurar que el bot pueda interactuar de manera efectiva con los clientes.

## Documentación principal
Este proyecto, tiene la particularidad que estará resuelto en un archivo Jupyter Notebook, [ver archivo notebook.ipynb](notebook.ipynb) por lo que encontrarás fácilmente toda la documentación y el paso a paso de un solo vistazo.

## Requisitos del entorno y dependencias
Asegúrate de tener instalado Python 3.x y las siguientes dependencias:

- pandas
- requests
- pytest (para ejecutar las pruebas)

De todas maneras te lo iré recordando en el notebook a medida que lo vayamos necesitando. Y también lo tendrás disponible en el archivo [requirements.txt](requirements.txt) para instalarlo directamente desde allí.

## Ejecución de las pruebas
Para ejecutar las pruebas unitarias, asegúrate de tener instalado pytest. Luego, en la línea de comandos, desde el directorio raíz del proyecto, ejecuta el siguiente comando:

pytest

## Autor
Cristian Aramayo Reyes , Inceptia

## Agradecimientos
Al Equipo de Inceptia por darme la oportunidad de participar de este proceso.
