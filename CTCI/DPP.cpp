/*


a child is running up a staircase with n steps and 
can hop either 1 step, 2 steps or 3 steps at a time.
 Implement a method to count how many possible ways the child can run up the stairs .

ex. ) n = 5

ways =



# Grid is the number of paths! 
# initialize grid to 1's
*/



int num_paths(int n)
{
    
    vector <int> ways =   {0, 1, 2}
    for (int i = 3; i < n ; ++n )
    {
        ways.emplace_back(n[i-1] + n[i -2]);
    } 

    return ways[n-1];
}




