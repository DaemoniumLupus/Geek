# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


# def print_operation_table(operation,num_rows = 6, num_columns = 6):
#   print(f"    {[f'{i}  ' for i in range(1,num_columns + 1)]}")
#   for i in range(1,num_columns+1):
#     print (f"{i}   {[f' {operation(j)} ' for j in range(1,num_columns +1)]}")


def print_operation_table(operation,num_rows = 6, num_columns = 6):
 
  print(*[i for i in range(0,num_columns + 1)])
  for j in range(1,num_columns +1):
    print()


print_operation_table(lambda x: x*x)