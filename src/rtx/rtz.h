
#include <iostream>
#include <sstream>  // 包含 stringstream 的头文件
// #include <tiffio.h>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <chrono>
#include <cstdint> // For uint16_t

struct Mat16 {
    std::vector<uint16_t> buffer;
    int width;
    int height;
    int cost;
    int error;
    std::string msg;

    // Constructor to initialize the structure
    Mat16() : width(0), height(0), cost(0), error(0), msg("") {}
};

Mat16 getTiff(const std::string& pp3file, const std::string& srcfile, const std::string& bundlePath, bool isSmallNEF);


// cp librtz.so ../../python/