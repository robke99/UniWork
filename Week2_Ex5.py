# -*- coding: utf-8 -*-


import random
flip_list=[]
i = 0
no_loops = 10000
bias_level = float(input('Enter level of bias for getting heads as a float: '))
while i < no_loops:
    flip = random.random()
    if flip < bias_level:
        flip_list.append('heads')
        flip_result = 'Heads'
        i+=1
        j = flip_list.count('heads')
        #print(flip_result, 'iteration No:', i,'Heads count:', j)
               
        
    else:
        flip_list.append('tails')
        flip_result = 'Tails'
        i+=1
        k = flip_list.count('tails')
        #print(flip_result, 'iteration No:', i,'Tails count:', k)
        
# print(flip_result)
print('Bias of heads is: ', 100*j/no_loops, '%')

