# ege4All
## Предназначение:
- Просто так
- Для КР
- Для учеников, которых заставляют решать ЕГЭ...
  - ...но они точно знают, что не будут сдавать этот экзамен
## Использование
### ЕГЭ 2:
```py
print(task2(table = '''''', results = [0,0,0], vars = 'xyz', F = lambda x,y,z: x==y==z, unique = True))
```
Здесь:
  - ```table``` - таблица истинности для переменных. Пропущенные значения можно заменять любым символом, кроме пробела, разделитель между символами - пробел;
  - ```results``` - столбец значений функции ```F```;
  - ```vars``` - переменные, записанные без разделителей (!). Например, ```vars = 'xyz'```;
  - ```F(*args)``` - собственно логическая функция из условия;
  - ```unique``` - уникальны ли все строки в таблице.
