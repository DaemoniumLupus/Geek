Console.Clear();
Console.Write("Enter number: ");
int a;
a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(a * a);

Console.WriteLine($"{a} -> {a * a}");


/*
Console.Clear();
Console.Write("Enter number: ");
string userInput = Console.ReadLine() ?? "";
int userNum = int.Parse(userInput);
Console.WriteLine(userNum);
*/
