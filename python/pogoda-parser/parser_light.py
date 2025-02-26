import json
import os

def process():
    f = open("data.txt","w")
    with open("dane.json","rt") as file:
        dataJSON = json.load(file)
        dataString = dataJSON["data"].strip()
        parts = dataString.split("\n")

        vSum = {}
        vCount = {}
        for i in range(24):
            vSum[f"{i:02d}:00"] = 0
            vSum[f"{i:02d}:30"] = 0
            vCount[f"{i:02d}:00"] = 0
            vCount[f"{i:02d}:30"] = 0
            
        for i in range(len(parts)):
            partJSON = json.loads(parts[i])
            timestamp = partJSON["timestamp_server"]
            year = timestamp[0:4]
            month = timestamp[4:6]
            day = timestamp[6:8]
            hour = timestamp[8:10]
            minute = timestamp[10:12]
            second = timestamp[12:14]
            for k in partJSON["data"]["data"]:
                 if k["type"] == "light_10kO":
                    v = k["ADC_VALUE"]
                    if not v == "nan":
                        if int(minute) < 30:
                            vSum[hour+":00"] += float(v)
                            vCount[hour+":00"] += 1
                        else:
                            vSum[hour+":30"] += float(v)
                            vCount[hour+":30"] += 1
                        print(v)
                        print(timestamp)
                        f.write(v)
                        f.write(",")
                        f.write(f"{int(hour)*60 +int(minute)}")
                        f.write(",")
                        f.write(f"{hour}")
                        f.write("\n")
    f.close()

    for k in vSum:
        # print(f"{k}: {round(vSum[k]/vCount[k],2)} ({vCount[k]}) {round((1-(vSum[k]/vCount[k])/1024) *100,1)}% naświetlenia")
        print(f"{k}, {round((1-(vSum[k]/vCount[k])/1024) *100,1)}")
def main():
    process()

if __name__ == "__main__":
    main()