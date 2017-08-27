#include <iostream>
#include "Heap.h"

using namespace std;

int main()
{
   
    CHeap<int> max;
    max.push(7);
    max.push(10);

    max.display();
    return 0;
}