#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <unordered_map>
using namespace std;

pair<int,int> getNumber(string line, int i) {
    // Get number
    stringstream number;
    while (line[i] != ' ') {
        number << line[i];
        i++;
    }
    return make_pair(stoi(number.str()),i);
}

pair<string,int> getColor(string line, int i) {
    stringstream cstream;
    while (line[i] != ',' && line[i] != ';' && line[i] != '\000') {
        cstream << line[i];
        i++;
    }
    return make_pair(cstream.str(),i);
}


bool isValid(string line) {

    unordered_map<string,int> cubes_max;
    cubes_max["green"] = 13;
    cubes_max["red"] = 12;
    cubes_max["blue"] = 14;

    int i = 0;

    while (line[i] != ':') {
        i++;
    }
    i++; i++;

    while (true) {
        // Get number
        int num;
        tie(num,i) = getNumber(line,i);
        i++;
        // Get color
        string color;
        tie(color, i) = getColor(line,i);
        if (cubes_max[color] < num) {
            return false;
        }

        if (line[i] == '\000') {
            break;
        }
        i++; i++;
    }
    return true;
}



int main() {

    string line;
    int i = 1;
    getline(cin,line);
    int sum = 0;
    while (!empty(line)) {
        if (isValid(line)) {
            sum += i;
        }
        i++;
        getline(cin,line);
    }
    cout << sum << endl;
    return 0;
}
