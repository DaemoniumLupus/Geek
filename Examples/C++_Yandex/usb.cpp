#include <fstream>
#include <iostream>

int main() {
  std::ofstream output;
  std::ifstream input;
  input.open("input.txt");
  output.open("output.txt");

	int n;
	input >> n;
	int m;
	input >> m;
	int c2;
	input >> c2;
	int c5;
	input >> c5;

	std::cout << c5;
	int buf = m - n;
  int res;

	int res2 = m % 2;
	int countres2 = m / 2;

	int res5 = m % 4;
	int countres5 = m / 4;

	if count res
	

	// if (buf <= 0){
	// 	output << 0;
	// }else if (buf == 1){
	// 	output << c2;
	// }else if (buf == 2){
	// 	if (c2 * 2 <= c5){
	// 		output << c2*2;
	// 	}else {
	// 		output << c5;
	// 	}
	// }else if (buf )



  
  // output << mas[0];
  input.close();
  output.close();
}