#file io
print('--reading--')
f = open('ex1/Europarl.txt', 'r+')
inp = f.read()
f.close()


print('--tokenizing--')
#Criteria of a sentence
#First letter should Capitalize
#End with ! or . or ? or \n

import re
reg = ur"([A-Z][^\.!?\n]*[\.!?\n])"  #regex
sens = re.findall(reg, inp)

nwords = [] #all words length
nsens = [] #all sentences length
wsens = [] #all sentences text 
c=0
for i in sens:
    if i.count("?") > 1 or i.count("!") > 1 or i.count(".") > 1: 
        c+=1 #find unsplitted sentence
        
    words = filter(None, i.split(' ')) #splitting sentence to words
    lenn = [len(j) for j in words if j.isalpha()] #check whether it's word or punctuation. if word, count the length
    nwords.extend(lenn) #put word length to list
    nsens.append(len(words)) #put length of sentence to list
    wsens.append(i) #put text of sentence to list

print('unsplitted sentence: '+str(c))
print('total words: '+str(len(nwords)))
print('total sentences: '+str(len(nsens)))

#calculate means    
mwords = float(sum(nwords))/len(nwords)
msens = float(sum(nsens))/len(nsens)

print('mean words: '+str(mwords))
print('mean sentences: '+str(msens))

#calculate variance
vsens = float(sum([(i-msens)**2 for i in nsens]))/len(nsens)
vwords = float(sum([(i-mwords)**2 for i in nwords]))/len(nwords)

print('variance words: '+str(vwords))
print('variance sentences: '+str(vsens))

#dictionary to count the occurence 
dwords = {}
dsens = {}
for i in nwords:
    dwords[i] = dwords.get(i, 0) + 1

for i in nsens:
    dsens[i] = dsens.get(i, 0) + 1

print('--plotting--')

#plotting
import matplotlib.pyplot as plt

fig1 = plt.figure() 
fig1.canvas.set_window_title('Sentences Plot') 
plt.plot(dsens.keys(), dsens.values(), 'ro')

fig2 = plt.figure() 
fig2.canvas.set_window_title('Words Plot') 
plt.plot(dwords.keys(), dwords.values(), 'ro')

plt.show()

print('--finish--')