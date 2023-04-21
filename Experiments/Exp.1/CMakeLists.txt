cmake_minimum_required(VERSION 3.25)

set(CMAKE_C_STANDARD 99)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

message(STATUS "bin:" ${PROJECT_BINARY_DIR})
message(STATUS "src:" ${PROJECT_SOURCE_DIR})
message(STATUS "cmake scr:" ${CMAKE_CURRENT_SOURCE_DIR})
add_executable(EXE raw2bmp.c)
