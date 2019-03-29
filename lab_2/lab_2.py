

message1 = 4321
message2 = 4322


# h_1


def h_1(message):
	seed = 1337228
	hashAddress = 0
	for i, j in enumerate(str(message)):
		hashAddress = (hashAddress*seed) + ord(j) + i

	return hashAddress


# h_2


def h_2(message):
	hashAddress = 0;
	for i, j in enumerate(str(message)):
		hashAddress = ord(j) + (hashAddress << 6) + (hashAddress << 16) - hashAddress


	return hashAddress


# h_3


def rwh_primes(n):
  sieve = [True] * n
  for i in range(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
  some = [2] + [i for i in range(3,n,2) if sieve[i]]
  return some[0]


def h_3(message):
	hashAddress = 0;
	for i, j in enumerate(str(message)):
		hashAddress = (hashAddress + ord(j))*rwh_primes(i)


	return hashAddress



# h_f 4



print(h_1(message1))
print(h_1(message2))
print('\n\n')



print(h_2(message1))
print(h_2(message2))
print('\n\n')




print(h_3(message1))
print(h_3(message2))
print('\n\n')












