#include <iostream>
using namespace std;

int n, m;
int check[8];
bool visited[8] = { false };

void solve(int cnt, int idx) {
	if (cnt == m) {
		for (int i = 0; i < m; i++) {
			cout << check[i] << ' ';
		}
		cout << '\n';
	}
	else {
		for (int i = idx; i < n; i++) {
			if (!visited[i]) {
				visited[i] = true;
				check[cnt] = i + 1;

				solve(cnt + 1,i+1);
				visited[i] = false;
			}
		}
	}
}

int main() {
	cin >> n >> m;
	solve(0, 0);
}