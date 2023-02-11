import java.util.HashMap;
import java.util.Scanner;

public class SummCalculator {

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Введите количество разных единиц товара");
        int totalCount = input.nextInt();
        System.out.println("Общая сумма покупки равна " + calculateSumm(totalCount));
    }
    public static int calculateSumm(int totalCount)
    {
        HashMap<String, Integer> namesAndCount = new HashMap<>();
        HashMap<String, Integer> namesAndPrice = new HashMap<>();
        namesAndCount.put("Дыня", 78);
        namesAndCount.put("Клубника", 234);
        namesAndCount.put("Гранат", 90);
        namesAndCount.put("Арбуз", 124);

        namesAndPrice.put("Клубника", 7);
        namesAndPrice.put("Дыня", 4);
        namesAndPrice.put("Гранат", 18);
        namesAndPrice.put("Арбуз", 9);

        int totalSum = 0;
        for (int i = 0; i != totalCount; i++)
        {
            Scanner input = new Scanner(System.in);
            System.out.println("Введи название товара");
            String thingName = input.nextLine();
            System.out.println("Введи количество");
            int thingCount = input.nextInt();
            while(thingCount > namesAndCount.get(thingName))
            {
                System.out.println("В данный момент в магазине всего " + namesAndCount.get(thingName) + " единиц " + thingName);
                System.out.println("Попробуйте взять меньше.");
                thingCount = input.nextInt();
            }
            System.out.println("Сумма данной покупки равна:" + (thingCount * namesAndPrice.get(thingName)));
            totalSum += thingCount * namesAndPrice.get(thingName);
        }
        return(totalSum);
    }
}