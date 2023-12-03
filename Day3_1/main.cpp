#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

pair<int,int> get_number(string line, int i) {
    int j = i;
    stringstream s;
    while (isdigit(line[j])) {
        s << line[j];
        j++;
    }
    int number = stoi(s.str());
    int len = j-i;
    return make_pair(number,len);
}
int main() {

    string line;
    vector<string> parts;
    getline(cin,line);
    // Read
    while (!empty(line)) {
        parts.push_back(line);
        getline(cin, line);
    }

    int line_size = line.size();
    int parts_size = parts.size();
    int sum = 0;
    for (int i = 0; i<parts.size(); i++) {
        line = parts[i];

        for (int j = 0; j<line.size(); j++) {
            int num = 0;
            int len = 0;
            if (isdigit(line[j])) {
                tie(num,len) = get_number(line,j);
            }
            if (num > 0) {
                bool symbol = false;
                int line_size = line.size();
                int parts_size = parts.size();
                for (int k = max(0,j-1); k <= min(line_size-2,j+len); k++) {
                    for (int l = max(0,i-1); l <= min(parts_size-1, i+1); l++) {
                        char c = parts[l][k];
                        if (c == '.' || isdigit(c)) {
                            continue;
                        }
                        symbol = true;
                    }
                }
                if (symbol) {
                    sum += num;
                }
                j+=len-1;
            }
        }
    }
    cout << sum << endl;
    return 0;
}
