#include<bits/stdc++.h>
#include <iostream>
#include <algorithm>
#include<vector>
using namespace std;

int main()
{
	
	int size = 4;
	int v=size;
	vector<int> AT;
	vector<int> BT;


	for(int i=0;i<size;i++){
		cout<<"\nAT["<<i<<"] ";
		cin>>v;
		AT.push_back(v);
		cout<<"\nBT["<<i<<"] ";
		cin>>v;
		BT.push_back(v);
	}

	cout<<endl<<endl<<endl;
	for (auto& it : AT) {
	    cout << it << endl;
	}
	cout<<endl<<endl<<endl;
	for (auto& it : BT) {
	    cout << it << endl;
	}






    return 0;
}




