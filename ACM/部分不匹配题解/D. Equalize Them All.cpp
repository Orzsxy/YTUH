/*
* @Author: Achan
* @Date:   2019-03-31 23:05:39
* @Last Modified by:   Achan
* @Last Modified time: 2019-04-01 08:45:04
*/
#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	cin.tie(0);
	int n; cin >> n;
	std::map<int, int> T; 
	std::vector<int> v(n+1); 
	int MT = -1;
	int Mx = -1;
    for(int i = 1; i <= n; i++)
    {
    	int t; cin >>t;
    	v[i] = t;
    	T[t]++;
    	if(T[t] > MT){
    		MT = T[t];
    		Mx = t; 
    	}
    }
    cout << n - MT << endl;
    int i = 1;
  	while(v[i] != Mx){i++;}
    for(int j = i-1; j >=1; j--)
    	cout << (v[j]<Mx?1:2) <<" "<< j << " " << j+1 << endl;
    for(int k = i+1; k<=n; k++)
    	if(v[k]!=Mx) cout << (v[k]<Mx?1:2)  <<" "<< k <<" " << k-1 <<endl; 
    return 0; 
}