public class CreditAccount extends AbstractAccount{

    public CreditAccount(double balance) {
        super(balance);
    }
    @Override
    public void take(double amount){
        super.take(amount);
        super.take(amount / 100);
    }
}
