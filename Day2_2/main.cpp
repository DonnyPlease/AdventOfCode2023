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


int power(string line) {

    unordered_map<string,int> cubes_min;
    cubes_min["green"] = 0;
    cubes_min["red"] = 0;
    cubes_min["blue"] = 0;

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
        if (cubes_min[color] < num) {
            cubes_min[color] = num;
        }

        if (line[i] == '\000') {
            break;
            cout << "Break" << endl;
        }
        i++; i++;
    }
    int result = cubes_min["green"]*cubes_min["red"]*cubes_min["blue"];
    return result;
}



int main() {

    string line;
    getline(cin,line);
    int sum = 0;
    while (!empty(line)) {
        sum += power(line);
        getline(cin,line);
    }
    cout << sum << endl;
    return 0;
}
