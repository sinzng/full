#include <stdio.h>
#include "libcheckprime.h"

void main(){
    while(1){

        int x;
        printf("\nInput integer (0:Exit) =>");
        scanf("%d", &x);

        if(x==0){
		    break;}
	    else
		    if(checkprime(x)==x){
			    printf("%d is prime number\n",x);
		        }
		else
			printf("%d is not prime number\n",x);
    
    }
}