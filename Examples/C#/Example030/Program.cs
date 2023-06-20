Console.Clear();
int[] Arr = new int[8];

ArrayRand(Arr);

Write(Arr);



void ArrayRand(int[] RandomArray)
{
  for (int i = 0; i < RandomArray.Length; i++)
  {
    RandomArray[i] = Rand(0, 2);
  }

}


int Rand(int a, int b)
{
  return new Random().Next(a, b);
}

void Write(int[] RandomArray)
{
  Console.Write("{");

  for (int i = 0; i < RandomArray.Length; i++)
  {
    if (i + 1 == RandomArray.Length)
    {
      Console.Write($"{RandomArray[i]}");
    }
    else
    {
      Console.Write($"{RandomArray[i]}, ");
    }
  }
  
  Console.Write("}");
}