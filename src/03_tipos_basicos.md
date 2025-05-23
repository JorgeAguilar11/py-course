# 🧩 Variables y Tipos de Datos Básicos en Python

---

## ❓ ¿Qué son las Variables?

Las variables en Python son **contenedores** que almacenan valores de datos.  
Puedes pensar en ellas como "cajas" con etiquetas donde guardas información para usar más tarde en tu programa.

**Características importantes:**
- No necesitas declarar el tipo de variable
- Python determina automáticamente el tipo basado en el valor asignado
- Los nombres de variables son sensibles a mayúsculas y minúsculas
- Pueden cambiar de valor durante la ejecución del programa

---

## 📝 Reglas para Nombrar Variables

### ✅ Nombres válidos:
- Deben comenzar con una letra (a-z, A-Z) o guión bajo (_)
- Pueden contener letras, números y guiones bajos
- No pueden contener espacios ni caracteres especiales

```python
# Ejemplos válidos
nombre = "Juan"
edad_usuario = 25
_variable_privada = 100
contador1 = 0
CONSTANTE = 3.14159
```

### ❌ Nombres inválidos:
```python
# Estos nombres causarán errores
2variable = 10      # No puede empezar con número
mi-variable = 5     # No puede contener guiones
class = "Python"    # 'class' es una palabra reservada
mi variable = 20    # No puede contener espacios
```

---

# 🔤 Tipos de Datos Básicos

---

## 1️⃣ Strings (Cadenas de Texto) - `str`

Los strings representan texto y se definen usando comillas simples o dobles.

```python
# Diferentes formas de crear strings
nombre = "María"
apellido = 'González'
mensaje = "Hola, ¿cómo estás?"
texto_largo = """Este es un texto
que ocupa varias
líneas"""
```

**Operaciones básicas con strings:**
```python
saludo = "Hola"
nombre_completo = nombre + " " + apellido  # Concatenación
print(f"Mi nombre es {nombre}")  # String formatting
```

**Métodos útiles de strings:**
```python
texto = "Python es genial"
print(texto.upper())        # "PYTHON ES GENIAL"
print(texto.lower())        # "python es genial"
print(texto.replace("genial", "increíble"))  # "Python es increíble"
print(len(texto))           # 16 (longitud del string)
```

### 🔹 Caracteres de Escape

```python
comillas = "Él dijo: \"Hola mundo\""
nueva_linea = "Primera línea\nSegunda línea"
tabulacion = "Nombre:\tJuan"
barra_invertida = "C:\\Users\\Juan\\Documents"
```

---

## 2️⃣ Números - `int` y `float`

Python maneja dos tipos principales de números: **enteros** y **decimales**.

### 🔸 Enteros (`int`)
```python
edad = 25
temperatura = -10
población = 1000000

# Operaciones con enteros
suma = 10 + 5
resta = 20 - 8
multiplicacion = 4 * 7
division_entera = 15 // 4   # 3 (división entera)
modulo = 17 % 5             # 2 (resto de la división)
potencia = 2 ** 3           # 8 (2 elevado a la 3)
```

### 🔸 Números Decimales (`float`)
```python
precio = 19.99
pi = 3.14159
temperatura = -2.5

# Operaciones con decimales
division = 15 / 4   # 3.75 (división normal)
resultado = 10.5 + 3.2  # 13.7

# Funciones útiles con números
import math
numero = 16.7
print(round(numero))      # 17 (redondear)
print(math.ceil(numero))  # 17 (redondear hacia arriba)
print(math.floor(numero)) # 16 (redondear hacia abajo)
print(abs(-5.3))          # 5.3 (valor absoluto)
```

---

## 3️⃣ Booleanos - `bool`

Los valores booleanos representan **verdadero** (`True`) o **falso** (`False`).

```python
es_estudiante = True
tiene_trabajo = False
mayor_de_edad = True

# Operaciones lógicas
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Comparaciones que devuelven booleanos
edad = 18
print(edad >= 18)       # True
print(edad == 21)       # False
print(edad != 16)       # True
```

**Valores que se consideran False:**
```python
print(bool(0))          # False
print(bool(""))         # False (string vacío)
print(bool(None))       # False
print(bool([]))         # False (lista vacía)
```
**Valores que se consideran True:**
```python
print(bool(1))          # True
print(bool("Hola"))     # True
print(bool(-1))         # True
```

---

# ➕➖✖️➗ Operadores en Python

Los operadores te permiten realizar operaciones con variables y valores.  
Aquí tienes los más usados:

## 🔢 Operadores Aritméticos

| Operador | Descripción           | Ejemplo         | Resultado      |
|----------|-----------------------|-----------------|---------------|
| `+`      | Suma                  | `2 + 3`         | `5`           |
| `-`      | Resta                 | `5 - 2`         | `3`           |
| `*`      | Multiplicación        | `4 * 3`         | `12`          |
| `/`      | División              | `10 / 2`        | `5.0`         |
| `//`     | División entera       | `7 // 2`        | `3`           |
| `%`      | Módulo (resto)        | `8 % 3`         | `2`           |
| `**`     | Potencia              | `2 ** 3`        | `8`           |

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## 🔍 Operadores de Comparación

Sirven para comparar valores y devuelven un booleano (`True` o `False`):

