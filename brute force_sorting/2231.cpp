#include <iostream>

using namespace std;

int main() {
	int N, M, i, temp;
    N = M = i = temp = 0;
    
    cin >> N;

    /*
    */
    while (true)
    {
        i++;
        temp = i;
        while(temp > 0){
            M = temp + temp % 10;
            temp = temp / 10;
        }

        if(M == N){
            break;
        }
    }

    cout << i;
    return 0;
}