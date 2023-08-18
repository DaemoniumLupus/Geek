
using System.Threading;
using System;
const int THREADS_NUMBER = 8;//Количество покотов
const int N = 100000;//размер массива
object locker = new object();
//int[] array = { 0, 2, -9, 2, 12, 10, 9, 1, -20 };

Random rand = new Random();
int[] resSerial = new int[N].Select(r => rand.Next(0, 5)).ToArray();

int[] resParallel = new int[N];
Array.Copy(resSerial, resParallel, N);

//CoutingSort(array);
CoutingSortExtended(resSerial);

ParallelCoutingSortExtended(resParallel);

Console.WriteLine(EqualityMatrix(resSerial, resParallel));

//Сортировка подсчетом
void CoutingSort(int[] inputArray)
{
  int[] counters = new int[10];//массив повторений


  //int ourNumber;
  for (int i = 0; i < inputArray.Length; i++)
  {
    // Варианты
    counters[inputArray[i]]++;
    /* ourNumber = inputArray[i];
    counters[ourNumber]++; */
  }
  int index = 0;
  for (int i = 0; i < counters.Length; i++)
  {
    for (int j = 0; j < counters[i]; j++)
    {
      inputArray[index] = i;
      index++;
    }
  }
}

void CoutingSortExtended(int[] inputArray)
{
  int max = inputArray.Max();
  int min = inputArray.Min();

  int offset = -min;

  int[] counters = new int[max + offset + 1];


  for (int i = 0; i < inputArray.Length; i++)
  {
    counters[inputArray[i] + offset]++;

  }

  int index = 0;
  for (int i = 0; i < counters.Length; i++)
  {
    for (int j = 0; j < counters[i]; j++)
    {
      inputArray[index] = i - offset;
      index++;
    }
  }

}
void ParallelCoutingSortExtended(int[] inputArray)
{
  int max = inputArray.Max();
  int min = inputArray.Min();

  int offset = -min;

  int[] counters = new int[max + offset + 1];

  int eachThreadCalc = N / THREADS_NUMBER;

  var threadsParall = new List<Thread>();

  for (int i = 0; i < THREADS_NUMBER; i++)
  {
    int startPos = i * eachThreadCalc;
    int endPos = (i + 1) * eachThreadCalc;

    if (i == THREADS_NUMBER - 1) endPos = N;

    threadsParall.Add(new Thread(() => CoutingSortParallel(inputArray, counters, offset, startPos, endPos)));
    threadsParall[i].Start();
  }
  foreach (var thread in threadsParall)
  {
    thread.Join();
  }

  int index = 0;
  for (int i = 0; i < counters.Length; i++)
  {
    for (int j = 0; j < counters[i]; j++)
    {
      inputArray[index] = i - offset;
      index++;
    }
  }


}

void CoutingSortParallel(int[] inputArray, int[] counters, int offset, int startPos, int endPos)
{
  for (int i = startPos; i < endPos; i++)
  {
    lock (locker)
    {
      counters[inputArray[i] + offset]++;
    }

  }



}

bool EqualityMatrix(int[] fmatrix, int[] smatrix)
{
  bool res = true;
  for (int i = 0; i < N; i++)
  {
    res = res && (fmatrix[i] == smatrix[i]);
  }
  return res;
}

