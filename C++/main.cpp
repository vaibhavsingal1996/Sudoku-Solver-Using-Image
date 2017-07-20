#include <bits/stdc++.h>

using namespace std;

struct node
{
    bool iscolumnnode;
    int sizeofcolumn;
    pair<int,int> location;
    node* columnode;
    node* right;
    node* left;
    node* up;
    node* down;
};

pair<int,int> defaultpair =  make_pair(-1,-1);

node* createnode(pair<int,int> loc= defaultpair, bool iscolumn=false, int colsize=0)
{
    node* temp;
    temp= new node;
    temp->iscolumnnode = iscolumn;
    temp->sizeofcolumn = colsize;
    temp->location = loc;
    //self-wrapping node
    temp->columnode = temp;
    temp->right = temp;
    temp->left = temp;
    temp->up = temp;
    temp->down = temp;

    return temp;
}

int m,n;
node* links[9][9];
node* columnnode[9];
node* headnode;

void makelistgrid();
vector<node*> solution;
void printsolution();
void search_vertexcover();
void cover(node*);
void uncover(node*);
node* choosenextcolumn();

int main()
{
    m=6;
    n=7;
    int matrix[m][n];

    //INPUT THE SPARSE MATRIX
    for (int i=0; i<m; i++)
        for (int j=0; j<n; j++)
            cin>>matrix[i][j];

    //MAKE AND INITIALIZE A LISTS
    for (int i=0; i<m; i++)
        for (int j=0; j<n; j++)
            if (matrix[i][j]==0)
                links[i][j]=NULL;
            else
                links[i][j]=createnode(make_pair(i,j));

    //MAKING COLUMN ROW
    for (int i=0; i<n; i++)
        columnnode[i] = createnode(make_pair(i,0),true, 0);
    for (int i=1; i<n-1; i++)
    {
        columnnode[i]->right = columnnode[i+1];
        columnnode[i]->left = columnnode[i-1];
    }
    headnode = createnode();
    headnode->right = columnnode[0];
    headnode->left = columnnode[n-1];
    columnnode[0]->left = headnode;
    columnnode[0]->right = columnnode[1];
    columnnode[n-1]->right = headnode;
    columnnode[n-1]->left = columnnode[n-2];

   // MAKE THE GRID OUT OF THE LISTS
    makelistgrid();
    solution.clear();
    search_vertexcover();
    return 0;
}

void makelistgrid()
{
    node *head, *temp;
    temp=columnnode[0];

    //ROWS
    for (int i=0; i<m; i++)
    {
        head=NULL;
        temp=NULL;
        for (int j=0; j<n; j++)
        {
            if (links[i][j]!=NULL)
            {
                if (head==NULL)
                {
                    head = links[i][j];
                    temp = links[i][j];
                }
                else
                {
                    temp->right = links[i][j];
                    links[i][j]->left = temp;
                    head->left = links[i][j];
                    links[i][j]->right = head;
                    temp = temp->right;
                }
            }
        }
    }

    //COLS
    for (int j=0; j<n; j++)
    {
        head = NULL;
        temp = NULL;
        for (int i=0; i<m; i++)
        {
            if (links[i][j]!=NULL)
            {
                if (head==NULL)
                {
                    head=links[i][j];
                    temp=links[i][j];
                    temp->up = columnnode[j];
                    temp->down = columnnode[j];
                    temp->columnode = columnnode[j];
                    columnnode[j]->down = links[i][j];
                }
                else
                {
                    temp->down = links[i][j];
                    links[i][j]->up = temp;
                    links[i][j]->down = columnnode[j];
                    links[i][j]->columnode = columnnode[j];
                    temp = temp->down;
                }
                columnnode[j]->sizeofcolumn += 1;
            }
        }
        if (temp!=NULL)
                columnnode[j]->up = temp;
    }
}

void printsolution()
{
    cout<<"VERTEX COVER IS AS FOLLOW: \n";
    vector<node*>::iterator it;
    node *row, *temp;
    for (it = solution.begin(); it!=solution.end(); it++)
    {
        row = *it;
        temp = row;
        do
        {
            cout<<temp->location.first<<" "<<temp->location.second<<" || ";
            temp = temp->right;
        }
        while (temp != row);
        cout<<"\n";
    }
}

void search_vertexcover()
{
    if (headnode->right==headnode)
    {
        printsolution();
        return;
    }
    node* column = choosenextcolumn();
    cout<<column->location.first<<" "<<column->location.second<<"\n";
    cover(column);

    for (node* row = column->down; row!=column; row = row->down)
    {
        solution.push_back(row);
        for (node* rightnode = row->right; rightnode!=row; rightnode = rightnode->right)
            cover(rightnode);
        search_vertexcover();
        solution.pop_back();

        for (node* leftnode = row->left; leftnode!=row; leftnode = leftnode -> left)
            uncover(leftnode);
    }
    uncover(column);
}

node* choosenextcolumn()
{
    node* result;
    int mincount = 10;
    for (node* temp = headnode->right; temp!=headnode; temp = temp->right)
    {
        if (temp->sizeofcolumn < mincount)
        {
            mincount = temp->sizeofcolumn;
            result = temp->columnode;
        }
    }
    return result;
}

void cover(node* c)
{
    node* column = c->columnode;

    column->right->left = column->left;
    column->left->right = column->right;

    for (node* row = column->down; row!=column; row = row->down)
    {
        for (node* rightnode = row->right; rightnode!=row; rightnode = rightnode->right)
        {
            rightnode->up->down = rightnode->down;
            rightnode->down->up = rightnode->up;
        }
    }
}

void uncover(node* c)
{
    node* column = c->columnode;

    for (node* row = column->up; row!=column; row = row->up)
    {
        for (node* leftnode = row->left; leftnode!=row; leftnode = leftnode->left)
        {
            leftnode->up->down = leftnode;
            leftnode->down->up = leftnode;
        }
    }
    column->right->left = column;
    column->left->right = column;
}
