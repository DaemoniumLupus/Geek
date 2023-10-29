import java.util.Comparator;

public class ComparatorEmployeeDepartament implements Comparator<Employee>{
    public int compare(Employee a, Employee b){
        return a.getDepartament().compareTo(b.getDepartament());
    }
}

class ComparatorEmployeeSalary implements Comparator<Employee>{
    public int compare(Employee a, Employee b){
        return a.getSalary().compareTo(b.getSalary());
    }
    
}
