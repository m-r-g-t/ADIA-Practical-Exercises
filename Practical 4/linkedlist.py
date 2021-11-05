# create Node type
class Node:
   def __init__(self, dataValue=None):
      self.dataval = dataValue
      self.nextval = None

# start linkedlist
class StartLinkedList:
   def __init__(self):
      self.headval = None
     
# add new node to the linkedlist
def AddEnd(self, newdata):
  newNode = Node(newdata)
  if self.headval is None:
     self.headval = newNode
     return
  laste = self.headval
  while(laste.nextval):
     laste = laste.nextval
  laste.nextval=newNode

weekdays = ["mon","tue", "wed", "thu", "fri"]

lista = StartLinkedList()

for c in weekdays:
    AddEnd(lista, c)
    
print(lista)


'''    
lista.headval = Node("monday")
e2 = Node("tuesday")
e3 = Node("wednesday")
lista.headval.nextval = e2
print(lista)
'''
