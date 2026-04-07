# TALLER 1 - RECURSIVIDAD

## Condiciones Generales

Si se presentan los 4 puntos, se sumará 0.75 a la práctica de recursividad, siempre y cuando:

- Se encuentren completos con pruebas que cubran al menos 2 escenarios diferentes.
- Se sustenten correctamente los puntos aleatorios escogidos por el profesor.
  - En caso contrario, se calificará proporcionalmente (puntos presentados vs sustentados completamente).
  - No se tendrán en cuenta sustentaciones parciales.
- La sustentación es presencial y únicamente en la fecha acordada.
- No se permiten comentarios en el código. Los puntos con comentarios tendrán calificación de 0.
- Todos los puntos deben resolverse con recursividad.
  - No se permite el uso de for ni while.

---

## Punto 1: Suma de diagonales impares

Cree una función recursiva que calcule la suma de todos los números impares contenidos en las dos diagonales de una matriz cuadrada n x n:

- Diagonal principal: de izquierda a derecha
- Diagonal secundaria: de derecha a izquierda

Ejemplo para una matriz 3x3:

- Diagonal principal: [0][0] -> [1][1] -> [2][2]
- Diagonal secundaria: [0][2] -> [1][1] -> [2][0]

Ejemplo para una matriz 4x4:

- Diagonal principal: [0][0] -> [1][1] -> [2][2] -> [3][3]
- Diagonal secundaria: [0][3] -> [1][2] -> [2][1] -> [3][0]

---

## Punto 2: Superdígito

Dado un número entero positivo, encontrar su superdígito:

- Si el número tiene un solo dígito, ese es el resultado.
- Si tiene más de un dígito, se suman sus dígitos y se repite el proceso.

Ejemplo:

super_digito(9875) -> 9 + 8 + 7 + 5 = 29  
super_digito(29) -> 2 + 9 = 11  
super_digito(11) -> 1 + 1 = 2  
super_digito(2) -> 2  

Resultado: 2

---

## Punto 3: Juego de extremos

Dos jugadores juegan con una lista de números enteros positivos.

- En cada turno pueden tomar el primer o el último elemento.
- Siempre eligen el mayor valor disponible entre los extremos.
- Se turnan comenzando por el Jugador 1.
- El número elegido se suma a su puntaje.
- El juego termina cuando no quedan números.

Requisitos:

- Implementar usando recursividad.
- Retornar una lista con el puntaje del Jugador 1 y Jugador 2.

Ejemplo:

Input: [4, 1, 7, 3]

Turnos:
Jugador 1 -> elige 4  
Jugador 2 -> elige 3  
Jugador 1 -> elige 7  
Jugador 2 -> elige 1  

Output: [11, 4]

---

## Punto 4: Decodificación de cadena

Dada una cadena codificada de la forma:

"k1[texto1]k2[texto2]..."

Cada k indica cuántas veces se repite el texto entre corchetes.

Restricciones:

- No hay anidamiento.
- La cadena es válida.
- Solo hay letras minúsculas.
- Solo se permite usar:
  - find
  - isdigit
  - slicing
  - concatenación
- No se permite usar ciclos ni expresiones regulares.

Ejemplos:

"3[a]2[bc]" -> "aaabcbc"  
"4[ab]" -> "abababab"  
"2[x]3[yz]" -> "xxyzyzyz"

---
