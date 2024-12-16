package linkedlist;

public class Queue_LL<T>{
    private class Node {
        T item;
        Node next;
    }

    Node first, last;

    public Queue_LL(){
        first = null;
        last = null;
    }

    public void enqueue(T item){
        Node oldLast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        
        if(isEmpty()){ //if there is one element the first node should point to the last node
            first = last;
        } else {
            oldLast.next = last;
        }


    }

    public T dequeue(){
        T item = first.item;
        first = first.next;
        return item;
    }

    public boolean isEmpty(){
        return first == null;
    }
    public static void main(String[] args) {
        
    }
}