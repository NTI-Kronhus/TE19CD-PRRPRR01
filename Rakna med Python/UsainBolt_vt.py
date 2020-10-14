import matplotlib.pyplot as plt

s = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # lista som håller sträckan
t = [0, 1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.14, 7.96, 8.79, 9.69]
v = [0]  # tom lista

for i in range(1, len(t)):
    v.append((s[i]-s[i-1])/(t[i]-t[i-1]))
    print(i)

print(len(v))
print(len(t))

# plot v-t graf
plt.plot(t, v, '*-')
plt.show()
