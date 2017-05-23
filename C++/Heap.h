#include <vector>

#ifndef HEAP_HEAP_H
#define HEAP_HEAP_H



template <typename T> 
class CHeap {

public:

    void push(T);
    void pop();

    void percolate_up();
    void percolate_down();

    void display();

private:

    std::vector<T> mData;
    uintmax_t mCount;
};




template <typename T>
void CHeap::push(const T &element)
{
    mData.emplace(element);
    ++mCount;
    percolate_up(); 

}

template <typename T>
void CHeap::percolate_up()
{
    auto i = mCount;
    bool swapping = true;

    while (i /2 != 0  && swaping)
    {
        if (mList[i] > mList[i/2] )
        {
            swap(mList[i/2] , mList[i]);
            i /=2;
        }
        else
        {
            swapping = false;
        }
    }


}


#endif //HEAP_HEAP_H