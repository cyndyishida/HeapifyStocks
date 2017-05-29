// https://www.hackerrank.com/challenges/ctci-is-binary-search-tree


bool inorder( Node * node, int &output, bool &is_BST)
{
    if (!node)
        return is_BST;
    
    inorder(node->left, output, is_BST);
    
    
    if( output == 0 || output < node->data )
    {
        output = node->data;
    }
    else
    {
        is_BST = false;
        
    }
       
    inorder(node->right, output, is_BST);
    
    return is_BST;
}


bool checkBST(Node* root) {
   
      bool is_BST = true;
      int output = 0;
    
      return inorder(root, output, is_BST);      
   }