#include <vector>
#include <cmath>
#include <iostream>
#ifndef HEAP_HEAP_H
#define HEAP_HEAP_H


using namespace std;


template <typename T> 
class CHeap 
{

public:
    CHeap();
    void push(const T &element );
    //void pop();

    void percolate_up();
    //void percolate_down();

    void display();

private:

    std::vector<T> mData;
    uintmax_t mCount;
};


template <typename T>
CHeap<T>::CHeap()
{
    mCount = 0;
    mData = {NULL};
}

template <typename T>
void CHeap<T>::push(const T &element)
{
     mData.emplace_back(element);
     cout << "element pushed: " <<  mData.back() << endl;
     ++mCount;
     percolate_up(); 
    
     

}

template <typename T>
void CHeap<T>::percolate_up()
{
    auto i = mCount;
    bool swapping = true;

    while (i /2 != 0  && swapping)
    {
        if (mData[i] > mData[i/2] )
        {
            swap(mData[i/2] , mData[i]);
            i /=2;
        }
        else
        {
            // first point where the parent is greater we no longer need to recurse down tree 
            swapping = false;
        }
    }


}


template <typename T>
void CHeap<T>::display()
{
    cout <<"Heap contains: " << mCount << " nodes.\n";
    long height = ceil(log2(mCount));
    long i = 0;
    long max_len = pow(2, height) * 2;
    int wid, max_width;

    for (int k = 0; k <= height; ++k)
    {
        max_width = pow(2,k);
        for (int n= 0; n< max_width ; ++n  )
        {
                if (i <= mCount)
                    cout << mData[++i] << " ";
        }
        cout << "\n";
    }



    for( auto el : mData)
        cout << el << endl;
}


#endif //HEAP_HEAP_H