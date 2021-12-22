cmake_minimum_required(VERSION 3.16)
project(CryptoLab)
add_definitions(-w)

MESSAGE(STATUS "----------------------------")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fpermissive -std=c++11  -Wall")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fpermissive -std=c11  -Wall")

IF (CMAKE_BUILD_TYPE MATCHES "Release")
    MESSAGE(STATUS "CMAKE_BUILD_TYPE is Release")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O2")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2")
ELSE ()
    MESSAGE(STATUS "CMAKE_BUILD_TYPE is Debug")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -g3 -ggdb3")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -g3 -ggdb3")
ENDIF ()

IF (ASAN_ENABLE MATCHES "True")
    MESSAGE(STATUS "ASAN is enabled")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fsanitize=address")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address")
ENDIF ()

MESSAGE(STATUS "----------------------------")

set(CMAKE_C_COMPILER "/usr/bin/gcc")
set(CMAKE_CXX_COMPILER "/usr/bin/g++")

add_executable(DES_test DES.cpp DES.h DES_test.cpp)
target_link_libraries(DES_test ${CMAKE_DL_LIBS})

add_executable(DH_test network.cpp network.h DH.cpp DH.h DH_test.cpp)
target_link_libraries(DH_test crypto ${CMAKE_DL_LIBS})

add_executable(SSL_test network.cpp network.h SSL_test.cpp)
target_link_libraries(SSL_test crypto ssl ${CMAKE_DL_LIBS})