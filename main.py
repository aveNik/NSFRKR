#hello
print("maded by tiny_mauss")
print("-------------------")
print(" ")

# LCD
def LCD():
  a=input("a = ")
  b=input("b = ")
  try:
    #int convert
    ai=int(a)
    bi=int(b)  #ai & bi is abreviation of "a interger"... Why i write it? Users of github can understand this shit-code
    while a*b != 0:
      if a >= b:
        a=a+b
      else:
        b=b%a
    LCD=a+b
    print(LCD)
  except ValueError:
    print("NaN")
    return

def Fragment():
  s=input("")
  n=len(s)
  s1=''
  for i in range(n):
    l=str(s[i])
    s1+=1
    if l==".":
      break
  print(s1)

def NoS():
  s=input("Input text: ")
  k=0
  n=len(s):
  for i in range(n):
    l=str(s[i])
     if l=='.' or l=="!" or l=="?":
       k=k+1
  print(k)
