import random



def generate_big_prime(n):
    while True:
        p = random.randint(2**(n-1), 2**n)
        if MillerRabin(p, 1000):
            return p

def toBinary(n):
    r = []
    while n > 0:
        r.append(n % 2)
        n = n / 2
        return r

def MillerRabin(n, s = 50): 
    for j in range(1, s + 1):
            a = random.randint(1, n - 1)
            b = toBinary(n - 1)
            d = 1
            for i in range(len(b) - 1, -1, -1):
                x = d
                d = (d * d) % n
                if d == 1 and x != 1 and x != n - 1:
                    return True # Составное
                if b[i] == 1:
                    d = (d * a) % n
                    if d != 1:
                        return True # Составное
                    return False # Простое

class People(object):
	def __init__(self, s_key, name):
		self.s_key = s_key
		self.temp = None
		self.s_key2 = None
		self.name = name


	def write(self, num):
		with open('dialog.txt', 'w', encoding='utf-8') as f:
			print('{} send {}'.format(self.name, num))
			f.write(str(num))


	def read(self):
		with open('dialog.txt', 'r', encoding='utf-8') as f:
			self.temp = int(f.read())
			print('{} read {}'.format(self.name, self.temp))

	def find_key(self):
		self.s_key2 = self.temp**self.s_key%p_key
		print(self.s_key2)

p_key = 20
gen = generate_big_prime(100)

print(gen)


Alice = People(7, 'Alice')
Bob = People(3, 'Bob')


Alice.write(gen**Alice.s_key%p_key)
Bob.read()

Bob.write(gen**Bob.s_key%p_key)
Alice.read()

Alice.find_key()
Bob.find_key()
	
