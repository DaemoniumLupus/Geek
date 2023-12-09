package Lesson2;

class Expr3 {

    public static double expr3(int a, int b) {
        // Введите свое решение ниже
        double res;
        try {
            res = a / b;
            res = (double)a / b;
        } catch (Exception e) {
            
            res = 0;
        }
        printSum(a, b);
        return res;

}

    public static void printSum(int a, int b) {
        // Введите свое решение ниже
        System.out.println( a + b);
    }
}

// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки

public class print3 {
    public static void main(String[] args) {
        int a;
        int b;

        if (args.length == 0) {
            a = 12;
            b = 0; // Default values if no arguments are provided
        } else {
            a = Integer.parseInt(args[0]);
            b = Integer.parseInt(args[1]);
        } 

        double result = Expr3.expr3(a, b);
        System.out.println(result);
    }
}
