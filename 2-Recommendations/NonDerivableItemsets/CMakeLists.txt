cmake_minimum_required(VERSION 3.24)
project(NonDerivableItemsets)

set(CMAKE_CXX_STANDARD 17)

add_executable(bf
        bf/data.cpp
        bf/item.cpp
        bf/ndi.cpp
        bf/nditest.cpp
        bf/qie.cpp
        )

add_executable(df
        df/data.cpp
        df/ndi.cpp
        df/testndi.cpp
        df/qie.cpp
        )

add_executable(Converter Converter.cpp)
