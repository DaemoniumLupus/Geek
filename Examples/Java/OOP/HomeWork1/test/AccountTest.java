package HomeWork1.test;


import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

import HomeWork1.src.Account;
import HomeWork1.src.CreditAccount;
import HomeWork1.src.DepositAccount;

public class AccountTest {
   
    @Test
    void testAccountPut(){
        Account account = new Account();
        assertEquals(500, account.put(500));
    }
    @Test
    void testAccountTake(){
        Account account = new Account();
        account.put(500);
        assertEquals(450, account.take(50));
    }


    @Test
    void testCreditTake(){
        CreditAccount creditAccount = new CreditAccount();
        creditAccount.put(255);
        assertEquals((double)199.45, creditAccount.take(55));
    }

    @Test
    void testCreditTake2(){
        CreditAccount creditAccount = new CreditAccount();
        creditAccount.put(255.5);
        assertEquals((double)199.95, creditAccount.take(55));
    }

    @Test
    void testDepositAccount(){
        DepositAccount depositAccount = new DepositAccount();
        depositAccount.put(500);
        assertEquals(450, depositAccount.take(50));
        assertEquals(-1, depositAccount.take(50));
    }
}
