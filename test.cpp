#include<iostream>
#include<fstream>
#include <cstring>

using namespace std;
int main()
{
 ofstream myfile;
 myfile.open("test.csv",ofstream::app);
 int inp=1;
 while(inp==1){
    int id;
    string name;
    cout<<"name\n";
    cin>>name;
    cout<<"id\n";
    cin>>id;

    cout<<"ctnu?\n";
    cin>>inp;

    myfile << id << "," << name << endl;
 }
//  for( int i=0 ; i<20; i++)
//  {
//     myfile << i << "," << i*i << endl;
//  }

ifstream myFile;
myFile.open("test.csv");
while(myFile.good()) {
   string line;
   getline(myFile , line, ',');
   cout<<line<<endl;
}
myFile.close();
}
