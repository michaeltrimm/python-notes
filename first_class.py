#!/usr/bin/python

# Closures Are First Class Citizens
def html(tag):
    def wrap(text):
        print("<{0}>{1}</{0}>".format(tag, text))
    return wrap

h1 = html("h1")

print(h1)
# <function wrap at 0x103b68398>

h1("Hello world!")
# <h1>Hello world!</h1>

h2 = html("h2")

print(h2)
# <function wrap at 0x103b68410>

h2("My name is Mike")
# <h2>My name is Mike</h2>

p = html("p")

print(p)
# <function wrap at 0x103b68488>

p("This is a cool paragraph!")
# <p>This is a cool paragraph!</p>

p("This is another cool paragraph!")
# <p>This is another cool paragraph!</p>
