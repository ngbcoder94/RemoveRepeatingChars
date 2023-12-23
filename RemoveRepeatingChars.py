
"""
Author: Nicholas G. Burkett
Date: 05/15/2023
Problem: Remove duplicate values from a sorted array
Expected input:  [1, 1, 2, 3, 3, 4]
Expected output: [1, 2, 3, 4]
Level: Easy
"""

#Here I will create a class for this problem
class Solution(object):	
    
	#Need to create a function that will remove the duplicates
	def removeDuplicates(self, nums): 
		"""
		:type nums: List[int]
		:type: int
		"""
		
		lenOfArr = len(nums)    #Calculate the length of the array
		boolVar = True          #Create a boolean variable to run the main while loop
		i = 0		        #Create a counter variable to index the array

		#Create a while loop to step through the array
		while(boolVar):
			#First I will perfrom a bounds check on a pointer
			if(i == (lenOfArr - 1)):
				boolVar = False	  #Set the boolVar to false becasue I am done

			#I will check to see if we have a duplicate pair
			elif(nums[i] == nums[i+1]):
				#If I fall in here I know I need to alter the array... aka replace some values
				#Here I will create a for loop to step through and alter the array

				#THINKING A WHILE LOOP HERE WILL FIX MY ISSUE!!!!!!!
				itr = i+1     #Declare a second counter variable for the for-loop
				for itr in range(itr, (lenOfArr - 1)): 
					#Possibly need to check bounds here, but I don't think I do... we will see
					nums[itr] = nums[itr+1]    #Perform the swap

				

				nums[(lenOfArr-1)] = "_" 	    #Perform the final replacement
				i += 1      			    #Increment the main counter
			
			#This else is intended for when I don't have a current match...
			#...i.e -> nums[i] != nums[i+=1]
			else: 
				i += 1    #Increment the main counter and keep moving

		return nums 	
    	#Here I will define a main method to run the show
	def main(self):
		#Here I will create test data and see what works
		#First I need to create a couple test arrays		
		testArr01 = [0, 0, 1, 1, 1, 2, 2, 2, 3, 4]    #Test array 1
		#testArr02 = [1, 2, 2, 3, 4]          #Test array 2
		#testArr03 = [1, 2, 3, 4, 5, 6, 7]    #Test array 3
		
		print("Entering testing...")	     #Display message to user stating they have started the process	
		
		#Here is where I test array 1
		print(test.removeDuplicates(testArr01))   #Display the result of test 1
		#print(test.removeDuplicates(testArr02))   #Display the result of test 2
		#print(test.removeDuplicates(testArr03))   #Display the result of test 3
 
#Now I need to call the main method
if __name__ == "__main__": 
	test = Solution()
	test.main()		 
