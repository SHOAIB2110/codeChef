#include<iostream>
using namespace std;
#define MAX_LENGTH 5000000
int main(){
	int t;
	cin>>t;
	while(t--){
		int n;
		char s[MAX_LENGTH];
		cin>>n;
		cin>>s;
		int aCnt=0,bCnt=0,aAtmt=0,bAtmt=0;
		int result=0;
		for(int i=0;i<2*n;i++){
			if(i%2==0){
				if(s[i]=='1')
					aCnt++;
				aAtmt++;

			}
			else{
				if(s[i]=='1')
					bCnt++;
				bAtmt++;
			}
			if(aCnt-bCnt>(n-bAtmt)){
				result=i+1;
				break;
			}
			else
				if (bCnt-aCnt >(n-aAtmt))
				{result=i+1;
					break;
					
				}
		}
		if(result==0){
			result=2*n;
		}
		cout<<result<<"\n";
	}
}
