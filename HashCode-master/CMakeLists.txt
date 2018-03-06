cmake_minimum_required(VERSION 2.6)
project(HashCode)
aux_source_directory(. SRC_LIST)
add_executable(HashCode main.cpp parser.h)


