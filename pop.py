import time 
from datetime import datetime





dt_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def history(oper, res):
    with open ('hist.txt', 'a', encoding='utf-8') as f:
        f.write (f"[{dt_now}] | Действие: {oper} Результат: {res} \n")

def chek_hist(cmd):
  try:
    with open('hist.txt', 'r', encoding='utf-8') as f: 
        content = f.read()
    if not content:
        print("файл пуст.")
    else:
        print(content)
  except FileNotFoundError:
    print("нет файла")



# давление воды 
def water_pressure(cmd):
  try:
    p = float(input("введите плостность жидкости:"))
    h = float(input("введите высоту столба жидкости:"))
    print("вычислеие....")
    time.sleep(2)
    print("гидростатическое давление равно:")
    res = p * h * 9.8
    oper = "wpr"
    print(res)

    history(f"Действие: {oper} ||Результат: ", res)


  except ValueError:
    print("ошибка")
  except ZeroDivisionError:
    print("ошибка")


# давление твердого тела
def solid_pressure(cmd):
  try:
    f = float(input("введите силу в ньютонах(H):"))
    s = float(input("введите площадь поверхности:"))
    print("вычислеие....")
    time.sleep(2)
    print("давление твердого тела равно:")
    res = f / s
    oper = "spr"
    print(res)
    history(f"Действие: {oper} ||Результат: ", res)
  except ValueError:
    print("ошибка")
  except ZeroDivisionError:
    print("ошибка")
# закон Гука
def elastic_force(cmd):
  try:
    k = float(input("введите коэффициент жесткости тела:"))
    l = float(input("введите удлинение или деформацию тела:"))
    print("вычислеие....")
    time.sleep(2)
    print("сила упругости равна:")
    res = k * l 
    oper = "elf" 
    print(res)
    history(f"Действие: {oper} ||Результат: ", res)
  except ValueError:
    print("ошибка")
  except ZeroDivisionError:
    print("ошибка")

# плотность
def density(cmd):
  try:
    m = float(input("введите массу:"))
    v = float(input("введите объем:"))
    res = m/v 
    oper = "den"
    print("вычислеие....")
    time.sleep(2)
    print(res)
    history(f"Действие: {oper}||Результат: ", res)
  except ValueError:
    print("ошибка")
  except ZeroDivisionError:
    print("ошибка")







def help(cmd):
    print("список команд:")
    print(" wpr-давление воды\n spr-давление твердого тела\n elf-закон Гука")








while True:
    cmd = input("введите команду(список команд-help):")
    if cmd.lower() == "wpr":
        water_pressure(cmd)
    elif cmd.lower() == "spr":
         solid_pressure(cmd)
    elif cmd.lower() == "elf":
         elastic_force(cmd)
    elif cmd.lower() == "den":
        density(cmd)
    elif cmd.lower() == "help":
           help(cmd)
    elif cmd.lower() == "chhs":
        chek_hist(cmd)
    elif cmd.lower() == "back":
        print("back\n<------------")
        break 










    else:
      print("такой команды нет") 









