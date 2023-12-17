#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <locale.h>
void greetings();
int count_of_sentences(char *str);
int input(char** str);
char** treatment(char* str, int count_sentanses, int len);
void output(char** str, int count_sentences);
void clear(char** str, int count_sentences);
char** clear_double(char** array, int size,int* new_size);
char* createLowerCaseArray(int size, char* str);
void change(char** str, int size, int command);
char** task_1(char** str, int size);
char** task_2(char** str, int size,int* new_size);
void task_3(char** str, int size);
char** task_4(char** str, int size,int* new_size);
int cmp(const void *a, const void *b);
char* removeWord(char* str, char* word);
int compareSentences(const void *a, const void *b);
float calculateAverage(const char *str);
char* space(char* str);


int main(){
    setlocale(LC_CTYPE, "");
    greetings();

    int command;        
    scanf("%d", &command);
    if(command > 5 || command < 0)
        printf("error: первый символ должнен быть числом от 0 до 5");
    else if(command == 5)
        printf("1: Во всемы тексте удалить слово введенное пользователем. Если после удаления в предложении не останется слов, его необходимо удалить.\n2: Для каждого предложения вывести все заглавные буквы в лексикографическом порядке.\n3: Отсортировать предложения по среднему арифметическому чисел в предложении. Число - слово состоящее только из цифр.\n4: Удалить все предложения в которых нет строчных букв.");

    else{
        
        char* str = NULL;
        int len = input(&str);
        int count_sentences = count_of_sentences(str);
        
        
        char ** sentences = treatment(str, count_sentences,len);
        
        change(sentences, count_sentences, command);
        
        if(str != NULL){
            free(str);
        }
    
    }
    return 0;
}

int cmp(const void *a, const void *b){
    const char *f = (const char *)a;
    const char *s = (const char *)b;
    return strcmp(f,s);
}

void change(char** str, int size, int command){
    int new_size = 0;
    if(command == 0){

            char** result = clear_double(str,size,&new_size);
            output(result,new_size);
            clear(result,new_size);
            clear(str,size);
        }
    if(command == 1){

            char** text = clear_double(str,size,&new_size);
            char** result = task_1(text, new_size);
            output(result,new_size);
            clear(result ,new_size);
            clear(text,new_size);
            clear(str,size);
        }
    if(command == 2){
            int size_after_t_2 = 0;
            char** text = clear_double(str,size,&new_size);
            char** result = task_2(text, new_size,&size_after_t_2);
            
            output(result,size_after_t_2);
            clear(result,size_after_t_2);
            clear(text,new_size);
            clear(str,size);
        }
    if(command == 3){
            task_3(str, size);
        }
    if(command == 4){
        int size_after_t_4 = 0;
        char** text = clear_double(str,size,&new_size);
        char** result = task_4(text, new_size, &size_after_t_4);
        output(result,size_after_t_4);
        clear(result,size_after_t_4);
        clear(text,new_size);
        clear(str, size);
    }

}
void output(char** str, int count_sentences){
    if(str != NULL){
        for(int i = 0; i < count_sentences; i++){
            printf("%s\n", str[i]);
        }
    }
}
char** task_1(char** str, int size){
    char* word = NULL;
    int idx = 0;
    for(int i = 0; i < strlen(str[0]) && str[0][i] != ' ' && str[0][i] != '.'; i++){
        word = realloc(word, sizeof(char) * ++idx);
        word[idx - 1] = str[0][i];
        
    }
    word[idx] = '\0';
    int len = 0;
    char** result = NULL;
    for(int i = 0;i < size;i++){
        char* sentence = removeWord(str[i], word);
        result = realloc(result, sizeof(char*) * ++len);
        result[len - 1] = malloc(strlen(sentence) + 1);
        for(int j = 0;j < strlen(sentence); j++){
            result[len - 1][j] = *(sentence + j);
        }
        
        result[len - 1][strlen(sentence)] = '\0';
        if(sentence != NULL){
            free(sentence);
        }
    }
    if(word != NULL){
        free(word);
    }
    return result;
}   
char** task_2(char** str, int size,int* new_size){
    int count = 0;
    for(int i = 0; i < size; i++){
        for(int j = 0;j < strlen(str[i]); j++){
            if(isupper(str[i][j])){
                count++;
                break;
            }
        
        }
    }
    *new_size = count;
    
    char** arr = malloc(sizeof(char*) * count);
    int len = 0;
    for(int i = 0; i < size; i++){
        char* word = NULL;
        int idx = 0;
        int flag = 0;
        for(int j = 0; j < strlen(str[i]); j++){
            if(isupper(str[i][j])){
                word = realloc(word, sizeof(char) * ++idx);
                word[idx - 1] = str[i][j];
                flag = 1;
            }
        }
        if(idx)
            word[idx] = '\0';
        
        if(flag){
            
            
            arr[len] = malloc(strlen(word) + 1);
            for(int i = 0; i < strlen(word);i++){
                arr[len][i] = word[i];
            }
            arr[len][strlen(word)] = '\0';
            len++;
            if(word != NULL){
                free(word);
            }
        }
    }

    for(int i = 0; i < count; i++){
        qsort(arr[i], strlen(arr[i]), sizeof(char), cmp);
    }
    return arr;
}
void task_3(char** str, int size){
    int new_size = 0;
    char** text = clear_double(str,size,&new_size);
    qsort(text, new_size, sizeof(char *), compareSentences);
    
    
    output(text,new_size);
    clear(text,new_size);
    clear(str,size);
}

