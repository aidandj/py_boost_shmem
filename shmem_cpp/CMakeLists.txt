cmake_minimum_required(VERSION 3.13)

include_directories(/usr/local/include /usr/include/python3.7m)
link_directories(/usr/local/lib)

add_link_options(-Wl,--unresolved-symbols=report-all)

add_executable(sharedmem_test main.cpp)
target_link_libraries(sharedmem_test pthread rt)