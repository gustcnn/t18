#--*--coding:utf-8
#Author:cnn
name_list=["张三","李四","王五"]
#取值和取索引
print(name_list[0])
print(name_list[1])
print(name_list[2])
if "张三" in name_list:
    print(name_list.index("张三"))
else:
    print("数据不在列表中.")
#修改
name_list[1]="gustcnn"
print(name_list)
#增加
name_list.append("kobe")
name_list.append("lbj")
print(name_list)
temp_list=["one","two","three"]
name_list.extend(temp_list)
print(name_list)
#删除
name_list.pop()#删除末尾的元素
print(name_list)
#删除第一个元素
name_list.pop(0)
print(name_list)
#删除指定元素
name_list.remove("lbj")
print(name_list)
#清空列表
name_list.clear()
print(name_list)
#插入
name_list.insert(1,"嘿嘿")
name_list.insert(name_list.__len__(),"cnn")
print(name_list)