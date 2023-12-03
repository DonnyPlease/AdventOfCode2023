#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <tuple>

using namespace std;

tuple<bool,int,int> getDigitWord(string s) {
    string s3 = s.substr(0,3);
    if (s3 == "one") {return make_tuple(true,1,3);}
    if (s3 == "two") {return make_tuple(true,2,3);}
    if (s3 == "six") {return make_tuple(true,6,3);}
    string s4 = s.substr(0,4);
    if (s4 == "zero") {return make_tuple(true,0,4);}
    if (s4 == "four") {return make_tuple(true,4,4);}
    if (s4 == "five") {return make_tuple(true,5,4);}
    if (s4 == "nine") {return make_tuple(true,9,4);}
    string s5 = s.substr(0,5);
    if (s5 == "three") {return make_tuple(true,3,5);}
    if (s5 == "seven") {return make_tuple(true,7,5);}
    if (s5 == "eight") {return make_tuple(true,8,5);}

    return make_tuple(false,0,0);
}

int getNumber(string &s) {
    int d1 = 0;
    int d2 = 0;
    int size = s.size();

    for (int i = 0; i < size; i++) {
        int theDigit;
        bool isDigit;
        int lenght;

        if (isdigit(s[i])) {
            theDigit = s[i] - '0';
        } else {
            tie(isDigit, theDigit, lenght) = getDigitWord(s.substr(i,5));
            if (!isDigit) {
                continue;
            }
        }

        if (d1 == 0) {
            d1 = theDigit;
        }
        d2 = theDigit;
    }
    return 10*d1+d2;
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
