import java.util.ArrayList;
import java.util.Collections;

public class TimeController {
    public static void main(String[] args)
    {
        ArrayList<String> clubs = new ArrayList<String>();
        ArrayList<Integer> time = new ArrayList<Integer>();
        clubs.add("Бег");
        clubs.add("Теннис");
        clubs.add("Волейбол");
        clubs.add("Баскетбол");
        clubs.add("Гимнастика");

        time.add(120);
        time.add(60);
        time.add(30);
        time.add(45);
        time.add(15);

        System.out.println("Название занятия с максимальным  суммарным временем: " + (getActionWithMaxTime(clubs,time)));
    }
    public static String getActionWithMaxTime(ArrayList<String> clubs, ArrayList<Integer> time)
    {
        return clubs.get(time.indexOf(Collections.max(time)));
    }
}
