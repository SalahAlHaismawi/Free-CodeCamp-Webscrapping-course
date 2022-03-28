from bs4 import BeautifulSoup
import requests
import time 

print('Put some skill you are not familiar with') #asks the user for unfimiliar skills to filter out .
unfamiliar_skill= input('>')                      #input prompt.
print(f'Filtering out {unfamiliar_skill}')        #showing the user which skills are going to be filtired out.

def find_jobs():                                 
      html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text #our web destenation
      soup= BeautifulSoup(html_text, 'lxml')                                              #creating an instance of BeautifulSoup to use Through out the program

      jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')                       #Searches all boxes that contain job and it's information from the website.
      for index, job in enumerate(jobs):                                                  #Searching for jobs and what it contains.
            job_published_date = job.find('span', class_='sim-posted').span.text          #Searching for publishing date
            
            if 'few' in job_published_date:                                               #Allowing only recent jobs.
                  company_name= job.find('h3',class_='joblist-comp-name').text.replace(' ','') #Searching the company name.
                  skills = job.find('span',class_='srp-skills').text.replace(' ', '')          #Searching for required skills.
                  more_info=job.header.h2.a['href']                                            #getting the link for the job listing.
                  
                  if unfamiliar_skill not in skills:                                           #Filter out unwanted skills.
                        with open(f'posts/{index}.txt','w') as f:                              #Creating and Writing to a txt file .
                                                                                               #Lines below are writing to the txt file we just created.
                              f.write(f"Company Name:{company_name.strip()}/n")                 
                              f.write(f"Required Skills:{skills.strip()}/n")
                              f.write(f"More info: {more_info}/n")
                        print(f'File saved{index}')      
                            
if __name__ == '__main__':                                                                      #if the program is compiled.
      while True:
            find_jobs()                         
            time_wait=10                                                                       #waiting time before the program runs again.
            print(f"Waiting {time_wait} Minutes")                                              #printing waiting time.
            time.sleep(time_wait*60)