numbers = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven'
           ,8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen'
           ,14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen'
           ,19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty'
           ,60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
 
lettersCount = 0
 
for i in range(1,1001):
 
    if i < 20:
        lettersCount += len(numbers[i])
       
 
    elif i >= 20 and i < 100:
        lettersCount += len(numbers[(i/10)*10]) + len(numbers[i%10])
       
 
    elif i >= 100 and i < 1000:
 
        if i%100 == 0:
            lettersCount += len(numbers[(i/100)]) + len('hundred')
           
        elif i%100 > 10 and i%100 < 20:
            lettersCount += len(numbers[(i/100)]) + len('hundredand')\
            + len(numbers[i%100])
        else:
            lettersCount += len(numbers[(i/100)]) + len('hundredand')\
            + len(numbers[((i%100)/10)*10]) + len(numbers[(i%100)%10])
           
    elif i == 1000:
        lettersCount += len('onethousand')
 
print lettersCount