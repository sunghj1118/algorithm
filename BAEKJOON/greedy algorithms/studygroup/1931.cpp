#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, start, end;
	int count = 1;

	vector<pair<int, int>> schedule;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> start >> end;
		schedule.push_back(make_pair(end, start)); //sort by ending time
	}

	sort(schedule.begin(), schedule.end());

	int time = schedule[0].first;
	for (int i = 1; i < N; i++)
	{
		//if the next meeting starts after the end of
		//the current meeting, replace the current time and add a counter.
		if (schedule[i].second >= time) { 
			count++;
			time = schedule[i].first;
		}
	}
	cout << count;
}