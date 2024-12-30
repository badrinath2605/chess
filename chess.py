#final chess game
#pieces : ♔♕♖♗♘♙ ♚♛♜♝♞♟
print("RULES\n1.please enter position in 'letternumber' format;(letters in caps)\n")
n="1.  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖     \n\n2.  ♙   ♙   ♙   ♙   ♙   ♙   ♙   ♙     \n\n3.  _   _   _   _   _   _   _   _     \n\n4.  _   _   _   _   _   _   _   _     \n\n5.  _   _   _   _   _   _   _   _     \n\n6.  _   _   _   _   _   _   _   _     \n\n7.  ♟   ♟   ♟   ♟   ♟   ♟   ♟   ♟     \n\n8.  ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜     \n\n..  A   B   C   D   E   F   G   H   \n \n "
print(n)
def bishop(n,v,u,t,u1,t1,U,T,Index,index,i):
      white="♔♕♖♗♘♙"
      black="♚♛♜♝♞♟" 
      if((u>U) and (t>T)):
          while((u>U) and (t>T) and n[Index]=="_"):
              Index+=44
              if(index==Index and((n[Index]=="_") or(n[Index] in black and i%2!=0) or(n[Index] in white and i%2==0))):
                  return n,v,u1,t1
      if((u>U) and (t<T)):
          while((u>U) and (t<T) and n[Index]=="_"):
              Index+=36
              if(index==Index and((n[Index]=="_") or(n[Index] in black and i%2!=0) or(n[Index] in white and i%2==0))):
                  return n,v,u1,t1
      if((u<U) and (t>T)):
          while((u<U) and (t>T) and n[(U-1)*40+(T-64)*4]=="_"):
              Index-=36
              if(index==Index and((n[Index]=="_") or(n[Index] in black and i%2!=0) or(n[Index] in white and i%2==0))):
                  return n,v,u1,t1
      if((u<U) and (t<T)):
          while((u>U) and (t>T) and n[(U-1)*40+(T-64)*4]=="_"):
              Index-=44
              if(index==Index and((n[Index]=="_") or(n[Index] in black and i%2!=0) or(n[Index] in white and i%2==0))):
                  return n,v,u1,t1
      
      n=n[:Index]+v+n[Index+1:]
      print('please make a valid move')
      n,v,u1,t1=move(n,i)
      return n,v,u1,t1
def rook(n,v,u,t,u1,t1,U,T,Index,index,i):
      white="♔♕♖♗♘♙"
      black="♚♛♜♝♞♟"
      if(T==t):
          if(u>U):
              print('hi😎')
              while((u>U) and n[(U-1)*40+(T-64)*4]=="_"):
                  U=U+1
                  if((u==U) and ((n[(U-1)*40+(T-64)*4] in black and i%2!=0)or(n[(U-1)*40+(T-64)*4] in white and i%2==0)or(n[(U-1)*40+(T-64)*4]=="_"))):
                      return n,v,u1,t1
          if(u<U):
              while((u<U) and n[(U-1)*40+(T-64)*4]=="_"):
                  U-=1
                  if((u==U) and ((n[(U-1)*40+(T-64)*4] in black and i%2!=0)or(n[(U-1)*40+(T-64)*4] in white and i%2==0)or(n[(U-1)*40+(T-64)*4]=="_"))):
                      return n,v,u1,t1
      if(U==u):
          if(t>T):
              while((t>T) and n[(U-1)*40+(T-64)*4]=="_"):
                  T+=1
                  if((t==T) and ((n[(U-1)*40+(T-64)*4] in black and i%2!=0)or(n[(U-1)*40+(T-64)*4] in white and i%2==0)or(n[(U-1)*40+(T-64)*4]=="_"))):
                      return n,v,u1,t1
          if(t<T):
              while((t<T) and n[(U-1)*40+(T-64)*4]=="_"):
                  T-=1
                  if((t==T) and ((n[(U-1)*40+(T-64)*4] in black and i%2!=0)or(n[(U-1)*40+(T-64)*4] in white and i%2==0)or(n[(U-1)*40+(T-64)*4]=="_"))):
                      return n,v,u1,t1
      n=n[:Index]+v+n[Index+1:]
      print('please make a valid move')
      n,v,u1,t1=move(n,i)
      return n,v,u1,t1
