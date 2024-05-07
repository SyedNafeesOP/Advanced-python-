
# Weight conversion tool

def weight():
    pounds=int(input("Enter weight in pounds \n"))
    kg=pounds * 0.45359237
    return kg

result = weight()
print("The weight in kilograms is:", result)

def convert_weight_gram(kg):
    print("1 gram=0.001kg")
    grams=kg*1000
    return grams
kg = int(input("Enter weight in kilograms: "))
result =convert_weight_gram(kg)
print("The weight in grams is:", result)

def convert_to_ounce(kg):
    print("1 kg = 35.274")
    ounce = kg * 35.274
    return ounce
kg =float(input("Enter weight in kilograms: "))
result = convert_to_ounce(kg)
print("The weight in ounce is:", result)
