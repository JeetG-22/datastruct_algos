package linkedlist;

public class LinkedList<T> {
	private class Node {
		T data;
		Node next;

	}

	Node head;

	public LinkedList() {
		head = null;
	}

	public boolean isEmpty() {
		return head == null;
	}

	public void add(T data) {
		if (head == null) {
			head = new Node();
			head.data = data;
			return;
		}

		Node temp = head;
		while (temp != null) {
			temp = temp.next;
		}

		temp = new Node();
		temp.data = data;

	}

	public T remove() {
		if (head == null) {
			return null;
		}
		T data = head.data;
		head = head.next;
		return data;
	}

	public String toString() {
		String list = "";
		for (Node temp = head; temp != null; temp = temp.next) {
			if (temp.next != null) {
				list += temp.data + " --> ";
			}
		}
		return list;
	}

	public static void main(String[] args) {
		LinkedList<String> linkedlist = new LinkedList<String>();
		linkedlist.add("test1");
		linkedlist.add("test2");
		linkedlist.add("test3");
		System.out.println(linkedlist);
	}
}
