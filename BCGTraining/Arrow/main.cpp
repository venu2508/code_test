#include<iostream>
#include"Arrow.h"
using namespace std;
int main()
{

 Arrow Aobj;
 Arrow *Aptr=&Aobj;
 Aobj.Print();
 Aptr->Print();

return 0;
}
