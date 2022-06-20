//https://olimpiada.ic.unicamp.br/pratique/p2/2021/f1/cifra/

#include <iostream>
#include <string>
#include <math.h>

using namespace std;

string input, output;
string vogais = "aeiou";
string alfabeto = "abcdefghijklmnopqrstuvxzz";

int main(void) {
  cin >> input;
  int alphabetIndex, vogalIndex, distancia, df;
  char vogalPerto, proximo;

  for (char letra : input) {
    cout << letra;

    //caso seja uma vogal
    if (vogais.find(letra) != string::npos) {
      continue;
    }

    df = 99;
    alphabetIndex = alfabeto.find(letra, 0);

    //achar a vogal mais proxima
    for (char vogal : vogais) {
      vogalIndex = alfabeto.find(vogal, 0);
      distancia = fabs(alphabetIndex - vogalIndex);
      if (distancia < df) {
        df = distancia;
        vogalPerto = vogal;
      }
    }
    cout << vogalPerto;

    //achar a proxima consoante
    proximo = alfabeto[alphabetIndex + 1];
    if (vogais.find(proximo, 0) != string::npos) {
      proximo = alfabeto[alphabetIndex + 2];
    }
    cout << proximo;
  }
  
  return 0;
}