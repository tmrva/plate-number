def validate(platenumber):
    if(len(platenumber)!=9):
        message="The length of the entered number does not match"
    elif(type(int(platenumber[0:1])) is not int and type(int(platenumber[6:9])) is not int):
        message="The numbers have entered incorrectly"
    elif(platenumber[3:5].isalpha() is False):
        message="The letters have entered incorrectly"
    elif(platenumber[3:5].upper() is not True):
        message="The plate series number must be capitalised"
    elif(platenumber[2]!="-" and platenumber[5]!="-"):
        message="There must be - in plate number"
    else:
        message="You have entered the plate series number correctly" 
    return message   

print(validate("10-AZ-621"))