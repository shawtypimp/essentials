package task;

public class DoubleLinkedListItem<T extends Comparable<T>> {

    private DoubleLinkedListItem<T> head;
    private DoubleLinkedListItem<T> tail;
    private T data;

    public DoubleLinkedListItem(T data){
        head = tail = null;
        this.data = data;
    }

    public DoubleLinkedListItem<T> getNext(){
        this.tail = tail;
        return tail;
    }
    public DoubleLinkedListItem<T> getPrev(){
        this.head = head;
        return head;
    }

    public T getData(){
        return  data;
    }

    public void setNext(DoubleLinkedListItem<T> newTail){
        this.tail = newTail;
    }

    public void setPrev(DoubleLinkedListItem<T> newHead){
        this.head = newHead;
    }

    public void setData(T newData){
        this.data =  newData;
    }
}
