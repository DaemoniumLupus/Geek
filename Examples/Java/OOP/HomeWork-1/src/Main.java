public class Main {
    public static void main(String[] args) throws Exception {
        Account acc = new Account();
        acc.put(255);
        acc.take(55);
        System.out.println(acc.getAmount());
        
        CreditAccount creditAccount = new CreditAccount();
        creditAccount.put(255);
        creditAccount.take(55);
        System.out.println(creditAccount.getAmount());

        DepositAccount depositAccount = new DepositAccount();
        depositAccount.put(255);
        depositAccount.take(55);
        System.out.println(depositAccount.getAmount());
        depositAccount.take(100);
        System.out.println(depositAccount.getAmount());

    }
}
