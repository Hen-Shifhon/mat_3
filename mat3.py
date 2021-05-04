# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 12:54:24 2021

@author: HEN
"""

def whatsApp_text(chat):
    
    import json 
    chat=chat+".txt"
    file= open(chat,'r',encoding=('utf-8'))
    text=file.readlines()
    file.close()
    
    list_messages=list()
    id_dict=dict()
    id_num=1

    for line in text[5:]:
        if line[4:8]=='2021':
            nameStart= line.find('-')
            nameEnd= line.find(':',nameStart)
            name=line[nameStart+1:nameEnd]
            if name not in id_dict:
                id_dict[name]=id_num
                id_num+=1
        if line[4:8]=='2021':
            datetime=line[:nameStart]
            num=id_dict[name]
            t=line[nameEnd:].strip()
            temp_dict={'datetime' : datetime, 'id':num ,'text':t}
            list_messages.append(temp_dict)
        else:
            list_messages[-1]['text']=list_messages[-1]['text']+line.strip()
            
            
    
    
    first_row=text[1]
    creation_date= first_row[:first_row.find('-')]
    firstGeresh=first_row.find('"')+1
    secondGeresh=first_row.find('"',firstGeresh)
    chat_name=first_row[firstGeresh:secondGeresh]
    start_creator=first_row.find('ידי')
    creator=first_row[start_creator+3:].strip()
    metadata={ 'chat_name':chat_name , 'creation_date':creation_date,'num_of_participants': len(id_dict) , 'creator' : creator}
    
    
    summary_dict={'messages': list_messages , 'metadata': metadata }

    file_json = json.dumps(summary_dict , ensure_ascii=False)
    with open(chat_name,'w',encoding=('utf8')) as theopen:
        theopen.writelines(file_json)
        theopen.close()

whatsApp_text('MyWhatsapp')

        
