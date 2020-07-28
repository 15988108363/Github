import os
pid = os.fork()
if pid <0:
    print("created")
elif pid ==0:
    print("new one")
else:
    print("old one")

print("fork test over")