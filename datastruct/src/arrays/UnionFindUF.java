package arrays;

/*
 * Desc:
 * connects elements together in a component using ids
 * Defect: way too slow when it comes to union as ids of all of one component much be changed when combined with another component
 */

public class UnionFindUF {
    private int id[];

    public UnionFindUF(int n){
        id = new int[n];
        for(int i = 0; i < n; i++){
            id[i] = i;
        }
    }

    //O(1) just needs to check if the ids are the same
    public boolean connected(int p, int q){
        return id[p] == id[q];
    }

    //has to change the id of each index when connected to another component
    public void union(int p, int q){
        int pid = id[p];
        int qid = id[q];
        for(int i = 0; i < id.length; i++){
            if(id[i] == pid) id[i] = qid;
        }
    }
}
