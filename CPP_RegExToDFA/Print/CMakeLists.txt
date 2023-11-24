cmake_minimum_required(VERSION 3.26)

project(Print CXX)

set(SOURCE_LIB Print.cpp)
set(HEADERS Print.h)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

add_library(Print ${SOURCE_LIB} ${HEADERS})
target_include_directories(Print PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})