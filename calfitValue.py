# 0.0 coding:utf-8 0.0

# 淘汰（去除负值）


def calfitValue(obj_value):
    fit_value = []
    c_min = 0
    for i in range(len(obj_value)):
        if(obj_value[i] + c_min > 0):
            temp = c_min + obj_value[i]
        else:
            temp = 0.0
        fit_value.append(temp)
    return fit_value

if __name__ == '__main__':
    pass
