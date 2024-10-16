# Píldora de Machine Learning Supervisado: Algoritmos Clásicos

## Objetivo de Aprendizaje

El objetivo de este proyecto es proporcionarte una introducción práctica al machine learning supervisado, explorando algunos de los algoritmos clásicos más utilizados. A través de ejemplos y ejercicios, practicarás la implementación y evaluación de modelos de machine learning supervisado.

## Tu formación como cadete en la Academia de la Flota Estelar 🚀✨

![71RtguTEIvL _AC_UF894,1000_QL80_](https://github.com/user-attachments/assets/fa1fca32-7977-4e68-8557-2fef9116954b)

Para hacer este proyecto más atractivo y pedagógico, he utilizado el universo de Star Trek como contexto; una de las franquicias de ciencia ficción más icónicas, ofrece un rico escenario lleno de datos y situaciones que son ideales para aplicar técnicas de machine learning supervisado. A través de ejemplos basados en personajes, naves espaciales y misiones de Star Trek, puedes aprender conceptos complejos de una manera divertida y relevante.

## Contexto del Bootcamp

Este proyecto forma parte de la tercera promoción del bootcamp en Inteligencia Artificial impartido por Factoría F5, una organización dedicada a la formación en tecnologías emergentes, con un enfoque en la inclusión y la diversidad. El bootcamp en IA está diseñado para proporcionar a los estudiantes las habilidades necesarias para desarrollar soluciones de inteligencia artificial en el mundo real.

## Instrucciones para Crear un Entorno Virtual

Para crear un entorno virtual en tu entorno de desarrollo, sigue estos pasos:

1. Abre una terminal y navega al directorio del proyecto.
2. Ejecuta el siguiente comando para crear un entorno virtual:
    ```bash
    python -m venv env
    ```
3. Activa el entorno virtual:
    - En Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source env/bin/activate
        ```

## Instalación de Librerías Necesarias

Una vez que el entorno virtual esté activado, instala las librerías necesarias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

El proceso de instalación de librerías con `pip` es consistente en los sistemas operativos Linux y macOS.

Para visualizar el árbol de decisiones, asegúrate de tener instaladas las bibliotecas **graphviz** (un programa externo necesario para renderizar los gráficos generados) y **pydotplus**. 
Puedes instalarlas utilizando los siguientes comandos:
```bash
pip install graphviz
pip install pydotplus
```

Además, asegúrate de tener Graphviz instalado en tu sistema. Puedes descargarlo e instalarlo desde [Graphviz Download](https://graphviz.gitlab.io/download/).

En macOS introduce el siguiente código para instalarlo vía HomeBrew:
```bash
brew install graphviz
```
Una vez que tengas todo instalado, ejecuta el código para visualizar el árbol de decisiones.


## Descripción de los Archivos del Proyecto

### complex_starship_dataset_generator.py

Contiene el código necesario para generar un conjunto de datos complejo sobre naves espaciales. El objetivo de este script es simular datos detallados sobre diferentes tipos de naves y sus características técnicas.

### alien_plants_dataset_generator.py

Se encarga de generar un conjunto de datos sobre plantas alienígenas. El script simula datos sobre diversas especies de plantas encontradas en un mismo planeta, incluyendo características como la altura, el color, y las propiedades medicinales.

### galactic_battles_dataset_generator.py

Genera un conjunto de datos sobre batallas galácticas. El objetivo de este script es crear datos que describan diferentes enfrentamientos espaciales, incluyendo información sobre las flotas involucradas y los resultados de las batallas.

## Agradecimientos 🖖🏻

Gracias por visitar este repositorio. Apreciaré cualquier contribución que desees hacer a través de forks en GitHub. ¡Tu participación es valiosa para mí!

¡Larga vida y prosperidad! Que tu aprendizaje en el mundo del machine learning sea tan emocionante y fructífero como las misiones de la Flota Estelar.
