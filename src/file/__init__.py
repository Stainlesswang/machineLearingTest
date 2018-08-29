'''
Created on 2018年7月10日
对文件的各种操作
@author: Allen Wong
'''
import os
#替换文件名
def replaceFileName(rootDir, oldStr, newStr):
    for dirpath, dirNames, fileNames in os.walk(rootDir):
        for fileName in fileNames:
            if oldStr in fileName:
                fileNameOld = os.path.join(dirpath, fileName)
                fileNameNew = os.path.join(dirpath,fileName.replace(oldStr, newStr))
                print(fileNameOld + ' --> '+ fileNameNew)
                os.renames(fileNameOld, fileNameNew)
 
#替换文件中的内容
def replaceFileContent(rootDir,oldStr,newStr):
    for dirpath,dirNames,fileNames in os.walk(rootDir):
        for fileName in fileNames:
            fileObj = os.path.join(dirpath,fileName)
            f = open(fileObj,'r+')
            all_the_lines=f.readlines()
            f.seek(0)
            f.truncate()
            for line in all_the_lines:
                print("执行 替换操作::"+line)
                f.write(line.replace(oldStr,newStr))
            f.close()
#修改文件扩展名
def Modifypostfix(Path,oldftype,newftype):
    all_file_list = os.listdir(Path)          #列出指定目录下的所有文件
    for file_name in all_file_list:
        currentdir =os.path.join(Path,file_name)
        if os.path.isdir(currentdir):                    #迭代
            Modifypostfix(currentdir,oldftype,newftype)
        fname = os.path.splitext(file_name)[0]
        ftype = os.path.splitext(file_name)[1]
        if oldftype in ftype[1:]:                         #找到需要修改的扩展名
#             typecount[0]+=1
            ftype=ftype.replace(oldftype,newftype)
            newname = os.path.join(Path,fname+ftype) #文件路径与原来的文件名字+新的扩展名
            os.rename(currentdir,newname)               #重命名

#执行流
if __name__ == '__main__':
    try:
#         填写需要修改的东西
        newStr = "CustomerDetection"
        newStr2 = "customerDetection"
        
        
        
        rootDir1 = r"C:\Users\chinaso\Desktop\test"
        oldStr = "AllenWang"
        oldStr2 = "allenWang"
# # #   修改AllenWang  
        replaceFileContent(rootDir1,oldStr,newStr)
        replaceFileContent(rootDir1,oldStr2,newStr2)  
#         最后修改文件名及后缀名
        replaceFileName(rootDir1,oldStr,newStr)
#         Modifypostfix(rootDir1,"txt","java")
#         Modifypostfix(rootDir1,"java","txt")
        pass
    except Exception as e:
        print(e)