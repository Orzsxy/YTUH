// Test_Cpp.cpp : 定义控制台应用程序的入口点。
//
//hdu1016
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

const LL maxn = 5009;
//ifstream fin("input.txt");
//ofstream fout("output.txt");
#define Time_counter(){ printf("%d ms.\n", clock()); }

int N;
int vis[maxn], res[maxn];
int isprime[maxn];

void _isprime(){
	for (int i = 0; i < maxn; i++) isprime[i] = 1;
	isprime[0] = isprime[1] = 0;
	for (int i = 2; i < maxn; i++){
		if (isprime[i]){
			for (int j = 2 * i; j < maxn; j += i){
				isprime[j] = 0;
			}
		}
	}
}
void dfs(int cur){
	if (cur == N&&isprime[res[N-1] + res[0]]){
		cout << res[0];
		for (int i = 1; i < N; i++)
			cout << " " << res[i];
		puts("");
	}
	for (int i = 2; i <= N; i++){
		if (vis[i] == 0&&isprime[res[cur-1]+i]){
			res[cur] = i;
			vis[i] = 1;
			dfs(cur + 1);
			vis[i] = 0;
		}
	}
}
int main(){
	_isprime(); res[0] = 1;
	int T = 1;
	while (cin >> N){
		cout << "Case " << T++ << ":" << endl;
		memset(vis, 0, sizeof(vis));
		dfs(1);
		puts("");
	}
	//Time_counter();
	return 0;
}