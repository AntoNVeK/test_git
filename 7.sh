#!/bin/bash

# Имя основной директории
MAIN_DIR="test_directory"

# Количество файлов
NUM_FILES=100

# Количество поддиректорий
NUM_SUBDIRS=10

# Размер каждого файла (в байтах)
FILE_SIZE=1024  # 1 KB

# Функция для получения размера директории
get_directory_size() {
    du -sb "$1" | awk '{print $1}'
}

# Создание основной директории
mkdir -p "$MAIN_DIR"
echo "Создана основная директория: $MAIN_DIR"
echo "Размер каталога после создания: $(get_directory_size "$MAIN_DIR") байт"
echo "----------------------------------------"

# Создание 100 файлов
for i in $(seq 1 $NUM_FILES); do
    dd if=/dev/urandom of="$MAIN_DIR/file_$i.txt" bs=$FILE_SIZE count=1 status=none
done
echo "Создано $NUM_FILES файлов."
echo "Размер каталога после создания файлов: $(get_directory_size "$MAIN_DIR") байт"
echo "----------------------------------------"

# Создание 10 поддиректорий
for i in $(seq 1 $NUM_SUBDIRS); do
    mkdir -p "$MAIN_DIR/subdir_$i"
done
echo "Создано $NUM_SUBDIRS поддиректорий."
echo "Размер каталога после создания поддиректорий: $(get_directory_size "$MAIN_DIR") байт"
echo "----------------------------------------"

# Удаление 65 файлов
for i in $(seq 1 65); do
    rm -f "$MAIN_DIR/file_$i.txt"
done
echo "Удалено 65 файлов."
echo "Размер каталога после удаления файлов: $(get_directory_size "$MAIN_DIR") байт"
echo "----------------------------------------"

# Удаление 7 поддиректорий
for i in $(seq 1 7); do
    rm -rf "$MAIN_DIR/subdir_$i"
done
echo "Удалено 7 поддиректорий."
echo "Размер каталога после удаления поддиректорий: $(get_directory_size "$MAIN_DIR") байт"
echo "----------------------------------------"

# Удаление основной директории
rm -rf "$MAIN_DIR"
echo "Основная директория удалена."
echo "----------------------------------------"