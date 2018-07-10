# coding=utf-8
import glob
import sys
import os
import subprocess
import time


global idcScriptFileName
global ida32qFilePath
global ida64qFilePath
global ida32wFilePath
global ida64wFilePath

# File these feilds with ur own ida file path and the idc file u want to execute!
idcScriptFileName = "myfunc2.idc"
ida32qFilePath = '"C:\Users\maxsen-pc\Documents\software\IDA\idaq.exe"'
ida64qFilePath = "C:\Users\maxsen-pc\Documents\software\IDA\idaq64.exe"
ida32wFilePath ='"C:\Users\maxsen-pc\Documents\software\IDA\idaw.exe"'
ida64wFilePath = "C:\Users\maxsen-pc\Documents\software\IDA\idaw64.exe"
#The binary file list text
# TargetList = "c:/test.txt"
#
# TargetFile_object = open(TargetList, "r").readlines()
# for eachline in TargetFile_object:

def idaParse(filepath):
    # path = os.getcwd()
    # os.chdir('%s/data' % path)
    os.chdir(filepath)
    for filename in glob.glob("*"):
        eachline = filename
        if os.path.exists(eachline):
            eachline = os.getcwd() + "\\" + filename
            tmpExecStr =  ida64wFilePath +" -B -S"+idcScriptFileName +" " + eachline
            print tmpExecStr,
            #os.system(tmpExecStr) singl process with cmdwindow
            #os.popen(tmpExecStr)  singl process without cmdwindow
            child = subprocess.Popen(tmpExecStr) #mulity process with cmd window
            # # child.wait()
            # time.sleep(5)
            # child.poll()
            # # child.send_signal()
            # child.terminate()

            # kill_command = 'taskkill -f ' + ida32wFilePath
            # subprocess.Popen(kill_command)


    print ("All Process have been started!")




if __name__ == '__main__':
    path = os.getcwd()+'/data/malware'
    idaParse(path)
