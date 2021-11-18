
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        randId = randint(0, 99999999)
        if self.get_member(randId):
            self._generateId()
        return randId

    def add_member(self, member):
        # fill this method and update the return
        if self.validate_member(member):
            member['last_name'] = self.last_name 
            self._members.append(member)        
        
        
    def validate_member(self, member):
        if (member.get('age') and isinstance(member.get('age'), int)
        and member.get('age')>0 and member.get('first_name')
        and isinstance(member.get('first_name'), str)):
            if not member.get('id'):
                member['id'] = self._generateId()
            return member
        print("No válido")    

    def delete_member(self, id):
        for member in self.get_all_members():
            if member["id"] == id:
                self._members.remove(member)

    def get_member(self, id):
        for member in self.get_all_members():
            if member["id"] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
