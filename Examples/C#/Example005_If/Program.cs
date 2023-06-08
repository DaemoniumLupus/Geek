Console.Write("Введите имя пользователя ");
string username = Console.ReadLine();
string lowUsername = username.ToLower();
if (lowUsername == "маша"){
  Console.WriteLine("Ура, это же МАША");
}else {
  Console.Write("Привет, ");
  Console.WriteLine(username);
}
