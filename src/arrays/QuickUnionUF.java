package arrays;

/*
 * Desc:
 * Uses trees to connect elements in the list  (attempts to be quicker in terms of combining 2 disjoint sets)
 * Defect: trees can get too tall causing a runtime of n when trying to find the root in worst case
 */
public class QuickUnionUF {
    private int parent[];

    public QuickUnionUF(int n){
        parent = new int[n];
        for(int i = 0; i < n; i++){
            parent[i] = i;
        }
    }

    //continually go up the tree until you find the root (parent[i] = i)
    private int root(int i){
        while(parent[i] != i) i = parent[i];
        return i;
    }

    //connected if the roots are the same
    public boolean connected(int p, int q){
        return root(p) == root(q);
    }

    //connect the root of the first value to the root of the second value
    public void union(int p, int q){
        int proot = root(p);
        int qroot = root(q);
        parent[proot] = qroot;
    }


}
