#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("Convertir grados Celsius  a grados Fahrenheit.")
    C= float(input("Grados Celsius "))
    F= (9.0/5.0)* C+ 32.0
   
   
    print("Grados Celsius {} es {}".format(C,F))
 
if __name__ == "__main__":
    main()

