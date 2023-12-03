#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int getNumber(string &s) {
    char i = 'n';
    char j = 'n';
    for (char &c : s) {
        if (i == 'n') {
            if ( isdigit(c) ) {
                i = c;
                j = c;
            }
        } else if (isdigit(c)) {
            j = c;
        }
    }

    stringstream res;
    res << i << j;
    string num = res.str();
    return stoi(num);
}

int sum(const vector<int>& v) {
    int result = 0;
    for (const int& e : v) {
        result += e;
    }
    return result;
}

int main() {

    string s;
    getline(cin, s);

    vector<int> numbers;

    while ( s != "") {
        numbers.push_back(getNumber(s));
        getline(cin, s);
    }

    cout << sum(numbers);
}

