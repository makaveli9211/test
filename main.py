import time
def hackkgb():
    for i in range (0,101,10):
        if i ==0:
            time.sleep(0.7)
            print("Starting Attack")
        time.sleep(0.5)
        print(f"hacking kgb {i} %")
        if i == 100:
            print("KGB is hacked")

hackkgb()
