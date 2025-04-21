// Reverse_String.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stack>
using namespace std; 

void reverseString(string& s, int i, int j) {
    if (i >= j) return;
    swap(s[i], s[j]);
    reverseString(s, i + 1, j - 1);
}


int main()
{




    //string s = "Sornam";

    //Method 1 - Using std ::reverse() STL function    
    string s = "Sornam";
    reverse(s.begin(), s.end());
    std::cout << "Method1: reverse() function\n";
    std::cout << s << endl;

    //Method 2 - Using Loop (Swapping with Two Pointers) 
    s = "Sornam";
    int n = s.length();
    for (int i = 0; i < n / 2; ++i)
    {
        swap(s[i], s[n - i - 1]);
    }
    std::cout << "Method2: Swapping with Two Pointers\n";
std:;cout << s << endl;

    //Method 3 - Using Stack 
    s = "Sornam";
    stack<char> st;
    for (char c : s) st.push(c);
    string reversed = "";
    while (!st.empty()) {
        reversed += st.top();
        st.pop();
    }
    std::cout << "Method3: Using Stack\n";
    std::cout << reversed << endl;

    //Method 4 - Using Recursion
    s = "Sornam";
    reverseString(s, 0, s.length() - 1);
    std::cout << "Method4: Using Recursion\n";
    std::cout << s << endl;

    //Method 5 - Using for loop (Appending in reverse)
    s = "Sornam";
    string rev = "";
    for (int i_5 = s.length() - 1; i_5 >=0; --i_5)
        rev += s[i_5];
    std::cout << "Method5: Using for loop (Appending in reverse)\n";
    std::cout << rev  << endl;

    //Method 6 - Using while loop
    s = "Sornam";
    rev = "";
    int i_6 = s.length() - 1; 
    while (i_6 >= 0) {
        rev += s[i_6];
        --i_6;
    }   
    std::cout << "Method6: Using While loop (Appending in reverse)\n";
    std::cout << rev << endl;


    //Method 7 - Using String Constructor + Reverse Iterator 
    s = "Sornam";
    string reversed_7(s.rbegin(), s.rend());

    std::cout << "Method7: Using String Constructor + Reverse Iterator\n";
    std::cout << reversed_7 << endl;
    
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
