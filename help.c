#include<stdio.h>

int main(){
    int num, i, j, sum = 0;
    printf("Enter number: ");
    scanf("%d", &num);

    for(int i = 1; i <= num; i++){
        // you have to do this because you want it to add numbers on every line
        // so for first line it is sum += 1. so sum is 1
        // next line you want sum to be 1 + 2 = 3. for that sum has to be zero
        // so sum has to be zero in every loop
        sum = 0; 
        for(j = 1; j <= i; ++j){
            printf("%d ", j);
            sum += j;
             // you don't want to print the last +
             // so you check if you have reached the end on each line
             // first line i = 1
             // so now when j = 1, it is not less than 1
             // + is not printed
             // if i = 2 and j will print + till j is less than 2
             // as soon as it is 2...+ is not printed
            if( j < i){
                printf("+ ");
            }
            
        }
        printf(" = %d", sum);
        printf("\n");
    }
    return 0;
}