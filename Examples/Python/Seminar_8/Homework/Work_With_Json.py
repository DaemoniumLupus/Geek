

import json

class Work_With_Json:


    def Load(self,sp):
        with open ('phonebook.json','w')as file:
            file.write(json.dumps(sp,indent=4))
            file.close()

    def Head_file() -> str:
        st = "{:15}    {:10}  {:10}    {}".format('Name','City','Status','Phones')
        return st

    def Data_file(person,sp) -> str:
        st = "{:15} -> {:10}  {:10} -> {}".format(person,sp[person]['city'],sp[person]['status'],sp[person]['phones'])
        return st
    
    def Read(self) -> dict:
        with open("phonebook.json","r") as file:
            sp = json.load(file)
            file.close()
        return dict(sp)