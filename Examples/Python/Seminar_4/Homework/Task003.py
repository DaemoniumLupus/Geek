""" Даны два многочлена, которые вводит пользователь. как две строки.
Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

Степени многочленов могут быть разные.

например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re """
import re

def Parse_Monomial(start:int,end:int,st:str) -> str:
	buf_str = st[start:end]
	buf_str.strip()

	if buf_str[0] == '+'and buf_str[1] == ' ':
		buf_str = buf_str[2:]
		buf_str.strip() 
	elif buf_str[0] == '-'and buf_str[1] == ' ':
		buf_str = "-" + buf_str[2:]

	count = 0
	for i in buf_str:
		if i == '*':
			buf_1 = buf_str[count+1:]
			buf_str = buf_str[:count]+buf_1
		count +=1

	if buf_str[-1] == ' ':
		buf_str = buf_str[:-1]
	return buf_str

def Parse_Full_Sring(st: str) -> []:
	delimiter_Start = []
	delimiter_End = []
	count_str = 0
	count_Monomial = 0

	delimiter_Start.append(0)
	for i in st:
		if i == '+' or i == '-' and count_str != 0:
			delimiter_End.append(count_str)	
			delimiter_Start.append(count_str)
			count_Monomial += 1
		if i == '=':
			delimiter_End.append(count_str)
			count_Monomial += 1
			break
		count_str += 1

		polynomial = []

	for i in range(count_Monomial):
		#print(Parse_Monomial(delimiter_Start[i],delimiter_End[i],st))
		polynomial.append(Parse_Monomial(delimiter_Start[i],delimiter_End[i],st))

	return polynomial

def Dictionary_Dergree(polynominal:[]) -> {}:
	parse_For_Degree = {}
	for i in range(len(polynominal)):

		buf = re.search('\^',polynominal[i])

		if buf != None:
			degree = re.search('\d',re.search('\^\d',str(polynominal[i]))[0])[0]
			parse_For_Degree[int(degree)] = re.search('[-+]?\d[x]',polynominal[i])[0]
		elif re.search('x',polynominal[i]) != None:
			#buf = re.search('x',polynominal[i])
			#if buf != None:
			parse_For_Degree[1] = polynominal[i]
		else:
			parse_For_Degree[0] = polynominal[i]

	print(parse_For_Degree)
	return parse_For_Degree	


def Reduction(polynominal_1:[],polynominal_2:[]) -> str:
	res_String = ""
	dict_Degree_1 = {} 
	dict_Degree_2 = {}
	dict_Degree_1 = Dictionary_Dergree(list(polynominal_1))
	dict_Degree_2 = Dictionary_Dergree(list(polynominal_2))

	list_Degree_1 =list( dict_Degree_1.keys())
	list_Degree_2 = list(dict_Degree_2.keys())

	degree = set(list_Degree_1 + list_Degree_2)

	num_1 = 0
	num_2 = 0
	for i in degree:
		if i == 0:
			num_1 = int(dict_Degree_1.get(i,0))
			num_2 = int(dict_Degree_2.get(i,0))
		



	print(degree)
	print (num_1 + num_2)
	return res_String


st1 = '2x^3 + 4x + 5 = 0'
st2 = '-5x^3 - 3*x^2 - 12 = 0'



res = Reduction(Parse_Full_Sring(st1),Parse_Full_Sring(st2))
print(res)