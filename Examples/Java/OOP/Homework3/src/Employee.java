public class Employee implements Comparable<Employee>{
    private String name;
    private Integer age;
    private String departament;
    private Integer salary;

    public Employee(String name,int age, String departament,int salary){
        this.name = name;
        this.age = age;
        this.departament = departament;
        this.salary = salary;
    }

    public int compareTo(Employee item){
        return this.age.compareTo(item.age);
    }

    public String write(){
        return String.format("name: %s, age: %d, departament: %s, salary: %d", this.name,this.age,this.departament,this.salary);
    }

    public Integer getAge() {
        return age;
    }
    public String getDepartament() {
        return departament;
    }
    public String getName() {
        return name;
    }
    public Integer getSalary() {
        return salary;
    }
}
