import js

def init():
    myList = [1,2,3,4]
    print(sum(myList))
    print("This is the total sales")
    para, button = view()

    button.onclick = lambda _:counter(para)


def getStore():
    store = {}
    return store

def view():
    para = js.document.createElement("p")
    para.innerText = "Counter"
    js.document.getElementById("Body").appendChild(para)

    para = js.document.createElement("p")
    para.innerText = "0"
    js.document.getElementById("Body").appendChild(para)

    button = js.document.createElement("button")
    button.innerText = "counter"
    js.document.getElementById("Body").appendChild(button) 

    test = Component()
    test.innetHTML = 'hello world'
    js.document.getElementById("Body").appendChild(test)  

    return para, button

def counter(para):
    state = int(para.innerText)
    para.innerText = str(state+1)

    


class Component(js.text):
    def state():
        pass
    
    def view():
        pass

    def render(self):
        self.innerHTML = self.view()