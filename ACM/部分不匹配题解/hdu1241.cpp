// Test_Cpp.cpp : 定义控制台应用程序的入口点。
//
//hdu1241
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <iterator>
#include <stdlib.h>
#include <queue>
#include <stack>
#include <fstream>
#include <iomanip>
#include <map>
#include <set>
#include <cstdio>
#include <time.h>
#include <functional>
//#include <random>
//#include <high_precision.h>
//#include <Windows.h>
#define LL long long
#define inf 0x7fffffff
#define eps 1e-7

using namespace std;

const LL maxn = 1009;
//ifstream fin("input.txt");
//ofstream fout("output.txt");
#define Time_counter(){ printf("%d ms.\n", clock()); }

int N, M;

char mat[maxn][maxn];
int vis[maxn][maxn];
int d[8][2] = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 }, { 1, 1 }, { -1, -1 }, { 1, -1 }, { -1, 1 } };
bool cango(int x, int y){
	return x >= 0 && x < N&&y >= 0 && y < M;
}
void dfs(int x, int y){
	vis[x][y] = 1;
	for (int i = 0; i < 8; i++){
		int nx = x + d[i][0], ny = y + d[i][1];
		if (cango(nx, ny) && vis[nx][ny] == 0 && mat[nx][ny] == '@')
			dfs(nx, ny);
	}
}

int main(){
	while (cin >> N >> M && N != 0 && M != 0){
		for (int i = 0; i < N; i++){
			for (int j = 0; j < M; j++)
				cin >> mat[i][j];
		}
		int res = 0;
		memset(vis, 0, sizeof(vis));
		for (int i = 0; i < N; i++){
			for (int j = 0; j < M; j++){
				if (vis[i][j] == 0 && mat[i][j] == '@'){
					dfs(i, j); res++;
				}
			}
		}
		cout << res << endl;
	}
	//Time_counter();
	return 0;
}