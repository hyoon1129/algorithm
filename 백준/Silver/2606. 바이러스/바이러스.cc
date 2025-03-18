#include <iostream>
#include <vector>
using namespace std;

bool visited[101];
int cnt = 0;
vector<int> arr[101];

void dfs(int now) {
	if (visited[now])return;
	visited[now] = true;
	cnt++;
	for (int i = 0; i < arr[now].size(); i++) {
		int nxt = arr[now][i];
		dfs(nxt);
	}
}

int main() {
	int n;
	int m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		arr[u].push_back(v);
		arr[v].push_back(u);
	}
	dfs(1);
	cout << cnt-1 << "\n";
}