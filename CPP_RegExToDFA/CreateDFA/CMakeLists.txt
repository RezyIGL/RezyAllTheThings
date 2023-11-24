cmake_minimum_required(VERSION 3.26)

project(CreateDFA CXX)

set(SOURCE_LIB CreateDFA.cpp)
set(HEADERS CreateDFA.h)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

add_library(CreateDFA ${SOURCE_LIB} ${HEADERS})
target_include_directories(CreateDFA PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})