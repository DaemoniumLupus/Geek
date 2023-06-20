# C#

* dotnet new console - создать новый проект
* dotnet run - запустить проект

## Команды
---
* `Console.WriteLine("Hello, World!");` - вывод строки в консоль с переходом на новую строку
* `Console.Write("Hello, World!");` - Вывод без перехода на новою строку
* `Console.ReadLine() ?? "";` - ввод из консоли
* `new Random().Next(min,max)` - даст случайное число от min до max-1
* переменная `.ToLower` - делает все буквы маленькими
* `Console.Clear();` - очистка консоли
* `Console.SetCursorPosition(10, 4);` - установка курсора (столбец, строка)
* `Convert.ToInt32(Console.ReadLine())` - Ввод числа
* `Console.WriteLine($"{a} -> {a * a}");` - a - переменная, все остальное выведется как есть
```csharp
try
{

}
catch (Exception exc)
{
  Console.WriteLine($"Ошибка ввода данных{exc.Message}");
  return;
}
```
`out int userNumber`  - определение переменной внутри параметра