#include <vector>
using namespace std;

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
