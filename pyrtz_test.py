import rtx.rtx as rtx
import cv2
import numpy as np
import logging
import os
import json
import time
import argparse

# https://github.com/Algomorph/pyboostcvconverter/tree/master
logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s %(levelname)-1.1s L%(lineno)-3.3d %(process)-5.5d [%(name)-12.12s] %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger("rtx_test")
logger.setLevel(logging.DEBUG)
pwd = os.path.dirname(os.path.realpath(__file__))
bundlePath=pwd+"/src/"

assert os.path.exists(bundlePath), f"Bundle Path not found: {bundlePath}"

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        t = 1000*(end_time - start_time)
        too_much = '[NOTICE]' if t > 1000 else ''
        logger.debug(f"Fun[{func.__name__}]{too_much} took {t:.2f}ms")
        return result
    return wrapper
def assert_exists(f):
    logger.debug(f"assert_exists: {f}")
    assert os.path.exists(f), f"file not found: {f}"


@timer_decorator
def test_rtx_dict():
    dict_data = {"name": "John", "age": "25", "city": "New York"}
    result = rtx.test_dict(dict_data)
    logger.debug(f"test_rtx_dict result: {result}")
    logger.debug(f"test_rtx_dict dict_data: {dict_data}")

@timer_decorator
def test_rtx_test_str():
    txt="hi"
    info = rtx.test_str(txt)
    logger.debug(f"test_rtx_dict txt: {txt}")
    logger.debug(f"test_rtx_dict info: {info}")

@timer_decorator
def test_genThumbNumpy():
    input:str=f"{bundlePath}/assets/414_0.NEF";
    pp3Path:str=f"{bundlePath}/assets/preview.pp3";
    isSmallNEF:bool = False
    assert_exists(input)
    assert_exists(pp3Path)
        
    cost = time.time()
    result_rgb = rtx.genThumbNumpy(input, pp3Path, bundlePath, isSmallNEF)
    cost = time.time() - cost
    
    logger.debug(f"genThumbNumpy cost: {cost:.2f}s")
    logger.debug(f"genThumb result: {result_rgb.shape} {result_rgb.dtype}")
    assert result_rgb.dtype == np.uint16, "genThumbNumpy result dtype is not uint16"
    bgr = cv2.cvtColor(result_rgb, cv2.COLOR_RGB2BGR)
    bgr8bit = cv2.convertScaleAbs(bgr, alpha=255.0/65535.0)
    output:str=f'{bundlePath}/assets/414_0_genThumbNumpy.jpg'
    cv2.imwrite(output, bgr8bit)
    logger.debug(f"genThumbNumpy result: {output}")
    assert_exists(output), f"genThumbNumpy result not found: {output}"

@timer_decorator
def test_genThumbNumpy2():
    input:str=f"{bundlePath}/assets/865_0.CR2";
    pp3Path:str=f"{bundlePath}/assets/preview.pp3";
    isSmallNEF:bool = False
    assert_exists(input)
    assert_exists(pp3Path)
        
    cost = time.time()
    result_rgb = rtx.genThumbNumpy(input, pp3Path, bundlePath, isSmallNEF)
    cost = time.time() - cost
    
    logger.debug(f"genThumbNumpy cost: {cost:.2f}s")
    logger.debug(f"genThumb result: {result_rgb.shape} {result_rgb.dtype}")
    assert result_rgb.dtype == np.uint16, "genThumbNumpy result dtype is not uint16"
    bgr = cv2.cvtColor(result_rgb, cv2.COLOR_RGB2BGR)
    bgr8bit = cv2.convertScaleAbs(bgr, alpha=255.0/65535.0)
    output:str=f'{bundlePath}/assets/865_0_genThumbNumpy.jpg'
    cv2.imwrite(output, bgr8bit)
    logger.debug(f"genThumbNumpy result: {output}")
    assert_exists(output), f"genThumbNumpy result not found: {output}"


@timer_decorator
def main():    
    logger.debug(f"------------> test_rtx_test_str")
    test_rtx_test_str()
    logger.debug(f"------------> test_genThumbNumpy2")
    test_genThumbNumpy2()
    logger.debug(f"------------> test_genThumbNumpy")
    test_genThumbNumpy()
"""
pip install -r requirements.txt 
rm -rf dist rtx.egg-info build
python setup.py bdist_wheel
pip uninstall rtx -y
pip install dist/*.whl 
python rtx_test.py
"""
if __name__ == '__main__':
    main()