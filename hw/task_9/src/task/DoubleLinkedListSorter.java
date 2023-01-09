package task;
public class DoubleLinkedListSorter {
    public static <T extends Comparable<T>> void sort(DoubleLinkedList<T> list) {
        for (int sortedListSize = 0; sortedListSize <= list.getSize(); sortedListSize++ ) {
            DoubleLinkedListItem<T> element = list.getFirst();
            int i = 0;
            while (i < list.getSize() - sortedListSize - 1){
                if (element.getData().compareTo(element.getNext().getData()) > 0) {
                    T newData = element.getData();
                    element.setData(element.getNext().getData());
                    element.getNext().setData(newData);
                }
                element = element.getNext();
                i++;
            }
        }
    }
}
