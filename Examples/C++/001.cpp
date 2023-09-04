#include <iostream>
#include <vector>

int main() {
  std::vector<int> mas;
  int n;
  int num;
  std::cin >> n;
  int count = 1;
  int res = 0;
  int res2 = 0;

  while (std::cin >> num && count < n) {
   /*  if (count == n) {
      break;
    } */
    mas.push_back(num);
    count++;
    if (num == 1) {
      res++;

    } else {
      if (res2 < res) {
        res2 = res;
      }
      res = 0;
    }
  }

  std::cout << res2;
}