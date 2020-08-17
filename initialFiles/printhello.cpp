#include <iostream> 
#include <stdlib.h>
#include <fstream>

using namespace std; 
  
int main(int argc, char** argv) 
{  
    
    ofstream myfile;
    myfile.open ("example.txt");

    for (int i = 1; i < argc; ++i){ 
        myfile << argv[i] << "\n";
    }
    myfile.close();

    cout << "File written successfully\n";
    
    return 0; 
}