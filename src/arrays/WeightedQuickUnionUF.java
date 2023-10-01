package arrays;

/*
 * Desc:
 * Better implementation of QuickUnion because it prioritizes the smaller trees connected to the bigger trees
 * TC for finding root = log(n)
 * TC for union = log(n) [the time it takes to find the roots]
 */

public class WeightedQuickUnionUF {
    private int id[], size[];

    public WeightedQuickUnionUF(int n) {
        id = new int[n];
        size = new int[n];
        for(int i = 0; i < n; i++){
            id[i] = i;
            size[i] = 1;
        } 
    }

    //finding the root of each node
    private int root(int p){
        while(id[p] != p){
            p = id[p];
        }
        return p;
    }

    //uses a second size arr to make sure that the smaller tree always get connected to the bigger tree (updates size arr)
    public void union(int p, int q){
        int pRoot = root(p);
        int qRoot = root(q);

        if(pRoot == qRoot) return; //will effect tree size if not used  

        if(size[p] > size[q]){
            id[qRoot] = pRoot;
            size[pRoot] += size[qRoot];
        } else {
            id[pRoot] = qRoot;
            size[qRoot] += size[pRoot];
        }
    }

    public boolean connected(int p, int q){
        return root(p) == root(q);
    }
}
