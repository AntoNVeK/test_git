#!/bin/bash

# Директория, в которой будут создаваться файлы
output_dir="$(pwd)/test"

# Создаем директорию, если она не существует
mkdir -p "$output_dir"

# Переходим в директорию
cd "$output_dir" || exit

# Максимальная длина имени файла
max_length=256

# Создаем файлы с именами разной длины
for ((i=1; i<=max_length; i++)); do
  # Генерируем имя файла, состоящее из 'a', повторенного i раз
  filename=$(printf "%0.sa" $(seq 1 $i))
  
  # Создаем пустой файл
  touch "$filename"
  
  # Проверяем, удалось ли создать файл
  if [[ $? -ne 0 ]]; then
    echo "Ошибка: не удалось создать файл с длиной имени $i"
    break
  fi
  
  echo "Создан файл: $filename"
done

echo "Все файлы созданы в директории: $(pwd)"