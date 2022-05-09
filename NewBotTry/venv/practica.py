
import schedule
def prent():
    f = open("Enlaces.txt", "r")
    enlace=f.readline()
    f.close()
    print(enlace)
schedule.every(2).minutes.do(fmensaje)
while True:
    schedule.run_pending()
    time.sleep(1)