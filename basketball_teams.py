# Create a class named BasketballTeam
# Has one attribute: members, which starts as an empty list in the constructor
# Has an instance method named add_member
    # Has one parameter, which is a new member's name
    # Adds the new member's name to the members attribute
    # Returns True

class BasketballTeam:
    def __init__(self, members = []):
        self.members = members

    def add_member(self, member_name):
        self.members.append(member_name)
        return True

conehead = BasketballTeam()
print(conehead.members)
conehead.add_member("Eunice")
print(conehead.members)
conehead.add_member("Brooke")
conehead.add_member("Tori")
print(conehead.members)

mavericks = BasketballTeam(["Kristel", "Lilly"])
print(mavericks.members)
mavericks.add_member("Lux")
print(mavericks.members)