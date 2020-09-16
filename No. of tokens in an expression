#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;
    int i=0;
    int c = 0,var = 0,opr = 0;
    while(i < s.length())
    {
        if(isdigit(s[i]) && (isdigit(s[i+1])))
          {
          i=i++;
          }
       else if(isdigit(s[i]) && !(isdigit(s[i+1])))
          {
          c++;
          i++;
          }
        else if(isalpha(s[i]) && (isalpha(s[i+1])))
        {
          i++;
        }
         else if(isalpha(s[i]) && !(isalpha(s[i+1])))
        {
          var++;
          i++;
        }
        else 
        {
          opr++;
          i++;
        }
    }
    cout<<"operators : "<<opr<<" "<<"variables :"<<var<<" "<<"constants :"<<" "<<c<<"tokens :"<<var+opr+c<<endl;
    return 0;
}
