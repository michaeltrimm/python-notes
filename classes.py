#!/usr/bin/python

class Group(object):
    def __init__(self,name, members=None):
        """Group initializer with nickname and members
    
        Args:
            name (str) Nickname of the group
            members (list) List of Employee objects
        """
        self.members = []
        self.name = name
        if isinstance(members,list):
            for member in members:
                if isinstance(member, Employee) and member not in self.members:
                    self.members.append(member)
        else:
            raise Exception("members must be a list")

    def get_members(self):
        """Combine Employee objects into a comma separated string
        
        Returns:
            Comma separated string containing each Employee.__str__()
        """
        output = ", ".join(map(str, self.members))
        return output
    
    def add_member(self, member):
        """Add a new Employee object to the group
        
        Args:
            member (Employee) Instance of the Employee wishing to be added to the group
        
        Returns:
            List of Employee objects part of this group
        """
        if member not in self.members:
            self.members.append(member)
        return self.members
        
    def remove_member(self, member):
        """Remove member from the collection
        
        Args:
            member (Employee) Instance of the Employee wishing to be removed from the group
        
        Returns:
            List of Employee objects part of this group
        """
        self.members.remove(member)
        return self.members
    
    def __str__(self):
        """Custom print() result for the Group object
        
        Returns:
            Formatted string of the Group Name: Members, Separated, By, Commas
        """
        return "{}: {}".format(self.name, self.get_members())


class Employee(object):
    def __init__(self,firstname,lastname,salary,domain="mts.yt"):
        """Create a new Employee object
        
        Args:
            firstname (str) First name of Employee
            lastname (str) Last name of Employee
            salary (int) Salary of Employee
            domain (str) Domain For Email Address (firstname.lastname@domain)
        """
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.domain = domain
        self.group = None
    
    @property
    def email(self):
        return "{}.{}@{}".format(self.firstname, self.lastname, self.domain)
    
    @property
    def fullname(self):
        """Format the full name of the Employee
        
        Returns:
            String of the first and last name separated by a space
        """
        return "{} {}".format(self.firstname, self.lastname)
    
    def __repr__(self):
        """Print the declaration of the object for development notes
        
        Returns:
            String containing Python code that can instantiate the instance of the object being accessed
        """
        return "Employee('{}','{}','{}','{}')".format(self.firstname, self.lastname, self.salary, self.domain)
    
    def __str__(self):
        """Configure how print(Employee) looks
        
        Returns:
            String with the Firstname Lastname (FirstName.LastName@Domain)
        """
        return "{} ({})".format(self.fullname,self.email)
    
    def __add__(self,other):
        """Configure addition operator when combining employees
        
        When two Employee objects are added together using the `+` operator, a new instance of Group is created
        if none exists yet for the Employee. Both members of the addition operation are added to the new group object.
        
        Args:
            other (Employee) Instance of Employee
        
        Returns:
            Group object containing the self Employee + other Employee
        """
        if self.group is None:
            group = Group("{}'s Group".format(self.firstname),[self,other])
            self.group = group
            return group
        else:
            self.group.add_member(other)
            return self.group
    
    def __sub__(self,other):
        """Configure subtraction operator when subtracting employees
        
        Similar to the __add__() function, the __sub__() function will remove ther other Employee member from the
        self Employee's group instance.
        
        Args:
            other (Employee) Instance of Employee to be removed from Group
        """
        if self.group is None:
            group = Group("{}'s Group".format(self.firstname),[self])
            self.group = group
            return group
        else:
            self.group.remove_member(other)
            return self.group


michael = Employee("Michael","Trimm",250000,"michaeltrimm.com")
john = Employee("John","Smith",250000,"gmail.com")

print(michael)
# Michael Trimm (Michael.Trimm@michaeltrimm.com)

print(john)
# John Smith (John.Smith@gmail.com)

print(michael + john)
# Michael's Group: Michael Trimm (Michael.Trimm@michaeltrimm.com), John Smith (John.Smith@gmail.com)

print(michael.__add__(john))
# Michael's Group: Michael Trimm (Michael.Trimm@michaeltrimm.com), John Smith (John.Smith@gmail.com)

print(john.__add__(michael))
# John's Group: John Smith (John.Smith@gmail.com), Michael Trimm (Michael.Trimm@michaeltrimm.com)

print(michael.__repr__())
# Employee('Michael','Trimm','250000','michaeltrimm.com')

print(michael.__str__())
# Michael Trimm (Michael.Trimm@michaeltrimm.com)

print(john.__repr__())
# Employee('John','Smith','250000','gmail.com')

print(john.__str__())
# John Smith (John.Smith@gmail.com)

bob = Employee("Bob","Nobody",250000,"hotmail.com")

print(michael + bob)
# Michael's Group: Michael Trimm (Michael.Trimm@michaeltrimm.com), John Smith (John.Smith@gmail.com), Bob Nobody (Bob.Nobody@hotmail.com)

print(john + bob)
# John's Group: John Smith (John.Smith@gmail.com), Michael Trimm (Michael.Trimm@michaeltrimm.com), Bob Nobody (Bob.Nobody@hotmail.com)

group = michael + bob
print(group.remove_member(bob))
# [Employee('Michael','Trimm','250000','michaeltrimm.com'), Employee('John','Smith','250000','gmail.com')]

group = john + bob
print(group)
# John's Group: John Smith (John.Smith@gmail.com), Michael Trimm (Michael.Trimm@michaeltrimm.com), Bob Nobody (Bob.Nobody@hotmail.com)

print(group.remove_member(michael))
# [Employee('John','Smith','250000','gmail.com'), Employee('Bob','Nobody','250000','hotmail.com')]






