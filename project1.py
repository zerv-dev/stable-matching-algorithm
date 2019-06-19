from itertools import permutations
men = []
women = []

def generate_permutations(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return [lst]
	else:
		listOfPermutations = []
		for i in range(len(lst)):
			currentElement = lst[i]
			remainingList = lst[:i] + lst[i+1:]
			for j in generate_permutations(remainingList):	
				listOfPermutations.append([currentElement] + j)
		return listOfPermutations





def man_prefer_woman(man,womenIndex,currentMatch):
	return man.index(womenIndex) < man.index(currentMatch)

def woman_prefer_man(womanIndex,manIndex,currentMatch):
	woman = women[int(womanIndex) - 1] #arrays are offset
	return woman.index(str(manIndex+1)) < woman.index(str(currentMatch+1))

def is_a_stable_match(lst):
	for i in range(0,len(lst)):
		man_current_match= lst[i]
		for woman in men[i]:
			# print(woman)
			if(woman == lst[i]):
				break
			if man_prefer_woman(men[i],woman,man_current_match): #checks if man at index i to leave his current match
				woman_current_match = lst.index(woman)
				if woman_prefer_man(woman,i,woman_current_match):# checks if woman wants to leave her current match for curent man int the loop
					return False
	return True
	

if __name__ == '__main__':
	file = open("input1.txt" , "r")
	number_of_pairs = int(file.readline())
	for i in range(number_of_pairs):
		men.append(list(file.readline().split()))# reads file
	for i in range(number_of_pairs):
		women.append(list(file.readline().split()))# reads file
	list_of_numbers = []
	for i in range(1,number_of_pairs+1):
		list_of_numbers.append(str(i))
	perm = permutations(list_of_numbers)# creates the permutaions.
	number_of_stable_matches= 0
	for lst in perm:
		if is_a_stable_match(lst):																																																																						
			number_of_stable_matches +=1
		
	print	(number_of_stable_matches)