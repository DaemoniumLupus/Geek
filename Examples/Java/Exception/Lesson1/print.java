package Lesson1;
class Answer2 {
    public void arrayOutOfBoundsException() {
        // Напишите свое решение ниже
      int[] res = new int[1];
      System.out.println(res[5]);
}

    public void divisionByZero() {
        // Напишите свое решение ниже
      int a = 5;
      a = a / 0;
      
}

    public void numberFormatException() {
        // Напишите свое решение ниже
       Integer.parseInt("surprise");
 }
}

public class print {
    public static void main(String[] args) {
        Answer2 ans = new Answer2();
        try {
            ans.arrayOutOfBoundsException();
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Выход за пределы массива");
        }

        try {
            ans.divisionByZero();
        } catch (ArithmeticException e) {
            System.out.println("Деление на ноль");
        }

        try {
            ans.numberFormatException();
        } catch (NumberFormatException e) {
            System.out.println("Ошибка преобразования строки в число");
        }
    }
}