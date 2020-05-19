#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	int i;
	cin>>t;
	while(t--){
	 int n;
	 cin>>n;
	 
	 int arr[n];
	 
	 for(i=0;i<n;i++){
	     cin>>arr[i];
	 }
	 
	 int diff[n];
	 for(i=1;i<n;i++){
	     diff[i]=arr[i]-arr[i-1];
	     }
	   int min=100,max=-1,count=1;  
	     
	 for(i=1;i<n;i++){
	     if(diff[i]<=2){
	         count++;
	     }
	     else{
	         if(min>count)
	            min=count;
	         if(max<count)
	            max=count;
	         count=1;
	     }
	 }
	 if(min>count)
         min=count;
	 if(max<count)
	      max=count;
	     
	 cout<<min<<" "<<max<<"\n"; 
	}
	return 0;
}