| Operador | Significado      | Ejemplo      | Resultado   |
|----------|------------------|--------------|-------------|
| `==`     | Igual a          | `5 == 5`     | `True`      |
| `!=`     | Distinto de      | `3 != 2`     | `True`      |
| `>`      | Mayor que        | `7 > 4`      | `True`      |
| `<`      | Menor que        | `2 < 1`      | `False`     |
| `>=`     | Mayor o igual    | `5 >= 5`     | `True`      |
| `<=`     | Menor o igual    | `3 <= 2`     | `False`     |

---

## 🤔 Operadores Lógicos

Permiten combinar condiciones:

| Operador | Descripción | Ejemplo             | Resultado   |
|----------|-------------|---------------------|-------------|
| `and`    | Y           | `True and False`    | `False`     |
| `or`     | O           | `True or False`     | `True`      |
| `not`    | No          | `not True`          | `False`     |

```python
x = 5
print(x > 2 and x < 10)   # True
print(x < 2 or x > 3)     # True
print(not(x == 5))        # False
```

---

## 🧩 Operadores de Asignación

Sirven para asignar y actualizar valores en variables:

| Operador | Ejemplo      | Equivalente a      |
|----------|--------------|--------------------|
| `=`      | `x = 5`      | Asigna 5 a x       |
| `+=`     | `x += 2`     | `x = x + 2`        |
| `-=`     | `x -= 1`     | `x = x - 1`        |
| `*=`     | `x *= 3`     | `x = x * 3`        |
| `/=`     | `x /= 4`     | `x = x / 4`        |
| `//=`    | `x //= 2`    | `x = x // 2`       |
| `%=`     | `x %= 3`     | `x = x % 3`        |
| `**=`    | `x **= 2`    | `x = x ** 2`       |

```python
x = 10
x += 5   # x ahora es 15
x *= 2   # x ahora es 30
```

---

## 🔄 Conversión entre Tipos de Datos

Python permite convertir entre diferentes tipos de datos usando funciones de conversión.

```python
# Conversión a string
numero = 42
numero_texto = str(numero)  # "42"
print("El número es: " + numero_texto)

# Conversión a entero
texto_numero = "123"
numero_entero = int(texto_numero)  # 123
resultado = numero_entero + 10     # 133

# Conversión a decimal
entero = 5
decimal = float(entero)  # 5.0

# Conversión a booleano
print(bool(1))      # True
print(bool(0))      # False
print(bool("si"))   # True
```

⚠️ **Cuidado con las Conversiones**
```python
# Estas conversiones causarán errores
# int("hola")         # ValueError
# float("texto")      # ValueError
# int("12.5")         # ValueError (usa float primero)

# Forma correcta para el último caso
decimal_texto = "12.5"
numero = int(float(decimal_texto))  # 12
```

---

## 🔍 Verificar el Tipo de una Variable

```python
# Función type() para verificar tipos
nombre = "Ana"
edad = 25
activo = True

print(type(nombre))    # <class 'str'>
print(type(edad))      # <class 'int'>
print(type(activo))    # <class 'bool'>

# Función isinstance() para verificar si es de un tipo específico
print(isinstance(nombre, str))    # True
print(isinstance(edad, int))      # True
print(isinstance(activo, bool))   # True
```

---

# 🧪 Ejemplos Prácticos

---

## Ejemplo 1: Calculadora Básica

```python
# Solicitar datos al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "No se puede dividir por cero"

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
```

---

## Ejemplo 2: Información Personal

```python
# Variables de información personal
nombre = "Carlos"
apellido = "Rodríguez"
edad = 28
es_programador = True
salario = 45000.50

# Crear un perfil
perfil = f"""
PERFIL PERSONAL
===============
Nombre completo: {nombre} {apellido}
Edad: {edad} años
Profesión: {'Programador' if es_programador else 'Otra profesión'}
Salario: ${salario:,.2f}
"""

print(perfil)
```

---

# 🏋️‍♂️ Ejercicios Prácticos

---

## Ejercicio 1: Variables Básicas

```python
# Crea variables con tu información personal
mi_nombre = "Tu nombre aquí"
mi_edad = 0  # Tu edad
soy_estudiante = True  # ¿Eres estudiante?

# Imprime la información
print(f"Hola, soy {mi_nombre}, tengo {mi_edad} años")
print(f"¿Soy estudiante? {soy_estudiante}")
```

---

## Ejercicio 2: Conversiones

```python
# Practica conversiones de tipos
texto_numero = "456"
numero_decimal = "78.9"

# Convierte y realiza operaciones
# (Completa el código)
```

---

## Ejercicio 3: Operaciones con Strings

```python
# Trabaja con strings
frase = "Me encanta programar en Python"

# Encuentra la longitud, convierte a mayúsculas, 
# reemplaza palabras, etc.
# (Completa el código)
```

---

# 💡 Consejos y Buenas Prácticas

- Usa nombres descriptivos: `edad_usuario` es mejor que `x`
- Sigue la convención `snake_case`: `nombre_completo` en lugar de `nombreCompleto`
- Inicializa las variables: Asigna un valor inicial apropiado
- Comenta tu código: Explica qué hace cada variable importante
- Verifica tipos cuando sea necesario: Usa `isinstance()` para validaciones

---

# 📝 Resumen

- Las variables son contenedores para almacenar datos
- Los strings representan texto y se definen con comillas
- Los números pueden ser enteros (`int`) o decimales (`float`)
- Los booleanos representan verdadero (`True`) o falso (`False`)
- Python permite conversión entre tipos de datos
- Usa `type()` e `isinstance()` para verificar tipos de variables
- ¡Y ahora también conoces los operadores más importantes!

---

¡Con estos fundamentos ya puedes empezar a crear programas más interesantes en Python! 🚀