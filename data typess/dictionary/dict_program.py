#to print purticular key value
sampleDict ={
    "class": {
        "student":{
            "name":"mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}
print(sampleDict)
print(sampleDict["class"]["student"]["marks"]["history"])
print(sampleDict['class']['student']['name'])


sampleDict ={ "class": {"student":{ "name":"mike","course":{"python":2023,"angular":2022,"marks":{"physics":70,"history":80 }}}}}
print(sampleDict['class']['student']['course']['marks']['physics'])


#to change the value of akey in a nested dict

sample_dict2 = {
    'dict1' : {"name":"chithra","age":12 ,"course":"pyhton"},
    'dict2' : {"place":"abc","qualification":"b-tech"},
    'dict3' : {"job":"pythondev","sal":456789}
}
print(sample_dict2)
sample_dict2['dict2']['qualification'] ="BCA"
print(sample_dict2)

#rename key of dict
dict1 ={"name":"chithra","age":12 ,"course":"pyhton"}
print(dict1)
dict1["class"]=dict1.pop('course')
print(dict1)
print((dict1["class"]))