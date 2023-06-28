

double b1 = GetNumberFromUser("Введите b1: ", "Ошибка ввода!");
double k1 = GetNumberFromUser("Введите k1: ", "Ошибка ввода!");
double b2 = GetNumberFromUser("Введите b2: ", "Ошибка ввода!");
double k2 = GetNumberFromUser("Введите k2: ", "Ошибка ввода!");

double[] res = new double[2];
Calculation(k1, k2, b1, b2, res);

Console.WriteLine($"b1 = {b1}, k1 = {k1}, b2 = {b2}, k2 = {k2} -> ({res[0]}; {res[1]})");




void Calculation(double k1, double k2, double b1, double b2, double[] res)
{
  res[0] = (b2 - b1) / (k1 - k2);
  res[1] = k1 * res[0] + b1;
}



double GetNumberFromUser(string message, string errorMessage)
{
  while (true)
  {
    Console.Write(message);
    if (double.TryParse(Console.ReadLine(), out double userNumber))
    {
      return userNumber;
    }
    Console.WriteLine(errorMessage);
  }
}