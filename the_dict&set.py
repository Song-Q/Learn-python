#dict    (key - value)且元素存储是无序的
d = {'Michael':95,'Bob':75, 'Tracy':85}
d['Michael']
#结果：95
d.pop('Bob')    #删除Bob
d['Adam'] = 67    #除了初始化时指定外，还可以通过key 放入
#dict的key必须是不可改变对象,不可放入list,最常用的key是字符串

#set    就是一组key的集合，没有重复的key
s = ([1, 2, 3])
s.add(4)    #添加元素
s.remove(4)    #删除元素
#可以做数学上的交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

