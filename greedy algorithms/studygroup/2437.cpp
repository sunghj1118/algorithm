#include <iostream>
#include <algorithm>
using namespace std;

int N;
int arr[1000];

int main(){
    // get input
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> arr[i];
    }

    //sort
    sort(arr, arr+N);

    //find answer
    int result = 1;
    for(int i =0; i < N; i++){
        if(arr[i]>result){
            break;
        }
        result+=arr[i];
    }
    
    // output
    cout<< result;
}