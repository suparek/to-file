#coding=utf-8


import os
import shutil

def search_real(i_rootpath,i_filetype,i_newpath):
    path1 = i_rootpath
    file_type1 = i_filetype
    search_file(path1,file_type1,i_newpath)

def search_file(path,file_type,newpath):  
        queue = []
        queue.append(path);
        fpath=[]
        tmpid = 2
        while len(queue) > 0:  
            tmp = queue.pop(0)  
            if(os.path.isdir(tmp)):  
                for item in os.listdir(tmp):  
                    queue.append(os.path.join(tmp, item))  
            elif(os.path.isfile(tmp)):
                tmpid = tmpid + 1
                name = os.path.basename(tmp)#获取文件名
                dirname = os.path.dirname(tmp)#获取文件目录
                full_path = os.path.join(dirname,name)#将文件名与文件目录连接起来，形成完整路径
                creatime = os.path.getctime(tmp)#获取文件创建时间
                modifytime = os.path.getmtime(tmp)#获取文件修改时间
                size = os.path.getsize(tmp)#获取文件大小
                abspath = os.path.abspath(tmp);
                if name[-1*len(file_type):] == file_type:
                    movetonewdir(full_path,newpath)

def movetonewdir(tmpfile,i_newpath):
	shutil.move(tmpfile,i_newpath) 

def safecheck(i_filepath):
	if(os.path.exists(i_filepath) == False):
		print "路径不存在！"
		return

if __name__ == '__main__':
     print "中文有吗？"
     m_rootpath = raw_input("输入文件目录：")
     safecheck(m_rootpath)
     m_neededtype = raw_input("你想提取的文件后缀：")
     m_newpath = raw_input("最终保存这些文件的地方")
     search_real(m_rootpath,m_neededtype,m_newpath)
    

	
        