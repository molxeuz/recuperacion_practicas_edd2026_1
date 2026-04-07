# TALLER DE LISTAS ENLAZADAS

## Condiciones Generales

Si se presentan los 4 puntos, se sumará 0.75 a la práctica 2, siempre y cuando:

- Se utilicen las clases base trabajadas en clase.
- Se encuentren completos con pruebas que cubran al menos 2 escenarios diferentes.
- Se sustenten correctamente los puntos escogidos por el profesor.
- La sustentación es presencial y en la fecha acordada.
- No se permiten comentarios en el código.

---

## Punto 1: Gestor de trenes y vagones

Implementar un sistema que simule la gestión de un tren con múltiples vagones.

Debe permitir:

- Iniciar el tren con un único vagón.
- Moverse al vagón siguiente o anterior.
  - Si no existe, permanecer en el actual.
- Acoplar un nuevo vagón detrás del actual.
- Desacoplar el vagón actual:
  - Mover el puntero al siguiente si existe.
  - Si no, mover al anterior.
  - Manejar el caso en que el tren quede vacío.
- Mover un vagón al inicio o al final del tren.

El orden de los vagones debe mantenerse válido después de cada operación.

---

## Punto 2: Fusionar segmentos entre ceros

Dada una lista enlazada:

- Contiene números separados por nodos con valor 0.
- El primer y último nodo siempre son 0.

Objetivo:

- Por cada par de ceros consecutivos:
  - Sumar los valores entre ellos.
  - Reemplazarlos por un solo nodo.
- La lista final no debe contener ceros.

Restricción:

- La solución debe ser in-place.
- No se permite usar estructuras auxiliares.

---

## Punto 3: Eliminar duplicados (última aparición)

Dada una lista doblemente enlazada con valores repetidos:

- Eliminar todos los nodos duplicados.
- Mantener solo la última aparición de cada valor.

Restricción:

- No usar estructuras auxiliares (listas, conjuntos, pilas, etc.).

---

## Punto 4: Rotar lista hasta máximo al frente

Dada una lista doblemente enlazada con valores enteros:

- Rotar la lista hacia la derecha (mover nodos del final al inicio).
- Repetir hasta que el nodo con el valor máximo quede en la cabeza.

Restricciones:

- Modificar la lista in-place.
- No usar estructuras auxiliares.
- No usar métodos de la clase base como:
  append, prepend, insert, delete, rotate, swap_nodes, etc.
