package Lesson2;

import java.util.Arrays;

class Expr1 {

    public static double expr1(int[] intArray, int d) {
        // Введите свое решение ниже
        double res = 0;

        try {
            int a = intArray[8];
            try {
                res = a / d;
                System.out.printf("intArray[8] / d = %s / %s = %s", a, d ,res);
                System.out.println();
            } catch (Exception e) {
                System.out.println("It's not possible to evaluate the expression - intArray[8] / d as d = 0.");
                res = Double.NaN;
            }
        } catch (Exception e) {
            System.out.println("It's not possible to evaluate the expression - intArray[8] / d as there is no 8th element in the given array.");
            res = Double.NaN;
        }
        
        return res;

//intArray[8] / d = 9 / 1 = 9.0
//It's not possible to evaluate the expression - intArray[8] / d as there is no 8th element in the given array.
    }
}

// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки

public class print2 {
    public static void main(String[] args) {
        int[] intArray;
        int d;

        if (args.length == 0) {
            intArray = new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            d = 1; // По умолчанию используем 0, если аргумент не передан
        } else {
            intArray = Arrays.stream(args[0].split(" ")).mapToInt(Integer::parseInt).toArray();
            d = Integer.parseInt(args[1]); // Можно использовать значение по умолчанию или передать его как аргумент.
        }

        double result = Expr1.expr1(intArray, d);
        System.out.println(result);
    }
}