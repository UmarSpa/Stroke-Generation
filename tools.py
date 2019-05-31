"""
Author: Muhammad Umar Riaz
"""
import os
from xml.dom import minidom
import glob

def folder2files(dataDir, format='.png'):
    """
    Function: It creates a list of all the files present in all the
              subfolders of dataDir.
    Input:
        dataDir: folder path containing the subfolders where the
                 files of interest are present.
    Output:
        dataList: list of files in the subfolders of dataDir.
    N.B.: It needs import os.
    """
    dataList = []
    for dirName, subdirList, fileList in os.walk(dataDir):
      dataList = dataList + sorted(glob.glob(dirName + '/*' + format))
    return dataList

def acc_strokes(svgFiles, desDir):
    """
    Function: It creates the sequential images of the accumulated
                strokes of the sketches.
    Input:
        svgFiles: list of svg files of skteches.
        desDir: folder path where the output svg files will be saved.
    Output:
        None [Svg files are saved in the desDir]
    N.B: It needs import glob, from xml.dom import minidom.
    """
    for svgFileName in svgFiles:
        if not os.path.exists(desDir + svgFileName.split("/")[-1].split(".")[0]):
            os.makedirs(desDir + svgFileName.split("/")[-1].split(".")[0])

        svgFile = minidom.parse(svgFileName)
        _name = svgFile.getElementsByTagName("g")[0]
        _name = _name.getElementsByTagName("g")[0]
        strokes = _name.getElementsByTagName("path")
        idx_tot = len(strokes)

        for idx, removeStroke in enumerate(reversed(strokes)):
            with open(desDir
                    + svgFileName.split("/")[-1].split(".")[0]
                    + "/"
                    + str(idx_tot - idx -1) + ".svg", "w") as f:
                f.write(svgFile.toxml())
            parentNode = removeStroke.parentNode
            parentNode.removeChild(removeStroke)

def sep_strokes(svgFiles, desDir):
    """
    Function: It creates the separate image for each stroke.
    Input:
        svgFiles: list of svg files of skteches.
        desDir: folder path where the output svg files will be saved.
    Output:
        None [Svg files are saved in the desDir]
    N.B: It needs import glob, from xml.dom import minidom.
    """
    for svgFileName in svgFiles:

        if not os.path.exists(desDir + svgFileName.split("/")[-1].split(".")[0]):
            os.makedirs(desDir + svgFileName.split("/")[-1].split(".")[0])

        svgFile1 = minidom.parse(svgFileName)
        _name1 = svgFile1.getElementsByTagName("g")[0]
        _name1 = _name1.getElementsByTagName("g")[0]
        strokes1 = _name1.getElementsByTagName("path")

        svgFile2 = minidom.parse(svgFileName)
        _name2 = svgFile2.getElementsByTagName("g")[0]
        _name2 = _name2.getElementsByTagName("g")[0]
        strokes2 = _name2.getElementsByTagName("path")

        for idx, removeStroke2 in enumerate(reversed(strokes2)):
            parentNode2 = removeStroke2.parentNode
            parentNode2.removeChild(removeStroke2)

        for idx, extractStroke1 in enumerate(strokes1):
            parentNode2.appendChild(extractStroke1)
            with open(desDir + svgFileName.split("/")[-1].split(".")[0]
                    + "/"
                    + str(idx + 1) + ".svg", "w") as f:
                dom_string = svgFile2.toprettyxml(indent='\r')
                dom_string = os.linesep.join([s for s in dom_string.splitlines() if s.strip()])
                f.write(dom_string)
            parentNode2.removeChild(extractStroke1)