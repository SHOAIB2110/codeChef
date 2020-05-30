#include <iostream>
using namespace std;

int main() {
	// your code goes here
    int t;
    cin>>t;
    while(t--){
        int count=0,n,c=5;
        cin>>n;
       
    //   for(i=5; n/i>0 ;i*=5){
    //       count+=n/i;
           
           
    //   }  
    
    while((n/c)>0){
       count+= n/c;
       c=c*5;
    }
        cout<<count<<endl;
    }
	return 0;
}
