#include <iostream>
#include <cstring>
#include <malloc.h>
#include <cstdio>
#define M 100
#define INF 999666333
using namespace std;
 struct Matrix
{
    string Sname;//��������,Ϊ�˽����ϣ��ͻ
    int count;//����������
    int edge;//��·����
    int m[M][M];//�����ڽӾ���
    string Pname[M];//�������������
};
struct Scenic
{
   Scenic(): next(NULL){}
    Matrix mat;
   struct Scenic *next;
};
int hash(string name);
void Welcome();//��ӭ����
void create_graph();//������������ͼ
void print_graph();//�������ֲ����ڽӾ������ʽ�����
void DFS(int c,struct Scenic *p);//�����������������·
void guide_line();//������·
void dfs(int i,struct Scenic *p);//�ݹ�ʵ��
void check_circuit();//�жϻ�·
void Floyd(int a,int b,struct Scenic *&p);//Floyd�㷢�����·
void min_distance();//���·��������
void prime(struct Scenic *&p,string name);//��С��������prime�㷨��
void build_road();//��·�޽��滮ͼ��
void scenic_message();//������о���������Ϣ
void change_sceic_name(struct Scenic *&p);//�޸ľ������ƣ�
void change_weight(struct Scenic *&p);//�޸ĸþ���ĳ����·�ϵ�Ȩֵ
void increase_number(struct Scenic *&p);//���Ӹþ���С·������
void change_information();//�޸ľ���������Ϣ
void MainFace();//������
void returnMainFace();//����������
