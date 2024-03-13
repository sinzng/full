#include <stdio.h>
#include "libcheckeod.h"

int main() {
	while(1){
	int x; 
	printf("input number: ");
	scanf("%d", &x);
	if(x==0){
		printf("Program exit~~\n");
		break;}
	else
		if(checkeod(x)==0){
			printf("%d is even\n",x);
		}
		else
			printf("%d is odd\n",x);
	}
	return 0;
}

