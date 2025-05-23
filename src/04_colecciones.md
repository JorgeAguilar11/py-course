# 📚 Colecciones en Python

En el capítulo anterior vimos algunos tipos básicos, como los números, las cadenas de texto y los booleanos.  
Ahora aprenderás sobre **colecciones de datos**: **listas**, **tuplas** y **diccionarios**.

---

## 📝 Listas

Una **lista** es una colección ordenada y mutable.  
En otros lenguajes se conocen como *arrays* o *vectores*.

- **Pueden contener cualquier tipo de dato:** números, cadenas, booleanos, ¡incluso otras listas!
- **Se definen con corchetes `[]` y los elementos separados por comas.**

```python
l = [22, True, "una lista", [1, 2]]
```

### 🔎 Acceso a elementos

El índice comienza en **0** (no en 1):

```python
l = [11, False]
mi_var = l[0]  # mi_var vale 11
```

Para acceder a elementos de una lista dentro de otra lista:

```python
l = ["una lista", [1, 2]]
mi_var = l[1][0]  # mi_var vale 1
```

### ✏️ Modificar elementos

```python
l = [22, True]
l[0] = 99  # Ahora l es [99, True]
```

### 🔙 Índices negativos

Puedes usar índices negativos para contar desde el final:

```python
l = [10, 20, 30, 40]
print(l[-1])  # 40 (último elemento)
print(l[-2])  # 30 (penúltimo elemento)
```

### ✂️ Slicing (Particionado)

Selecciona porciones de la lista usando `[inicio:fin]` (sin incluir el fin):

```python
l = [99, True, "una lista", [1, 2]]
print(l[0:2])      # [99, True]
print(l[0:4:2])    # [99, "una lista"]
print(l[1:])       # [True, "una lista", [1, 2]]
print(l[:2])       # [99, True]
print(l[:])        # [99, True, "una lista", [1, 2]]
print(l[::2])      # [99, "una lista"]
```

### 🛠️ Modificar porciones

Puedes cambiar varias posiciones a la vez:

```python
l = [99, True, "una lista", [1, 2]]
l[0:2] = [0, 1]         # [0, 1, "una lista", [1, 2]]
l[0:2] = [False]        # [False, "una lista", [1, 2]]
```

---

## 📦 Tuplas

Las **tuplas** son como listas, pero **inmutables** (no se pueden modificar) y se definen con **paréntesis `()`**.

```python
t = (1, 2, True, "python")
```

- El constructor real es la **coma**, pero se recomienda usar paréntesis por claridad.
- Para tuplas de un solo elemento, ¡no olvides la coma!

```python
t = (1)      # Esto es un int
t = (1,)     # Esto es una tupla
```

### 🔎 Acceso y slicing

```python
mi_var = t[0]      # 1
mi_var = t[0:2]    # (1, 2)
```

> **Nota:** Las cadenas de texto también son secuencias, así que puedes hacer slicing igual que con listas y tuplas.

```python
c = "hola mundo"
print(c[0])     # h
print(c[5:])    # mundo
print(c[::3])   # hauo
```

- Las tuplas **no se pueden modificar** después de crearlas.
- Son más ligeras y rápidas que las listas.

---

## 🗂️ Diccionarios

Un **diccionario** (o *mapping*) es una colección de pares **clave-valor**.  
Se definen con llaves `{}` y los pares separados por comas.

```python
d = {
    "Love Actually": "Richard Curtis",
    "Kill Bill": "Tarantino",
    "Amélie": "Jean-Pierre Jeunet"
}
```

- Las **claves** deben ser inmutables (números, cadenas, tuplas...).
- Los **valores** pueden ser de cualquier tipo.

### 🔎 Acceso y modificación

```python
print(d["Love Actually"])  # "Richard Curtis"
d["Kill Bill"] = "Quentin Tarantino"
```

- Los diccionarios **no tienen orden** (hasta Python 3.6+ donde conservan el orden de inserción).
- No soportan slicing.

---

# 🧪 Ejercicios Prácticos

## 1️⃣ Listas

- Crea una lista con tus tres colores favoritos y muestra el segundo color.
- Cambia el primer color por "negro" y muestra la lista resultante.
- Extrae los dos últimos elementos usando slicing.

## 2️⃣ Tuplas

- Crea una tupla con tu nombre, edad y país.
- Intenta cambiar el país (¿qué sucede?).
- Usa slicing para mostrar solo el nombre y la edad.

## 3️⃣ Diccionarios

- Crea un diccionario con tres películas y sus directores favoritos.
- Cambia el director de una película.
- Muestra el director de una película usando su clave.

---

# 💡 Resumen

- **Listas:** Colecciones ordenadas y mutables (`[]`)
- **Tuplas:** Colecciones ordenadas e inmutables (`()`)
- **Diccionarios:** Colecciones de pares clave-valor (`{}`)

¡Practica creando y manipulando colecciones para dominar Python! 🚀git add mi_proyecto