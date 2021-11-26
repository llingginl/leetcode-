## 如何实现一个变长数组
    ## 支持

    ## 记录 size 和 capacity
    #if size 》= capcity ，重新申请两倍的连续空间，拷贝到新空间 释放旧空间
    #