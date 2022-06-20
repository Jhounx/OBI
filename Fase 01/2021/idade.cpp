//https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/idade/
#include <iostream>

using namespace std;

int idades[3]; 
int main(void) { 
  for (int i = 0; i < 3; i++) {
    cin >> idades[i]; 
  }
  //sortear a ordem das idades por bubble sort
  int aux;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (idades[i] < idades[j]) {
        aux = idades[i];
        idades[i] = idades[j];
        idades[j] = aux;
      }
    }
  }
  cout << idades[1] << endl;
  return 0;
}