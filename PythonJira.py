import requests,json,os
import mysql.connector as mysql

con = mysql.connect(
    host='localhost',
    user='root',
    password='1',
    database='Jira'
)
mycursor = con.cursor()

def CreateTicket():

    Url = "https://magical.atlassian.net/rest/api/2/issue/"
    Headers = {
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    payloads = json.dumps(
        {
            "fields": {
                "project":
                {
                    "key": "JIR"
                },
                "summary": "This ticket its important for all member",
                "description": "we can get so many thing from creating this jira",
                "issuetype": {
                    "name": "Task"
                }
            }
        }
    )
    Response = requests.post(Url,headers=Headers,data=payloads,auth=("bhumeshkewat10@gmail.com","vpaqB9vnQZtRCWKrhAWhE4C4"))
    print(Response.text)


def FetchAllTicket():

    url = "https://magical.atlassian.net/rest/api/3/search"
    headers = {
            "Accept":"application/json",
            "Content-Type":"application/json"
    }
    query = {
            "jql":"project = JIR"
    }
    response = requests.get(url,headers=headers,params=query,auth=("bhumeshkewat10@gmail.com","vpaqB9vnQZtRCWKrhAWhE4C4"))
    data = response.json()

    issues = data['issues']

    TicketQuery = "SELECT * FROM AllTicket"
    mycursor.execute(TicketQuery)
    allTicket = mycursor.fetchall()

    TicketId = []
    for ticket in allTicket:
        TicketId.append(int(ticket[1]))

    for issue in issues:

        number,name,description = issue['id'],issue['fields']['issuetype']['name'],issue['fields']['description']["content"][0]["content"][0]["text"]
        reporter,status,DueDate = issue['fields']['reporter']['displayName'],issue['fields']['status']['name'],issue['fields']['created']

        if int(number) in TicketId:
            TicketQ = f'UPDATE AllTicket SET Number={number},Name="{name}",Description="{description}",Reporter="{reporter}",Status="{status}",DueDate="{DueDate}" WHERE Number={number}'
            mycursor.execute(TicketQ)
            con.commit()
        else:
            ticketQuery = f'INSERT INTO AllTicket (Number,Name,Description,Reporter,Status,DueDate) VALUES({number},"{name}","{description}","{reporter}","{status}","{DueDate}")'
            mycursor.execute(ticketQuery)
            con.commit()
    print(data)
        
    print('successfully excuted....')


def CreateTable():
    try:
        mycursor.execute("CREATE TABLE AllTicket (id INT AUTO_INCREMENT PRIMARY KEY, Number INT, Name VARCHAR(255), Description VARCHAR(255), Reporter VARCHAR(255), Status VARCHAR(255), DueDate VARCHAR(255))")
        print('Table Created Successfully...')
    except:
        print('Table Allready Exist....')


def StatusAndComment():

    url2 = "https://magical.atlassian.net/rest/api/3/issue/JIR-9/transitions"

    Header = {
            "Accept":"application/json",
            "Content-Type":"application/json"
    }
    payload = json.dumps(
        {
            "transition":{
                "id":"31"
            }
        }
    )
    requests.post(url2,headers=Header,data=payload,auth=('bhumeshkewat10@gmail.com','vpaqB9vnQZtRCWKrhAWhE4C4'))

    url3 = "https://magical.atlassian.net/rest/api/3/issue/JIR-9/comment"
    Head = {
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    data = json.dumps(
        {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{
                        "text": "wow beutiful ticket",
                        "type": "text"
                    }]
                }]
            }
        }
    )
    res = requests.post(url3,headers=Head,data=data,auth=('bhumeshkewat10@gmail.com','vpaqB9vnQZtRCWKrhAWhE4C4'))

    if(res.status_code == 201):
        print('Status Changed and Comment added  successfully ...')
    else:
        print(res.status_code)
        print(res.text)


while True:
    print("\nWELCOME TO THE JIRA SOFTWARE\n\n1.Create Ticket\n2.Fetch All Ticket\n3.CreateTable\n4.Change Status And add Comment\n5.Exit\n")
    choice = int(input('Enter Your Choice :- '))
    if(choice == 1):  
        CreateTicket()
    elif (choice == 2):
        FetchAllTicket()    
    elif (choice == 3):
        CreateTable()
    elif(choice ==4):
        StatusAndComment()
    elif(choice == 5):
        break