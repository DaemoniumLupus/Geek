package Lesson2;
class IsFloat {
    public static float isFloat(String input) {
        // Введите свое решение ниже 
        float res;  
        try {
            res = Float.parseFloat(input);
            
        } catch (Exception e) {
            res =  Float.NaN;
        }
        return res;


    }
}

// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки
public class print1 {
    public static void main(String[] args) {
        String input;

// При отправке кода на Выполнение, вы можете варьировать эти параметры
        if (args.length == 0) {
            input = "one"; // По умолчанию используем "3.14", если аргумент не передан
        } 
        else {
            input = args[0];
        }

        float result = IsFloat.isFloat(input);
        System.out.println(result);
    }
}