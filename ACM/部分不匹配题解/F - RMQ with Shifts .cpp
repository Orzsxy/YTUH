#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>

using namespace std;
#define inf 0X3f3f3f3f
const int N=1000050;

int sum[21][2*N],add[21][2*N],SET[21][2*N]; //add ÿһ��������Ҫ�ӵ�����SET ��ʾ v
int maxx[21][2*N],minn[21][2*N];

void pushDown(int i,int l,int r,int num,int op)
{
    if(op==2)
    {
        if(SET[num][i]!=-1)
        {
            int mid=(l+r)>>1;
            SET[num][i<<1]=SET[num][i];
            sum[num][i<<1]=(mid-l+1)*SET[num][i];
            SET[num][i<<1|1]=SET[num][i];
            sum[num][i<<1|1]=(r-mid)*SET[num][i];
            minn[num][i<<1]=maxx[num][i<<1]=maxx[num][i<<1|1]=minn[num][i<<1|1]=SET[num][i];
            add[num][i<<1]=add[num][i<<1|1]=0;
            SET[num][i]=-1;
        }
    }
    else
        if(op==1)
    {
        if(add[num][i]!=0)
        {
            int mid=(l+r)>>1;
            pushDown(i<<1,l,mid,num,2);
            pushDown(i<<1|1,mid+1,r,num,2);

            add[num][i << 1 | 1] += add[num][i];
            add[num][i << 1] += add[num][i];
            sum[num][i << 1] += (mid - l + 1) * add[num][i];  //[l, mid]�������������
            sum[num][i << 1 | 1] += (r - mid) * add[num][i];  //[mid + 1, r]�����Ҷ�������
            minn[num][i<<1]+=add[num][i];
            maxx[num][i<<1]+=add[num][i];
            maxx[num][i<<1|1]+=add[num][i];
            minn[num][i<<1|1]+=add[num][i];
            add[num][i] = 0;
        }
    }
}

void update(int i,int l,int r,int ql,int qr,int val,int num,int op)
{
    //�߶�������ʼλ�� i����������� l�����Ҷ����� r��
    //������� ql,�����Ҷ� qr,v,�ڼ��� num,����ָ�� op

    if(l > qr || ql > r)
		//�������䲻�ڵ�ǰ������
        return ;
    if(l >= ql && r <= qr)	//Ҫ���µ�����ѵ�ǰ������ȫ��������ѵ�ǰ��������+val��Ȼ�󷵻���һ��
	{
		if (op==1)  //add
		{
			if (SET[num][i]!=-1)
				pushDown(i,l,r,num,2);//add֮ǰ�Ȱ�SET����ȥ

			sum[num][i] += (r - l + 1) * val;
			maxx[num][i]+=val;
			minn[num][i]+=val;
			add[num][i]+=val;
        }
		else
			if (op==2)			//SET
			{
				add[num][i]=0;
				sum[num][i]= (r - l + 1) * val;
				maxx[num][i]=val;
				minn[num][i]=val;
				SET[num][i]=val;
			}
			return ;
    }
				//�������ûreutrn ��ʾҪ�����Ҷ�������update�����԰��ӳٱ�Ƿ���ȥ
	pushDown(i,l,r,num,2);	//�ȴ�SET
		pushDown(i, l, r,num,1);	//�ٴ�add


    int mid = (l + r) >> 1;
    update(i << 1, l, mid, ql, qr, val,num,op);
    update(i << 1 | 1, mid + 1, r, ql, qr, val,num,op);

    sum[num][i] = sum[num][i << 1] + sum[num][i << 1 | 1];
	maxx[num][i] = max(maxx[num][i << 1] , maxx[num][i << 1 | 1]);
	minn[num][i] = min(minn[num][i << 1] , minn[num][i << 1 | 1]);

}

int query(int i, int l, int r, int ql, int qr,int num)	 //��ѯ����Ϊql��qr,��ǰ����Ϊl,r,����ǰ����͵Ľڵ�Ϊi
{
    if(l > qr || ql > r)
        return 0;
    if(l >= ql && r <= qr)
        return sum[num][i];

	pushDown(i,l,r,num,2);
		pushDown(i, l, r,num,1);
    int mid =( l + r) >> 1;
    return query(i << 1, l, mid, ql, qr,num)   + query(i << 1 | 1, mid + 1, r, ql, qr,num);
}

int query_max(int i, int l, int r, int ql, int qr,int num)
{
    if(l > qr || ql > r)
        return 0;
    if(l >= ql && r <= qr)
        return maxx[num][i];

	pushDown(i,l,r,num,2);
		pushDown(i, l, r,num,1);
    int mid =( l + r) >> 1;
    return max(query_max(i << 1, l, mid, ql, qr,num)   , query_max(i << 1 | 1, mid + 1, r, ql, qr,num));
}
int query_min(int i, int l, int r, int ql, int qr,int num)
{
    if(l > qr || ql > r)
        return inf;
    if(l >= ql && r <= qr)
        return minn[num][i];

	pushDown(i,l,r,num,2);
		pushDown(i, l, r,num,1);
    int mid =(  l + r) >> 1;
 return min(query_min(i << 1, l, mid, ql, qr,num)   , query_min(i << 1 | 1, mid + 1, r, ql, qr,num));
}

int main()
{
	int op;
    int r,c,m,i,j;
	int x1,x2,y1,y2,v;
	while(    scanf("%d%d%d", &r,&c,&m)!=EOF)
	{
		memset(sum,0,sizeof(sum));
		memset(add,0,sizeof(add));
		memset(maxx,0,sizeof(maxx));
		memset(minn,0,sizeof(minn));
		memset(SET,-1,sizeof (SET));
		for(  i = 1; i <= m; i++)
		{
			scanf("%d",&op);
			if (op==1)
			{
				scanf("%d%d%d%d%d",&x1,&y1,&x2,&y2,&v);
				for (j=x1;j<=x2;j++)
				{
					update(1,1,c,y1,y2,v,j,1);
				}
			}
			else
				if (op==2)
				{
					scanf("%d%d%d%d%d",&x1,&y1,&x2,&y2,&v);
					for (j=x1;j<=x2;j++)
					{
						update(1,1,c,y1,y2,v,j,2);
					}

				}
				else
				{
					scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
					int ans1=0;
					int ans2=0;
					int ans3=inf;
					for (j=x1;j<=x2;j++)
					{
						ans1+=query(1,1,c,y1,y2,j);
						ans2=max(ans2,query_max(1,1,c,y1,y2,j));
						ans3=min(ans3,query_min(1,1,c,y1,y2,j));
					}
					printf("%d %d %d\n",ans1,ans3,ans2);

				}

		}

	}
	return 0;
}
