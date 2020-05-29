#include <iostream>

using namespace std;

int main()
{   int t,n,temp,max;
    
    cin>>t;
    
    while(t--){
        cin>>n;
        //int a[n];
        
        /*for(int i=0;i<n;i++){
            cin>>a[i];
        }
        
        int max=a[0];
        int count=0;
    
        for(int i=0;i<n;i++){
            if(max>=a[i]){
                count++;
                max=a[i];
            }
        }*/
        cin>>max;
        int count=1;
        while(--n){
            cin>>temp;
            if(temp<=max){
                max=temp;
                count++;
            }
            
        }
    
        cout<<count<<endl;
    }
    return 0;
}
