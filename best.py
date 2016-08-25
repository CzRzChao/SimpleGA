# 0.0 coding:utf-8 0.0
# 找出最优解和最优解的基因编码


def best(pop, fit_value):
    px = len(pop)
    best_individual = []
    best_fit = fit_value[0]
    for i in range(1, px):
        if(fit_value[i] > best_fit):
            best_fit = fit_value[i]
            best_individual = pop[i]
    return [best_individual, best_fit]

if __name__ == '__main__':
    pass
