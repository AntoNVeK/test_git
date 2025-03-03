#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    char ch;

    // Открываем файл, к которому нужен доступ
    file = fopen("/home/testuser/secret_file.txt", "r");
    if (file == NULL) {
        perror("Ошибка при открытии файла");
        exit(EXIT_FAILURE);
    }

    // Читаем и выводим содержимое файла
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);
    return 0;
}
