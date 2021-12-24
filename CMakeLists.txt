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

set(DES_SRC src/DES.cpp src/DES.h)
add_executable(DES_test src/DES_test.cpp ${DES_SRC})
target_link_libraries(DES_test ${CMAKE_DL_LIBS})

set(DH_SRC src/network.cpp src/network.h src/DH.cpp src/DH.h)
add_executable(DH_test src/DH_test.cpp ${DH_SRC})
target_link_libraries(DH_test crypto ${CMAKE_DL_LIBS})

add_executable(SSL_test src/network.cpp src/network.h src/SSL_test.cpp)
target_link_libraries(SSL_test crypto ssl ${CMAKE_DL_LIBS})

set(AFFINE_SRC src/Affine.cpp src/Affine.h)
add_executable(Affine_test src/Affine_test.cpp ${AFFINE_SRC})
target_link_libraries(Affine_test ${CMAKE_DL_LIBS})

set(LFSR_SRC src/LFSR.cpp src/LFSR.h)
add_executable(LFSR_test src/LFSR_test.cpp ${LFSR_SRC})
target_link_libraries(LFSR_test ${CMAKE_DL_LIBS})

set(RC4_SRC src/RC4.cpp src/RC4.h)
add_executable(RC4_test src/RC4_test.cpp ${RC4_SRC})
target_link_libraries(RC4_test ${CMAKE_DL_LIBS})

set(RSA_SRC src/RSA.cpp src/RSA.h)
add_executable(RSA_test src/RSA_test.cpp ${RSA_SRC})
target_link_libraries(RSA_test ${CMAKE_DL_LIBS})

add_library(cryptolab SHARED src/libso.cpp ${DES_SRC} ${DH_SRC} ${AFFINE_SRC} ${RC4_SRC} ${LFSR_SRC} ${RSA_SRC})
target_link_libraries(cryptolab crypto ssl)

add_executable(libso_test src/libso_test.cpp)
target_link_libraries(libso_test ${CMAKE_DL_LIBS})