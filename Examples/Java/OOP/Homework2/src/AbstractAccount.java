public abstract class AbstractAccount implements Account{

    private double balance;

    public AbstractAccount(double balance){
        this.balance = balance;
    }

    private void doTake(double amount){
        this.balance -= amount;
    }

    private void doPut(double amount){
        this.balance += amount;
    }

    public void take(double amount){
        if (amount > 0){
            doTake(amount);
        }else{
            throw new IllegalArgumentException("Сумма снятия должна быть положительной");
        }
    }

    public void put (double amount){
        if (amount > 0){
            doPut(amount);
        }else{
            throw new IllegalArgumentException("Сумма пополнения должна быть положительной");
        }
    }

    public final double getAmount(){
        return this.balance;
    }
}
