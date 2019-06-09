# -*- coding: UTF-8 -*-

from django.db import models
import json

'''
    这个版本里，emojiinfo 表示为字典，不用类
    {''}
'''
class emlist:
    _list=[]

    def addsymble(self,symble):
        for item in self._list:
            if symble['unicode']==item['unicode']:
                item.update(symble)
                break
        else:
            self._list.append(symble)


    def LoadformXXL(self,filename):
        with open(filename,encoding='utf-8') as load_f:
            self._list = json.load(load_f)
        
       
    
    def SavetoJson(self,filename):
        with open(filename, "w", encoding='utf-8') as fw:
            fw.write(json.dumps(self._list, indent=4))
        
    def savetoSougou(self,filename,Default_Position=3):
        try:
            filename=open(filename,'w',encoding='utf-8')
            for symble in self._list:
                if 'info输入串' in  symble.keys():
                    filename.write(symble['info输入串']+','+repr(Default_Position)+'='+symble['unicode']+"\n")
            filename.close()
        except IOError:
            print("导出到 %S 时出错",filename)


if __name__=="__main__":
    
    a_emojiList=emlist()
    a_emojiList.LoadformXXL(r"..\resources\try.json")
    print("Load data from JSON file") 


    aaa={'unicode':'⭐','info中文名':'星星','info输入串':'xingxing'}
    a_emojiList.addsymble(aaa)

    bbb={'unicode':'🌹','info中文名':'玫瑰','info输入串':'meigui'}
    a_emojiList.addsymble(bbb)

    ccc={'unicode':'😄','info输入串':'xiaolian','info中文名':'笑脸'}
    a_emojiList.addsymble(ccc)

    for symble in a_emojiList._list:
        print(symble,end=' ')


    a_emojiList.SavetoJson(r'..\temp\myjson.json')

    a_emojiList.savetoSougou(r'..\temp\sougou.txt',Default_Position=2)