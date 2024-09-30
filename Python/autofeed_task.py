#inputs 
#:weight of food and size of dog (small med or large)
#processes   
#2.store a message that states if the total weight of food is within the recommended range 
# 3- calculate the average weight of food in the five containers 
# 4- round the average weight of food to one decimal place
#"/n" makes a new line
#def then pass on next line creates a stub, so that code is runnable while still writing your code
def getWeightOfFood():
    print("Hello user, here are the recomended daily  portion sizes for your dog: \n If your dog is small, we recomend 110g to 140g \n If you have a medium sized dog, wer recommend 330g to 440g \n If your dog is large, we recommend 690g to 900g")
    total_weight = 0
    for counter in range (5):  #start fixed loop 5 times
        container_weight = int(input("Please enter a valid weight for each container in grams")) #enter the foodWeight
        while container_weight <0 or container_weight >200: # while the foodWeight < 0 or foodWeight > 200
            print("Invalid, please enter a valid weight a single container can only hold up to 200g") # display “Invalid, a single container can only hold up to 200g”
            container_weight = int(input("Please enter a valid weight for each container in grams")) # re-enter the foodWeight
    total_weight = total_weight + container_weight # end while # totalWeight = totalWeight + foodWeight # end fixed loop
    return total_weight

def Get_Dog_size(total_weight):
    #1.calc total weight of food in 5 containers, 
    dog_size = input("Please enter the size of your dog, small, medium or large") #display “Please enter the size of your dog: small, medium or large”
    if  dog_size == "small" and total_weight > 110 and total_weight < 140:
        weight_msg = print("This weight is suitable!!")
    elif dog_size == "medium" and total_weight > 330 and total_weight <440:
        weight_msg = print("This weight is suitable")
    elif dog_size == "large" and total_weight > 690 and total_weight <900:
        weight_msg = print("This weight is suitable")
    return total_weight, dog_size



    
    
        


    
#outputs 
#1 the weight of food in each container
#2 the average weight of food in the five containers
#3the rounded average weight of food
#4 the stored message stating if the total weight of food is within the recommended range

#assumptions 
#the user can enter a weight using whole numbers or real numbers
#the user does not need to fill all five containers
#the user will not refill any of the containers until all containers are empty

# main program
tw = getWeightOfFood()
