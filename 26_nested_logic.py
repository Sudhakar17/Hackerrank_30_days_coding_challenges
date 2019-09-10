Da,Ma,Ya = input().strip().split(' ')
De,Me,Ye = input().strip().split(' ')

fine = 0
if Ya == Ye:
    if int(Ma) <= int(Me):
        if int(Da) > int(De):
            fine = 15 * (int(Da)-int(De))
    else:
        fine = 500*(int(Ma) - int(Me))
elif int(Ya) < int(Ye):
    pass
elif int(Ya) > int(Ye):
    fine = 10000

print(fine)



