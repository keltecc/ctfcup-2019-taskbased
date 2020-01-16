# Crypto | Eternal Classic

## Информация

> Задумывались ли вы когда-нибудь над вопросом: сколько секунд в вечности?
> 
> Как-то давно братья Гримм привели аналогию с большой Алмазной горой, на которую раз в 100 лет прилетает птичка и точит свой клюв.
> 
> С появлением кибернетизированных животных эта аналогия устарела. Но мы смогли придумать новую:
> 
> «Когда XOR перестанут использовать для шифрования, лишь тогда пройдёт первая секунда вечности.» 


## Описание

В [таске](task/task.py) из файла читается флаг, шифруется с помощью побайтового XOR и записывается в выходной файл.


## Решение

Нужно заметить, что ключ "умножается" на 2, то есть итоговый ключ выглядит как `key||key`, где `key` — оригинальный ключ, который мы не знаем, а `||` — конкатенация.

Для реализации побайтового ксора выбран `PyCrypto.Cipher.XOR`, который поддерживает длину ключа не длиннее 32 байт. Длина самого флага, как можно понять из шифртекста, 37 байт. Их длины взаимно простые, а значит мы можем восстановить флаг.

Нужно перебрать длину ключа, составить несколько систем линейных уравнений и решить их.

[Пример решения](task/exploit.py)


## Флаг

`Cup{dfe5ceef4386709f64c2837547b5d5228ac41}`