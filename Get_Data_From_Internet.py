import requests
import re
from bs4 import BeautifulSoup

def Get_Names_codes(URL):
    resp=requests.get(URL)
    html_doc=BeautifulSoup(resp.text,features="html.parser")
    for option in html_doc.find_all("option")[1:]:
        yield(option.text,option.get("value"))

def Get_Data(URL,Constituency_Code):
    main_list=[]
    resp=requests.get(URL)
    html_doc=BeautifulSoup(resp.text,features="html.parser")
    i=0
    for div in html_doc.find_all("div","cand-info"):
        list1=[f"candidate_{Constituency_Code}_{i}"]
        s=div.text
        list1.append(div.find('h5').text)
        list1.append(div.find('h6').text)
        if "won" in s:
            list1.append("won")
        elif "lost" in s:
            list1.append("lost")
        else:
            list1.append("not applicable")
        r=re.findall(r"(\d+)\s.\s?([-+]?\s?\d*)",s)
        if r:
            for vote_count in r[0]:
                list1.append(vote_count)
        else:
            list1.append("0")
            list1.append("0")
        list1.append(Constituency_Code)
        i=i+1
        yield list1
    #     main_list.append(list1)
    # return main_list
