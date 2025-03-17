#include "rtz.h"
#include <map>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <string>
#include <cstdlib>
#include <iostream>

namespace py = pybind11;

std::string test_str(std::string &info)
{
    info="updated in cpp code";
    return "hello";
}
std::string test_dict(std::map<std::string, std::string> &dict)
{
    std::string result = "";
    for (const auto &pair : dict) {
        result += pair.first + ": " + pair.second + "\n";
    }
    dict["added"] = "value";
    return result;
}

py::array_t<uint16_t> wrapper_genThumbTiff_np(const std::string &input,
                                           const std::string &pp3Path,
                                           const std::string &bundlePath,
                                           bool isSmallNEF)
{
    Mat16 mat16 = getTiff(pp3Path, input, bundlePath, isSmallNEF);

    // Check for errors in Mat16
    if (mat16.error != 0) {
        throw std::runtime_error("Error generating TIFF: " + mat16.msg);
    }

    // Define the shape of the numpy array
    std::vector<ssize_t> shape = {mat16.height, mat16.width, 3}; // Assuming 3 channels (RGB)
    // std::vector<ssize_t> strides = {mat16.width * 3 * sizeof(uint16_t), 3 * sizeof(uint16_t), sizeof(uint16_t)};
    std::vector<ssize_t> strides = {
        static_cast<ssize_t>(mat16.width * 3 * sizeof(uint16_t)),
        static_cast<ssize_t>(3 * sizeof(uint16_t)),
        static_cast<ssize_t>(sizeof(uint16_t))
    };

    // Create a numpy array with the buffer from Mat16
    return py::array_t<uint16_t>(
        py::buffer_info(
            mat16.buffer.data(),                          // Pointer to data
            sizeof(uint16_t),                             // Size of one scalar
            py::format_descriptor<uint16_t>::format(),    // Data type
            3,                                            // Number of dimensions
            shape,                                        // Shape of the array
            strides                                       // Strides for each dimension
        )
    );
}


PYBIND11_MODULE(rtx, m)
{
    py::module_::import("numpy");
    m.def("test_str", &test_str, "Where there is a will, there is a way");
    m.def("test_dict", &test_dict, "Where there is a will, there is a way");
    m.def("genThumbNumpy", &wrapper_genThumbTiff_np, "Where there is a will, there is a way");
}
