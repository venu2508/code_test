/*Basic program demonstrating
 C++ Maps*/
#include<iostream>
#include<string>
#include<map>
using namespace std;
int main()
{
 map<int,string>ClassInfo;
 ClassInfo.insert(pair<int,string>(1,"Krishna"));
 ClassInfo[2]="Shiva";
 ClassInfo[3]="Guna";
 map<int,string>::iterator iter=ClassInfo.find(1);
 cout<<"Roll Number "<<iter->first<<" is "<<iter->second<<endl;
/*iter->first denotes the first part of the map which is "int" and iter->second denotes the second part of the map which is "string"*/
 return 0;
}
