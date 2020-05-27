/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin>>n;
    long long a[n];
    
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    
    sort(a,a+n);
    
    long long rev;
    long long maxP=0;
    
    for(int i=0;i<n;++i){
        rev=a[i]*(n-i);
        maxP=max(rev,maxP);
    }
   cout<<maxP;
    
    
    
    
}
