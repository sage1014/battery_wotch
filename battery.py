import psutil

#バッテリー残量取得
def battery_life():
    btr = psutil.sensors_battery()

    return btr.percent

def battery_hower():
    btr = psutil.sensors_battery()

    m, s = divmod(btr.secsleft, 60)
    h, m = divmod(m, 60)
    return h, m,

def battery_charge():
    btr = psutil.sensors_battery()
    situation = btr.power_plugged
    return situation

hyuman = input(str("確認したい項目を入れてください"))
if hyuman == "バッテリー残量":
    print(battery_life())



