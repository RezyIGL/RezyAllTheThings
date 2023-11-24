cmake_minimum_required(VERSION 3.26)
project(TvSU-RegEx-To-NFA-To-DFA)

set(CMAKE_CXX_STANDARD 20)

set(SOURCE_EXE main.cpp)

add_executable(main ${SOURCE_EXE})

add_subdirectory(CreateDFA)
add_subdirectory(CreateNFA)
add_subdirectory(Print)

target_link_libraries(main CreateNFA)
target_link_libraries(main CreateDFA)
target_link_libraries(main Print)