#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include<ctype.h>

#define IF_dir de->d_type == DT_DIR && strcmp(de->d_name, ".") && strcmp(de->d_name, "..")
int readFile(char* filename, char* name_command){
    int res = 0;

    if(strcmp(name_command, "mul") == 0)
        res = 1;

    FILE *f = fopen(filename, "r");

    if(!f)
        return 0;
    
    char s[100];
    while(fgets(s,100,f)){

        char num[10];
        int size = 0;
        for(int i = 0; i < strlen(s); i ++){
            if(isdigit(s[i]) || s[i] == '-'){
                num[size] = s[i];
                size++;
            }
            if(s[i] == ' ' || i == strlen(s) - 1){
                num[size] = '\0';
                if(strcmp(name_command, "add") == 0)
                    res += atoi(num);
                else if(strcmp(name_command, "mul") == 0)
                    res *= atoi(num);
                
                
                size = 0;
            }
        }
    }
    fclose(f);
    
    return res;

}
int listDir(char* startDir, char* name_command){
    int result = 0;
        if(strcmp(name_command, "mul") == 0)
        result = 1;
    char next[200] = {0};
    strcpy(next, startDir);
    DIR *dir = opendir(startDir);
    if(!dir)
        return 0;

    struct dirent *de = readdir(dir);

    while(de){

        if(IF_dir)
        {
            int len = strlen(next);
            strcat(next, "/");
            strcat(next, de->d_name);
            if(name_command != NULL && strcmp(name_command, "add") == 0)
                result += listDir(next, de->d_name);
            else if(name_command != NULL && strcmp(name_command, "mul") == 0)
                result *= listDir(next, de->d_name);
            else
                result = listDir(next, de->d_name);
            next[len] = '\0';  
        }
        if(de->d_type == DT_REG){
            int len = strlen(next);
            strcat(next, "/");
            strcat(next, de->d_name);
            if(name_command != NULL && strcmp(name_command, "add") == 0)
                result += readFile(next, name_command);
            else if(name_command != NULL && strcmp(name_command, "mul") == 0)
                result *= readFile(next, name_command);
            next[len] = '\0';  
        }
        de = readdir(dir);
    }
    closedir(dir);
    return result;
}



int main(){

    printf("%d\n",listDir("..\\..\\root", NULL));

    return 0;
}
