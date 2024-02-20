#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include<ctype.h>
void printFile(char* filename, char* name_command){
    int res = 0;

   // if(strcmp(name_command, "mul") == 0)
   //     res = 1;

    FILE *f = fopen(filename, "r");

    if(!f)
        return;
    printf("filename : %s:\n", filename);
    char s[100];
    while(fgets(s,100,f)){
        printf("\t%s: ",s);
        char num[10];
        int size = 0;
        for(int i = 0; i < strlen(s); i ++){
            if(isdigit(s[i]) || s[i] == '-'){
                num[size] = s[i];
                size++;
            }
            if(s[i] == ' ' || i == strlen(s) - 1){
                num[size] = '\0';
                if(strcmp(name_command, "add") == 0){
                    res += atoi(num);
                }
                else if(strcmp(name_command, "mul") == 0){
                    res *= atoi(num);
                }
                
                size = 0;
            }
        }
    }
    fclose(f);
    printf("%d\n", res);


}
void listDir(char* startDir, char* name_command){
    char next[200] = {0};
    strcpy(next, startDir);
    DIR *dir = opendir(startDir);
    if(!dir)
        return;

    struct dirent *de = readdir(dir);

    while(de){
        if(de->d_type == DT_DIR && strcmp(de->d_name, ".")
         && strcmp(de->d_name, ".."))
            strcpy(name_command,de->d_name);
            name_command[4] = '\0';

        if(de->d_type == DT_REG)
            printf("de->d_name: %s\n", de->d_name);
        if(de->d_type == DT_DIR && strcmp(de->d_name, ".")
         && strcmp(de->d_name, ".."))
        {
            int len = strlen(next);
            strcat(next, "/");
            strcat(next, de->d_name);
            listDir(next, name_command);
            next[len] = '\0';  
        }
        if(de->d_type == DT_REG){
            int len = strlen(next);
            strcat(next, "/");
            strcat(next, de->d_name);
            printFile(next, name_command);
            next[len] = '\0';  
        }
        de = readdir(dir);
    }
    closedir(dir);

}



int main(){
    char* name_command = malloc(4 * sizeof(char));

    listDir("..\\..\\root", name_command);

    return 0;
}
