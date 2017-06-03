#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
/*
Assumes all distinct sorted values
bool MagicIndex( const vector<int> &A)
{
    int m;
    int l = 0;
    int h = A.size() -1;
     
    bool Found = false;
    
    while (l <= h && !Found)
    {
        m = (l + h ) /2;
        if (A[m] == m)
        {
             Found = true;
        }   
        else if (A[m]  > m)
        {
            h = m -1;
        }
        else
        {
            l = m + 1;
        }
            
    }
    
    return Found;   
}

*/


// non distinct recursive
bool MagicIndex(const vector<int> &T, int l, int h)
{
    
    if (l <= h )
    {
    int mid = (l + h )/ 2;
    if ( mid == T[mid])
        return true;
    
    return MagicIndex(T, max(mid+1, T[mid]) , h) || MagicIndex(T, l, min(mid-1, T[mid]) );
    }
    else
    {
        return false;
    }
    
}



bool MagicIndex(const vector<int> &T)
{
    return MagicIndex(T, 0, (int)(T.size() -1)  );
}









int main()
{
  int t;
  vector<int> nums;
  cin >>t;
  int k;
  for (int i = 0; i < t; ++i)
  {
      cin >> k;
      nums.emplace_back(k);

  }
  string val=  MagicIndex(nums) ? "Yes": "No";
  cout <<val <<endl;



}