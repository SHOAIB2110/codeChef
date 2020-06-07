#include<iostream>
#include <stdlib.h> 
using namespace std;
#define lli long long int
#define rep(i,n) for(int i=0;i<n;i++)

int main(){
int t;
cin>>t;
while(t--){
    int n,k;
    cin>>n>>k;
    lli a[n];
    rep(i,n) cin>>a[i];
    
    lli sum=0,sum1=0;
    
    rep(i,n) sum+=a[i];

    rep(i,n) {
        if(a[i]>k){
             a[i]=k;
            sum1+=a[i];       
        }
        else
        {
          sum1+=a[i];
        }
    }
    cout<<abs(sum-sum1)<<"\n";

}
return 0;
}
