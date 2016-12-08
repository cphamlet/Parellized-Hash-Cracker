# multiproc_test.py

import random, multiprocessing, hashlib, string, itertools


#alphabet = string.lowercase+string.uppercase+"0123456789"
alphabet = string.lowercase + string.uppercase + "0123456789"

#FUNCTIONS
#This function returns a random string with uppercase characters, lowercase characters, and numbers
def randomstring(length):
                #string.lowercase + uppercase and the numbers indicate the character space
   return ''.join(random.choice(alphabet) for i in range(length))

def generateHash_process(first_bits, id, N):
	"""
	Creates an empty list and then appends a 
	random number to the list 'count' number
	of times. A CPU-heavy operation!
	"""
#	for i in range(count):
#		out_list.append(random.random())
	if(id == 1):
		print("First child")
	elif(id==2):
		print("Second child")
	for precomputedWord in itertools.product(first_bits, alphabet,alphabet,alphabet):
			hashTemp = hashlib.md5(bytes(precomputedWord)).hexdigest()[0:N]
			if(hashTemp in mapofHashes):
	    			precomputedWord = ''.join(precomputedWord)
	      			print(precomputedWord)
     	 	


if __name__ == "__main__":

	N = 9
	f = open("testResults.txt", 'w')
	f.write("These are the results\n\n")
	f.close()

	mapofHashes = {}
        #get random string
   

	#size = 100000000   # Number of random numbers to add
	procs = 3  # Number of processes to create
	num_part = procs
	part_size = len(alphabet) // num_part
	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list 
	jobs = []

	for precomputedWord in itertools.product(alphabet, repeat=9):
		hashTemp = hashlib.md5(bytes(''.join(precomputedWord)).hexdigest()[0:N]
		if len(mapofHashes) < 125000:
		     	 	    mapofHashes[hashTemp] = precomputedWord
		else:
		 	break

	for i in range(0, procs):
		if i == num_part - 1:
				first_bit = alphabet[part_size*i :]
		else:
        		first_bit = alphabet[part_size * i : part_size * (i+1)]

		process = multiprocessing.Process(target=generateHash_process, args=(first_bit, i, N))
		jobs.append(process)


	# Start the processes (i.e. calculate the random number lists)		
	for j in jobs:
		j.start()

	# Ensure all of the processes have finished
	for j in jobs:
		j.join()

	print "List processing complete."
