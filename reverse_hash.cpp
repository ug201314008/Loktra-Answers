#include<iostream>
#include<stdlib.h>
#include<cstring>

using namespace std;

long long hash_fn (string s) 
{
        long long h = 7;
        string letters = "acdegilmnoprstuw";
        for(int i = 0; i < s.length(); i++) {
            size_t found = letters.find(s[i]);
            if (found!=std::string::npos)
            {
                  h = (h * 37 + found);
            }
            else
			{
                  h = (h * 37 + -1);
            }
        }
        return h;
}


void getAllKLengthRec(char* set,string prefix,int n, int k,long long int hashVal)
{
        if (k == 0)
        {
            if(hash_fn(prefix)==hashVal) 
			{
                cout<<"Output string is "<<prefix<<endl;
            }
            return;
        }
        
        for (int i = 0; i < n; ++i)
        {
            string newPrefix = prefix + set[i];
            getAllKLengthRec(set, newPrefix, n, k - 1,hashVal);
        }
}

void getAllKLength(char* set,int len,long long int hashVal)
{
        int n = strlen(set);
        getAllKLengthRec(set, "", n, len,hashVal);
}


int main()
{
	    int len;
	    long long int hashVal;
        string str = "acdegilmnoprstuw";
        int n=str.length();
        char set1[n+1];
        strcpy(set1, str.c_str()); 
        cout<<"Enter the string length value"<<endl;
        cin>>len;
        cout<<"Enter the hash value of string "<<endl;
        cin>>hashVal;
        getAllKLength(set1,len,hashVal);
        
        return 0;
}



