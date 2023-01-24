a = int(input("What do you have left in yuan?: "))
b = int(input("What do you have left in yen?: "))
c = int(input("What do you have left in won?: "))
root1 = a * 0.14
root2 = b * 0.7 * 0.01
root3 = c * 0.75 * 0.01 *0.01
print(root1 + root2 + root3)
