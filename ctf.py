def generate():
     string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
     from random import choice
     wrd:list = []
     for i in range(25):
          a = choice(string)
          wrd.append(a)
     new_wrd:str = "CTF{"
     for i in wrd:
          new_wrd = new_wrd + i 
     new_wrd=new_wrd+"}"
     return new_wrd
