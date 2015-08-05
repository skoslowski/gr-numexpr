INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_NUMEXPR numexpr)

FIND_PATH(
    NUMEXPR_INCLUDE_DIRS
    NAMES numexpr/api.h
    HINTS $ENV{NUMEXPR_DIR}/include
        ${PC_NUMEXPR_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    NUMEXPR_LIBRARIES
    NAMES gnuradio-numexpr
    HINTS $ENV{NUMEXPR_DIR}/lib
        ${PC_NUMEXPR_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(NUMEXPR DEFAULT_MSG NUMEXPR_LIBRARIES NUMEXPR_INCLUDE_DIRS)
MARK_AS_ADVANCED(NUMEXPR_LIBRARIES NUMEXPR_INCLUDE_DIRS)