def restrictions(n,v,u,t,w,index,u1,t1,i):
  U=w//40+1;T=(w%40)//4+64
  Index=w
  p={"♙"}
  P={"♟"}
  r={"♖","♜"}
  b={"♗","♝"}
  h={"♘","♞"}
  k={"♔","♚"}
  q={"♕","♛"}
  if(v in q):
      if(T==t or U==u):
         return rook(n,v,u,t,u1,t1,U,T,Index,index,i)
      else:   
         return bishop(n,v,u,t,u1,t1,U,T,Index,index,i)
  if(v in h):
      if((w+84==index)or(w+76==index)or(w+48==index)or(w-32==index)or(w+32==index)or(w-48==index)or(w-84==index)or(w-76==index)):
          return n,v,u1,t1
  if(v in k):
      if((w+4==index)or(w-4==index)or(w+40==index)or(w-40==index)or(w+44==index)or(w-44==index)or(w+36==index)or(w-36==index)):
          return n,v,u1,t1
  if(v in b):
     return bishop(n,v,u,t,u1,t1,U,T,Index,index,i)
  if(v in r):
     return rook(n,v,u,t,u1,t1,U,T,Index,index,i)
  if(v in p):
    if((n[w+44]!="" and w+44==index ) or (n[w+36]!="" and w+36==index)):
      return n,v,u1,t1
    if(n[w+40]=="_"):
      if(((index==w+80) and (v in n[39:81])) or (index==w+40)):
        return n,v,u1,t1
  if(v in P):
    if((w-44==index and n[w-44]!="") or (w-36==index and n[w-36]!="")):
      return n,v,u1,t1
    if(n[w-40]=="_"):
      if(((v in n[239:281]) and (index==w-80)) and (n[w-40]=="_")):
        return n,v,u1,t1
  n=n[:Index]+v+n[Index+1:]
  print('please make a valid move')
  n,v,u1,t1=move(n,i)
  return n,v,u1,t1      
def move(n,i):
   v=input("what do you want to move:");meliodas=v[0].upper()
   u1,t1=int(v[1]),ord(meliodas);index1=(u1-1)*40+(t1-64)*4
   v=n[index1]
   print(v)
   white="♔♕♖♗♘♙"
   black="♚♛♜♝♞♟"
   if((v in n) and (((v in white) and (i%2!=0)) or ((v in black) and (i%2==0)))):
     i=input("where do you want to move it:")
     w=index1
     u,t=int(i[1]),ord(i[0]);index=(u-1)*40+(t-64)*4
     n=n[:index1]+"_"+n[index1+1:]
     temp,v,u1,t1=restrictions(n,v,u,t,w,index,u1,t1,i)
     index1=(u1-1)*40+(t1-64)*4
     n=temp[:index]+v+temp[index+1:]
     return n,v,u1,t1
   else:
       return move(n,i)
i=1
while((i<10000) and ('♚' in n) and('♔' in n)):
  if(i%2!=0):
    n,v,u1,t1=move(n,i)
    print(n)
    i+=1
  elif('♔' in n):
    n,v,u1,t1=move(n,i)
    print(n)
    i+=1
  else:
    print("🥳🥳🥳🥳🥳🥳🥳🥳🥳  WHITE WON  🥳🥳🥳🥳🥳🥳🥳🥳🥳")
else:
  print("🥳🥳🥳🥳🥳🥳🥳🥳🥳  BLACK WON  🥳🥳🥳🥳🥳🥳🥳🥳🥳")