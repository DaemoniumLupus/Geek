Console.Clear();
Console.Write("Введите первое целое число-");
string input_1 = Console.ReadLine() ?? "";
Console.Write("Введите второе целое число-");
string input_2 = Console.ReadLine() ?? "";

int numIn_1 = int.Parse(input_1);
int numIn_2 = int.Parse(input_2);
int result = numIn_1 * numIn_1;

if (result == numIn_2){
  Console.Write("Yes");
}else{
  Console.WriteLine("No");
}