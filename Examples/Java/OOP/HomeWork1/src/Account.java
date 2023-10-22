
public class Account {
    protected double balance = 0;



    public void put(int num){
        if (num > 0){
            balance += num;
        }else {
            System.err.println("Only positive numbers!");
        }
    }

    public void take(int num){
        if (num > 0){
            balance -= num;
        }else {
            System.err.println("Only positive numbers!");
        }
    }

    public double getAmount(){
        return balance;
    }



}
