
"""
Author: Nicholas G. Burkett
Date: 05/15/2023
Problem: Remove duplicate values from a sorted array
Expected input:  [1, 1, 2, 3, 3, 4]
Expected output: [1, 2, 3, 4, _, _]
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
				#Here is my attempt to fix my issue with a while loop: 
				itr = (i+1)		#Need to set my counter ahead one
				boolHelper = True	#Need to set another counter for my 2nd while loop
				counter = 1 		#Needed to create a vairable to keep track of how many repeated chars I encounter
				
				#Now I need to enter the second while loop. This will allow me to count how many repeated chars I have
				while(boolHelper): 
					#Now I need to check ahead
					if(itr >= len(nums)-1): 
						boolHelper = False
					elif(nums[itr] == nums[itr+1]):
						#If I fall in here then I know I have more than one occurrence of the same character.
						print(nums[itr]) 
						counter += 1
						itr += 1
					else:
						print(nums[itr]) 
						#If I fall in here, then I just need to stop and exit the loop.
						boolHelper = False	#Need to terminate the loop. 

				#Now I need to actually go in and change the appropriate values within my array
				for j in range((i+1), (len(nums))):
					#In here I will loop through the array and replace with I need

					#Here I need to check if I am replacing with a int or a '_'
					if(j < (len(nums)-counter)): 
						'''
						 -------------------------------------------------------------------------------
						 --- Here I have the following understanding: If i is < j+counter or how many 
						 --- repeating occurences I find... aka-->counter then I am looking at an index
						 --- that needs to be replaced w an integer and not a '_'.
						 ------------------------------------------------------------------------------- 
						'''
						nums[j] = nums[j+counter]	#Replace with the respected value ahead in the array
					
					elif(j < len(nums)):
						#If I fall in here then I need to replace w a '_'
						nums[j] = '_'	#Replace with an underscore	

					else: 
						#If I end up in here something bad happened
						print("ERROR")
						

				i += 1

			#This else is intended for when I don't have a current match...
			#...i.e -> nums[i] != nums[i+=1]
			else: 
				i += 1    #Increment the main counter and keep moving
		return nums 	
    	#Here I will define a main method to run the show
	def main(self):
		#Here I will create test data and see what works
		#First I need to create a couple test arrays		
		testArr01 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]    #Test array 1
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
