public class FixedAmountAccount extends AbstractAccount{

    public FixedAmountAccount(double balance) {
        super(balance);
    }

    @Override
    public void put(double amount){
            System.out.println("Вы не можете изменить баланс");
    }
    
    @Override
    public void take(double amount){
        System.out.println("Вы не можете изменить баланс");
    }
}
