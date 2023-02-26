#include <iostream>

using namespace std;

// declare global list of cubes
int cube[21]; //set as size 21 since 20 is max size

// declare count to check number of cubes needed
long long count;

// function to recursively solve min num of cubes needed
void min_cubes(int l, int w, int h, int c_idx){
    int flag = 0;
    int k, a;
    if(l==0 || w==0 || h==0){
        return ;
    }

    k= min({l,w,h});
    c_idx = log2(k);

    for(int i=c_idx; i>=0; i--){
        if(cube[i]>0){
            c_idx = i;
            flag = 1;
            break;
        }
    }

    if(flag == 0){
        printf("-1\n");
        exit(0);
    }

    a = pow(2, c_idx);
    count++;
    cube[c_idx]--;
    min_cubes(l-a, w, h, c_idx);
    min_cubes(a, w-a, h, c_idx);
    min_cubes(a, a, h-a, c_idx);
}

int main(){
    // declare variables
    int l, w, h;
    int n_cubes;
    int a, b;
    
    // take input length, width, height
    scanf("%d %d %d", &l, &w, &h);
    scanf("%d", &n_cubes);

    // take input amount of cubes available
    for(int i=0; i<n_cubes; i++){
        scanf("%d %d", &a, &b);
        cube[a] = b;
    }

    // calculate minimum amount of cubes needed
    min_cubes(l, w, h, n_cubes-1);

    // print result
    printf("%lld\n", count);
}