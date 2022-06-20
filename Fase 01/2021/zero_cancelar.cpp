//https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/zero/

#include <iostream>

using namespace std;

int main(void) {
  int n, numero, soma, p;
  cin >> n;
  int numbers[n];
  p = 0;
  soma = 0;
  for (int i = 0; i < n; i++) {
    cin >> numero;
    if (numero == 0) {
      soma -= numbers[p -1];
      p -= 1;
    } else {
      numbers[p] = numero;
      p += 1;
    }
    soma += numero;
  }
  cout << soma << endl;
  return 0;
}