char** task_4(char** str, int size,int* new_size){
    char** res = NULL;
    int idx = 0;
    for(int i = 0; i < size; i++){
        int flag = 1;
        for(int j = 0; j < strlen(str[i]); j++){
            if(islower(str[i][j])){
                flag = 0;
                break;
            }
        }
        if(flag == 0){

            res = realloc(res, sizeof(char*) * ++idx);
            res[idx - 1] = malloc(sizeof(char) * (strlen(str[i]) + 1));
            for(int k = 0; k < strlen(str[i]); k ++){
                res[idx - 1][k] = str[i][k];
            }
        res[idx - 1][strlen(str[i])] = '\0';
        }
        

    }
    
    *new_size = idx;
    return res;

}


void greetings(){

    printf("Course work for option 4.20, created by Anton Kornienko\n");

}


int input(char** str)
{
    int iter = 0;
    char c;
    int count_n = 0;
    while (1) {
            c = getchar();

            if(c == '\n'){
                count_n ++;
                if(count_n == 2){
                    break;
                }
                else{
                    iter++;
                    *str = (char *)realloc(*str, (iter) * sizeof(char));
                    *(*str + iter - 1) = c;
                }
            }
            else{
                count_n = 0;
                iter++;
                *str = (char *)realloc(*str, (iter) * sizeof(char));
                *(*str + iter - 1) = c;
            }

    }
    iter ++;
    *str = (char *)realloc(*str, (iter) * sizeof(char));
    *(*str + iter - 1) = '\0';
    return iter;
}

int count_of_sentences(char *str)
{
    int count = 0;
    for(int i = 0; i < strlen(str); i++){
        if(str[i] == '.'){
            count ++;
        }

    }
    return count;
}
char** treatment(char* str, int count_sentanses, int len){
    char ** result = malloc(sizeof(char*) * count_sentanses);
    int number = 0;
    int idx = 0;
    
    char* sentence = NULL;



    for(int i = 0; i < len;i++){
        
        if(str[i] != '.'){
            sentence = realloc(sentence, sizeof(char) * (++idx));
            sentence[idx - 1] = str[i];
            
        }

        if(str[i] == '.' && i > 0){
            sentence = realloc(sentence, sizeof(char) * ((++idx) + 1));
            sentence[idx - 1] = str[i];
            sentence[idx] = '\0';

            if (sentence[0] == ' '){
                int start = 0;
                while(sentence[start] == ' '){
                    start ++;
                }
                memmove(sentence, sentence + start, strlen(sentence));
            }

            result[number] = malloc((strlen(sentence) + 1) * sizeof(char*));
            for(int k = 0; k < strlen(sentence); k++){
                result[number][k] = sentence[k];
            }   
             result[number][strlen(sentence)] = '\0';
             number++;
             
             
             idx = 0;           
        }
    }
    return result;
}




