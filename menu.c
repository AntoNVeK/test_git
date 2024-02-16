#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>




int count(char* str){

    int count_space = 0;

    int flag = 1;

    for(int i = 0;i < strlen(str);i++){

        if(str[i] == ' ' && flag){

            count_space ++;

            flag = 0;

        }

        else if(str[i] != ' ')

            flag = 1;

    }

    char** text = malloc((count_space + 1) * sizeof(char*));

    



    char* word = NULL;

    int idx = 0;

    int number = 0;

    for(int i = 0; i < strlen(str);i++){

        

        if(str[i] != ' '){

            word = realloc(word, sizeof(char) * (++idx));

            word[idx - 1] = str[i];

            

        }



        if((str[i] == ' ' && i > 0) || i == strlen(str) - 1){

            word = realloc(word, sizeof(char) * ((++idx) ));

 

            word[idx - 1] = '\0';



            



            text[number] = malloc((strlen(word) + 1) * sizeof(char));

            for(int k = 0; k < strlen(word); k++){

                text[number][k] = word[k];

            }   

             text[number][strlen(word)] = '\0';

             number++;

             

             

             idx = 0;           

        }



    }



    int Max = 1;

    for(int j = 0; j < number - 1; j++){

        int tek_count = 1;

        for(int k = j + 1; k < number; k++){

            if(strcmp(text[j],text[k]) == 0){

                tek_count++;

                if(tek_count > Max)

                    Max = tek_count;



            }

        }



    }
    free(word);
    for(int i = 0; i < number;i ++){
        free(text[i]);
    }
    free(text);


    return Max;

}





int main(){

    char s[201];

    fgets(s, 201, stdin);

    s[strcspn(s, "\n")] = 0;



    int c = count(s);

    printf("%d", c);

    return 0;

}
