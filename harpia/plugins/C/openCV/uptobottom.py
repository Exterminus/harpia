#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.GUI.fieldtypes import *
from harpia.plugins.C.openCV.opencvplugin import OpenCVPlugin

class UpToBottom(OpenCVPlugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        OpenCVPlugin.__init__(self)

    # --------------------------Help Text--------------------------------------------
    def get_help(self):#Função que chama a help
        return "Coloca uma imagem debaixo da outra"

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        return \
            'if(block$id$_img_i0 && block$id$_img_i1){\n' + \
            'int width = (block$id$_img_i0->width > block$id$_img_i1->width)? block$id$_img_i0->width : block$id$_img_i1->width;\n' + \
            'int height = block$id$_img_i0->height + block$id$_img_i1->height;\n' + \
            'block$id$_img_o0=cvCreateImage(cvSize(width,height),IPL_DEPTH_8U,3); \n' + \
            'cvSetImageROI(block$id$_img_o0, cvRect(0, 0, block$id$_img_i0->width, block$id$_img_i0->height) );\n' + \
            'cvCopy(block$id$_img_i0,block$id$_img_o0,NULL);\n' + \
            'cvResetImageROI(block$id$_img_o0);\n' + \
            'cvSetImageROI(block$id$_img_o0, cvRect(0, block$id$_img_i0->height, block$id$_img_i1->width, height) );\n' + \
            'cvCopy(block$id$_img_i1,block$id$_img_o0,NULL);\n' + \
            'cvResetImageROI(block$id$_img_o0);\n' + \
            '}\n'

    # ----------------------------------------------------------------------
    def generate_dealloc(self):
        return 'if (block$id$_img_o0) cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n'+ \
            'cvReleaseImage(&block$id$_img_i1);\n'

    # ------------------------------------------------------------------------------
    def get_description(self):
        return {"Label": "Up to Bottom",
                "Icon": "images/and.png",
                "Color": "10:180:10:150",
                "InTypes": {0: "HRP_IMAGE", 1: "HRP_IMAGE"},
                "OutTypes": {0: "HRP_IMAGE"},
                "TreeGroup": "Arithmetic and logical operations"
                }

    # ------------------------------------------------------------------------------
    def get_properties(self):
        return {}

# ------------------------------------------------------------------------------