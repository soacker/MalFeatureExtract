# coding=utf-8
import glob
import sys
import os
import subprocess


global idcScriptFileName
global ida32qFilePath
global ida64qFilePath
global ida32wFilePath
global ida64wFilePath

# File these feilds with ur own ida file path and the idc file u want to execute!
idcScriptFileName = "C:\Users\maxsen-pc\Documents\software\IDA\myfunc2.idc"
ida32qFilePath = '"C:\Users\maxsen-pc\Documents\software\IDA\idaq.exe"'
ida64qFilePath = "C:\Users\maxsen-pc\Documents\software\IDA\idaq64.exe"
ida32wFilePath ='"C:\Users\maxsen-pc\Documents\software\IDA\idaw.exe"'
ida64wFilePath = "C:\Users\maxsen-pc\Documents\software\IDA\idaw64.exe"
#The binary file list text
# TargetList = "c:/test.txt"
#
# TargetFile_object = open(TargetList, "r").readlines()
# for eachline in TargetFile_object:

path = os.getcwd()
# os.chdir('%s/data' % path)
os.chdir('C:\data')
for filename in glob.glob("*.*"):
    eachline = filename
    if os.path.exists(eachline):
        eachline = os.getcwd() + "\\" + filename
        tmpExecStr =  ida32wFilePath +" -B -S"+idcScriptFileName +" " + eachline
        print tmpExecStr,
        #os.system(tmpExecStr) singl process with cmdwindow
        #os.popen(tmpExecStr)  singl process without cmdwindow
        subprocess.Popen(tmpExecStr) #mulity process with cmd window

print ("All Process have been started!")