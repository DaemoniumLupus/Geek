package Lesson3;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        while (true){
            Parse data;
            String buf = in.nextLine();
            try {
                data = new Parse(buf);
            } catch (Exception e) {
                in.close();
                throw new Exception(e.getMessage());
            }
            Data.Write(data);
            
        }
    }
}
