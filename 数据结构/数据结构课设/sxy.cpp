#include <iostream>
#include <cstring>
#include <fstream>
#include <malloc.h>
#include <cstdio>
#include <sstream>
#include <vector>
#include<conio.h>//getch
#include<cstdlib>//清屏函数头文件
#define l 1<<10
#define mod (1<<10)-1
#include "sxy.h"
using namespace std;
Scenic S[10000];
//用哈希表的形式进行建立查找景区名称地址
int Hash(string name)
{
    int key=0,t=name.size();
    for(int i=0;i<t;++i)
        key+='0'-name[i];
        key&=mod;
    return key;
}
//创建一个景区(邻接矩阵形式）
void create_graph()
{
	ofstream outFile;  //输出流对象
	outFile.open("景区景点信息表.txt",ios::app);  //将输出流对象和输出文件建立关联
    string name;
    int i,n1,n2,key;
    cout<<"\n*请输入景区的名称：";
    cin>>name;
    getchar();
    key=Hash(name);
    Scenic *p=new Scenic,*q=new Scenic;
    q=S[key].next;
    while(q)//不为空时说明该位置存在景区（ASCII可以相同）
    {
        if(q->mat.Sname==name)//名称不能相同，才可以输入景区
          {
             cout<<"该景点名称已存在，重新输入景点名称: ";
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
    //包含文件操作
    outFile<<"*****************************************************************"<<endl;
    outFile<<"景区名称为"<<name<<"的景点信息如下"<<endl;
    cout<<"\n*请输入该景区的景点总数目：";
    cin>>p->mat.count;
    outFile<<"该景区的景点总数目为:"<<p->mat.count<<endl;
    cout<<"\n*请输入景区的道路总数目：";
    cin>>p->mat.edge;
    outFile<<"该景区的道路数目为:"<<p->mat.edge<<endl;
    cout<<"\n*请输入道路两边连接的两个景点编号、名称及道路的长度\n";
    outFile<<"*各个道路连接的两个景点编号、名称及道路的长度信息如下："<<endl;
    memset(p->mat.m,0,sizeof(p->mat.m));
    for(i=1;i<=p->mat.edge;i++)
    {
            cout<<"\n*第 "<<i<<" 条道路\n";
            cout<<"\t-景点 1 编号：";
            cin>>n1;
            outFile<<"************************第"<<i<<"条道路,"<<endl;
            cout<<"\t-景点 1 名称：";cin>>p->mat.Pname[n1];
            outFile<<"景点编号为"<<n1<<"名称为"<<p->mat.Pname[n1]<<endl;
            cout<<"\t-景点 2 编号：";cin>>n2;
            cout<<"\t-景点 2 名称：";cin>>p->mat.Pname[n2];
            outFile<<"景点编号为"<<n2<<"名称为"<<p->mat.Pname[n2]<<endl;
            cout<<"\t-两景点之间的道路长度：";cin>>p->mat.m[n1][n2];
            outFile<<p->mat.Pname[n1]<<"和"<<p->mat.Pname[n2]<<"之间的直接道路长度是"<<p->mat.m[n1][n2]<<endl;
            p->mat.m[n2][n1]=p->mat.m[n1][n2];

    }
    p->next=S[key].next;
    S[key].next=p;
    cout<<"\n*景区创建成功！";
    outFile.close();  //关闭文件
     returnMainFace();
}
//输出景点分布（邻接矩阵的形式输出）
void print_graph()
{
    string name;
    int key,tag=1;
    Scenic *p;
    cout<<"*景区名称："<<endl;
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*景区景点分布图为"<<name<<"的景区查询不成功！\n";
    else
    {
        while(p)
        {
          if(p->mat.Sname==name)//找到的地址不为空，只有名字相同时才，进行输出有关信息
          {
            cout<<"*************查询景区名称为 "<<name<<" 的各景点分布图如下（以邻接矩阵表示）： "<<endl;
            for(int i=1;i<=p->mat.count;++i)
            {
                cout<<"景点名称 "<<p->mat.Pname[i];
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
        cout<<"\n*景区景点分布图为"<<name<<"的景区查询不成功！\n";

    }
      returnMainFace();
}
//深度优先搜索导游线路
int visited[100]={0};
int np;//找到的景点个数，用于在递归时找到出口
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
//导游线路
void guide_line()
{
     //checked();
     Scenic *p;
     int key,c,tag=1;
     cout<<"\n*请输入对应景区的名称：";
     string name;
     cin>>name;
     getchar();
     key=Hash(name);
    p=S[key].next;
    if(p==NULL)
      cout<<"\n*景区景点分布图（邻接矩阵表示）查询不存在！\n";
    else
    {
        while(p)
        {
            if(p->mat.Sname==name)
            {
                memset(visited,0,sizeof(visited));
                np=0;
                cout<<"输入对应景点的编号"<<endl;
                cin>>c;
                cout<<"*形成的导游线路图（采用深度优先策略）如下所示：\n\n\t";
                DFS(c,p);
                tag=0;
                break;
            }
            else
                p=p->next;
        }
        if(tag)
        cout<<"\n*景区景点分布图为"<<name<<"的景区查询不成功！\n";
     }
    returnMainFace();
}
int DFS_Count;
int vis[100];
void dfs(int i,struct Scenic *p)
{
    vis[i]=1;//标记顶点i被访问
    for(int j=1;j<=p->mat.count;j++)
    {
        if(p->mat.m[i][j]!=0&&vis[j]==0)
            dfs(j,p);
    }
}
//判断回路
void check_circuit()
{
    int key,tag=1;
    Scenic *p;
    string name;
    cout<<"*景区名称："<<endl;
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*景区景点分布图查询不成功！\n";
    else
    {
        while(p)
        {
            if(p->mat.Sname==name)
            {
                memset(vis,0,sizeof(vis));//初始化vis数组，表示一开始所有顶点都未被访问过
                DFS_Count=0;
                for(int i=1;i<=p->mat.count;i++)//深度优先搜索
                {
                    if(vis[i]==0)//如果这个顶点为被访问过，则从i顶点出发进行深度优先遍历
                    {
                        DFS_Count++;//统计调用void dfs(int i);的次数
                        dfs(i,p);
                    }
                }
                if(p->mat.edge+DFS_Count>p->mat.count)//遍历结束，若联通的数量个数加上边的数量个数>节点的数量个数，就判定为有环
                    cout<<"该景区中存在环"<<endl;
                else
                    cout<<"该景区中不存在环"<<endl;
                    tag=0;
                    break;
            }
            else
                p=p->next;
        }
        if(tag)
          cout<<"\n*景区景点分布图查询不成功！\n";
    }
    returnMainFace();
}
//Floyd算发求最短路
void Floyd(int a,int b,struct Scenic *&p)
{
    int i,j,k;
    int A[M][M],path[M][M];
    for(i=1;i<=p->mat.count;i++)//对进行求最短路的矩阵进行处理
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
        cout<<"\n*从 "<<p->mat.Pname[a]<<" 到 "<<p->mat.Pname[b]<<" 的最短路径为：";
        k=path[a][b];
        d=0;
        apath[d]=b;
       while(k!=-1&&k!=a)//循环实现记录对应的节点编号
       {
           d++;
           apath[d]=k;
           k=path[a][k];
       }
         d++;
         apath[d]=a;
         cout<<p->mat.Pname[apath[d]];
         cout<<apath[d];
         for(int s=d-1;s>=0;s--)//输出节点名称
         {
            cout<<" --> "<<p->mat.Pname[apath[s]];
             cout<<','<<apath[s];
         }
          cout<<" ，最短距离为："<<A[a][b]<<endl;
    }
    else if(a==b)
      cout<<"\n*景点编号输入不合法！\n";
    else
     cout<<"\n*这两个景点间不存在路径\n";
}
//最短路径、距离
void min_distance()
{
    Scenic *p;//=new Scenic;
    string name;
    int a,b,key,tag=1;
    cout<<"*景区名称："<<endl;
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*景区分布图查询不成功！\n";
    else
    {
        while(p)
        {
            if(p->mat.Sname==name)
            {
                cout<<"*******下面为该景区的一些信息："<<endl;
                cout<<"*******景区名称："<<p->mat.Sname<<endl;
                for(int i=1;i<=p->mat.count;++i)
                {
                    cout<<"编号为 "<<i<<' '<<"的景点名称为 "<<p->mat.Pname[i];
                    for(int j=1;j<=p->mat.count;++j)
                        cout<<' '<<p->mat.m[i][j];
                        cout<<endl;
                }
                cout<<"*请输入要查询的 最短路径和最短距离 的两个景点的编号：\n";
                cout<<"\t-景点 1：";
                cin>>a;
                getchar();
                cout<<"\t-景点 2：";
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
        cout<<"\n*景区景点分布图查询不成功！\n";
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
                cout<<"请输入您开始要建造的景点编号";
                cin>>a;
                cout<<"请输入您要完成到的达景点编号";
                cin>>b;
                cout<<"\n*道路修建规划图（prime算法）规划如下：\n";
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
                    cout<<"\t-修建的第 "<<++num<<" 条路为：景点  "<<p->mat.Pname[closest[k]]<<"  到景点  "<<p->mat.Pname[k]<<"  ，该条道路长度为："<<min<<endl;
                    sum+=lowcost[k];
                    lowcost[k]=0;
                    if(k==b)
                    {
                        cout<<"从景点  "<<a<<" 到景点  "<<b<<" 的总路径长度为 "<<sum<<endl;
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
            cout<<"\n*景区景点分布图查询不成功！\n";
}
void build_road()//道路修建规划图、最小生成树（prime算法）
{
    Scenic *p;
     int key;
     cout<<"\n*请输入对应景区的名称：";

     string name;
     cin>>name;
     getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
      cout<<"\n*景区景点分布图（邻接矩阵表示）查询不存在！\n";
    else
    {
        prime(p,name);
        returnMainFace();
    }
}
void scenic_message()//文件输出所有信息
{
    system("cls");
    char ch[200];
   ifstream inFile; //输入流对象
   inFile.open("景区景点信息表.txt",ios::in);
   while(!inFile.eof())
   {
       inFile.getline(ch,sizeof(ch),'\n');
       cout<<ch<<endl;
   }
   returnMainFace();
}
//修改景点名称；
void change_sceic_name(struct Scenic *&p)
{
    int i;
    string name,rname,str;
    ifstream inFile("景区景点信息表.txt",ios::in);
    vector<string> v;
    cout<<"请输入原先的景点名称: ";
    cin>>name;
    cout<<"请输入要修改后的名称： ";
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
    stream << i; //将int输入流
    stream >> r; //从stream中抽取前面插入的int值
    s="景点编号为"+r;
    s+="名称为";
    a=s;
    s+=name;
    a+=rname;
    ofstream outFile("景区景点信息表.txt",ios::out);
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
    cout<<"景点名称修改成功(您可以在主界面下输出景点分布图和者浏览景区信息进行查看，或者直接打开景区文件进行查看"<<endl;
}
void change_weight(struct Scenic *&p)
{
    int weight,weight1,i,x=0,y=0;
    string name1,name2,a,b,str;
    ifstream inFile("景区景点信息表.txt",ios::in);
    vector<string> v;
    cout<<"请输入的该道路上景点1的名称: ";
    cin>>name1;
    cout<<"请输入的该道路上景点2的名称: ";
    cin>>name2;
    cout<<"请输入的该道路上原先的权值: ";
    cin>>weight;
    cout<<"请输入该道路上要修改后的的权值: ";
    cin>>weight1;
    for( i=1;i<=p->mat.count;++i)//修改到程序里面
    {
        if(p->mat.Pname[i]==name1)
            x=i;
        if(p->mat.Pname[i]==name2)
            y=i;
    }
    p->mat.m[x][y]=p->mat.m[y][x]=weight1;
    while(inFile)//下面修改到文件里面
    {
        getline(inFile, str);
        v.push_back(str);
    }
    //outFile<<p->mat.Pname[n1]<<"和"<<p->mat.Pname[n2]<<"之间的直接道路长度是"<<p->mat.m[n1][n2]<<endl;
    stringstream stream,stream1;
    string ss,s,w,w1;// std::string result;
    stream << weight; //将int输入流
    stream >> w; //从stream中抽取前面插入的int值
    stream1 << weight1; //将int输入流
    stream1 >> w1; //从stream中抽取前面插入的int值
    s=name1;ss=name2;
    s+="和";ss+="和";
    s+=name2;ss+=name1;
    s+="之间的直接道路长度是";ss+="之间的直接道路长度是";
    a=s;b=ss;
    s+=w;ss+=w;
    a+=w1;b+=w1;
    ofstream outFile("景区景点信息表.txt",ios::out);
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
    cout<<"景点名称修改成功(您可以在主界面下输出景点分布图和者浏览景区信息进行查看，或者直接打开景区文件进行查看"<<endl;
}
void increase_number(struct Scenic *&p)
{
    string name1,name2,str;
    int i,x=0,y=0,weight;
    ifstream inFile("景区景点信息表.txt",ios::in);
    vector<string> v;
    cout<<"请输入小路两旁的1景区";
    cin>>name1;
    cout<<"请输入小路两旁的2景区";
    cin>>name2;
    cout<<"请输入该小路的权值";
    cin>>weight;
    for(i=1;i<=p->mat.count;++i)
    {
        if(p->mat.Pname[i]==name1)
            x=i;
        if(p->mat.Pname[i]==name2)
            y=i;
    }
    p->mat.m[x][y]=p->mat.m[y][x]=weight;
    while(inFile)//下面修改到文件里面
    {
        getline(inFile, str);
        v.push_back(str);
    }
    ofstream outFile("景区景点信息表.txt",ios::out);
     stringstream stream,stream1,stream2;
    string s,s1,ss,num,num1,w,m;
    vector<string>::const_iterator it=v.begin();
    stream<<p->mat.edge;
    stream>>num;
    p->mat.edge+=1;
    stream1<<p->mat.edge;
    stream1>>num1;
    s="该景区的道路数目为:";s1="该景区的道路数目为:";
    s+=num;s1+=num1;
    for(;v.end()!=it;++it)
    {
       if(*it==s)
            outFile<<s1<<endl;
       else
            outFile<<*it<<endl;
    }
    m="************************第"+num1+"条道路,";
    outFile<<m<<endl;
    stream<<x;
    stream>>num;
    stream1<<y;
    stream1>>num1;
    s="景点编号为"+num+"名称为"+name1;
    outFile<<s<<endl;
    s="景点编号为"+num1+"名称为"+name2;
    outFile<<s<<endl;
    stream2<<weight;
    stream2>>w;
    s=name1+"和"+name2+"之间的直接道路长度是"+w;
    outFile<<s<<endl;
    inFile.close();
    outFile.close();
    cout<<"道路添加修改成功(您可以在主界面下输出景点分布图和者浏览景区信息进行查看，或者直接打开景区文件进行查看"<<endl;
}
void change_information()
{
    int tag=1,n,key;
    Scenic *p;
    string name;
    cout<<"输入您要修改的景区名称";
    cin>>name;
    getchar();
    key=Hash(name);
    p=S[key].next;
    if(p==NULL)
     cout<<"\n*您要修改的"<<name<<"景区不存在！\n";
    else
    {
        while(p)
        {
          if(p->mat.Sname==name)
          {
              cout<<"*******下面为该景区的一些信息："<<endl;
              cout<<"*******景区名称："<<p->mat.Sname<<endl;
              for(int i=1;i<=p->mat.count;++i)
              {
                cout<<"编号为 "<<i<<' '<<"的景点名称为 "<<p->mat.Pname[i];
                for(int j=1;j<=p->mat.count;++j)
                cout<<' '<<p->mat.m[i][j];
                cout<<endl;
              }
              cout<<"请根据提示选择修改*************************"<<endl;;
              cout<<"\t1、修改该景区对应景点的名称；\n";
              cout<<"\t2、修改该景区某条道路上的权值；\n";
              cout<<"\t3、增加该景区小路的数量；\n";
              cout<<"\t0、返回主界面\n";
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
            cout<<"*您要修改的"<<name<<"景区不存在"<<endl;
    }
    returnMainFace();

}
void returnMainFace()
{
    cout<<"\n\t\t\t按任意键返回主菜单... ...";
    getch();
    system("cls");
    MainFace();
}
void Welcome()
{
    cout<<               "\n\n\t\t******欢迎使用景区旅游信息管理系统******\n\n";
    cout<<" \t \t \t 按任意键进入系统... ...";
    getch();
    MainFace();
}
void MainFace()//主界面
{      system("cls");
    cout<<"\n主菜单：\n";
    cout<<"\t1、创建景区景点分布图；\n";
    cout<<"\t2、输出景区景点分布图（邻接矩阵）；\n";
    cout<<"\t3、输出导游线路图；\n";
    cout<<"\t4、判断导游线路图有无回路；\n";
    cout<<"\t5、求某个景区景点间的最短路径和最短距离；\n";
    cout<<"\t6、输出道路修建规划图；\n";
    cout<<"\t7、浏览所有景区景点信息；\n";
    cout<<"\t8、修改景区景点信息；\n";
    cout<<"\t0、退出。\n";
    cout<<"\n*请输入操作选择：";
    char c;
    c=getch();
    cout<<c<<endl;
    while(!(c>='0'&&c<='8'))
    {
        cout<<"*输入有误，请重新输入：";
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
            guide_line();break;//导游线路
        case '4':
            check_circuit();break;//判断回路
        case '5':
            min_distance();break;//最短距离
        case '6':
            build_road();break;//最小生成树
        case '7':
            scenic_message();break;//文件的简单操作
        case '8':
            change_information();break;//修改景区
        case '0':
            cout<<"\n\t\t\t*按任意键关闭本系统*\n";
            exit(0);
    }
}

