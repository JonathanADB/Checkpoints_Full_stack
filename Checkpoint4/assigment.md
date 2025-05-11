## 1. ¿Cuál es la diferencia entre una lista y una tupla en Python?

### Listas
- **Mutabilidad**: Las listas son mutables, lo que significa que puedes modificar sus elementos después de haberlas creado.
- **Sintaxis**: Se definen utilizando corchetes `[]`.

**Ejemplo**:
```python
mi_lista = [1, 2, 3]
mi_lista[0] = 100  # Modificando el primer elemento
print(mi_lista)  # Salida: [100, 2, 3]
```

### Tuplas
- **Inmutabilidad**: Las tuplas son inmutables, no puedes cambiar sus elementos una vez creadas.
- **Sintaxis**: Se definen utilizando paréntesis `()`.

**Ejemplo**:
```python
mi_tupla = (1, 2, 3)
# mi_tupla[0] = 100  # Esto causará un error
nueva_tupla = mi_tupla + (4,)  # Crear una nueva tupla
print(nueva_tupla)  # Salida: (1, 2, 3, 4)
```

### Buenas Prácticas
- Usa listas cuando necesites una colección de elementos que pueda cambiar.
- Usa tuplas para datos que no deberían cambiar, como coordenadas o registros fijos.

---

## 2. ¿Cuál es el orden de las operaciones?

El orden de las operaciones en Python sigue la regla de PEMDAS:
- **P**aréntesis
- **E**xponentes
- **M**ultiplicación y **D**ivisión (de izquierda a derecha)
- **A**dición y **S**ustracción (de izquierda a derecha)

**Ejemplo**:
```python
resultado = 3 + 5 * 2 ** 2  # Primero se evalúan los exponentes, luego la multiplicación y finalmente la suma
print(resultado)  # Salida: 3 + 20 = 23
```

### Buenas Prácticas
- Usa paréntesis para aclarar la intención, especialmente en expresiones complejas.

---

## 3. ¿Qué es un diccionario en Python?

Un diccionario es una colección desordenada de pares clave-valor. Se define usando llaves `{}`.

**Ejemplo**:
```python
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print(mi_diccionario["nombre"])  # Salida: Juan
```

### Buenas Prácticas
- Usa diccionarios cuando necesites asociar valores con claves únicas.

---

## 4. ¿Cuál es la diferencia entre el método `sort()` y la función `sorted()`?

### `sort()`
- Modifica la lista original en su lugar.
- Solo se puede usar con listas.

**Ejemplo**:
```python
mi_lista = [3, 1, 2]
mi_lista.sort()  # Ordena la lista original
print(mi_lista)  # Salida: [1, 2, 3]
```

### `sorted()`
- Devuelve una nueva lista ordenada.
- Puede usarse con cualquier iterable (listas, tuplas, etc.).

**Ejemplo**:
```python
mi_tupla = (3, 1, 2)
nueva_lista = sorted(mi_tupla)  # Crea una nueva lista ordenada
print(nueva_lista)  # Salida: [1, 2, 3]
```

### Buenas Prácticas
- Usa `sort()` cuando no necesites conservar la lista original.
- Usa `sorted()` cuando necesites mantener la lista original sin cambios.

---

## 5. ¿Qué es un operador de reasignación?

Un operador de reasignación permite cambiar el valor de una variable existente. En Python, esto se hace mediante el uso del operador `=`.

**Ejemplo**:
```python
x = 10  # Asignación inicial
x = x + 5  # Reasignación
print(x)  # Salida: 15
```

### Buenas Prácticas
- Usa operadores de reasignación para actualizar valores de variables de manera clara y concisa.

---