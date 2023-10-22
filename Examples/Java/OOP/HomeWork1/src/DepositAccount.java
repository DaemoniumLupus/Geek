
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class DepositAccount extends Account{

    private LocalDate lastTakeOperation = LocalDate.of(2000, 1, 1);
    
    @Override
    public void take(int num){
        LocalDate now = LocalDate.now();
        if(lastTakeOperation.isBefore(now.minus(1, ChronoUnit.MONTHS))){
            lastTakeOperation = LocalDate.now();
            super.take(num);
        }else{ 
            System.out.println("A month has not passed since the last withdrawal");
        }
    }
}
