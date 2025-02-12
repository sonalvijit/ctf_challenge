from ctf import generate

def check_ans(file_path:str,opt:int=1):
     with open(file_path,"r") as f:
          if opt == 1:
               for i in f:
                    if i[0:6] == "ROBOTS":
                         ans = i[7:]
                         return ans
          if opt == 2:
               for i in f:
                    if i[0:11] == "SOURCE-CODE":
                         ans = i[12:]
                         return ans
          if opt == 3:
               for i in f:
                    if i[0:6] == "Cookie":
                         ans = i[7:]
                         return ans
          if opt == 4:
               for i in f:
                    if i[0:8] == "Site-Map":
                         ans = i[9:]
                         return ans
def _GENERATE_FLAG():
     with open("./templates/1.htm","r",encoding='utf-8-sig') as f:
          lines = f.readlines()
          if lines[-1][0:10] == "<!--   CTF":
               pass
          else:
               with open("./templates/1.htm","a") as f:
                    data = generate()
                    f.write(f"<!--   {data}   -->")
                    with open("./onsite/answer.txt","a") as f:
                         f.write(f"SOURCE-CODE:{data}\n")
                         f.close()
                    f.close()
     with open("./static/robots.txt","r") as f:
          lines = f.readlines()
          if lines[-1][0:3] == "CTF":
               pass
          else:
               with open("./static/robots.txt","a") as f:
                    data = generate()
                    f.write(f"\n{data}")
                    with open("./onsite/answer.txt","a") as f:
                         f.write(f"ROBOTS:{data}\n")
                         f.close()
                    f.close()
     ADD_COOKIE()
     GENERATE_SITEMAP_FLAG()

def GENERATE_SITEMAP_FLAG():
     try:
          with open("./onsite/answer.txt", 'r') as file:
               lines = file.readlines()
               cookie_found = False
               for line_number, line in enumerate(lines, start=1):
                    if line.strip().startswith('Site-Map:'):
                         cookie_found = True
                         cookie_value = line.strip().split(":", 1)[1].strip()
                         break
          if not cookie_found:
               generated_code = generate()
               with open("./onsite/answer.txt", 'a') as file:
                    file.write(f"Site-Map:{generated_code}\n")
     except FileNotFoundError:
          pass
     except Exception as e:
          print(f"Error: {e}")

def GET_SITEMAP_FLAG():
      with open("./onsite/answer.txt", 'r') as file:
          lines = file.readlines()
          cookie_found = False
          for line_number, line in enumerate(lines, start=1):
               if line.strip().startswith('Site-Map:'):
                    cookie_found = True
                    cookie_value = line.strip().split(":", 1)[1].strip()
                    return cookie_value

def ADD_COOKIE():
     try:
          with open("./onsite/answer.txt", 'r') as file:
               lines = file.readlines()
               cookie_found = False
               for line_number, line in enumerate(lines, start=1):
                    if line.strip().startswith('Cookie:'):
                         cookie_found = True
                         break
          if not cookie_found:
               generated_code = generate()
               with open("./onsite/answer.txt", 'a') as file:
                    file.write(f"Cookie:{generated_code}\n")

     except FileNotFoundError:
          pass
     except Exception as e:
          print(f"Error: {e}")

def GET_COOKIE():
     with open("./onsite/answer.txt", 'r') as file:
               lines = file.readlines()
               cookie_found = False
               for line_number, line in enumerate(lines, start=1):
                    if line.strip().startswith('Cookie:'):
                         cookie_found = True
                         cookie_value = line.strip().split(":", 1)[1].strip()
                         return cookie_value

def _NORMALIZING():
     with open("./static/robots.txt","r+") as f:
          lines = f.readlines()
          if not lines:
              raise ValueError("File is empty")
          f.seek(0)
          f.writelines(lines[:-1])
          f.truncate()
     with open("./onsite/answer.txt","w") as f:
          f.write("")
          f.close()
     with open("./templates/1.htm","r+",encoding='utf-8-sig') as f:
          lines = f.readlines()
          if not lines:
              raise ValueError("File is empty")
          f.seek(0)
          f.writelines(lines[:-1])
          f.write("\n\n")
          f.truncate()