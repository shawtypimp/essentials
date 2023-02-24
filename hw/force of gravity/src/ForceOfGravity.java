import java.util.Scanner;

public class ForceOfGravity {
    public static void main(String[] args) {
        System.out.println("Choose a planet by inputting a number from 1 to 8 (all planets spread out in increase order )");
        Scanner scan = new Scanner(System.in);
        int number = scan.nextInt();

        double m1 = 5.97600 * Math.pow(10, 24);
        double g = 6.674 * Math.pow(10, -11);
        double r = 0;
        double m2 = 0;
        double F = g * m1 * m2 / r * r;

        switch (number) {
            case 1:
                double v = m2 = 0.07350 * Math.pow(10, 24); // Луна
                double n = r = 3.84 * Math.pow(10, 8);
                break;
            case 2:
                double v1 = m2 = 0.32868 * Math.pow(10, 24); // Меркурий
                double n1 = r = 57.91 * Math.pow(10, 9);
                break;
            case 3:
                double v2 = m2 = 0.63345 * Math.pow(10, 24); // Марс
                double n2 = r = 227.94 * Math.pow(10, 9);
                break;
            case 4:
                double v3 = m2 = 4.81068 * Math.pow(10, 24); // Венера
                double n3 = r = 108.20 * Math.pow(10, 9);
                break;
            case 5:
                double v4 = m2 = 86.05440 * Math.pow(10, 24); // Уран
                double n4 = r = 2870.99 * Math.pow(10, 9);
                break;
            case 6:
                double v5 = m2 = 101.59200 * Math.pow(10, 24); // Нептун
                double n5 = r = 4497.07 * Math.pow(10, 9);
                break;
            case 7:
                double v6 = m2 = 561.80376 * Math.pow(10, 24); // Сатурн
                double n6 = r = 1426.98 * Math.pow(10, 9);
                break;
            case 8:
                double v7 = m2 = 1876.64328 * Math.pow(10, 24); // Юпитер
                double n7 = r = 778.33 * Math.pow(10, 9);
                break;
            default:
                System.out.println("Your number incorrect!");
        }
        System.out.println(F);
    }
}
