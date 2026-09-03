import time,sys
# Insert the path of My_Methods folder  
sys.path.insert(0, "C:\\softwares\\My_Methods") #sys.path.append("C:\\softwares\\My_Methods") 
import Get_Data_From_Internet,CSV_Generator,Insert_Data_To_DB
Base_URL="https://results.eci.gov.in/PcResultGenJune2024/"
Current_Time=time.time()
State_URL=f"{Base_URL}index.htm"
for Stat_Name,State_Code in Get_Data_From_Internet.Get_Names_codes(State_URL):
    listi=[State_Code,Stat_Name]
    Insert_Data_To_DB.Insert_Into_DB("states",listi)
    Constituency_URL=f"{Base_URL}partywiseresult-{State_Code}.htm"
    for Constituency_Name,Constituency_Code in Get_Data_From_Internet.Get_Names_codes(Constituency_URL):
        listi1=[Constituency_Code,Constituency_Name,State_Code]
        Insert_Data_To_DB.Insert_Into_DB("constituencies",listi1)
        Candidate_URL=f"{Base_URL}candidateswise-{Constituency_Code}.htm"
        for list1 in Get_Data_From_Internet.Get_Data(Candidate_URL,Constituency_Code):
            Insert_Data_To_DB.Insert_Into_DB("candidates",list1)
            #CSV_Generator.Generate_CSV(Stat_Name,list1)
    
print(round(time.time()-Current_Time),1)
