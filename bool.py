my_age=int(input())
is_con_nit = False
if my_age < 10:
    is_con_nit = True
if is_con_nit:
    print("con nit")
elif my_age<18:
    print("Tre trau")
    if my_age >=15 and my_age <=17:
        print("sieu tre trau")
else:
    print("nguoi lon")