import java.util.*;

class BinaryTree{
    Node root;
    class Node{
        int value;
        Node left;
        Node right;
        boolean color;// black = 1, red = 0
    }

    public void insert(int value){
        if(null == root){
            root = new Node();
            root.value = value;
            root.color = true;
            
        }else{
            insert(root, value);
            root = Rebalance(root);
        }
        root.color = true;
    }

    private void insert(Node node, int value){
        if(node.value == value){
            
        }else{
            if(node.value < value){
                if(node.right != null){
                    insert(node.right, value);
                    node.right = Rebalance(node.right);
                }else{
                    node.right = new Node();
                    node.right.value = value;
                    node.right.color = false;     
                }
            }else{
                if(node.left != null){
                    insert(node.left, value);
                    Rebalance(node.left);
                }else{
                    node.left = new Node();
                    node.left.value = value;
                    node.left.color = false;
                }
            }
        }
    }

    private Node RotateRight(Node node){
        Node x = node.left;
        node.left = x.right;
        x.right = node;
        x.color = node.color;
        node.color = false;
        return x;
    }

    private Node RotateLeft(Node node){
        Node x = node.right;
        node.right = x.left;
        x.left = node;
        x.color = node.color;
        node.color = false;
        return x;
    }
    private void FlipColor(Node node){
        node.color = !node.color;
        node.left.color = !node.left.color;
        node.right.color = !node.right.color;
    }

    private Node Rebalance(Node node){
        
                if (null != node.left && null != node.right && !node.left.color && !node.right.color){
                    FlipColor(node);
                    return node;
                }else{
                    if (null!= node.right && !node.right.color){
                        return RotateLeft(node);
                    }else{
                        if (null != node.left && null != node.left.left && !node.left.color && !node.left.left.color){
                            return RotateRight(node); 
                        }
                    }
                }
                return node;

            
        }

        public void printTree() { // метод для вывода дерева в консоль
            Stack<Node> globalStack = new Stack<Node>(); // общий стек для значений дерева
            globalStack.push(root);
            int gaps = 32; // начальное значение расстояния между элементами
            boolean isRowEmpty = false;
            String separator = "-----------------------------------------------------------------";
            System.out.println(separator);// черта для указания начала нового дерева
            while (isRowEmpty == false) {
                Stack<Node> localStack = new Stack<Node>(); // локальный стек для задания потомков элемента
                isRowEmpty = true;

                for (int j = 0; j < gaps; j++)
                    System.out.print(' ');
                while (globalStack.isEmpty() == false) { // покуда в общем стеке есть элементы
                    Node temp = (Node) globalStack.pop(); // берем следующий, при этом удаляя его из стека
                    if (temp != null) {
                        System.out.format("%d-%s",temp.value,temp.color); // выводим его значение в консоли
                        localStack.push(temp.left); // соохраняем в локальный стек, наследники текущего элемента
                        localStack.push(temp.right);
                        if (temp.left != null ||
                                temp.right != null)
                            isRowEmpty = false;
                    }
                    else {
                        System.out.print("__");// - если элемент пустой
                        localStack.push(null);
                        localStack.push(null);
                    }
                    for (int j = 0; j < gaps * 2 - 2; j++)
                        System.out.print(' ');
                }
                System.out.println();
                gaps /= 2;// при переходе на следующий уровень расстояние между элементами каждый раз уменьшается
                while (localStack.isEmpty() == false)
                    globalStack.push(localStack.pop()); // перемещаем все элементы из локального стека в глобальный
            }
            System.out.println(separator);// подводим черту
        }
    

    public boolean find(int value){
        return find(root, value);
    }

    private boolean find(Node node, int value){
        if(node == null){
            return false;
        }
        if(node.value == value){
            return true;
        }

        if(node.value < value){
            return find(node.right, value);
        }else{
            return find(node.left, value);
        }
    }
}


public class Main {
    public static void main(String[] args) {

        BinaryTree tree = new BinaryTree();

        tree.insert(71);
        tree.insert(5);
        tree.insert(3);
        tree.insert(4);
        tree.insert(1);
        tree.insert(2);
        tree.insert(7);
        tree.insert(8);
        tree.insert(6);
        tree.insert(25);
        
        tree.printTree();// black = true, red = false
        
        // while(null != tree.root.left && null != tree.root.right)
        // System.out.println(tree.find(7));
        // System.out.println(tree.find(7));
        // System.out.println(tree.find(9));

    }
}