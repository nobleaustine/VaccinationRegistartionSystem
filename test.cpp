#include<iostream>
#include<fstream>
using namespace std;
int main()
{
 ofstream myfile;
 myfile.open("test.csv");
 for( int i=0 ; i<20; i++)
 {
    myfile << i << "," << i*i << endl;
 }
}