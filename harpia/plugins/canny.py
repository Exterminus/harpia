#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.s2icommonproperties import APP, DIR
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *

class Division():

# ------------------------------------------------------------------------------
    def __init__(self):
        self.id = -1
        self.type = "83"
        self.apertureSize = 3
        self.threshold1 = 16
        self.threshold2 = 33

    # ----------------------------------------------------------------------
    def get_help(self):#Função que chama a help
        return "Operacão de filtragem que implementa o algoritmo Canny para detecção de contornos e bordas.\nPropriedades\nLimiar 1 e Limiar 2: os dois valores de limiar são utilizados em conjunto. O menor valor é utilizado para a realizar a conexão de cantos e bordas. O maior valor é utilizado para encontrar segmentos iniciais das bordas mais significativas."

    # ----------------------------------------------------------------------
    def generate(self, blockTemplate):
        blockTemplate.imagesIO = \
            'IplImage * block$$_img_i1 = NULL;\nIplImage * block$$_img_o1 = NULL;\n'
        blockTemplate.imagesIO += \
            'int block$$_arg_threshold2 = ' + self.threshold2 + \
            ';\nint block$$_arg_aperture_size = ' + self.apertureSize + \
            ';\nint block$$_arg_threshold1 = ' + self.threshold1 + ';\n'
        blockTemplate.functionCall = '\nif(block$$_img_i1){\n' + \
                                     'block$$_img_o1 = cvCreateImage(cvSize(block$$' + \
                                     '_img_i1->width,block$$_img_i1->height),block$$' + \
                                     '_img_i1->depth,block$$_img_i1->nChannels);\n IplImage * tmpImg$$' + \
                                     ' = cvCreateImage(cvGetSize(block$$_img_i1),8,1);\n if(block$$'+ \
                                     '_img_i1->nChannels == 3)\n {cvCvtColor(block$$_img_i1,tmpImg$$' + \
                                     ',CV_RGB2GRAY);}\n else\n{tmpImg$$ = block$$' + \
                                     '_img_i1 = NULL;}\n cvCanny(tmpImg$$, tmpImg$$' + \
                                     ', block$$_arg_threshold1, block$$' + \
                                     '_arg_threshold2, block$$_arg_aperture_size);\n' + \
                                     'if(block$$_img_i1->nChannels == 3)\n{cvCvtColor(tmpImg$$' + \
                                     ', block$$_img_o1,CV_GRAY2RGB);}\nelse\n{cvCopyImage(tmpImg$$' + \
                                     ', block$$_img_o1);}\ncvReleaseImage(&tmpImg$$);}\n'
        blockTemplate.dealloc = 'cvReleaseImage(&block$$_img_o1);\n' + \
                                'cvReleaseImage(&block$$_img_i1);\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
            "Label": _("Canny"),
            "Icon": "images/canny.png",
            "Color": "250:180:80:150",
            "InTypes": {0: "HRP_IMAGE"},
            "OutTypes": {0: "HRP_IMAGE"},
            "Description": _("Filtering operation that employs the Canny algorithm to detect edges."),
            "TreeGroup": _("Gradients, Edges and Corners")
            }
    # ----------------------------------------------------------------------
    def set_properties(self, data):
        self.apertureSize = data["apertureSize"]
        self.threshold1 = data["threshold1"]
        self.threshold2 = data["threshold2"]


    # ----------------------------------------------------------------------
    def get_properties(self):
        return {"apertureSize":{"name": "Aperture Size",
                            "type": HARPIA_INT,
                            "value": self.apertureSize,
                            "lower":1,
                            "upper":10,
                            "step":1
                            },
            "threshold1":{"name": "Threshold 1",
                            "type": HARPIA_INT,
                            "value": self.threshold1,
                            "lower":1,
                            "upper":100,
                            "step":1
                            },
            "threshold2":{"name": "Threshold 2",
                            "type": HARPIA_INT,
                            "value": self.threshold2,
                            "lower":1,
                            "upper":100,
                            "step":1
                            }
                }
    # ----------------------------------------------------------------------
    def get_xml(self):
        return """
 <properties>
      <block type='"""+ str(self.type) + """' id='"""+ str(self.id) + """'>
    <property name='threshold1' value='"""+ str(self.threshold1) + """' />
    <property name='threshold2' value='"""+ str(self.threshold2) + """' />
    <property name='apertureSize' value='"""+ str(self.apertureSize) + """' />
    </block>
</properties>
    """
# ------------------------------------------------------------------------------
