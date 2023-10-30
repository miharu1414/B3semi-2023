from gurobipy import *

model = Model("section1_2")
x1 = model.addVar(vtype="I", name="x1")
x2 = model.addVar(vtype="I", name="x2")
x3 = model.addVar(vtype="I", name="x3")

model.update()

model.addConstr( 6*x1 + 4*x2 + 2*x3 <= 180)
model.addConstr( 5*x1 + 3*x2 + 2*x3 <= 140)
model.setObjective( 9*x1 + 7* x2 + 4* x3, GRB.MAXIMIZE)
model.optimize()
print(model.ObjVal)
print(x1.X,x2.X,x3.X)