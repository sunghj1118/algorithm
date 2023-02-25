// take inputs: num classes and classtimes
// calculate how many rooms are needed
// output min rooms

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

// class times list
vector< pair<int, int> > class_time;

// priority queue of endtimes
priority_queue< int, vector<int>, greater<int> > pq_less;

int greedy(int class_count){
    // push first class' endtime into pq
    pq_less.push(class_time[0].second);

    // find the necessary class
    for(int i=1; i<class_count; i++){
        // push ith class' endtime into pq
        pq_less.push(class_time[i].second);
        // if ith's endtime starts later than top, can use same class
        if(pq_less.top() <= class_time[i].first){
            // pop last top
            pq_less.pop();
        }
    }

    // return amount of rooms needed
    return pq_less.size();
}


int main(){
    // get how many classes need to be filled
    int n_classes; 
    cin >> n_classes;

    // get classes
    for (int i=0; i<n_classes; i++){
        // class start and end times
        int start_time, end_time;
        cin >> start_time >> end_time;

        // save class times
        class_time.push_back(make_pair(start_time, end_time));
    }

    // sort by class start time
    sort(class_time.begin(), class_time.end());

    // print how many rooms are needed
    cout << greedy(n_classes) << endl;
}