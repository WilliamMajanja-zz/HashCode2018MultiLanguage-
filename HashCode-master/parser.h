#pragma once

#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;
#include <time.h>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
/*
 * Ex de lecture et d'écriture de csv/txt verts des maps, à adapter
 *
template <typename Element>
void readCsvToMap(map<int,Element> & readMap, string filename){
    ifstream read(filename.c_str());
    if (!read.is_open()) throw;
    string line;
    getline(read, line); // nbElements or objective value
    getline(read, line); // Description line
    while (getline(read, line)){
        removeOneSubstring(line, ",");

        Element elem(line);
        readMap.insert(pair<int, Element>(elem.getIndex(), elem));
    }
}

template <typename Element>
void printMapToCsv(map<int,Element> printedMap, string filename, int sol){
    ofstream write(filename.c_str());
    if (!write.is_open())
    {
        throw;
    }
    write << "Objective: " << sol << endl;
    write << printedMap.begin()->second.classDescription() << endl;
    for (typename map<int,Element>::iterator it = printedMap.begin(); it!= printedMap.end(); ++it){
        write << it->second.toString() << endl;
    }
}*/

