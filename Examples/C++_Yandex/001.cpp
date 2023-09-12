#include <iostream>
#include <string>
#include <vector>

int main() {
  std::vector<int> mas;
  int n;
  std::string num_str;
  std::cin >> n;
  std::cin.ignore();
  int count = 1;
  int res = 0;
  int res2 = 0;
  int num = 0;

  while ((std::getline(std::cin, num_str)) && count <= n) {

    /*  if (count == n) {
       break;
     } */
    num = std::stoi(num_str);
    mas.push_back(num);
    count++;
  }
  for (int i = 0; i < n; i++) {
    if (mas[i] == 1) {
      res++;

    } else {
      if (res2 < res) {
        res2 = res;
      }
      res = 0;
    }
  }
  if (res2 < res) {
    res2 = res;
  }

  std::cout << res2;
}