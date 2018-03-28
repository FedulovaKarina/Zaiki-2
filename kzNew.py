#Spinkoins
#область работы карины

#подключение функции рандома
import random

#задаем рандомное число для отгадывания
random_num=random.randint(1000,9999)
#переводим рандомное число в строку для проверки
stroka_randoma=str(random_num)
#начало рекурсивной ловушки для рандомного числа
if stroka_randoma[0]!=stroka_randoma[1]!=stroka_randoma[2]!=stroka_randoma[3]:
        1+1
else  :
        while stroka_randoma[0]==stroka_randoma[1] or stroka_randoma[0]==stroka_randoma[2] or stroka_randoma[0]==stroka_randoma[3] or 
stroka_randoma[1]==stroka_randoma[2] or stroka_randoma[1]==stroka_randoma[3] or stroka_randoma[2]==stroka_randoma[3] :
                stroka_randoma=str(random.randint(1000,9999))

#конец ловушки

print(q)

#начало функции по вводу пользовательского числа
def num():
#!!!!проблемный блок кода (невыходящая рекурсия)
	#вводим пользовательское число
	n=str(input())
	#ограничение для числа and рекурсивная ловушка
	l=len(n)
	if l==3 and n[0]!=n[1]!=n[2]!=n[3] and n[1]!=n[0]!=n[2]!=n[3] and n[2]!=n[0]!=n[1]!=n[3] and n[3]!=n[0]!=n[1]!=n[2]:
        	print("OK")
	elif l<4 or l>4 or [0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3]:
        	while l<4 or l>4 or [0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3]:
                    n=str(input())
                    print("False")

		

	#переводим число в строку для проверк
	#начало второй рекурсивной ловушки
	#if n[0]!=n[1]!=n[2]!=n[3] and n[1]!=n[0]!=n[2]!=n[3] and n[2]!=n[0]!=n[1]!=n[3] and n[3]!=n[0]!=n[1]!=n[2]:
       	#	 1+1
	#elif n[0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3]  :
       	#	 while n[0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3] :
        #        	n=str(input())

	return n
#конец функции 


#начало функции топоры и тузы
def Ace_Axe(n,q):

	#Начало реализации правил игры
	#система работы топоров
	i=0
	c=0

	for i in range(4):
       		 if q[i]==n[i]:
                	c=c+1
       		 else :
                	i=i+1
	
	print ('Вы имеете'+' '+str(c)+' '+'Топора')
	#cистема работы топоров отлажена
	
	#система работы тузов	
	r=0
	g=0
	d=0

	for r in range(4):
        	for g in range(4):
                	if q[r]==n[g]:
                        	d=d+1
               		else :
                       		g=g+1

	d=d-c
	print ('Вы имеете'+' '+str(d)+' '+'Туза')
	#cистема работы тузов отлажена
	return c

#конец функии 

#функция самой игры 

def open(num,stroka_randoma):
	z=num()
	c=Ace_Axe(z,stroka_randoma)
	return c
#конец функции
p=open(num,stroka_randoma)
#условие цикличности
if p==4:
	print("OK")
elif p!=4 or p==0 :
	while p!=4 :
		p  #=open(num,q)
#Конец
