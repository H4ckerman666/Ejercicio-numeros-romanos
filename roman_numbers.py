# keys for unique numbers
keys=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#roman number for each key
dict_numbers={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
#var to save the final result
complete_result = []     

#function to covert decimal numbers to roman rumbers
def roman_numbers(number):
    result = ""
    more_digit = 0
    if number in keys:
        result += dict_numbers[number]
    else:
        for num in keys:
            if number > num:
                multi = number // num
                more_digit = number % num
                result += dict_numbers[num]*multi
                break
                
    complete_result.append(result)    
    if more_digit > 0 :
        roman_numbers(more_digit)         

# cycle to print numbers in a determinate range 
for number in range(1,21):
    #function 
    roman_numbers(number)
    #joins the results of the list into only one 
    result = "".join(complete_result)
    #cleans the list to use it for new numbers 
    complete_result.clear()
    #print result 
    print(f'El número {number} en romano es : {result}')


    
    
        

