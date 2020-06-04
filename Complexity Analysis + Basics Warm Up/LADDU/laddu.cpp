#include<iostream>
#include<string>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    while(t--){
        int n;
        long long int sum=0;
        string country;
        cin>>n;
        cin>>country;
        
        while(n--){
            string activity;
            cin>>activity;
            if(activity=="CONTEST_WON") {
                int rank;cin>>rank;
                if(rank<20){
                    sum+=300+20-rank;
                }
                else
                    sum+=300;
            }
                
            
            else if (activity=="TOP_CONTRIBUTOR")
            {
                sum+=300;
            }
            else if (activity=="BUG_FOUND")
            {
                int severity;
                cin>>severity;
                sum+=severity;
            }
            else if(activity=="CONTEST_HOSTED")
                sum+=50;
        }

        if(country=="NON_INDIAN")
        {
           cout<<sum/400<<"\n";
        }
        else 
        {
            cout<<sum/200<<"\n";
        }
    }
    return 0;
}
