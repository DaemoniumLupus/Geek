
public class CreditAccount extends Account{

    @Override
    public void take(int num){
        if (num > 0){
            balance -= num;
            balance -= num * 0.01;
            
        }else {
            System.err.println("Only positive numbers!");
        }
    }
}
