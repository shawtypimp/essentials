package task;

public class DoubleLinkedList<T extends Comparable<T>> {

    private DoubleLinkedListItem<T> head;
    private DoubleLinkedListItem<T> tail;
    private int listSize;

    public DoubleLinkedList(){
        head = tail = null;
        listSize = 0;
    }

    public DoubleLinkedListItem<T> findFirstItem(T number){
        if (listSize == 0) return null;
        DoubleLinkedListItem<T> element = head;
        while (element != null && !element.getData().equals(number)) {
            element = element.getNext();
        }
        return element;
    }

    public DoubleLinkedListItem<T> findLastItem(T value){
    if (listSize == 0) return null;
    DoubleLinkedListItem<T> element = tail;
    while (element != null && !element.getData().equals(value)) element = element.getPrev();
        return element;
    }

    public void insertAfter(DoubleLinkedListItem<T> numberItemWeWantInsert, T data){
        if (listSize == 0){
            head = tail = new DoubleLinkedListItem<>(data);
            listSize++;
            return;
        }
        DoubleLinkedListItem<T> item = new DoubleLinkedListItem<>(data);
        if (numberItemWeWantInsert == null){
            item.setNext(head);
            head = item;
        }

        else if (numberItemWeWantInsert == tail) {
            tail.setNext(item);
            tail = item;
        }
        else {
            item.setPrev(numberItemWeWantInsert);
            item.setNext(numberItemWeWantInsert.getNext());
            numberItemWeWantInsert.getNext().setPrev(item);
            numberItemWeWantInsert.setNext(item);
        }
        listSize++;
    }

    public void insertBefore (DoubleLinkedListItem<T> numberItemWeWantInsert, T data){
        if (listSize == 0){
            head = tail = new DoubleLinkedListItem<>(data);
            listSize++;
            return;
        }
        DoubleLinkedListItem<T> item = new DoubleLinkedListItem<>(data);
        if (numberItemWeWantInsert == null){
            tail.setNext(item);
            item.setPrev(tail);
            tail = item;
        }
        else if (numberItemWeWantInsert == head) {
            item.setNext(head);
            head.setPrev(item);
            head = item;
        } else {
            item.setNext(numberItemWeWantInsert);
            item.setPrev(numberItemWeWantInsert.getPrev());
            numberItemWeWantInsert.getPrev().setNext(item);
            numberItemWeWantInsert.setPrev(item);
        }
        listSize++;
    }

    public void remove(DoubleLinkedListItem<T> itemNumberRemove) {
        if (listSize == 1){
            head = tail = null;
        }
        else if (itemNumberRemove == tail) {
            itemNumberRemove.getPrev().setNext(null);
            tail = itemNumberRemove.getPrev();
        }
        else if (itemNumberRemove == head) {
            itemNumberRemove.getNext().setPrev(null);
            head = itemNumberRemove.getNext();
        }
        else {
            itemNumberRemove.getNext().setPrev(itemNumberRemove.getPrev());
            itemNumberRemove.getPrev().setNext(itemNumberRemove.getNext());
        }
        listSize--;
    }

    public int getSize(){
        this.listSize = listSize;
        return listSize;
    }

    public DoubleLinkedListItem<T> getFirst(){
        this.head = head;
        return head;
    }

    public DoubleLinkedListItem<T> getLast(){
        this.tail = tail;
        return tail;
    }
}

