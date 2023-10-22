// {@link }

public class App {
    public static void main(String[] args) throws Exception {
       BaseAccount account = new BaseAccount(100);
       account.take(10);
       account.put(200);
       double summ = account.getAmount();
       System.out.println(summ);

       FixedAmountAccount accFix = new FixedAmountAccount(100);
       accFix.take(10);
       accFix.put(200);
       double summFix = accFix.getAmount();
       System.out.println(summFix);
    }
}
