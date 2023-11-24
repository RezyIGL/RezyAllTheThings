cmake_minimum_required(VERSION 3.26)

project(CreateNFA CXX)

set(SOURCE_LIB CreateNFA.cpp)
set(HEADERS CreateNFA.h)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

add_library(CreateNFA ${SOURCE_LIB} ${HEADERS})
target_include_directories(CreateNFA PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})