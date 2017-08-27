#include <iostream>
using namespace std;


int mul(int sum, int val, int rept)
{
    if (rept == 0)
        return sum;
    return mul(sum +val, val , rept -1);
}




int multiply(int val, int rept)
{
    int end = mul(0, abs(val) , abs(rept) );
    return (val < 0 && rept < 0) ?  end : end;
}

int main()
{
    int val, rept;
    cin >> val >> rept;

    cout << multiply(val, rept) << endl;


    return 0;
}