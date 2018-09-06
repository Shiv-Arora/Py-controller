import speech_recognition as sr


def SUM(a, b):
    return a + b


def SUB(a, b):
    return a - b


def PERCENTAGE(a, t):
    return (a*100)/t


def PROD(a, b):
    return a*b


def DIVIDE(a, b):
    return a/b


def LCM(x, y):
    lcm = (x*y)//HCF(x, y)
    return lcm


def HCF(x, y):
    while(y):
        x, y = y, x % y
    return x


def converstr(strr):
    strr = strr.lower()
    strr = strr.replace("calculate", "")
    strr = strr.replace("what is", "")
    strr = strr.replace("and", ",")
    strr = strr.replace("or", ",")
    strr = strr.replace("the", "")
    strr = strr.replace("of", "")
    strr = strr.replace(" ", "")
    return strr


def contains(val, strin):
    return (val in strin)


def getValues(strin):
    temp = strin.split(',')
    a = int(temp[0])
    b = int(temp[1])
    return a, b


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    x = r.recognize_google(audio)
    print("You Said : "+x)
    val = converstr(x)
    if contains("+", val) or contains("add", val) or contains("sum", val) or (""):
        temp = val.replace("+", ",").replace("add", "").replace("sum", "")
        a, b = getValues(temp)
        print("Sum is : " + str(SUM(a, b)))

    elif contains("-", val) or contains("subtract", val) or contains("sub", val) or contains("subtaction", val):
        temp = val.replace("-", ",").replace("subtract", "").replace("sub", "")
        a, b = getValues(temp)
        print("Subtract is : " + str(SUB(a, b)))

    elif contains("x", val) or contains("multiplyby", val) or contains("product", val):
        temp = val.replace("x", ",").replace("multiplyby", "").replace("product", "")
        a, b = getValues(temp)
        print("Product is : " + str(PROD(a, b)))

    elif contains("/", val) or contains("divideby", val) or contains("divide", val):
        temp = val.replace("/", ",").replace("divideby","").replace("divide", "")
        a, b = getValues(temp)
        if b == 0:
            print("Divison by Zero")
        else:
            print("Divide is : " + str(DIVIDE(a, b)))

    elif contains("out", val):
        temp = val.replace("out", ",")
        a, b = getValues(temp)
        if a > b:
            a, b = b, a
        print("Percentage is : " + str(PERCENTAGE(a, b)))

    elif contains("hcf", val):
        temp = val.replace("hcf", "")
        a, b = getValues(temp)
        print("HCF is : " + str(HCF(a, b)))

    elif contains("lcm", val):
        temp = val.replace("lcm", "")
        a, b = getValues(temp)
        print("LCM is : " + str(LCM(a, b)))

except ValueError:
    print("Could not recognize")

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print(
        "Could not request results from  Speech Recognition service; {0}".format(e))