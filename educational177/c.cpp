#include <bits/stdc++.h>
#include <vector>
using namespace std;

void solve() {
	// hash and check if current element is already used or not
	// the answer will always be increasing
	int n; cin >> n;
	vector<int> og;
	vector<int> queries;
	int c = n;
	int c2 = n;

	while (c--) {
		int num; cin >> num;
		og.push_back(num);
	}

	while (c2--) {
		int num2; cin >> num2;
		queries.push_back(num2);
	}
	unordered_map<int, int> check;
	vector<int>::iterator i;


}
