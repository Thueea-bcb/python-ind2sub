def sub2ind(s_shape, s_sub_index):
    # 将下标转换为线性索引
    # 采用由低维向高维的索引形式，即0,0,1对应于1
    index = 0
    multiplefactor = 1
    for i in range(len(s_shape)-1,-1,-1):
        index = index + multiplefactor*s_sub_index[i]
        multiplefactor = multiplefactor*s_shape[i]
    return index

def ind2sub(s_shape, s_index):
    # 将线性索引转换为下标
    s_sub_index = np.zeros(len(s_shape))
    multiplefactor = np.ones(len(s_shape))
    index_temp = s_index
    for i in range(len(s_shape)-1,0,-1):
        multiplefactor[i-1] = multiplefactor[i]*s_shape[i]
    for i in range(len(s_shape)):
        s_sub_index[i] = math.floor(index_temp/(multiplefactor[i])) # 计算得到本次的位数
        index_temp = index_temp%(multiplefactor[i])    # 计算下一次的设定值
    return s_sub_index
