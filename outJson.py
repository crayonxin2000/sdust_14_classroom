
from os import kill
import xlwings as xw
from xlwings.main import App

app = xw.App(add_book=False)
for i in range(18):
    print("正在处理第"+str(i)+"个表格")
    z=i+1
    wb = app.books.open("excel/"+str(z)+".xlsx")
    sht = wb.sheets[0]
    info = sht.used_range
    nrows = info.last_cell.row
    ncolums=info.last_cell.column
    dict={}
    for i in range(nrows):
        if i==1 or i==0: # 跳过第一、二行标题
            continue
        if ncolums==37:
            r=sht[i,1:]# 选取一行的数据
            data={}
            for t in range(36):
                a=t//5
                b=t%5
                if r[0,t+1].value == None:
                    s=""
                else:
                    s=r[0,t+1].value
                data[str(a)+"_"+str(b)]=s
            dict[r[0,0].value[4:7]]=data.copy()
            data.clear

    import os
    import json
    file=open("json/"+str(z)+".json","w")
    file.write(json.dumps(dict))
    file.close()
    wb.close()
app.kill()


