#include<iostream>
#include<math.h>
using namespace std;
#define MAX_LENGTH 500
int main(){


	
	int TC;
	cin>>TC;
	//TC=1;
	while(TC--)
	{
		int n,ans=0,temp=0,mn=100000000000;
		cin>>n;
		for (int i = 0; i < n; ++i)
		{
			cin>>temp;
			mn= min(temp,mn);
			ans+=mn;
		}
		cout<<ans<<endl;
		
	}
	return 0;
}
	
