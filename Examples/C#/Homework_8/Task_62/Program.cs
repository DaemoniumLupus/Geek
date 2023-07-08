int n = 4;
int[,] result = new int[n, n];

int pos = 0;
int count = n;
int value = -n;
int sum = -1;

do
{
  value = -1 * value / n;
  for (int i = 0; i < count; i++)
  {
    sum += value;
    result[sum / n, sum % n] = pos++;
  }
  value *= n;
  count--;
  for (int i = 0; i < count; i++)
  {
    sum += value;
    result[sum / n, sum % n] = pos++;
  }
} while (count > 0);

for (int i = 0; i < result.GetLength(0); i++)
{
  for (int j = 0; j < result.GetLength(1); j++)
  {
    Console.Write(String.Format("{0,3}", result[i, j]), " ");
  }
  Console.Write("\n");
}
