import os
import requests
import time
import datetime

def getPlanURL(weekNumber):
  currentTime = time.time()

  url = f"https://boehringer.webspeiseplan.de/index.php?token=2fda60f9e49030893165d438b7b4e946&request=pdf&menu=2058&time={ currentTime * 1000}&lang=1&cw={ weekNumber }"

  payload={}
  headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "de,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Host": "boehringer.webspeiseplan.de",
    "Referer": "https://boehringer.webspeiseplan.de/Menu",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": 'Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return (response.json())

def downloadPlan(url, filename):
  response = requests.get(url,verify=False)
  file = open(filename, "wb").write(response.content)
  return file

def getPlanInfo():
  currentTime = time.time()

  url = f"https://boehringer.webspeiseplan.de/index.php?token=2fda60f9e49030893165d438b7b4e946&model=menu&location=1100&languagetype=1&time={ currentTime * 1000}"

  payload={}
  headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "de,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Host": "boehringer.webspeiseplan.de",
    "Referer": "https://boehringer.webspeiseplan.de/Menu",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": 'Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  response = response.json()

  def findMir2(item):
    return item["speiseplanAdvanced"]["titel"] == "Ingelheim MIR 2"
    
  mir2 = filter(findMir2, response["content"])

  return (mir2)


def main():

  currentDate = datetime.date.today()
  year, weekNumber, dayOfTheWeek = currentDate.isocalendar()

  speiseplan = getPlanInfo()

  print(getPlanURL(34))

  # planName = f'speiseplan_kw{ weekNumber }.pdf'

  # downloadPlan(speiseplanURL, planName)

  print(speiseplan)

  # os.remove(f"./{planName}")

main()