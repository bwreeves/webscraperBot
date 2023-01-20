from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from csv import writer
import time
import re

#open csv
with open('top16timesMEN.csv', 'w', encoding='utf-8', newline='') as f1, open('top16timesWOMEN.csv', 'w', encoding='utf-8', newline='') as f2:
  thewriter1 = writer(f1)
  thewriter2 = writer(f2)
  header = ['Title', 'Rank', 'Name', 'School', 'Time']
  thewriter1.writerow(header)
  thewriter2.writerow(header)

  #function to print out the top 16 for each event
  def grabTop16(thisUrl, gender):
    #define the function here 
    driver.get(thisUrl)
    time.sleep(5)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'html.parser')
    times = soup.find('table', class_="c-table-clean")
    title = soup.find('h2', class_="c-title c-title--small")
    title = title.text.strip()

    counter = 0
    for row in times.tbody.find_all('tr'):
      if (counter == 16):
        break
      counter += 1
      #find data in each col
      columns = row.find_all('td')

      if(columns != []):
        rank = columns[0].text.strip()
        name = columns[1].text.strip()
        swimTime = columns[4].text.strip()

        name = re.split('(?<=.)(?=[A-Z])', name)
        first = ""
        second = ""
        school = ""

        count = 0
        for i in name:
          if count > 1:
            school = school + name[count]
          elif (count==0):
            first = name[count]
          else:
            second = name[count]
          count += 1

        if(school == ""):
          school = second
          second = ""

        fullName = first + second
        # swimmer = rank + " " + fullName + " " + school + " " + swimTime
        swimmer = [title, rank, fullName, school, swimTime]
        if (gender == 0):
          thewriter1.writerow(swimmer)
        else:
          thewriter2.writerow(swimmer)

  event = "1"
  distance = "50"
  gender = 'M'
  url = "https://www.swimcloud.com/country/usa/college/conference/horizon/times/?dont_group=false&event=" + event + distance + "&gender=" + gender + "&page=1&region=conference_10&season_id=26"
  driver = webdriver.Chrome()
  driver.get(url)
  time.sleep(4)

  #big loop for men and women
  for m in range(2):
    if (m == 0):
      gender = "M"
    else:
      gender = "F"

    #grab free events
    for i in range(6):
      event = "1"
      j = i + 1
      if(j == 1):
        distance = "50"
      elif(j == 2):
        distance = "100"
      elif(j == 3):
        distance = "200"
      elif(j == 4):
        distance = "500"
      elif(j == 5):
        distance = "1000"
      else:
        distance = "1650"

      newUrl = "https://www.swimcloud.com/country/usa/college/conference/horizon/times/?dont_group=false&event=" + event + distance + "&gender=" + gender + "&page=1&region=conference_10&season_id=26"
      grabTop16(newUrl, m)
        
    #grab back events
    for i in range(3):
      event = "2"
      j = i + 1
      if (j==1):
        distance = "50"
      elif (j==2):
        distance = "100"
      else:
        distance = "200"
      
      newUrl = "https://www.swimcloud.com/country/usa/college/conference/horizon/times/?dont_group=false&event=" + event + distance + "&gender=" + gender + "&page=1&region=conference_10&season_id=26"
      grabTop16(newUrl, m)

    #grab breast events
    for i in range(3):
      event = "3"
      j = i + 1

      if (j == 1):
        distance = "50"
      elif(j == 2):
        distance = "100"
      else:
        distance = "200"

      newUrl = "https://www.swimcloud.com/country/usa/college/conference/horizon/times/?dont_group=false&event=" + event + distance + "&gender=" + gender + "&page=1&region=conference_10&season_id=26"
      grabTop16(newUrl, m)

    #grab fly events
    for i in range(3):
      event = "4"
      j = i + 1

      if(j == 1):
        distance = "50"
      elif(j == 2):
        distance = "100"
      else:
        distance = "200"

      newUrl = "https://www.swimcloud.com/country/usa/college/conference/horizon/times/?dont_group=false&event=" + event + distance + "&gender=" + gender + "&page=1&region=conference_10&season_id=26"
      grabTop16(newUrl, m)

    #grab IM events
    for i in range (3):
      event = "5"
      j = i + 1
      if (j == 1):
        distance = "100"
      elif (j == 2):
        distance = "200"
      else:
        distance = "400"

      newUrl = "https://www.swimcloud.com/country/usa/college/conference/horizon/times/?dont_group=false&event=" + event + distance + "&gender=" + gender + "&page=1&region=conference_10&season_id=26"
      grabTop16(newUrl, m)

  driver.quit()
