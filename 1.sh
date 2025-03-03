#!/bin/bash

# Проверяем, был ли передан аргумент с именем файла
if [ -z "$1" ]; then
    echo "Пожалуйста, укажите имя выходного файла."
    exit 1
fi

output_file="$1"

# Очищаем выходной файл
> "$output_file"

# Функция для поиска и записи первого найденного файла определённого типа
find_and_write() {
    type=$1
    description=$2
    result=$(ls -lR / 2>/dev/null | grep "^$type" | head -n 1)
    if [ -n "$result" ]; then
        file_name=$(echo "$result" | awk '{print $NF}')
        if [ "$type" == "l" ]; then
            # Для символьных ссылок извлекаем директорию и целевой путь
            link_path=$(echo "$result" | awk '{print $9}')
            target_path=$(echo "$result" | awk '{print $11}')
            # Если путь относительный, объединяем с директорией ссылки
            if [[ "$target_path" != /* ]]; then
                full_path=$(dirname "$link_path")/$target_path
                full_path=$(readlink -f "/$full_path")
            else
                full_path=$(readlink -f "/$target_path")
            fi
        else
            # Для остальных типов используем find
            full_path=$(find / -name "$file_name" 2>/dev/null | head -n 1)
        fi
        if [ -n "$full_path" ]; then
            echo "$description:" >> "$output_file"
            echo "$result" >> "$output_file"
            echo "Полный путь: $full_path" >> "$output_file"
            echo "" >> "$output_file"
        else
            echo "$description: не удалось найти полный путь" >> "$output_file"
        fi
    else
        echo "$description: не найдено" >> "$output_file"
    fi
}

# Поиск и запись файлов каждого типа
find_and_write '-' "Обычный файл"
find_and_write 'b' "Блочное устройство"
find_and_write 'c' "Символьное устройство"
find_and_write 'd' "Директория"
find_and_write 'l' "Символьная ссылка"
find_and_write 'p' "FIFO"
find_and_write 's' "Сокет"

echo "Результаты сохранены в файл: $output_file"