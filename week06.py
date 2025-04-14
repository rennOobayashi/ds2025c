from queue import Queue

q = Queue()

q.put("NayutanSeijin")
q.put("Deco27")
q.put("PinocchioP")

print(q.qsize())
print(q.get())

print(q.qsize())
print(q.get())

print(q.qsize())
print(q.get())