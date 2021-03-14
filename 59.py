words_upto_19=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
words_for_tens=['','','TWENTY','THERTY','FOURTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
words_for_hundred=['HUNDRED']

n=int(input("enter an integer"))
#outut=""
if n==0:
    print("ZERO")
elif n<=19:
    print(words_upto_19[n])
elif n<=99:
    print(words_for_tens[n//10]+" "+words_upto_19[n%10])
else:
    print(" pls enter invalid input ")