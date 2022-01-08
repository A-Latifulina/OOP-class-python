codes= {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9}
message=input('Enter coded numeric message' )

print('The real message is ')
for i in range (8):
    print(codes[ message[i] ] , end='')
