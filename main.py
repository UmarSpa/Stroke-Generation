"""
Author: Muhammad Umar Riaz
"""
import os
import argparse
import tools as myTools

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--inDir', type=str, default='./Input/', help='Input directory containing TU Berlin style data with transformed values')
    parser.add_argument('--outDir', type=str, default='./Output/', help='Output directory')
    parser.add_argument('--procType', type=str, default='AccStroke', help='AccStroke: to create accumulated stroke svg sketches, SepStroke: to create separate stroke svg sketches')
    args = parser.parse_args()

    if not os.path.exists(args.outDir):
        os.makedirs(args.outDir)

    dataList = myTools.folder2files(args.inDir, format='.svg')
    if args.procType == 'AccStroke':
        myTools.acc_strokes(dataList, args.outDir)
    elif  args.procType == 'SepStroke':
        myTools.sep_strokes(dataList, args.outDir)