import json
import os
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from Posts.models import Qual_List, Age_Limit_List, Imp_Dates_List, Fees_List, Post, Vacancy_List, Column_List, \
    Links_List


class Worker(webdriver.Chrome):
    """Class for creating a web scraper for scraping job blogs.
       Currently, it can scrape "FreeJobAlert" Website and get data of new job opportunities and reduce the hassle of
       content creators to write all day and create one post, where this class scrapes websites and its algorithm will
       use its creativity for bypassing plagiarism checks and use its own set of words taken from different thesauruses
       to create brand-new posts. This all happens at a speed of 100 posts/min."""

    def __init__(self, **kwargs):
        """Initializing class with __init__ method,
        :argument path, url
        :url  URL """
        # checking os name for distinguishing between my development environment vs production environment
        if os.name == "nt":
            # sets driver path to my machine's chromedriver Path
            self.path = kwargs["path"]
            super().__init__(executable_path=self.path)
        else:
            # code for deploying on heroku
            self.chrome_options = webdriver.ChromeOptions()
            # doesn't show new window everytime i run it on server
            self.chrome_options.add_argument("--headless")

            self.chrome_options.add_argument("--disable-dev-shm-usage")
            self.chrome_options.add_argument("--no-sandbox")
            # location of chromedriver on my hosting server
            self.chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

            super().__init__(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                             chrome_options=self.chrome_options)
        # url of website to scrape
        self.url = kwargs["url"]
        # going to url address
        self.get(self.url)
        # Primary variables
        self.links = []
        self.post_name = ""
        self.post_date = ""
        self.latest_date = ""
        self.total_vacancy = ""
        self.brief_info = ""
        self.advt_no = ""
        self.qualification_list = []
        self.fee_list = []
        self.dates_list = []
        self.ages_list = []
        self.applications = {}
        self.count = 0

    # checking if the post already exists on database
    def check_if_exists(self, json_obj):
        self.post = Post.objects.filter(name_of_the_post=json_obj).exists()
        if self.post == False:
            return False
        return True

    # Method for creating the post
    def create_post(self, json_obj):
        # local variables required for creating a post
        self.js = dict(json_obj)
        self.qu_list = []
        self.ag_list = []
        self.dt_list = []
        self.fe_list = []
        self.vacc_list = []
        self.link_list = []
        self.col_list = []
        if self.js.get("QUALIFICATION LIST") != None or self.js.get("QUALIFICATION LIST") != []:
            for i in self.js["QUALIFICATION LIST"]:
                # Feeding data into QualificationList Model
                self.qu = Qual_List(**i)
                self.qu.save()
                self.qu_list.append(self.qu)
        if self.js.get("AGES LIST") != None or self.js.get("AGES LIST") != []:
            for i in self.js["AGES LIST"]:
                # Feeding data into Age_Limit_List Model
                self.ag = Age_Limit_List(**i)
                self.ag.save()
                self.ag_list.append(self.ag)
        if self.js.get("DATES LIST") != None or self.js.get("DATES LIST") != []:
            for i in self.js["DATES LIST"]:
                # Feeding data into DatesList Model
                self.dt = Imp_Dates_List(**i)
                self.dt.save()
                self.dt_list.append(self.dt)
        if self.js.get("FEES LIST") != None or self.js.get("FEES LIST") != []:
            for i in self.js["FEES LIST"]:
                # Feeding data into FeesList Model
                self.fe = Fees_List(**i)
                self.fe.save()
                self.fe_list.append(self.fe)
        if self.js.get("VAC LIST") != None or self.js.get("VAC LIST") != []:
            for i in self.js["VAC LIST"]:
                # Feeding data into VacancyList Model
                self.vacc = Vacancy_List(**i)
                self.vacc.save()
                self.vacc_list.append(self.vacc)
        if self.js.get("IMP LINKS LIST") != None or self.js.get("IMP LINKS LIST") != []:
            for i in self.js["IMP LINKS LIST"]:
                # Feeding data into LinkList Model
                self.link = Links_List(**i)
                self.link.save()
                self.link_list.append(self.link)
        if self.js.get("SUB PARENT LIST") != None or self.js.get("SUB PARENT LIST") != []:
            for i in self.js["SUB PARENT LIST"]:
                # Feeding data into ColumnsList Model
                self.col = Column_List(**i)
                self.col.save()
                self.col_list.append(self.col)
        # base values required for post model
        self.applic = {
            "name_of_the_post": str(self.js.get("NAME OF THE POST")),
            "post_heading": str(self.js.get("POST HEADING")),
            "post_date": str(self.js.get("POST DATE")),
            "latest_update": str(self.js.get("LATEST DATE")),
            "vacancy": str(self.js.get("TOTAL VACANCY")),
            "vacancy_header": str(self.js.get("VACANCY HEADER")),
            "brief_info": str(self.js.get("BRIEF INFORMATION")),
            "advt_no": str(self.js.get("ADVT NO.")),
            "vacancy_rows": self.js.get("VAC ROWS"),
        }
        # Feeding all the values collected above to Post Model
        self.ap = Post(**self.applic)
        # saving model to get id
        self.ap.save()
        # feeding data from other models
        self.ap.age_limit_list.add(*self.ag_list)
        self.ap.qualification_list.add(*self.qu_list)
        self.ap.important_dates.add(*self.dt_list)
        self.ap.application_fee.add(*self.fe_list)
        self.ap.vacancy_details_list.add(*self.vacc_list)
        self.ap.important_links.add(*self.link_list)
        self.ap.vacancy_columns.add(*self.col_list)
        # final save for Post Model
        self.ap.save()

    def start_application(self):
        start = time.time()
        self.soup = BeautifulSoup(self.page_source, 'lxml')
        self.div = self.soup.find_all("div", class_="listcontentj")
        for i in self.div:
            for j in i.find_all("a"):
                self.links.append(j["href"])

        for count, link in enumerate(self.links):
            if self.count < 10:
                self.get(link)
                self.implicitly_wait(30)
                self.soup = BeautifulSoup(self.page_source, 'lxml')
                self.div = self.soup.find("div", class_="Post")
                self.post_heading = str(self.div.find("div", class_="PostMetadataHeader").text).strip().strip(
                    "\n").strip()
                self.post_body = self.div.find("div", class_="PostContent")
                self.vac_rows = 1
                self.p = self.post_body.find_all("p")
                self.body_p_list = []
                self.body_p_list_cleaned = []
                for i in self.p:
                    self.body_p_list.append(i.text)

                for i in self.body_p_list:
                    if bool(re.match(r"^Name of the Post:", i)):
                        self.post_name = str(re.split(":", i, 1)[1]).replace(r"\xa0", " ").replace(r"\u", "").strip()

                    elif bool(re.match(r"^Post Date:", i)):
                        self.post_date = str(re.split(":", i, 1)[1]).replace(r"\xa0", " ").strip()

                    elif bool(re.match(r"^Latest Update:", i)):
                        self.latest_date = str(re.split(":", i, 1)[1]).replace(r"\xa0", " ").strip()

                    elif bool(re.match(r"^Total Vacancy:", i)):
                        self.total_vacancy = str(re.split(":", i, 1)[1]).replace(r"\xa0", " ").strip()

                    elif bool(re.match(r"^Brief Information:", i)):
                        self.brief_info = str(re.split(":", i, 1)[1]).replace(r"\xa0", " ").replace(u"\u00a0", " ") \
                            .replace(r"\u", "") \
                            .strip()

                    elif bool(re.match(r"^Advt No", i)):
                        self.advt_no = str(i).replace(r"\xa0", " ").strip()

                self.check = self.check_if_exists(self.post_name)
                if self.check == True:
                    continue

                self.tbody = self.post_body.find("tbody")
                self.tr_list = self.tbody.find_all("tr")
                self.td = self.tbody.find_all("td")
                self.td_list = []
                for i in self.td:
                    self.td_list.append(i.text)
                self.tr_list_cleaned = []
                self.tr_list_clean = []
                self.vac = [0, 1]
                self.vac_list = []
                self.vac_list_cl = []
                self.vac_list_cleaned = []
                self.imp_links_list = []
                self.imp_links_list_cl = []
                self.imp_links_list_cleaned = []
                self.sub_parent_list = []
                self.sub_parent_list_cleaned = []
                for i, j in enumerate(self.tr_list):
                    self.tr_list_cleaned.append(str(j.text).strip("\n").strip())
                    if str(j.text).strip("\n").strip() == "Vacancy Details":
                        self.vac[0] = i
                    if str(j.text).strip("\n").strip() == "Important Links":
                        self.vac[1] = i
                for i in self.tr_list[self.vac[0]:self.vac[1]]:
                    self.vac_list.append(str(i.text).strip().strip("\n").strip())
                for i in self.vac_list:
                    self.vac_list_cl.append(str(i).splitlines())
                for i, j in enumerate(self.vac_list_cl):
                    if len(j) > 1:
                        self.sub_parent_list = j
                        break
                for i in self.tr_list[self.vac[1]:]:
                    name = str(i.text).strip('\n')
                    link_name = str(i.text).strip('\n').split("\n")
                    try:
                        if len(list(i)) > 3:
                            if i.find("a") != None:
                                link = i.find("a").get("href")
                            else:
                                link = str(i.find_all("strong")[1].text).strip().strip("\n").strip()
                            if bool(re.search(r"^https://img\.freejobalert\.com", link)):
                                # response = requests.get(link)
                                # location = f"{BASE_DIR}\\staticfiles\\pdf"
                                # file_name = f"{link_name[0].lower()}{link_name[1].lower()}{self.post_name}.pdf"
                                # if not os.path.exists(location):
                                #     os.makedirs(location)
                                # pdf = open(f"{location}\\{file_name}", "wb")
                                # pdf.write(response.content)
                                # pdf.close()
                                # print("PDF MADE FOR :-", f"{location}\\{file_name}")
                                # self.imp_links_list.append(
                                #     name + "\n" + f"{location}\\{file_name}" + "\n" + "FILE LINK")
                                self.imp_links_list.append(
                                    name + "\n" + link + "\n" + "CLICK LINK")
                    except Exception as e:
                        print(e)

                    self.imp_links_list.append(name + "\n" + link + "\n" + "CLICK LINK")
                for i in self.imp_links_list:
                    self.imp_links_list_cl.append(i.split("\n"))
                for i in self.imp_links_list_cl:
                    if i[-1] == "CLICK LINK":
                        self.imp_links_list_cleaned.append({
                            "name": i[0],
                            "link": i[-2],
                            "parent": self.post_name
                        })
                    elif i[-1] == "FILE LINK":
                        self.imp_links_list_cleaned.append({
                            "name": i[0],
                            "download_file": i[-2],
                            "parent": self.post_name
                        })
                for i in self.vac_list:
                    self.vac_list_cl.append(str(i).splitlines())

                for i, j in enumerate(self.tr_list_cleaned):
                    self.tr_list_clean.append(str(re.sub("\n", " ", j)).strip().replace(r"\xa0", " ").strip())

                self.tbody_p = self.tbody.find_all("p")
                self.p_list = []
                self.p_list_cleaned = []
                self.tr_post_name = ""
                for i in self.tbody_p:
                    self.p_list.append(i.text)

                for i in self.p_list:
                    if bool(re.search(r"Vacancy", i)) or bool(re.search(r"Exam", i)) or bool(re.search(r"Job", i)) \
                            or bool(re.search(r"Course", i)):
                        self.tr_post_name = i.strip().strip("\n").replace(r"\xa0", " ").strip()

                self.tbody_li = self.tbody.find_all("li")
                self.li_list = []
                self.li_list_cleaned = []
                self.vac_count = 0
                # print("Vacancy List:- ", end='')
                # print(self.vac_list_cl)
                # print("Sub Parent List:- ", end='')
                # print(self.sub_parent_list)
                for i in self.vac_list_cl[1:]:
                    # print(i)
                    if len(i) < len(self.sub_parent_list) or len(i) > len(self.sub_parent_list):
                        if bool(re.search("^Interested Candidates", i[0])):
                            continue
                        self.vacancy_header = i[0]
                        continue
                    elif i == self.sub_parent_list:
                        continue
                    elif len(i) == len(self.sub_parent_list):
                        for j in i:
                            if self.vac_count < len(self.sub_parent_list):
                                self.vac_list_cleaned.append({
                                    "parent": self.post_name,
                                    "sub_parent": self.sub_parent_list[self.vac_count],
                                    "name": str(j),
                                    "row_number": str(self.vac_rows),
                                    "rowspan": ""
                                })
                                self.vac_count += 1
                                print(str(j) + ":-", self.vac_count)
                            else:
                                self.vac_rows += 1
                                self.vac_count = 0
                    else:
                        self.vac_rows = 0
                        # self.vac_list_cleaned[-1:-(len(self.sub_parent_list))]["row_number"] = str(self.vac_rows)
                        # TODO: Create for loop to solve the problem of under indexing of rows

                for i in self.sub_parent_list:
                    self.sub_parent_list_cleaned.append({
                        "parent": self.tr_post_name,
                        "name": i
                    })
                for i in self.tbody_li:
                    self.li_list.append(i.text)

                for i in self.li_list:
                    if bool(re.search(r"Vacancy", i)) or bool(re.search(r"Exam", i)) or bool(
                            re.search(r"Job", i)) \
                            or bool(re.search(r"Course", i)):
                        self.li_list_cleaned.append("JOB: " + i.strip().strip("\n").replace(r"\xa0", " ").strip())

                    elif bool(re.search(r"[Dd]egree", i, re.I)) or bool(re.search(r"[Pp]ossess", i, re.I)):
                        self.q = str(i.strip().strip("\n").replace("\xa0", " ").strip())
                        self.qualification = {
                            "name": self.q,
                            "parent": self.post_name
                        }
                        self.qualification_list.append(self.qualification)

                    elif bool(re.search(r"[Cc]andidates", i)) or bool(re.search(r"Rs", i)) or \
                            bool(re.search(r"NIL", i)):
                        self.f = str(i.strip().strip("\n").replace("\xa0", " ").strip())
                        self.fee = {
                            "name": self.f,
                            "parent": self.post_name
                        }
                        self.fee_list.append(self.fee)

                    elif bool(re.search(r"[Dd]ate|[Dd]ates", i)):
                        self.d = str(i.strip().strip("\n").replace("\xa0", " ").strip()).split(":")
                        if len(self.d) >= 2:
                            self.date = {
                                "name": self.d[0],
                                "date": self.d[1],
                                "parent": self.post_name
                            }
                        else:
                            self.date = {
                                "name": self.d[0],
                                "date": "",
                                "parent": self.post_name
                            }
                        self.dates_list.append(self.date)

                    elif bool(re.search(r"[Yy]ear", i)) or bool(re.search(r"[Yy]ears", i)) or \
                            bool(re.search(r"[Aa]ge", i)):
                        self.a = str(i.strip().strip("\n").replace(r"\xa0", " ").strip()).split(":")
                        if len(self.a) >= 2:
                            self.age = {
                                "name": self.a[0],
                                "age": self.a[1],
                                "parent": self.post_name
                            }
                        else:
                            self.age = {
                                "name": self.a[0],
                                "age": "",
                                "parent": self.post_name
                            }
                        self.ages_list.append(self.age)

                    elif bool(re.search(r"^WWW\.FREEJOBALERT\.COM", i)) or \
                            bool(re.search(r"^Mobile App", i)):
                        continue
                    else:
                        pass
                        # self.li_list_cleaned.append("No Match Found: " + i.strip().strip("\n").replace(r"\xa0",
                        # " ").strip())

                self.mixed_list = self.p_list_cleaned + self.li_list_cleaned
                self.applications[str(self.post_name)] = {
                    "NAME OF THE POST": str(self.post_name),
                    "POST HEADING": str(self.post_heading),
                    "POST DATE": str(self.post_date),
                    "LATEST DATE": str(self.latest_date),
                    "TOTAL VACANCY": str(self.total_vacancy),
                    "VACANCY HEADER": str(self.vacancy_header),
                    "BRIEF INFORMATION": str(self.brief_info),
                    "ADVT NO.": str(self.advt_no),
                    "VAC ROWS": self.vac_rows,
                    "TR POST NAME": str(self.tr_post_name),
                    "AGES LIST": self.ages_list,
                    "IMP LINKS LIST": self.imp_links_list_cleaned,
                    "DATES LIST": self.dates_list,
                    "QUALIFICATION LIST": self.qualification_list,
                    "FEES LIST": self.fee_list,
                    "VAC LIST": self.vac_list_cleaned,
                    "SUB PARENT LIST": self.sub_parent_list_cleaned,
                }
                self.post_name = ""
                self.post_date = ""
                self.latest_date = ""
                self.total_vacancy = ""
                self.brief_info = ""
                self.advt_no = ""
                self.qualification_list = []
                self.fee_list = []
                self.dates_list = []
                self.ages_list = []
                self.count += 1
            else:
                self.json_obj = json.dumps(self.applications, indent=4)
                if self.json_obj == {} and self.applications == {}:
                    break
                for j, i in self.applications.items():
                    self.check = self.check_if_exists(j)
                    if self.check == False:
                        self.create_post(i)
                print("COMPLETE")
                end = time.time()
                print(f"{end - start}")
                break
