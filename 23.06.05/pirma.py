def skaiciai_ir_rezultatas(func):
    def ivestis(*args, **Kwargs):
        print(f"Paduoti parametrai: {args}")
        result = func(*args, **Kwargs)
        print(f"lygu: {result}")
        return result
    return ivestis

@skaiciai_ir_rezultatas
def daugyba(a, b):
    return a * b

print(daugyba(2, 3 ))