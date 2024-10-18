import features
from features import per_addition, per_subtract
def app_UI():
      print("**********Welcome to Calclator app***********")
      print("""Operations available are
       1.Addition
       2.Subtraction
            """)
def num_bers():
      inp_1=int(input("Enter first number: "))
      inp_2=int(input("Enter second number: "))
      return inp_1, inp_2
def func_tions(inp_1, inp_2):
      user_inp=int(input("Enter your preferred opration: "))
      if user_inp==1:
            return per_addition(inp_1, inp_2)
      elif user_inp==2:
            return per_subtract(inp_1, inp_2)
      else:
            print("invalid operation")
app_UI()
num1, num2=num_bers()
result=func_tions(num1, num2)
print(f"your final calculation is: {result}")

