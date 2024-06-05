import random as rand
outcomes=[['draw','lose','win'],['win','draw','lose'],['lose','win','draw']]
print("Best of 3")
u=0
c=0
def translation(x, str):
    if x==0:
        print(f"{str} chose rock")
    elif x==1:
        print(f"{str} chose paper")
    else:
        print(f"{str} chose scissors")
for i in range(3):
    n=rand.randint(0,2)
    m=int(input("Enter 0 for rock, 1 for paper or 2 for scissors: "))
    if m>2 and m>0:
        raise ValueError("Input must be between 0 and 2")
    translation(m,'You')
    translation(n,'Computer')
    result=outcomes[m][n]
    if result=='win':
        u+=1
    elif result=='lose':
        c+=1
    print(f"result: You {result}")
    print(f"score: user: {u}     computer: {c}")
if c>u:
    print("Computer wins")
else:
    print("User wins")

