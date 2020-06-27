/*------------------------------------------------------------
题意：乘坐电车，一共会有n次乘坐，之后n行会一次给出每次乘坐的时间。问你最少花的钱是多少。每次输出应该支付的钱。
用dp[n]表示第n次旅行一共所要花费的最小钱数。那么对于dp[n]
1.就是花20快钱买咯。
2.和上面的一起能凑个90分钟就凑个90分钟。
3.和上面的一起能凑个一天就凑个1天。
那么当前的值就是这3个值的最小值。
--------------------------------------------------------------*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN=1e5+7;
int n;
int dp[MAXN];
long long tt[MAXN];
int main()
{
    int i,j;
    scanf("%d",&n);
    for(i=1;i<=n;++i)
    {
        scanf("%I64d",&tt[i]);
    }
   int sum=0;
    for(i=1;i<=n;++i)
    {
        dp[i]=dp[i-1]+20;
        for(j=i-1;j>=1;--j)
        {
            if(tt[i]-tt[j]<90)dp[i]=min(dp[i],dp[j-1]+50);
            else
            if(tt[i]-tt[j]<1440)dp[i]=min(dp[i],dp[j-1]+120);
            else break;
        }
        printf("%d\n",dp[i]-sum);
        sum=dp[i];
    }
    return 0;
}