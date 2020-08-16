#include <iostream> 
using namespace std; 
  
int main(int argc, char** argv) 
{  

    for(int j = 0; j < *(argv[1]) - 48; j++){
        for (int i = 2; i < argc; ++i) 
        cout << argv[i] << "\n"; 
    }
    
    return 0; 
}