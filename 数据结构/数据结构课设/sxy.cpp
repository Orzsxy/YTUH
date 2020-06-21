#include <iostream>
#include <cstring>
#include <fstream>
#include <malloc.h>
#include <cstdio>
#include <sstream>
#include <vector>
#include<conio.h>//getch
#include<cstdlib>//��������ͷ�ļ�
#define l 1<<10
#define mod (1<<10)-1
#include "sxy.h"
using namespace std;
Scenic S[10000];
//�ù�ϣ�����ʽ���н������Ҿ������Ƶ�ַ
int Hash(string name)
{
    int key=0,t=name.size();
    for(int i=0;i<t;++i)
        key+='0'-name[i];
        key&=mod;
    return key;
}
//����һ������(�ڽӾ�����ʽ��
void create_graph()
{
	ofstream outFile;  //���������
	outFile.open("����������Ϣ��.txt",ios::app);  //����������������ļ���������
    string name;
    int i,n1,n2,key;
    cout<<"\n*�����뾰�������ƣ�";
    cin>>name;
    getchar();
    key=Hash(name);
    Scenic *p=new Scenic,*q=new Scenic;
    q=S[key].next;
    while(q)//��Ϊ��ʱ˵����λ�ô��ھ�����ASCII������ͬ��
    {
        if(q->mat.Sname==name)//���Ʋ�����ͬ���ſ������뾰��
          {
             cout<<"�þ��������Ѵ��ڣ��������뾰������: ";
             cin>>name;
             getchar();
             key=Hash(name);
             q=S[key].next;
             break;
          }
          else
            q=q->next;
    }
    delete q;
    p->mat.Sname=name;
    //�����ļ�����
    outFile<<"*****************************************************************"<<endl;
    outFile<<"��������Ϊ"<<name<<"�ľ�����Ϣ����"<<endl;
    cout<<"\n*������þ����ľ�������Ŀ��";
    cin>>p->mat.count;
    outFile<<"�þ����ľ�������ĿΪ:"<<p->mat.count<<endl;
    cout<<"\n*�����뾰���ĵ�·����Ŀ��";
    cin>>p->mat.edge;
    outFile<<"�þ����ĵ�·��ĿΪ:"<<p->mat.edge<<endl;
    cout<<"\n*�������·�������ӵ����������š����Ƽ���·�ĳ���\n";
    outFile<<"*������·���ӵ����������š����Ƽ���·�ĳ�����Ϣ���£�"<<endl;
    memset(p->mat.m,0,sizeof(p->mat.m));
    for(i=1;i<=p->mat.edge;i++)
    {
            cout<<"\n*�� "<<i<<" ����·\n";
            cout<<"\t-���� 1 ��ţ�";
            cin>>n1;
            outFile<<"************************��"<<i<<"����·,"<<endl;
            cout<<"\t-���� 1 ���ƣ�";cin>>p->mat.Pname[n1];
            outFile<<"������Ϊ"<<n1<<"����Ϊ"<<p->mat.Pname[n1]<<endl;
            cout<<"\t-���� 2 ��ţ�";cin>>n2;
            cout<<"\t-���� 2 ���ƣ�";cin>>p->mat.Pname[n2];
            outFile<<"������Ϊ"<<n2<<"����Ϊ"<<p->mat.Pname[n2]<<endl;
            cout<<"\t-������֮��ĵ�·���ȣ�";cin>>p->mat.m[n1][n2];
            outFile<<p->mat.Pname[n1]<<"��"<<p->mat.Pname[n2]<<"֮���ֱ�ӵ�·������"<<p->mat.m[n1][n2]<<endl;
            p->mat.m[n2][n1]=p->mat.m[n1][n2];

    }
    p->next=S[key].next;
    S[key].next=p;
    cout<<"\n*���������ɹ���";
    outFile.close();  //�ر��ļ�
     returnMainFace();
}
//�������ֲ����ڽӾ������ʽ�����
void print_graph()
{
    string name;
    int key,tag=1;
    Scenic *p;
    cout<<"*�������ƣ�"<<endl;
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*��������ֲ�ͼΪ"<<name<<"�ľ�����ѯ���ɹ���\n";
    else
    {
        while(p)
        {
          if(p->mat.Sname==name)//�ҵ��ĵ�ַ��Ϊ�գ�ֻ��������ͬʱ�ţ���������й���Ϣ
          {
            cout<<"*************��ѯ��������Ϊ "<<name<<" �ĸ�����ֲ�ͼ���£����ڽӾ����ʾ���� "<<endl;
            for(int i=1;i<=p->mat.count;++i)
            {
                cout<<"�������� "<<p->mat.Pname[i];
                for(int j=1;j<=p->mat.count;++j)
                    cout<<' '<<p->mat.m[i][j];
                    cout<<endl;
            }
             tag=0;
             break;
          }
          else
                p=p->next;
        }
        if(tag)
        cout<<"\n*��������ֲ�ͼΪ"<<name<<"�ľ�����ѯ���ɹ���\n";

    }
      returnMainFace();
}
//�����������������·
int visited[100]={0};
int np;//�ҵ��ľ�������������ڵݹ�ʱ�ҵ�����
void DFS(int c,struct Scenic *p)
{
    np++;
    if(np==p->mat.count)
    {
        cout<<p->mat.Pname[c]<<endl;
        returnMainFace();
    }
    else
        cout<<p->mat.Pname[c]<<" --> ";
    visited[c]=1;
     for(int i=1;i<=(p->mat.count);i++)
    {
        if(p->mat.m[c][i]>0&&!visited[i])
        {
              DFS(i,p);
        if(p->mat.count>np)
        {
            cout<<p->mat.Pname[c]<<"-->";
        }
        }
    }
     if(np==p->mat.count)
        returnMainFace();
}
//������·
void guide_line()
{
     //checked();
     Scenic *p;
     int key,c,tag=1;
     cout<<"\n*�������Ӧ���������ƣ�";
     string name;
     cin>>name;
     getchar();
     key=Hash(name);
    p=S[key].next;
    if(p==NULL)
      cout<<"\n*��������ֲ�ͼ���ڽӾ����ʾ����ѯ�����ڣ�\n";
    else
    {
        while(p)
        {
            if(p->mat.Sname==name)
            {
                memset(visited,0,sizeof(visited));
                np=0;
                cout<<"�����Ӧ����ı��"<<endl;
                cin>>c;
                cout<<"*�γɵĵ�����·ͼ������������Ȳ��ԣ�������ʾ��\n\n\t";
                DFS(c,p);
                tag=0;
                break;
            }
            else
                p=p->next;
        }
        if(tag)
        cout<<"\n*��������ֲ�ͼΪ"<<name<<"�ľ�����ѯ���ɹ���\n";
     }
    returnMainFace();
}
int DFS_Count;
int vis[100];
void dfs(int i,struct Scenic *p)
{
    vis[i]=1;//��Ƕ���i������
    for(int j=1;j<=p->mat.count;j++)
    {
        if(p->mat.m[i][j]!=0&&vis[j]==0)
            dfs(j,p);
    }
}
//�жϻ�·
void check_circuit()
{
    int key,tag=1;
    Scenic *p;
    string name;
    cout<<"*�������ƣ�"<<endl;
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*��������ֲ�ͼ��ѯ���ɹ���\n";
    else
    {
        while(p)
        {
            if(p->mat.Sname==name)
            {
                memset(vis,0,sizeof(vis));//��ʼ��vis���飬��ʾһ��ʼ���ж��㶼δ�����ʹ�
                DFS_Count=0;
                for(int i=1;i<=p->mat.count;i++)//�����������
                {
                    if(vis[i]==0)//����������Ϊ�����ʹ������i�����������������ȱ���
                    {
                        DFS_Count++;//ͳ�Ƶ���void dfs(int i);�Ĵ���
                        dfs(i,p);
                    }
                }
                if(p->mat.edge+DFS_Count>p->mat.count)//��������������ͨ�������������ϱߵ���������>�ڵ���������������ж�Ϊ�л�
                    cout<<"�þ����д��ڻ�"<<endl;
                else
                    cout<<"�þ����в����ڻ�"<<endl;
                    tag=0;
                    break;
            }
            else
                p=p->next;
        }
        if(tag)
          cout<<"\n*��������ֲ�ͼ��ѯ���ɹ���\n";
    }
    returnMainFace();
}
//Floyd�㷢�����·
void Floyd(int a,int b,struct Scenic *&p)
{
    int i,j,k;
    int A[M][M],path[M][M];
    for(i=1;i<=p->mat.count;i++)//�Խ��������·�ľ�����д���
    {
        for(j=1;j<=p->mat.count;j++)
        {
        if(p->mat.m[i][j]==0&&i!=j)
             A[i][j]=INF;
        else if(i==j)
            A[i][j]=0;
        else
            A[i][j]=p->mat.m[i][j];
        if(i!=j&&p->mat.m[i][j]<INF)
            path[i][j]=i;
        else
            path[i][j]=-1;
        }
    }
    for(k=1;k<=p->mat.count;k++)
    {
          for(i=1;i<=p->mat.count;i++)
            {
              for(j=1;j<=p->mat.count;j++)
              {
                  if(A[i][j]>A[i][k]+A[k][j])
                  {
                       A[i][j]=A[i][k]+A[k][j];
                       path[i][j]=path[k][j];
                  }
              }
            }
    }
    int apath[M],d;
    if(A[a][b]<INF&&a!=b)
    {
        cout<<"\n*�� "<<p->mat.Pname[a]<<" �� "<<p->mat.Pname[b]<<" �����·��Ϊ��";
        k=path[a][b];
        d=0;
        apath[d]=b;
       while(k!=-1&&k!=a)//ѭ��ʵ�ּ�¼��Ӧ�Ľڵ���
       {
           d++;
           apath[d]=k;
           k=path[a][k];
       }
         d++;
         apath[d]=a;
         cout<<p->mat.Pname[apath[d]];
         cout<<apath[d];
         for(int s=d-1;s>=0;s--)//����ڵ�����
         {
            cout<<" --> "<<p->mat.Pname[apath[s]];
             cout<<','<<apath[s];
         }
          cout<<" ����̾���Ϊ��"<<A[a][b]<<endl;
    }
    else if(a==b)
      cout<<"\n*���������벻�Ϸ���\n";
    else
     cout<<"\n*����������䲻����·��\n";
}
//���·��������
void min_distance()
{
    Scenic *p;//=new Scenic;
    string name;
    int a,b,key,tag=1;
    cout<<"*�������ƣ�"<<endl;
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*�����ֲ�ͼ��ѯ���ɹ���\n";
    else
    {
        while(p)
        {
            if(p->mat.Sname==name)
            {
                cout<<"*******����Ϊ�þ�����һЩ��Ϣ��"<<endl;
                cout<<"*******�������ƣ�"<<p->mat.Sname<<endl;
                for(int i=1;i<=p->mat.count;++i)
                {
                    cout<<"���Ϊ "<<i<<' '<<"�ľ�������Ϊ "<<p->mat.Pname[i];
                    for(int j=1;j<=p->mat.count;++j)
                        cout<<' '<<p->mat.m[i][j];
                        cout<<endl;
                }
                cout<<"*������Ҫ��ѯ�� ���·������̾��� ����������ı�ţ�\n";
                cout<<"\t-���� 1��";
                cin>>a;
                getchar();
                cout<<"\t-���� 2��";
                cin>>b;
                getchar();
                Floyd(a,b,p);
                tag=0;
                break;
            }
            else
                p=p->next;
        }
        if(tag)
        cout<<"\n*��������ֲ�ͼ��ѯ���ɹ���\n";
    }
        returnMainFace();
}
void prime(struct Scenic *&p,string name)
{
    int A[M][M],a,b,tag=1;
    while(p)
        {
            if(p->mat.Sname==name)
            {
                for(int i=1;i<=p->mat.count;i++)
                {
                    for(int j=1;j<=p->mat.count;j++)
                    {
                        if(p->mat.m[i][j]==0&&i!=j)
                        A[i][j]=INF;
                        else if(i==j)
                        A[i][j]=0;
                        else
                        A[i][j]=p->mat.m[i][j];
                    }
                }
                cout<<"����������ʼҪ����ľ�����";
                cin>>a;
                cout<<"��������Ҫ��ɵ��Ĵﾰ����";
                cin>>b;
                cout<<"\n*��·�޽��滮ͼ��prime�㷨���滮���£�\n";
                int lowcost[M],closest[M],k=0,sum=0,num=0;
                for(int i=1;i<=p->mat.count;++i)
                {
                    lowcost[i]=A[a][i];
                    closest[i]=a;
                }
                for(int i=1;i<p->mat.count;++i)
                {
                    int min=INF;
                    for(int j=1;j<=p->mat.count;++j)
                    {
                        if(lowcost[j]&&(lowcost[j]<min))
                        {
                            min=lowcost[j];
                            k=j;
                        }
                    }
                    if(min<INF)
                    cout<<"\t-�޽��ĵ� "<<++num<<" ��·Ϊ������  "<<p->mat.Pname[closest[k]]<<"  ������  "<<p->mat.Pname[k]<<"  ��������·����Ϊ��"<<min<<endl;
                    sum+=lowcost[k];
                    lowcost[k]=0;
                    if(k==b)
                    {
                        cout<<"�Ӿ���  "<<a<<" ������  "<<b<<" ����·������Ϊ "<<sum<<endl;
                        break;
                    }
                    for(int j=1;j<=p->mat.count;++j)
                    {
                        if(A[k][j]&&A[k][j]<lowcost[j])
                        {
                            lowcost[j]=A[k][j];
                            closest[j]=k;
                        }
                    }
                }
            tag=0;
            break;
            }
            else
                p=p->next;
        }
        if(tag)
            cout<<"\n*��������ֲ�ͼ��ѯ���ɹ���\n";
}
void build_road()//��·�޽��滮ͼ����С��������prime�㷨��
{
    Scenic *p;
     int key;
     cout<<"\n*�������Ӧ���������ƣ�";

     string name;
     cin>>name;
     getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
      cout<<"\n*��������ֲ�ͼ���ڽӾ����ʾ����ѯ�����ڣ�\n";
    else
    {
        prime(p,name);
        returnMainFace();
    }
}
void scenic_message()//�ļ����������Ϣ
{
    system("cls");
    char ch[200];
   ifstream inFile; //����������
   inFile.open("����������Ϣ��.txt",ios::in);
   while(!inFile.eof())
   {
       inFile.getline(ch,sizeof(ch),'\n');
       cout<<ch<<endl;
   }
   returnMainFace();
}
//�޸ľ������ƣ�
void change_sceic_name(struct Scenic *&p)
{
    int i;
    string name,rname,str;
    ifstream inFile("����������Ϣ��.txt",ios::in);
    vector<string> v;
    cout<<"������ԭ�ȵľ�������: ";
    cin>>name;
    cout<<"������Ҫ�޸ĺ�����ƣ� ";
    cin>>rname;
    for(i=1;i<=p->mat.count;++i)
    {
        if(p->mat.Pname[i]==name)
           {
              p->mat.Pname[i]=rname;
              break;
           }
    }
    while(inFile)
    {
        getline(inFile, str);
        v.push_back(str);
    }
    stringstream stream;
    string result,s,a,r;// std::string result;
    stream << i; //��int������
    stream >> r; //��stream�г�ȡǰ������intֵ
    s="������Ϊ"+r;
    s+="����Ϊ";
    a=s;
    s+=name;
    a+=rname;
    ofstream outFile("����������Ϣ��.txt",ios::out);
    vector<string>::const_iterator it=v.begin();
    for(;v.end()!=it;++it)
    {
       if(*it==s)
        {
            //v.erase(v.begin()+j);
            outFile<<a<<endl;
        }
        else
            outFile<<*it<<endl;
    }
    inFile.close();
    outFile.close();
    cout<<"���������޸ĳɹ�(�����������������������ֲ�ͼ�������������Ϣ���в鿴������ֱ�Ӵ򿪾����ļ����в鿴"<<endl;
}
void change_weight(struct Scenic *&p)
{
    int weight,weight1,i,x=0,y=0;
    string name1,name2,a,b,str;
    ifstream inFile("����������Ϣ��.txt",ios::in);
    vector<string> v;
    cout<<"������ĸõ�·�Ͼ���1������: ";
    cin>>name1;
    cout<<"������ĸõ�·�Ͼ���2������: ";
    cin>>name2;
    cout<<"������ĸõ�·��ԭ�ȵ�Ȩֵ: ";
    cin>>weight;
    cout<<"������õ�·��Ҫ�޸ĺ�ĵ�Ȩֵ: ";
    cin>>weight1;
    for( i=1;i<=p->mat.count;++i)//�޸ĵ���������
    {
        if(p->mat.Pname[i]==name1)
            x=i;
        if(p->mat.Pname[i]==name2)
            y=i;
    }
    p->mat.m[x][y]=p->mat.m[y][x]=weight1;
    while(inFile)//�����޸ĵ��ļ�����
    {
        getline(inFile, str);
        v.push_back(str);
    }
    //outFile<<p->mat.Pname[n1]<<"��"<<p->mat.Pname[n2]<<"֮���ֱ�ӵ�·������"<<p->mat.m[n1][n2]<<endl;
    stringstream stream,stream1;
    string ss,s,w,w1;// std::string result;
    stream << weight; //��int������
    stream >> w; //��stream�г�ȡǰ������intֵ
    stream1 << weight1; //��int������
    stream1 >> w1; //��stream�г�ȡǰ������intֵ
    s=name1;ss=name2;
    s+="��";ss+="��";
    s+=name2;ss+=name1;
    s+="֮���ֱ�ӵ�·������";ss+="֮���ֱ�ӵ�·������";
    a=s;b=ss;
    s+=w;ss+=w;
    a+=w1;b+=w1;
    ofstream outFile("����������Ϣ��.txt",ios::out);
    vector<string>::const_iterator it=v.begin();
    for(;v.end()!=it;++it)
    {
       if(*it==s)
            outFile<<a<<endl;
       else if(*it==ss)
            outFile<<b<<endl;
       else
            outFile<<*it<<endl;
    }
    inFile.close();
    outFile.close();
    cout<<"���������޸ĳɹ�(�����������������������ֲ�ͼ�������������Ϣ���в鿴������ֱ�Ӵ򿪾����ļ����в鿴"<<endl;
}
void increase_number(struct Scenic *&p)
{
    string name1,name2,str;
    int i,x=0,y=0,weight;
    ifstream inFile("����������Ϣ��.txt",ios::in);
    vector<string> v;
    cout<<"������С·���Ե�1����";
    cin>>name1;
    cout<<"������С·���Ե�2����";
    cin>>name2;
    cout<<"�������С·��Ȩֵ";
    cin>>weight;
    for(i=1;i<=p->mat.count;++i)
    {
        if(p->mat.Pname[i]==name1)
            x=i;
        if(p->mat.Pname[i]==name2)
            y=i;
    }
    p->mat.m[x][y]=p->mat.m[y][x]=weight;
    while(inFile)//�����޸ĵ��ļ�����
    {
        getline(inFile, str);
        v.push_back(str);
    }
    ofstream outFile("����������Ϣ��.txt",ios::out);
     stringstream stream,stream1,stream2;
    string s,s1,ss,num,num1,w,m;
    vector<string>::const_iterator it=v.begin();
    stream<<p->mat.edge;
    stream>>num;
    p->mat.edge+=1;
    stream1<<p->mat.edge;
    stream1>>num1;
    s="�þ����ĵ�·��ĿΪ:";s1="�þ����ĵ�·��ĿΪ:";
    s+=num;s1+=num1;
    for(;v.end()!=it;++it)
    {
       if(*it==s)
            outFile<<s1<<endl;
       else
            outFile<<*it<<endl;
    }
    m="************************��"+num1+"����·,";
    outFile<<m<<endl;
    stream<<x;
    stream>>num;
    stream1<<y;
    stream1>>num1;
    s="������Ϊ"+num+"����Ϊ"+name1;
    outFile<<s<<endl;
    s="������Ϊ"+num1+"����Ϊ"+name2;
    outFile<<s<<endl;
    stream2<<weight;
    stream2>>w;
    s=name1+"��"+name2+"֮���ֱ�ӵ�·������"+w;
    outFile<<s<<endl;
    inFile.close();
    outFile.close();
    cout<<"��·����޸ĳɹ�(�����������������������ֲ�ͼ�������������Ϣ���в鿴������ֱ�Ӵ򿪾����ļ����в鿴"<<endl;
}
void change_information()
{
    int tag=1,n,key;
    Scenic *p;
    string name;
    cout<<"������Ҫ�޸ĵľ�������";
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*��Ҫ�޸ĵ�"<<name<<"���������ڣ�\n";
    else
    {
        while(p)
        {
          if(p->mat.Sname==name)
          {
              cout<<"*******����Ϊ�þ�����һЩ��Ϣ��"<<endl;
              cout<<"*******�������ƣ�"<<p->mat.Sname<<endl;
              for(int i=1;i<=p->mat.count;++i)
              {
                cout<<"���Ϊ "<<i<<' '<<"�ľ�������Ϊ "<<p->mat.Pname[i];
                for(int j=1;j<=p->mat.count;++j)
                cout<<' '<<p->mat.m[i][j];
                cout<<endl;
              }
              cout<<"�������ʾѡ���޸�*************************"<<endl;;
              cout<<"\t1���޸ĸþ�����Ӧ��������ƣ�\n";
              cout<<"\t2���޸ĸþ���ĳ����·�ϵ�Ȩֵ��\n";
              cout<<"\t3�����Ӹþ���С·��������\n";
              cout<<"\t0������������\n";
              cin>>n;
              switch(n)
              {
              case 1:
                  change_sceic_name(p);
                  break;
              case 2:
                  change_weight(p);
                  break;
              case 3:
                  increase_number(p);
                  break;
              case 0:
                  returnMainFace();
                  break;
              }
            tag=0;
            break;
          }
          else
            p=p->next;
        }
        if(tag)
            cout<<"*��Ҫ�޸ĵ�"<<name<<"����������"<<endl;
    }
    returnMainFace();

}
void returnMainFace()
{
    cout<<"\n\t\t\t��������������˵�... ...";
    getch();
    system("cls");
    MainFace();
}
void Welcome()
{
    cout<<               "\n\n\t\t******��ӭʹ�þ���������Ϣ����ϵͳ******\n\n";
    cout<<" \t \t \t �����������ϵͳ... ...";
    getch();
    MainFace();
}
void MainFace()//������
{      system("cls");
    cout<<"\n���˵���\n";
    cout<<"\t1��������������ֲ�ͼ��\n";
    cout<<"\t2�������������ֲ�ͼ���ڽӾ��󣩣�\n";
    cout<<"\t3�����������·ͼ��\n";
    cout<<"\t4���жϵ�����·ͼ���޻�·��\n";
    cout<<"\t5����ĳ���������������·������̾��룻\n";
    cout<<"\t6�������·�޽��滮ͼ��\n";
    cout<<"\t7��������о���������Ϣ��\n";
    cout<<"\t8���޸ľ���������Ϣ��\n";
    cout<<"\t0���˳���\n";
    cout<<"\n*���������ѡ��";
    char c;
    c=getch();
    cout<<c<<endl;
    while(!(c>='0'&&c<='8'))
    {
        cout<<"*�����������������룺";
        c=getch();
        cout<<c<<endl;
    }
    switch(c)
    {
        case '1':
            create_graph();break;
        case '2':
             print_graph();break;
        case '3':
            guide_line();break;//������·
        case '4':
            check_circuit();break;//�жϻ�·
        case '5':
            min_distance();break;//��̾���
        case '6':
            build_road();break;//��С������
        case '7':
            scenic_message();break;//�ļ��ļ򵥲���
        case '8':
            change_information();break;//�޸ľ���
        case '0':
            cout<<"\n\t\t\t*��������رձ�ϵͳ*\n";
            exit(0);
    }
}

