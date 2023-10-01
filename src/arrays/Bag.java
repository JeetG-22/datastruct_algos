package arrays;

import java.util.ArrayList;
import java.util.Iterator;


public class Bag<T> implements Iterable<T>{
    private ArrayList<T> bag;

    public Bag(){
        bag = new ArrayList<T>();
    }

    public void add(T item){
        bag.add(item);
    }

    public int size(){
        return bag.size();
    }

    public boolean isEmpty(){
        return bag.isEmpty();
    }

    @Override
    public Iterator<T> iterator() {
        return bag.iterator();
    }
}