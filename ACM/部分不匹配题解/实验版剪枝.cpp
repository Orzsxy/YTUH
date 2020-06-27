#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BOARD_SIZE 12
#define EMPTY 0
#define BLACK 1
#define WHITE 2
typedef int BOOL;
#define TRUE 1
#define FALSE 0
typedef int OPTION;
#define UP 0
#define DOWN 1
#define LEFT 2
#define RIGHT 3
#define UP_LEFT 4
#define UP_RIGHT 5
#define DOWN_LEFT 6
#define DOWN_RIGHT 7
#define MAX_BYTE 10000
#define START "START"
#define PLACE "PLACE"
#define TURN  "TURN"
#define END   "END"
struct Command
{
  int x;
  int y;
  OPTION option;
};
struct Command _command={0,0,0};//用来返回棋子和方向 
char buffer[MAX_BYTE] = {0};
char board[BOARD_SIZE][BOARD_SIZE] = {0};
int me_flag;
int other_flag;
int score[12][12];
int x,y,dir;
const int DIR[8][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };
void debug(const char *str) {
  printf("DEBUG %s\n", str);
  fflush(stdout);
}
void printBoard() {
  char visual_board[BOARD_SIZE][BOARD_SIZE] = {0};
  for (int i = 0; i < BOARD_SIZE; i++) {
    for (int j = 0; j < BOARD_SIZE; j++) {
      if (board[i][j] == EMPTY) {
        visual_board[i][j] = '.';
      } else if (board[i][j] == BLACK) {
        visual_board[i][j] = 'O';
      } else if (board[i][j] == WHITE) {
        visual_board[i][j] = 'X';
      }
    }
    printf("%s\n", visual_board[i]);
  }
}
BOOL isInBound(int x, int y) {
  return x >= 0 && x < BOARD_SIZE && y >= 0 && y < BOARD_SIZE;
}
 BOOL place_new(int x, int y, OPTION option, int cur_flag,char (*board)[12]) //判断下一步能不能走棋 
 {
	int new_x = x + DIR[option][0];
	int new_y = y + DIR[option][1];
	if (isInBound(new_x, new_y)&&board[new_x][new_y] == EMPTY) 
		return TRUE;
		else
		return FALSE;
}
void move(int x, int y, OPTION option, int cur_flag,char board[12][12])//在新棋盘里面移动棋子并改变棋盘 
 {
    int new_x = x + DIR[option][0];
  int new_y = y + DIR[option][1];
   board[x][y] = EMPTY;
  board[new_x][new_y] = cur_flag;
  int cur_other_flag = 3 - cur_flag;
  int intervention_dir[4][2] = { {1, 0}, {0, 1}, {1, 1}, {1, -1} };
  for (int i = 0; i < 4; i++) {
    int x1 = new_x + intervention_dir[i][0];
    int y1 = new_y + intervention_dir[i][1];
    int x2 = new_x - intervention_dir[i][0];
    int y2 = new_y - intervention_dir[i][1];
    if (isInBound(x1, y1) && isInBound(x2, y2) && board[x1][y1] == cur_other_flag && board[x2][y2] == cur_other_flag) {
      board[x1][y1] = cur_flag;
      board[x2][y2] = cur_flag;
    }
  }
  int custodian_dir[8][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1} };
  for (int i = 0; i < 8; i++) {
    int x1 = new_x + custodian_dir[i][0];
    int y1 = new_y + custodian_dir[i][1];
    int x2 = new_x + custodian_dir[i][0] * 2;
    int y2 = new_y + custodian_dir[i][1] * 2;
    if (isInBound(x1, y1) && isInBound(x2, y2) && board[x2][y2] == cur_flag && board[x1][y1] == cur_other_flag) {
      board[x1][y1] = cur_flag;
    }
  }
}
int SCORE(char board[12][12])//估值函数，由棋盘数值和棋子数量组成 
{
	int black=0,white=0,s2=0;
	int ss,scoresum;
score[0][0]=score[11][0]=score[0][11]=score[11][11]=100;
	for(int i=0;i<11;i++)
	{
		score[0][i]=score[i][0]=score[11][i]=score[i][11]=50;
	}
	for(int i=3;i<9;i++)
	{
		for(int j=3;j<9;j++)
		score[i][j]=600;
	}
	for(int i=0;i<12;i++)
	for(int j=0;j<12;j++)
	{
		if(board[i][j]==me_flag)
		{
			black++;
			s2=s2+score[i][j];
		}
		else if(board[i][j]==3-me_flag)
		{
			white++;
		}
	}
		ss=black-white;
		scoresum=1000*ss+s2;
	return scoresum;
}
int Search(char board[12][12],int deep,int me_flag,int cut)//剪枝 
{
	int alpha=-10000,beta,other_flag;
	beta=cut;
if(me_flag==1)
other_flag=2;
else if(me_flag==2)
other_flag=1;
	int score,scoresum=-10000,i,j,a;
	char newboard[12][12];
	for(int m=0;m<12;m++)
	for(int n=0;n<12;n++)
		newboard[m][n]=board[m][n];
   for(i=0;i<12;i++)
	{
		for(j=0;j<12;j++)
		{
			if(board[i][j]==me_flag)
			{
				for(a=0;a<8;a++)
				{
						if (place_new(i, j, a, me_flag, newboard) == 1)
						{
							move(i,j,a,me_flag,newboard);
							if(deep==4)
							score=-SCORE(newboard);
							else
							score=-Search(newboard,deep+1,other_flag,-alpha);
							for(int u=0;u<12;u++)
							for(int v=0;v<12;v++)
								newboard[u][v]=board[u][v];
							if(scoresum<=score)
							{
									scoresum=score;
								alpha=score;
								if(deep==1)
								{
								
								_command.x=i;
								_command.y=j;
								_command.option=a;
								}
							}
								if(alpha>beta)
							return scoresum;
						}
						else
						continue;
				}
	}
}
}
	return scoresum;
}
BOOL place(int x, int y, OPTION option, int cur_flag) {
    if (board[x][y] != cur_flag) {
    return FALSE;
  }
  int new_x = x + DIR[option][0];
  int new_y = y + DIR[option][1];
    if (!isInBound(new_x, new_y) || board[new_x][new_y] != EMPTY) {
    return FALSE;
  }
  board[x][y] = EMPTY;
  board[new_x][new_y] = cur_flag;
  int cur_other_flag = 3 - cur_flag;
  int intervention_dir[4][2] = { {1, 0}, {0, 1}, {1, 1}, {1, -1} };
  for (int i = 0; i < 4; i++) {
    int x1 = new_x + intervention_dir[i][0];
    int y1 = new_y + intervention_dir[i][1];
    int x2 = new_x - intervention_dir[i][0];
    int y2 = new_y - intervention_dir[i][1];
    if (isInBound(x1, y1) && isInBound(x2, y2) && board[x1][y1] == cur_other_flag && board[x2][y2] == cur_other_flag) {
      board[x1][y1] = cur_flag;
      board[x2][y2] = cur_flag;
    }
  }
  int custodian_dir[8][2] = { {1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1} };
  for (int i = 0; i < 8; i++) {
    int x1 = new_x + custodian_dir[i][0];
    int y1 = new_y + custodian_dir[i][1];
    int x2 = new_x + custodian_dir[i][0] * 2;
    int y2 = new_y + custodian_dir[i][1] * 2;
    if (isInBound(x1, y1) && isInBound(x2, y2) && board[x2][y2] == cur_flag && board[x1][y1] == cur_other_flag) {
      board[x1][y1] = cur_flag;
    }
  }
  return TRUE;
}
void start(int flag) {
  memset(board, 0, sizeof(board));
  for (int i = 0; i < 3; i++) {
    board[2][2 + i] = WHITE;
    board[6][6 + i] = WHITE;
    board[5][3 + i] = BLACK;
    board[9][7 + i] = BLACK;
  }

  for (int i = 0; i < 2; i++) {
    board[8 + i][2] = WHITE;
    board[2 + i][9] = BLACK;
  }
}
  void turn() {
  	Search(board,1,me_flag,10000);
 struct Command command = _command;//这个地方有所改动，其余地方没有改变 
  place(command.x, command.y, command.option, me_flag);
  printf("%d %d %d\n", command.x, command.y, command.option);
  fflush(stdout);
}
void end(int x) {

}
void loop() {
  while (TRUE)
  {
    memset(buffer, 0, sizeof(buffer));
    gets(buffer);

    if (strstr(buffer, START))
    {
      char tmp[MAX_BYTE] = {0};
      sscanf(buffer, "%s %d", tmp, &me_flag);
      other_flag = 3 - me_flag;
      start(me_flag);
      printf("OK\n");
      fflush(stdout);
    }
    else if (strstr(buffer, PLACE))
    {
      char tmp[MAX_BYTE] = {0};
      int x, y;
      OPTION option;
      sscanf(buffer, "%s %d %d %d", tmp, &x, &y, &option);
      place(x, y, option, other_flag);
    }
    else if (strstr(buffer, TURN))
    {
      turn();
    }
    else if (strstr(buffer, END))
    {
      char tmp[MAX_BYTE] = {0};
      int x;
      sscanf(buffer, "%s %d", tmp, &x);
      end(x);
    }
  }
}
int main(int argc, char *argv[]) {
  loop();
  return 0;
}
