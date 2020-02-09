cmake_minimum_required(VERSION 3.5)
project(double_linked_list)

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
set(double_linked_list_SRCS
src/double_linked_list.cpp
)

# header files
include_directories(include)
set(double_linked_list_HDRS
include/double_linked_list/double_linked_list.h
)

add_executable(double_linked_list ${double_linked_list_SRCS} ${double_linked_list_HDRS})
set_target_properties(double_linked_list PROPERTIES LINKER_LANGUAGE CXX)
ament_target_dependencies(double_linked_list)

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
    double_linked_list
  DESTINATION
    lib/${PROJECT_NAME}
  )

ament_package()
