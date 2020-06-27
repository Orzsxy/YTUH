#include<cstdio>
#include<cstdlib>
#include<cstring>
struct Node{
    Node* parent;
    Node* lChild;
    Node* rChild;
    char name[30];
    int deep;
    int num;
};
const int maxn = 10010;
Node* root;
int p[maxn];
int find(int x){
    return (x == p[x]) ? p[x] : (p[x] = find(p[x]));
}
int trie[maxn][62], tot = 0;
bool vis[maxn];
int cnt = 0;
Node* tr[maxn];
int insert(char* s, Node* node){
    int rt = 0;
    int x;
    for(int i = 0; s[i]; i++){
        if(s[i] >= 'a' && s[i] <= 'z') x = s[i] - 'a';
        else if(s[i] >= 'A' && s[i] <= 'Z') x = s[i] - 'A' + 26;
        else x = s[i] - '0' + 52;
        if(trie[rt][x] == 0) trie[rt][x] = ++tot;
        rt = trie[rt][x];
    }
    tr[rt] = node;
    return rt;
}
int query(char* s){
    int rt = 0;
    int x;
    for(int i = 0; s[i]; i++){
        if(s[i] >= 'a' && s[i] <= 'z') x = s[i] - 'a';
        else if(s[i] >= 'A' && s[i] <= 'Z') x = s[i] - 'A' + 26;
        else x = s[i] - '0' + 52;
        rt = trie[rt][x];
    }
    return rt;
}
bool read(char* s, char* s1, char* s2){
    char ch;
    int len[3] = {0};
    int i = 0;
    ch = getchar();
    while(1){
        bool flag = false;
        while(ch == ' '){
            if(!flag){
                flag = true;
                if(i == 0){
                    s[len[0]] = '\0';
                }else if(i == 1){
                    s1[len[1]] = '\0';
                }else if(i == 2){
                    s2[len[2]] = '\0';
                }
                i++;
                flag = true;
            }
            ch = getchar();
        }
        if(ch == '\n' || ch == EOF){
            if(i == 1){
                s1[len[1]] = '\0';
            }else if(i == 2){
                s2[len[2]] = '\0';
            }
            break;
        }
        if(i == 0){
            s[len[0]++] = ch;
        }else if(i == 1){
            s1[len[1]++] = ch;
        }else if(i == 2){
            s2[len[2]++] = ch;
        }
        ch = getchar();
    }
    if(len[2] == 0) return false;
    else return true;
}
void build(Node* self, char* str1, char* str2){
    self->lChild = new Node;
    self->lChild->num = insert(str1, self->lChild);
    strcpy(self->lChild->name, str1);
    self->lChild->parent = self;
    self->lChild->lChild = self->lChild->rChild = NULL;
    self->lChild->deep = self->deep + 1;

    self->rChild = new Node;
    self->rChild->num = insert(str2, self->rChild);
    strcpy(self->rChild->name, str2);
    self->rChild->parent = self;
    self->rChild->lChild = self->rChild->rChild = NULL;
    self->rChild->deep = self->deep + 1;
}
void trav(Node* rt){
    printf("%s\n", rt->name);
    if(rt->lChild) trav(rt->lChild);
    if(rt->rChild) trav(rt->rChild);
}
char* ans;
bool tarjin(Node* root, int s, int t){
    bool flag = false;
    if(root->lChild) flag = tarjin(root->lChild, s, t);
    if(flag) return true;
    if(root->rChild) flag = tarjin(root->rChild, s, t);
    if(flag) return true;
    if(root->num == s && find(t) == s){
        ans = root->name;
        return true;
    }else if(root->num == t && find(s) == t){
        ans = root->name;
        return true;
    }else if(find(s) == find(t)){
        ans = root->name;
        return true;
    }
    vis[root->num] = 1;
    p[find(root->num)] = root->parent->num;
    return false;
}
int main(){
    char s[50], s1[50], s2[50];
    read(s, s1, s2);
    root = new Node;
    root->parent = NULL;
    root->deep = 1;
    root->num = ++cnt;
    strcpy(root->name, s);
    build(root, s1, s2);
    while(read(s, s1, s2)){
        int tmp = query(s);
        build(tr[tmp], s1, s2);
    }
    for(int i = 1; i < maxn; i++) p[i] = i;
    tarjin(root, query(s), query(s1));
    printf("%s", ans);
    printf(" %d", abs(tr[query(s)]->deep - tr[query(s1)]->deep));
}





