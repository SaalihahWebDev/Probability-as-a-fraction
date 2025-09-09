machine1={"Red":4,"White":0}
machine2={"Red":3,"White":1}
machine3={"Red":0,"Blue":4}
def probality_fraction(machine,color):
    total=sum(machine.values())
    count=machine.get(color,0)
    return str(count)+"/"+str(total)
print("Machine 1,Red:",probality_fraction(machine1,"Red"))
print("Machine 2,Red:",probality_fraction(machine2,"Red"))
print("Machine 2,White:",probality_fraction(machine2,"White"))
print("Machine 3,Red:",probality_fraction(machine3,"Red"))