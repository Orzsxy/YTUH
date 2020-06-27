/*--------------------------------------------------
����������һ���ַ��������ɵ��Ӵ���Ȼ���ǴӺ��濪ʼ���ȷֱ�Ϊ1.2.3...��һЩ�Ӵ���
����dp[i]��ʾ����Ϊi���ַ������ܵķָ�������Ȼ����f[i]��ʾ�ָ�������С���Ӵ�����
jΪ���к����¼��ַ����Ӵ�
��i-j+1��i���ַ����Ϸ�����ô��
1.dp[i]+=dp[i-j];
2.f[i]=min(f[i],f[i-j]+1);
3.���1~i-j���ַ���Ҳ�Ϸ�����ô�ַ������ȵ����ֵΪmax(ans,j);��ʵǰ��ıض��Ϸ���
��Ϊ����Ϊ1�ıض��Ϸ���
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
    for(i=1;i<=n;++i)//����Ϊi
    {
        f[i]=1e9;
        for(j=1;j<=i;++j)//����
        {
            if(check(i-j+1,i))//����ĵ�ǰ���кϷ�
            {
                dp[i]=(dp[i]+dp[i-j])%mod;
                f[i]=min(f[i],f[i-j]+1);
                MAX=max(MAX,j);
            }
        }
    }
    printf("%I64d\n%d\n%d\n",dp[n],MAX,f[n]);
}