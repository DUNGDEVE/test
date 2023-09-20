#1 divided by 3
# fraction equals = numerator divided by demominator
s_demominator=0
for i in range(100):
	if i ==1:
		continue

	if i % 2 == 0:
		continue

	s_demominator = s_demominator + 1/i

s=1/s_demominator

print(s)