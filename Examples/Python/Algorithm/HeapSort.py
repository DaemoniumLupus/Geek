class HeapSort:
  mas = []#massive
  n = 0#length of massive

  def Heapify(self,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < self.n and self.mas[l] > self.mas[largest]:
      largest = l
    
    if r < self.n and self.mas[r] > self.mas[largest]:
      largest = r

    if largest != i:
      self.mas[i],self.mas[largest] = self.mas[largest],self.mas[i]
      self.Heapify(largest)
      

  def heapSort(self):
    self.n = len(self.mas)
    # i = self.n / 2 - 1
    for i in range(len(self.mas) // 2 - 1,-1,-1):
      self.Heapify(i)
    
    for i in range(self.n-1,-1,-1):
      self.mas[0],self.mas[i] = self.mas[i],self.mas[0]
      self.n -= 1
      self.Heapify(0)
    print(self.mas)

a = HeapSort()
a.mas = [12, 11, 13, 5, 6, 7]
a.heapSort()
