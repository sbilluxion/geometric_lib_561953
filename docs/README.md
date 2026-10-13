# Documentation of the project "geometric_lib"

> Made by: Balberin Sergey, M3101\
> Checked by: Povyshev Vladislav

## Table of contents

1) [Project structure](#project-structure)
2) [Area function](#area-function)
3) [Perimeter function](#perimeter-function)
4) [History of commits](#history-of-commits)

## Project structure

This project contains 4 .py files, related to geometric figures:
1) [circle.py](../circle.py)
2) [rectangle.py](../rectangle.py)
3) [square.py](../square.py)
4) [triangle.py](../triangle.py)

Each file has **two** functions in it: 
**Area** and **Perimeter**. 

Each function has a brief description about it's work and how to use it

> [!TIP]
> Execute [tests.py](../tests/tests.py) to check functions' workability

## Area function

### 1) Circle

This function takes circle's radius <span style="color: rgb(52, 152, 219)">**int**</span> and returns it's area in <span style="color: red">**float**</span>

```python
import math
def area(r):
    return math.pi * r * r
```

<ins>Example</ins>: area(10) = 314.1592653589793 

### 2) Rectangle

This function takes length of two sides in **int** and returns result of their multiplication in **int**

```python
def area(a,b):
    return a * b
```

<ins>Example</ins>: area(2,5) = 10 

### 3) Square

This function takes length of the square's side in **int** and returns area of the square in **int**

```python
def area(a):
    return a * a
```

<ins>Example</ins>: area(10) = 100

### 4) Triangle

This function takes lengths of the side and it's altitude in <span style="color: rgb(52, 152, 219)">**int**</span> and returns square of the triangle in <span style="color: red">**float**</span>

```python
def area(a,h):
    return a * h / 2
```

<ins>Example</ins>: area(10,5) = 25.0

## Perimeter function

### 1) Circle

This function takes radius of the circle in <span style="color: rgb(52, 152, 219)">**int**</span> and returns it's perimeter in <span style="color: red">**float**</span>

```python
import math
def perimeter(r):
    return 2 * math.pi * r
```

<ins>Example</ins>: perimeter(10) = 62.83185307179586

### 2) Rectangle

This function takes length of two sides in **int** and returns result of their double summary(periemeter) in **int** 

```python
def perimeter(a,b):
	return 2 * ( a + b )
```

<ins>Example</ins>: perimeter(2,5) = 14

### 3) Square

This function takes length of the square's side in **int** and returns it's perimeter in **int**

```python
def perimeter(a):
    return 4 * a
```

<ins>Example</ins>: perimeter(10) = 40

### 4) Triangle

This function takes length of all three sides of the triangle in **int** and returns it's perimeter in **int**

```python
def perimeter(a,b,c):
    return a + b + c
```

<ins>Example</ins>: perimeter(1,2,3) = 6

## History of commits

### Branch: main

#### 1) 8ba9aeb3cea847b63a91ac378a2a6db758682460

**Name**: L-03: Circle and square added\
**Author**: smartiqa <info@smartiqa.ru>  
**Date**: Thu Mar 4 14:54:08 2021 +0300 

**Changes**

New lines added in circle.py:

```python
import math


def area(r):
    return math.pi * r * r


def perimeter(r):\
    return 2 * math.pi * r

```

New lines added in square.py:

```python


def area(a):
    return a * a


def perimeter(a):
    return 4 * a
```

#### 2) 6adb96248a4d00d3bea13bd95d78ef52352cd1b4
**Name**: L-03: Docs added\
**Author**: smartiqa <info@smartiqa.ru>\
**Date**: Thu Mar 4 14:55:29 2021 +0300

**Changes**

New lines added in docs/README.md:

>\# Math formulas\
>\## Area\
>\- Circle: S = πR²\
>\- Rectangle: S = ab\
>\- Square: S = a²\
>\
>\## Perimeter\
>\- Circle: P = 2πR\
>\- Rectangle: P = 2a + 2b\
>\- Square: P = 4a

### Branch: new_features_561953

#### 1) 2ee7540e59483434d96869c0b1766d001e286d9f 

**Name**: Added descriptions to all functions\
**Author**: Sergey Balberin <sbilluxion@gmail.com>\
**Date**: Fri Sep 18 13:31:40 2026 +0300

**Changes**

New lines added in circle.py

>\#Возвращает площадь круга в формате float\
>\#	Параметры:\
>\#		r: радиус окружности\
>\#	Пример: area(10) = 314.1592653589793

>\#Возвращает периметр круга в формате float\
>\#	Параметры:\
>\#		r: радиус окружности\
>\#	Пример: perimeter(10) = 62.83185307179586\
>\#

New lines added in rectangle.py

>\#Принимает длины сторон, равные  a,b(десятичные целые числа), возвращает площадь, равную a*n\
>\#   Пример: area(2,5) = 10 (десятичное целое число)

>\#Принимает длины сторон, равные a,b(десятичные целые числа),\ 
>\#   возвращает периметр, равный 2*(a*b)\
>\#   Пример: perimeter(2,5) = 20 (десятичное целое число)

New lines added in square.py

>\#Возвращает площадь квадрата в формате int\
>\#	Параметры:\
>\#		a(int) :  длина стороны квадрата \
>\#	Пример: area(10) = 100

>\#Возвращает периметр квадрата в формате int\
>\#	Параметры:\
>\#		a(int) :  длина стороны квадрата \
>\#	Пример: perimeter(10) = 40

New lines added in triangle.py

>\#Принимает длину стороны(a,целое десятичное число) и высоты(h,целое десятичное число), \
>\#   проведённой к ней. Возвращает площадь равную a*h/2 в формате float

>\#Принимает длину сторон(a,b,c - целые десятичные числа), \
>\#   Возвращает периметр  равный a*b*c в формате int