#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n; cin >> n;
	int arr[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	
	int sum = 0;
	for (int i = 0; i < n; i += 2){
		sum += arr[i];
	}

	cout << sum;
}

int main() {
	solve();
}
