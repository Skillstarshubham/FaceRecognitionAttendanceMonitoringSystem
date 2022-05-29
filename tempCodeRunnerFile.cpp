#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[n][3];
    int i=0;
    int y=1;
    while(n--){
        cin>>a[i][0]>>a[i][1]>>a[i][2];
        i++;
    }
    while(i--){
        if(a[i][0]+a[i][1]+a[i][2]!=0){
            y=0;
            break;
        }
    }
    if(y==1){
        cout<<"YES"<<endl;
    }
    else{
        cout<<"NO"<<endl;
    }

    return 0;
}