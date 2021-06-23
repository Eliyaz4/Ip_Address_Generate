a = 255;
b = 255;
c = 255;
d = 255;
count = 0;
f = open("data1.txt", "w");
for i in range(0, a+1):
	for j in range(0, b+1):
		for k in range(0, c+1):
			for l in range(0, d+1):
				print(str(i) + "." + str(j) + "." + str(k) + "."+str(l))
				f.write(str(i) + "." + str(j) + "." + str(k) + "." + str(l) + "\n")
				count += 1
f.write("total no.of ip's are:" + str(count) + "\n")
f.close()		
print(count);
