import java.util.Comparator;
import java.util.Random;
import java.util.Set;
import java.util.TreeSet;


public class App {
    public static void main(String[] args) throws Exception {
        Comparator<Employee> ecomp = new ComparatorEmployeeDepartament()
                            .thenComparing(new ComparatorEmployeeSalary());
        Set <Employee> employees = new TreeSet<Employee>();
        Set <Employee> comparatorEmployees = new TreeSet<Employee>(ecomp);
        Random r = new Random();
        String[] names = {"Vova","Sasha","Max","Ilya","Kirill","Pasha","Petr","Elena"};
        int maxNames = 8;
        String[] departamets = {"IT","Administration","Office","Create"};
        int maxDep = 4;
        
        int agePerson = 18;
        for (int i = 0;i < 20; i++){
            employees.add(new Employee(names[r.nextInt(maxNames)], agePerson, departamets[r.nextInt(maxDep)], 20000 + r.nextInt(50000)));
            //При сортировке удаляет обьекты с одинаковым значением возраста
            comparatorEmployees.add(new Employee(names[r.nextInt(maxNames)], 18 + r.nextInt(20), departamets[r.nextInt(maxDep)], 20000 + r.nextInt(50000)));
            agePerson++;
        }
        
        // employees.add(new Employee("Vova", 25, "Administration", 25000));
        // employees.add(new Employee("Kirill", 22, "IT", 30000));
        // employees.add(new Employee("Ilya", 24, "IT", 32000));        
        // employees.add(new Employee("A", 18, "A", 18000));
        // employees.add(new Employee("B", 18, "B", 33000));
        // employees.add
        
        
        for (Employee person : employees){
            System.out.println(person.write());
        }
        System.out.println();
        for (Employee person : comparatorEmployees){
            System.out.println(person.write());
        }
    
    }
}
