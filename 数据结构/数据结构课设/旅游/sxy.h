#include <iostream>
#include <cstring>
#include <malloc.h>
#include <cstdio>
#define M 100
#define INF 999666333
using namespace std;
 struct Matrix
{
    string Sname;//景区名称,为了解决哈希冲突
    int count;//景点总数量
    int edge;//道路数量
    int m[M][M];//景点邻接矩阵
    string Pname[M];//各个景点的名称
};
struct Scenic
{
   Scenic(): next(NULL){}
    Matrix mat;
   struct Scenic *next;
};
int hash(string name);
void Welcome();//欢迎界面
void create_graph();//创建景区景点图
void print_graph();//输出景点分布（邻接矩阵的形式输出）
void DFS(int c,struct Scenic *p);//深度优先搜索导游线路
void guide_line();//导游线路
void dfs(int i,struct Scenic *p);//递归实现
void check_circuit();//判断回路
void Floyd(int a,int b,struct Scenic *&p);//Floyd算发求最短路
void min_distance();//最短路径、距离
void prime(struct Scenic *&p,string name);//最小生成树（prime算法）
void build_road();//道路修建规划图、
void scenic_message();//浏览所有景区景点信息
void change_sceic_name(struct Scenic *&p);//修改景点名称；
void change_weight(struct Scenic *&p);//修改该景区某条道路上的权值
void increase_number(struct Scenic *&p);//增加该景区小路的数量
void change_information();//修改景区景点信息
void MainFace();//主界面
void returnMainFace();//返回主界面
