#Task 2

from random import choice 
from random import seed 
seed(109) 
for i in range(1000): 
    print(choice(['─','│','┌','┐','├','┤','┼','╭', '╮' ,'╯' ,'╰']), end='')
for i in range(500):
    print('┼', end ='')
    print('╭', end ='')
    print('├', end ='')
    print('╯', end ='')
for i in range(1000): 
    print(choice(['─','│','┌','┐','├','┤','┼','╭', '╮' ,'╯' ,'╰']), end='')