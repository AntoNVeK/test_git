#include <stdio.h>
#include <stdlib.h>
#include "index_first_even.h"
#include "index_last_odd.h"
#include "sum_between_even_odd.h"
#include "sum_before_even_and_after_odd.h"

#define N 100

int main()
{   

    int k=0;
    int arr[N];
    int i=0;
    char space =' ';
    scanf("%d", &k);
    while (i < N && space == ' '){
        scanf("%d%c", &arr[i], &space);
        i++;
        }




    switch(k){
        case 0:
            printf("%d\n", index_first_even(arr,i));
            break;
        case 1:
            printf("%d\n", index_last_odd(arr,i));
            break;
        case 2:
            printf("%d\n", sum_between_even_odd(arr,i));
            break;
        case 3:
            printf("%d\n", sum_before_even_and_after_odd(arr,i));
            break;
        default:
            printf("Данные некорректны");
            break;


    }

    return 0;
}