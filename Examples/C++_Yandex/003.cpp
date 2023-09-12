#include <fstream>
#include <iostream>

int main() {
  std::ofstream output;
  std::ifstream input;
  input.open("input.txt");
  output.open("output.txt");

  int mas[2];
  int n;
  input >> n;

  mas[0] = INT32_MAX - 1;
  for (int i = 0; i < n; i++) {
    input >> mas[1];

    if (mas[0] != mas[1]) {
      mas[0] = mas[1];
      output << mas[0] << std::endl;
    }
    if (input.eof()) {
      break;
    }
  }
  // output << mas[0];
  input.close();
  output.close();
}