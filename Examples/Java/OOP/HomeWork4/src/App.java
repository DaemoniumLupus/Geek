import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Iterator;

public class App {
    public static void main(String[] args) {
        Box<Apple> appleBox = new Box();
        System.out.println(appleBox.getWeight()); // 0
    
        appleBox.add(new Apple(2)); // Должно компилироваться
        appleBox.add(new Apple(4)); // Должно компилироваться
        System.out.println(appleBox.getWeight()); // 6
        // appleBox.add(new Orange(4)); // Не должно компилироваться!!!
        appleBox.add(new GoldenApple(4)); // Должно компилироваться
        System.out.println(appleBox.getWeight()); // 10
    
        Box<Orange> orangeBox = new Box();
        // orangeBox.add(new Apple(2)); // Не должно компилироваться!!!
        orangeBox.add(new Orange(8)); // Должно компилироваться
        System.out.println(orangeBox.getWeight()); // 8
    
        // orangeBox.move(appleBox); // Не должно компилироваться!!!
        // appleBox.move(orangeBox); // Не должно компилироваться!!!
    
        Box<GoldenApple> goldenAppleBox = new Box();
        goldenAppleBox.add(new GoldenApple(20)); // Должно компилироваться
        // goldenAppleBox.add(new Apple(20)); // Не должно компилироваться!!!
    
        // appleBox.move(goldenAppleBox); // Не должно компилироваться!!!
        goldenAppleBox.move(appleBox); // Должно компилироваться
    
        System.out.println(goldenAppleBox.getWeight()); // 0
        System.out.println(appleBox.getWeight()); // 30
    
        for (Apple apple: appleBox) { // Должно компилироваться
            System.out.println(apple.getWeight());
        }
    
        for (GoldenApple goldenApple: goldenAppleBox) { // Должно компилироваться
            System.out.println(goldenApple.getWeight());
        }
    
        for (Orange orange: orangeBox) { // Должно компилироваться
            System.out.println(orange.getWeight());
        }
    
      
    }


static class Box <T extends Fruit> implements Iterable<T>{

    private final List<T> fruits;
    public Box(){
        this.fruits = new ArrayList<>();

    }

    public void add(T fruit) { // FIXME Должен быть дженерик!
        // FIXME Реализовать добавления фрукта
        this.fruits.add(fruit);
        // throw new UnsupportedOperationException();
    }

    public int getWeight() {
        // FIXME Реализовать подсчет суммарного веса
        // throw new UnsupportedOperationException();
        int sum = 0;
        for (T t : this.fruits) {
            sum += t.getWeight();
        }
        return sum;
    }

    public void move(Box<? super T> another) { // FIXME Должен быть дженерик!
        // FIXME Реализовать пересыпание
        // throw new UnsupportedOperationException();
        for (T fruit : this.fruits) {
            another.add(fruit);
        }
        this.fruits.clear();
    }

    @Override
    public Iterator<T> iterator(){
        return new Iterator<T>() {
            private int index;

            @Override
            public boolean hasNext(){
                return index < fruits.size();
            }

            @Override
            public T next(){
                return fruits.get(index++);
            }
        };
        
    }
}

static class Fruit {

    private int weight;

    public Fruit(int weight) {
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }
}

static class Apple extends Fruit {
public Apple(int weight) {
    super(weight);
}
}

static class GoldenApple extends Apple {
public GoldenApple(int weight) {
    super(weight);
}
}

static class Orange extends Fruit {
    public Orange(int weight) {
        super(weight);
    }
}
}


