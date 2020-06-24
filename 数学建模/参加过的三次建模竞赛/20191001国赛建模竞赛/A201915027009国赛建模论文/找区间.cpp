#include <bits/stdc++.h>
using namespace std;
int main(){
	
	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	
	double a=0.02893;
	double b=3.077;
	double c=1572;
	double A=4*a*c-b*b;
			A=sqrt(A*1.0);
	double F0=100.0, s0=0.850;
	double C=log(s0)-2.0*atan((2*a*F0+b)/A)/A;//C=-0.252946
	cout<<(A*0.5*tan(A*(log())*
	double F[500],s[500];
	memset(F,0,sizeof(F));
//	cout<<0.5*(A*tan(0.5*A*(log(0.85)-C))-b)/a<<endl; 
	for(int i=0;i<21;++i){
		cin>>s[i];
	}
	for(int i=0;i<21;++i){
		//F[i]=(1/B)*1.0*(tan(((4*a*c-b*b)*(log(s[i])-C))/(4*a*1.0))-0.5*b/a);
		F[i]=0.5*(A*tan(0.5*A*(log(s[i])-C))-b)/a;
		cout<<i<<' '<<s[i]<<' '<<F[i]<<endl;
	}
	
 
	
	return 0;
} 

