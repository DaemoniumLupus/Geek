""" Даны два многочлена, которые вводит пользователь. как две строки.
Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

Степени многочленов могут быть разные.

например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
на выходе будет 5x^3 - x^2 + 4х - 7 = 0
можно использовать модуль re """
import re

def Parse_Monomial(start:int,end:int,st:str) -> str:
	# Создание строковых одночленов 
	buf_str = st[start:end]
	buf_str.strip()
	# Убираем пробелы между знаком и одночленом 
	# Убираем +  
	if buf_str[0] == '+'and buf_str[1] == ' ':
		buf_str = buf_str[2:]
		buf_str.strip() 
	elif buf_str[0] == '-'and buf_str[1] == ' ':
		buf_str = "-" + buf_str[2:]

	count = 0
	# Проверка и удаление знака *
	for i in buf_str:
		if i == '*':
			buf_1 = buf_str[count+1:]
			buf_str = buf_str[:count]+buf_1
		count +=1
	# Удаление пробела в конце
	if buf_str[-1] == ' ':
		buf_str = buf_str[:-1]
	return buf_str

def Parse_Full_Sring(st: str) -> []:
	# Создание отрезков с одночленами по знакам '+' '-' или '='
	delimiter_Start = []
	delimiter_End = []
	count_str = 0 # Для пропуска '-' в начале выражения
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
		polynomial.append(Parse_Monomial(delimiter_Start[i],delimiter_End[i],st))

	return polynomial

def Dictionary_Dergree(polynominal:list) -> dict:
	# Создание словарей со степенями х где 0 - без х, 1 - х без степени
	parse_For_Degree = {}
	for i in range(len(polynominal)):
		# Проверка на наличие степени чтобы регулярка не ругалась 
		buf = re.search('\^',polynominal[i])

		#Выделение степеней
		if buf != None:
			degree = re.search('\d',re.search('\^\d',str(polynominal[i]))[0])[0]
			parse_For_Degree[int(degree)] = re.search('[-+]?\d[x]',polynominal[i])[0]
		elif re.search('x',polynominal[i]) != None:
			parse_For_Degree[1] = polynominal[i]
		else:
			parse_For_Degree[0] = polynominal[i]

	return parse_For_Degree	

def Creat_Res_String(dict_res:dict,degree: list) -> str:
	res_str = ""

	# Сортировка max->min для корректного сбора строки
	degree.sort(reverse = True) 

	# Максимальная степень будет стоять в начале и если у нее есть '-' 
	# то пробел после '-' не нужен
	max_degree = degree[0] 

	# Создание пробелов между знаками + и -
	for i in dict_res.items():
		buf = str(i[1])
		if int(i[0]) == max_degree:
			continue
		if buf[0] == '-':
			dict_res[i[0]] = "{0} {1}".format(buf[0],buf[1:])
		else:
			dict_res[i[0]] = "{0} {1}".format('+',buf)
	
	for i in degree: # Сбор строки
		if i <= 1:
			res_str += str(dict_res.get(i)) + ' '
		else:
			res_str += str(dict_res.get(i)) + '^' + str(i) + ' '
		
	res_str += "= 0"
	return res_str


def Reduction(polynominal_1:[],polynominal_2:[]) -> str:
	# Создание словарей со степенями х где 0 - без х, 1 - х без степени
	dict_Degree_1 = {} 
	dict_Degree_2 = {}
	dict_Degree_1 = Dictionary_Dergree(list(polynominal_1)) 
	dict_Degree_2 = Dictionary_Dergree(list(polynominal_2))

	# Создание множества возможных степенией
	list_Degree_1 = list(dict_Degree_1.keys())
	list_Degree_2 = list(dict_Degree_2.keys())
	degree = set(list_Degree_1 + list_Degree_2)

	dict_Res = {}
	num_1 = 0
	num_2 = 0
	# Сложение значений с одинаковыми степенями
	for i in degree:
		if i == 0:
			num_1 = int(dict_Degree_1.get(i,0))
			num_2 = int(dict_Degree_2.get(i,0))
			dict_Res[i] = num_1 + num_2
			if dict_Res[i] == 0:
				dict_Res.pop(i)
		else:
			# Выделение значений без х 
			num_1 = int(re.search('[-+]?\d+',dict_Degree_1.get(i,'0'))[0])
			num_2 = int(re.search('[-+]?\d+',dict_Degree_2.get(i,'0'))[0])
			dict_Res[i] = num_1 + num_2 
			if dict_Res[i] == 0:# Удаляем нулевые значения из словаря
				dict_Res.pop(i)
			elif dict_Res[i] == -1: #убираем 1 и -1
				dict_Res[i] = '-x'
			elif dict_Res[i] == 1:
				dict_Res[i] == 'x'
			else:
				dict_Res[i] = str(dict_Res[i]) + 'x'
	# Переопределение существующих степенией		
	degree = set(dict_Res.keys())
	
	return Creat_Res_String(dict_Res,list(degree))


#st1 = '2x^2 + 4x + 5 = 0'
#st2 = '5x^3 - 3*x^2 - 12 = 0'

st1 = input("Enter first: ")
st2 = input("Enter second: ")

res = Reduction(Parse_Full_Sring(st1),Parse_Full_Sring(st2))
print(f"Reult -> {res}")