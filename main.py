import time

#hello
print("maded by tiny_mauss")
print("-------------------")
print(" ")

# LCD
def LCD():
  a=int(input('a= '))
  b=int(input('b= '))
  while a*b != 0:
    if a>=b:
      a = a % b
    else:
      b = b % a
  LCD=a+b
  print(LCD)

def Fragment():
  s=input("input text > ")
  n=len(s)
  s1=''
  for i in range(n):
    l=str(s[i])
    s1+=l
    if l==".":
      break
  print(s1)

def NoS():
  s=input("Input text > ")
  k=0
  n=len(s)
  for i in range(n):
    l=str(s[i])
    if l=='.' or l=="!" or l=="?":
       k=k+1
  print(k)

def main():
  print("What function you want to try? (1 or 2 or 3):")
  print("1) LCD; 2) Fragment; 3) NoS")
  choise = input("> ")
  if choise == "1":
    LCD()
  elif choise == "2":
    Fragment()
  elif choise == "3":
    NoS()
  else:
    print("Err: restart after 3 seconds")
    time.sleep(3)
    main()

main()