void clear(char** str, int count_sentences){
    if(str != NULL){
        for (int i = 0; i < count_sentences; i++) {
            if(str[i] != NULL){
                free(str[i]);
            }
        }
        free(str);
    }
}
char** clear_double(char** array, int size,int* new_size){
    char** text_res = malloc(0);
    int idx = 0;
    for(int i = 0; i < size;i++){
        char* str = array[i];
        char* str_low = createLowerCaseArray(strlen(str), str);
        int flag = 1;
        for(int j = 0; j < idx;j++){
            char* str_0 = array[j];
            char* str_0_low = createLowerCaseArray(strlen(str_0), str_0);
            if(strcmp(str_low, str_0_low) == 0){
                flag = 0;
                break;
            }
        }
        if(flag){
            text_res = realloc(text_res, sizeof(char*) * ++idx);
            text_res[idx - 1] = space(str);
        }
    }
    *new_size = idx;
    return text_res;
}

char* createLowerCaseArray(int size, char* str){
    char* arr = malloc((sizeof(char) + 1) * size);
    int i = 0;
    for(;i < size; ++i){
        arr[i] = tolower(str[i]);
    }

    arr[i] = '\0';
    return space(arr);

}



    
char* removeWord(char* str, char* word) {
    char arr[strlen(str)];
    for(int i = 0;i < strlen(str);i++){
        if(str[i] != '.')
            arr[i] = *(str + i);
    }
    char sep[10] = " ";
    char* result = malloc(sizeof(char) * strlen(str) + 1);
    int idx = 0;
    arr[strlen(str) - 1] = '\0';
    char *token = strtok(arr, sep);
    while(token != NULL){
            if(strcmp(token, word) != 0){
                for(int i = 0; i < strlen(token); i++){
                        result[idx++] = token[i];    
                }
                result[idx++] = ' ';

            }
            token = strtok(NULL, sep);

    }
 
    if(idx){
        result[idx - 1] = '.';
        result[idx] = '\0';
    }
    else{
        result[idx] = '.';
        result[idx + 1] = '\0';
    }
    return result;
}



float calculateAverage(const char *str) {
    char arr[strlen(str)];
    for(int i = 0; i < strlen(str) && str[i] != '.'; i++){
        arr[i] = *(str + i);
    }
    int count = 0;
    float sum = 0.0;
    arr[strlen(str) - 1] = '\0';
    char *token = strtok(arr, " ");
    while (token != NULL) {
        int flag = 1;
        for(int i = 0; i < strlen(token); i++){
            if(isdigit(token[i]) == 0){
                flag = 0;
                break;
            }
        }
        if(flag){
            sum += atoi(token);
            count++;
        }
        token = strtok(NULL, " ");
    }
    return count > 0 ? (sum / count) : 0;
}



int compareSentences(const void *a, const void *b) {
    const char **sentenceA = (const char **)a;
    const char **sentenceB = (const char **)b;
    float averageA = calculateAverage(*sentenceA);
    float averageB = calculateAverage(*sentenceB);

    if (averageA < averageB) {
        return -1;
    } else if (averageA > averageB) {
        return 1;
    } else {
        return 0;
    }
}



char* space(char* str){
    char* res = calloc(strlen(str) + 1, sizeof(char));
    int start = 0;
    while (str[start] == '\t' || str[start] == ' ' || str[start] == '\n'){
        start++;
    }
    for (int i = 0; i < strlen(str) - start; i++){
        res[i] = str[start + i];
    }
    res[strlen(str) - start] = '\0';
    return res;
}
