#!/bin/bash

if [ -z "$1" ]; then
    echo "Использование: $0 <путь_к_файлу>"
    exit 1
fi

# Получаем полный путь к целевому файлу
target=$(readlink -f "$1")

# Проверяем, существует ли указанный файл
if [ ! -e "$target" ]; then
    echo "Ошибка: Файл '$1' не существует!"
    exit 2
fi

echo "Поиск всех символьных ссылок на файл: $target"

# Ищем символические ссылки по всей файловой системе (ограничим поиск, например, /home)
links=$(find /home -type l 2>/dev/null | while read -r link; do
    # Проверяем, куда указывает символическая ссылка
    resolved=$(readlink -f "$link" 2>/dev/null)
    if [ "$resolved" == "$target" ]; then
        echo "Символическая ссылка найдена: $link"
    fi
done)

# Подсчитываем количество найденных ссылок
count=$(echo "$links" | wc -l)

# Выводим результат
echo "Найдено $count символьных ссылок:"
echo "$links"
