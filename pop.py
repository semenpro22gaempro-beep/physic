import time 
from datetime import datetime

print("Добро пожаловать в мой калькулятор")
print("__________________________________")



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

# сила тяжести
def gravity(cmd):
  try:
    m = float(input("введите массу:"))
    res = m * 10 
    oper = "grv"
    print("вычислеие....")
    time.sleep(2)
    print(res)
    history(f"Действие: {oper}||Результат: ", res)
  except ValueError:
    print("ошибка")
  except ZeroDivisionError:
    print("ошибка")


# скорость при прямом направлении
def speed(cmd):
  try:
    s = float(input("введите путь:"))
    t = float(input("введите время:"))
    res= s / t 
    oper = "spd"
    print("вычислеие....")
    time.sleep(2)
    print(res)
    history(f"Действие: {oper}||Результат: ", res)
  except ValueError:
    print("ошибка")
  except ZeroDivisionError:
    print("ошибка")



# калькулятор 
def calc2(cmd):
 try:
   name = input("введите величину(cm2,pa,km/h)")
   perev = input("введите во что перевести(m2,kpa,m/s)")
   chis = float(input("введите количество:"))
   if name.lower() == "cm2" and perev.lower() == "m2":
      res = chis / 10000
      print("вычисление....")
      time.sleep(2)
      print(res)
   if name.lower() == "pa" and perev.lower() == "kpa":
      res = chis / 10000 
      print("вычислеие....")
      time.sleep(2)
      print(res)
   if name.lower() == "km/h" and perev.lower() == "m/s":
      res = chis / 3.6 
      print("вычислеие....")
      time.sleep(2)
      print(res)
 except ValueError:
      print("ошибка")
 except ZeroDivisionError:
    print("ошибка")


 
def calc(cmd):
  num1 = float(input("введите число 1:"))
  num2 = float(input("введите число 2:"))
  go = input("введите действие:")
  if go == "+":
    print(num1 + num2)
  elif go == "-":
    print(num1 - num2)
  elif go == "*":
    print(num1 * num2)
  elif go == "/":
    print(num1 / num2)
  else:
    print("доступны только действия: * / + -")













# документация
def doc(cmd):
  print("!Пишите сразу готовые велчины измерения никаких сантиметров2 и тп ")
  print("!Иначе калькулятор посчитает неправильно")
  print("!Для преобразование величин есть калькулятор(calc2),на данный момент там 3 еденицы для перевода")

# help 
def help(cmd):
    print("список команд:")
    print(" wpr-давление воды\n spr-давление твердого тела\n elf-закон Гука\n back-выход\n chhs-просмотр истории\n den-плотность\n")
    print(" grv-сила тяжести\n spd-скорость при прямом направлении\n cmd-докуменатция,предупреждения\n calc-простой калькулятор,выводит сразу несколько действий")
    print(" calc2-калькулятор,переводит величины\n")





# команды
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
    elif cmd.lower() == "grv":
            gravity(cmd)
    elif cmd.lower() == "spd":
            speed(cmd)
    elif cmd.lower() == "calc2":
           calc(cmd)
    elif cmd.lower() == "calc":
           calc(cmd)
    elif cmd.lower() == "help":
           help(cmd)
    elif cmd.lower() == "chhs":
           chek_hist(cmd)
    elif cmd.lower() == "doc":
           doc(cmd)
    elif cmd.lower() == "back":
            print("back\n<------------")
            break 




