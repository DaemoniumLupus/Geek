package HomeWork1.src;

public class Account {
    protected double balance = 0;



    public double put(double num){
        if (num > 0){
            balance += num;
            return balance;
        }else {
            System.err.println("Only positive numbers!");
            return balance;
        }
    }

    public double take(double num){
        if (num > 0){
            balance -= num;
            return balance;
        }else {
            System.err.println("Only positive numbers!");
            return balance;
        }
    }

    public double getAmount(){
        return balance;
    }



}
