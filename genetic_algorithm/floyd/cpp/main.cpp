#include <stdio.h>
#include "Population.h"

int main()
{
   int i;
   Population *pop;

   srand((unsigned int)time(NULL));

   pop = new Population();
   for(i = 1; i <= GEN_MAX; i++) {
      printf("Generation: %d\n",i);
      pop->alternate();
   }
   pop->printResult();
   delete pop;

   return 0;
}
