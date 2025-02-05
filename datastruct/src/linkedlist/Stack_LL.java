package linkedlist;

public class Stack_LL<T> {

    private class Node {
        T item;
        Node next;
    }

    Node first;

    public Stack_LL(){
        first = null;
    }

    public boolean isEmpty(){
        return first == null;
    }

    public void push(T item){

        Node newNode = new Node();
        newNode.item = item;

        //first 
        if(isEmpty()){
            first = newNode;
        } else {
            Node temp = first;
            first = newNode;
            first.next = temp;
        }
    }

    public T pop(){
        if(isEmpty()){
            return null;
        } else {
            T item = first.item;
            first = first.next;
            return item;
        }
    }




}


