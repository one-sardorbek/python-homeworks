def convert_cel_to_far(celcius):
    return celcius * 9/5 + 32
def convert_far_to_cel(f):
    return  (f - 32) * 5/9
celcius=int(input("Enter a temperature in degrees C: "))
print(float(convert_cel_to_far(celcius)))
f=int(input("Enter a temperature in degrees F: "))
print(float(convert_far_to_cel(f)))

