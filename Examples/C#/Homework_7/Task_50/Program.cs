Console.WriteLine("");
int pos = GetNumberFromUser("Ошибка ввода!");








int GetNumberFromUser(/* string message,  */string errorMessage)
{
  while (true)
  {
    //Console.Write(message);
    if (int.TryParse(Console.ReadLine(), out int userNumber))
    {
      return userNumber;
    }
    Console.WriteLine(errorMessage);
  }
}