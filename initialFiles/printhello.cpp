#include <iostream> 
#include <stdlib.h>
#include <fstream>

using namespace std; 
  
int main(int argc, char** argv) 
{  
    
    /*
    ofstream myfile;
    myfile.open ("example.txt");

    for (int i = 1; i < argc; ++i){ 
        myfile << argv[i] << "\n";
    }
    myfile.close();

    cout << "File written successfully\n";
    
    return 0; 
    */
   ofstream myfile ("hello.txt");
    if (myfile.is_open())
    {
        myfile << "This is a line.\n";
        myfile << "This is another line.\n";
        myfile.close();
    }
    else cout << "Unable to open file";
    return 0;
}