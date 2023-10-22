public class FixedAmountAccount extends AbstractAccount{

    public FixedAmountAccount(double balance) {
        super(balance);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void put(double amount){
        if (amount > 0){
            System.out.println("Вы не можете изменить баланс");
        }else{
            throw new IllegalArgumentException("Сумма пополнения должна быть положительной");
        }
    }
    
    @Override
    public void take(double amount){
        if(amount > 0){
            System.out.println("Вы не можете изменить баланс");
        }else {
            throw new IllegalArgumentException("Сумма снятия должна быть положительной");    
        }
    }
}
