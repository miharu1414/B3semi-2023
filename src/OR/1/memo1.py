from gurobipy import *

model = Model("section1_2")
x1 = model.addVar(vtype="I", name="x1")
x2 = model.addVar(vtype="I", name="x2")
x3 = model.addVar(vtype="I", name="x3")

model.update()

model.addConstr( x1 + x2 + x3 == 32)
model.addConstr( 2*x1 + 4*x2 + 8*x3 == 80)
model.setObjective( x2 + x3, GRB.MINIMIZE)
model.optimize()
print(model.ObjVal)
print(x1.X,x2.X,x3.X)