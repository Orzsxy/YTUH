/*
* @Author: Achan
* @Date:   2019-04-17 00:11:10
* @Last Modified by:   Achan
* @Last Modified time: 2019-04-18 12:58:15
*/
#include<bits/stdc++.h>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<iomanip>
#include<vector> 
#include<queue>
#include<cmath> 
using namespace std;

#define X 			first
#define Y 			second
#define eps  		1e-2
#define gcd 		__gcd
#define pb 			push_back
#define PI 			acos(-1.0)
#define lowbit(x) 	(x)&(-x)
#define fin         freopen("in.txt","r",stdin);
#define fout        freopen("out.txt","w",stdout);
#define Debug(format, ...) printf(format, ##__VA_ARGS__)
#define bug 		printf("!!!!!\n");
#define mem(x,y)	memset(x,y,sizeof(x))
#define rep(i,j,k)  for(int i=j;i<(int)k;i++)
#define per(i,j,k)  for(int i=j;i<=(int)k;i++)
#define pset(x)     setiosflags(ios::fixed)<<setprecision(x)
#define io std::ios::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);

typedef long long ll;
typedef long double LD; 
typedef pair<int,int> pii;
typedef unsigned long long ull; 

const int inf  = 1<<30;
const ll  INF  = 1e18 ;
const int mod  = 1e9+7;
const int maxn = 2e5+2;
const int mov[4][2] = {-1,0,1,0,0,1,0,-1};
const int Mov[8][2] = {-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};
 
inline int read(){
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}

void read(int &x)
{
    x=0;int f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    x*=f;return;
}

typedef struct node
{
	int num;
	int id;
}node;
bool cmp(node a, node b)
{
	return a.num > b.num;
}

int main(void)
{
	int n, k;
	cin >> n >> k;
	std::vector<node> v(n+1);
	std::vector<int> vis(n+1);
	std::vector<int> L(n+2);
	std::vector<int> R(n+2);
	for(int i = 1; i <= n; i++)
	{
		cin >> v[i].num;
		v[i].id = i;
		L[i] = i - 1;
		R[i] = i + 1;
	}
	sort(v.begin()+1,v.end(),cmp);
    int turn = 1;
    for(int i = 1; i <= n; i++)
    {
    	int p = v[i].id;
    	// cout << p << endl;
    	if(vis[p]) continue;
    	vis[p] = turn;
    	int r = R[p];
    	for (int j = 0; j < k && r <= n; ++j)
    	{
    		vis[r] = turn;
    		r = R[r];
    	}
    	int l = L[p];
    	for (int j = 0; j < k && l; ++j)
    	{
    		vis[l] = turn;
    		l = L[l];
    	}
    	L[r] = l;
    	R[l] = r;
    	turn ^= 3;
    }
    for(int i =1; i <= n; i++)
    	cout << vis[i];
    cout << endl;



    
 #ifdef LOCAL
    Debug("My Time: %.3lfms\n", (double)clock() / CLOCKS_PER_SEC);
#endif   
}