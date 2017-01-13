bob = 'bob'
count = 0
idx = 0
while True:
    idx = s.find(bob, idx)
    if idx >= 0:
        count += 1
        idx += 1
    else:
        break
print ('Number of times bob occurs is: ' + str(count))