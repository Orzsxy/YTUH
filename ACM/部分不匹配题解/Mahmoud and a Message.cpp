/*--------------------------------------------------
对于新来的一个字符，新生成的子串自然就是从后面开始长度分别为1.2.3...的一些子串。
所以dp[i]表示长度为i的字符串的总的分隔方法，然后用f[i]表示分隔出的最小的子串数。
j为带有后面新加字符的子串
从i-j+1到i的字符串合法，那么有
1.dp[i]+=dp[i-j];
2.f[i]=min(f[i],f[i-j]+1);
3.如果1~i-j的字符串也合法，那么字符串长度的最大值为max(ans,j);其实前面的必定合法。
因为长度为1的必定合法。
------------------------------------------------------*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int n,m;
const int MAXN=1e3+7;
const int mod=1e9+7;
int limit[30];
long long dp[MAXN];
int f[MAXN];
char s[MAXN];

int check(int i,int j)
{
    int l=j-i+1;
    for(int k=i;k<=j;++k)
    {
        if(limit[s[k]-'a']<l)return 0;
    }
    return 1;
}

int main()
{
    int i,j;
    scanf("%d",&n);
    scanf("%s",s+1);
    for(i=0;i<26;++i)scanf("%d",&limit[i]);
    int MAX=0;
    dp[0]=1;
    for(i=1;i<=n;++i)//长度为i
    {
        f[i]=1e9;
        for(j=1;j<=i;++j)//长度
        {
            if(check(i-j+1,i))//后面的当前序列合法
            {
                dp[i]=(dp[i]+dp[i-j])%mod;
                f[i]=min(f[i],f[i-j]+1);
                MAX=max(MAX,j);
            }
        }
    }
    printf("%I64d\n%d\n%d\n",dp[n],MAX,f[n]);
}