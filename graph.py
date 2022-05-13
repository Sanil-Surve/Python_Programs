import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2],label = "Mathamatics", color = 'g')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label = "English", color = 'b')
plt.legend()
plt.xlabel("Mathamatics Marks")
plt.ylabel("English Marks")
plt.title("Data")
plt.show()
plt.savefig("im3.png", transparent= True)
