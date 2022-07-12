#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;
 
// Main() function: where the execution of program begins
int main()
{
    int npoints,nsize;
    npoints = 1000;
    nsize = 1020;
    float u_xy[nsize][nsize], added[nsize][nsize];
    for(int i=1; i<=npoints; i++)
    {
        for(int j=1;j<=npoints;j++)
        {
            u_xy[i][j]=0;
            added[i][j]=1;
        }    
    }
    auto start = high_resolution_clock::now();
    for(int k=1; k<=2000; k++)
    {
        for(int i=1; i<=npoints; i++)
        {
            for(int j=1;j<=npoints;j++)
            {
                u_xy[i][j]=  u_xy[i][j]*0.1 + added[i][j];
            }    
        }
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by function: "
         << duration.count()/1e6 << " seconds" << endl;

    return 0;
}