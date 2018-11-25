import os
def renameFiles():
    fileList = os.listdir(r'C:\Users\julio\Downloads\alphabet\alphabet')
    # r = rawpack
    # print(fileList)
    savedPath = os.getcwd()
    print('Current Working Directory is '+savedPath)
    os.chdir(r'C:\Users\julio\Downloads\alphabet\alphabet')
    #CWD = Current Working Directory

    for fileName in fileList:
        print('Old Name - '+fileName)
        print('New Name - '+fileName.translate(None, '0123456789'))
        os.rename(fileName, fileName.translate(None, '0123456789'))
    os.chdir(savedPath)
    
renameFiles()
