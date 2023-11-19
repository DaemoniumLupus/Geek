
package HomeWork1.src;


public class CreditAccount extends Account{

    @Override
    public double take(double num){
        if (num > 0){
            balance -= num;
            balance -= num * 0.01;
            return balance;
            
        }else {
            System.err.println("Only positive numbers!");
            return balance;
            
        }
    }

    
}
