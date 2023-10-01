class Answer {
    public void printPrimeNums(){
        // Напишите свое решение ниже
        int n = 1;
        while (n < 1000) {
            int i = 2;
            int j = 0;
            while (i * i <= n && j!= 1){
                if(n % i == 0){
                    j = 1;
                }
                i++;
                
            }
            if (j != 1){
                System.out.println(n);
            }
            n++;
        }
    }
}

// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки
public class Task_2{ 
    public static void main(String[] args) { 
      
      Answer ans = new Answer();      
      ans.printPrimeNums();
    }
}