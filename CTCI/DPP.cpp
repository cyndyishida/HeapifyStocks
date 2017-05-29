/*


a child is running up a staircase with n steps and 
can hop either 1 step, 2 steps or 3 steps at a time.
 Implement a method to count how many possible ways the child can run up the stairs .

ex. ) n = 5

ways =



# Grid is the number of paths! 
# initialize grid to 1's
*/



#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


struct Node {
      int data;
      Node* left;
      Node* right;
   };

bool checkBST(Node* root) 
{

      bool is_BST = true ;
      Node* current; 
    
    
      queue<Node*> bfs;
      bfs.push(root);

      while(!(bfs.empty() ) && is_BST)
      {
          current = bfs.front();
          bfs.pop();          
          if (current->left)
          {
              if ( current->left->data <  current->data )
              {  
                  bfs.push(current->left);
              }
              else
              { 
                  is_BST = false; 
              }
 
          }
          
          if (current->right)
          {
              if ( current->right->data  > current->data ) 
              {
                  bfs.push(current->right );
              }
              else
              {
                  is_BST = false; 
              }
              
          }
      }
       
     
      return is_BST;      
}







string is_prime(int n)
{
    
int len = n > 10? ceil(sqrt(n)): n ;
    

    double shorter = sqrt(n);
    
        
    for(int i = 2; i < ceil(shorter) ; ++i)
        if (!(n % i) )
          return "Not prime";
    
    return n == 1 ||  abs( shorter - ceil(shorter) ) < 0.001   ? "Not prime": "Prime";
    
}


int main(){
    int p,n;
    cin >> p;
    for(int a0 = 0; a0 < p; a0++){
        cin >> n;
        cout << is_prime(n) << endl;
        cout << n % (int)sqrt(n) << endl;
    }   
    return 0;
}
