'''Exercício 7:
Indique o resultado lógico das seguintes expressões:
a. 2 < 3
b. ( 6 < 3 ) OU ( 10 > 11 )
c. ((( 6 // 3 ) % 2 ) > 5 ) E ( 2 < ( 3 % 2 ) )
d. !( 2 < 3 )
'''

print("============================")
print(" ")


print("a. 2 < 3")
a = 2 < 3
print(a)
print("")


print("b. ( 6 < 3 ) OU ( 10 > 11 )")
b = 6 < 3 or 10 > 11
print(b)
print("")


print("((( 6 // 3 ) % 2 ) > 5 ) E ( 2 < ( 3 % 2 ) )")
c = ((( 6 // 3 ) % 2 ) > 5 ) and ( 2 < ( 3 % 2 ) )
print(c)
print("")

print("d. !( 2 < 3 )")
d = not(2<3)
print(d)