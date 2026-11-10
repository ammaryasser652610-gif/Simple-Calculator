
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطأ: لا يمكن القسمة على صفر!"
    return x / y

print("--- آلة حاسبة بسيطة بلغة بايثون ---")
print("اختر العملية:")
print("1. جمع")
print("2. طرح")
print("3. ضرب")
print("4. قسمة")

choice = input("أدخل رقم العملية (1/2/3/4): ")

num1 = float(input("أدخل الرقم الأول: "))
num2 = float(input("أدخل الرقم الثاني: "))

if choice == '1':
    print(f"النتيجة: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"النتيجة: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"النتيجة: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"النتيجة: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("إدخال غير صحيح!")