cmake_minimum_required(VERSION 3.5)
project(splay_tree)
#set(CMAKE_BUILD_TYPE Debug)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

# core files
set(splay_tree_SRCS
src/splay_tree.cpp
)

# header files
include_directories(include)
set(splay_tree_HDRS
include/splay_tree/splay_tree.h
)

add_executable(splay_tree ${splay_tree_SRCS} ${splay_tree_HDRS})
set_target_properties(splay_tree PROPERTIES LINKER_LANGUAGE CXX)
ament_target_dependencies(splay_tree)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()


install(
  TARGETS
    splay_tree
  DESTINATION
    lib/${PROJECT_NAME}
  )

ament_package()
