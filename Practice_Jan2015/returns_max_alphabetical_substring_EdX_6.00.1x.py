print ("Give me a string and I will find the longest string that contain letters in alphabetical order.")
s = raw_input()

count=1
i=0
maxcount=0
maxindex=0
for i in range(len(s)-1):
	if s[i] <=s[i+1]:
		count+=1
	else:
		if maxcount<count:
			maxcount=count
			count=1
			maxindex=i
		else:
			count=1
if maxcount<count:
	maxcount=count
	maxindex=i+1

print s[maxindex-maxcount+1:maxindex+1]