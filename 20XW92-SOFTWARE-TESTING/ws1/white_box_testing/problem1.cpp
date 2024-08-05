#include<iostream>
using namespace std;
void countChar (int& vocNumber, int& totalNumber)
{
    char chr;
    cin>> chr;
    while ((chr >='A' ́) && (chr <='Z' ́) && (totalNumber <INT_MAX))
    {
        totalNumber +=1;
        if ((chr =='A'))
        {
            vocNumber +=1;
        }
        cin>> chr;
    }
}