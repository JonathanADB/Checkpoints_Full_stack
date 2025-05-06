# Preguntas y Respuestas sobre Python

## 1. ¿Cuáles son los tipos de Datos en Python?
Los principales tipos de datos en Python son:
- **Numéricos**: 
  - `int` (enteros) → 42
  - `float` (decimales) → 3.14
  - `complex` → 2+3j
- **Secuencias**:
  - `str` (texto) → "Hola"
  - `list` → [1, 2, 3]
  - `tuple` → (1, "a", True)
- **Mapeos**:
  - `dict` → {"clave": "valor"}
- **Booleanos**: `bool` → True/False
- `NoneType` → None
- **Sets**: `set` → {1, 2, 3}

```python
ejemplo = {
  "entero": 10,
  "texto": "Python",
  "lista": [True, False]
}
```

## 2. ¿Qué tipo de convención de nomenclatura deberíamos utilizar para las variables en Python?
- Usar **snake_case** para variables y funciones → `mi_variable`
- **MAYÚSCULAS** para constantes → `PI = 3.1416`
- Nombres descriptivos y significativos
```python
edad_usuario = 25
temperatura_promedio = 36.5
calcular_impuesto_total = lambda x: x * 0.21


VELOCIDAD_LUZ = 299_792_458  # m/s
MAX_INTENTOS_LOGIN = 3
CODIGO_PAIS_DEFAULT = "ES"
```



## 3. ¿Qué es un Heredoc en Python?
Es una forma de crear cadenas multilínea usando triples comillas:
```python
texto_largo = '''
Esto es un texto
que abarca múltiples
líneas sin necesidad de
usar \\n
'''
```

## 4. ¿Qué es una interpolación de cadenas?
Métodos para insertar variables en cadenas:
1. **f-strings** (recomendado):
   ```python
   nombre = "Ana"
   print(f"Hola {nombre}")  # Hola Ana
   ```
2. **format()**:
   ```python
   "{} + {} = {}".format(2, 3, 5)
   ```
3. **% operator** (legado):
   ```python
   "Valor: %d" % 42
   ```

## 5. ¿Cuándo deberíamos usar comentarios en Python?
- Para explicar **por qué** se hace algo, no el qué
- Documentar funciones con docstrings:
  ```python
  def calcular_area(radio):
      '''
      Calcula el área de un círculo
      Parámetros:
          radio (float): Radio del círculo
      Retorna:
          float: Área calculada
      '''
      return 3.1416 * radio**2
  ```
- Advertencias importantes
- *Evitar* comentarios obvios:
  ```python
  x = 5  # Asignar 5 a x (redundante)
  ```

## 6. ¿Cuáles son las diferencias entre aplicaciones monolíticas y de microservicios?
Las diferencias entre aplicaciones monolíticas y de microservicios básicamente están en cómo están organizadas. Las aplicaciones monolíticas son como un solo bloque donde todo está junto: la interfaz, la lógica y la base de datos funcionan como un único sistema. Esto hace que sean más fáciles de entender y manejar al principio, por eso suelen usarse en proyectos pequeños o medianos. Un ejemplo clásico es WordPress.

Por otro lado, las aplicaciones con arquitectura de microservicios dividen la aplicación en partes más pequeñas e independientes, llamadas servicios, que se comunican entre sí usando APIs. Esto tiene varias ventajas, como poder escalar solo las partes que necesiten más recursos, usar diferentes tecnologías para cada servicio y actualizar o desplegar cada parte sin afectar a las demás. Un buen ejemplo de esto es Netflix.