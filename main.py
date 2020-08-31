from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

import json
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
datelist = date.split("-")

pontos = datetime.now().strftime("%Y-%m-%d-%H-%M")

class P(FloatLayout):
    pass

def show_popup(thecontent):
    show = P() # Create a new instance of the P class

    popupWindow = Popup(title="Popup", content=Label(text=thecontent), size_hint=(None,None),size=(400,400))
    # Create the popup window

    popupWindow.open() # show the popup

class MainWindow(Screen):
    def osszbevetel(self):
        with open("years.json", "r") as k:
            dumping = json.load(k)

        bevetelek = 0

        for i in dumping:
            for a in dumping[i]:
                ahonap = list(dumping[i][a].values())
                for asd in ahonap:
                    bevetelek += asd
        show_popup(str(bevetelek))

    def biztonsagimentes(self):
        with open("years.json", "r") as k:
            dumping = json.load(k)

        with open("biztment%s.json" % (pontos), "w") as k:
            json.dump(dumping, k)
        mentve = "mentve biztment%s.json néven" % (pontos)
        show_popup(mentve)

    pass


class SecondWindow(Screen):
    def maiosszbevetel(self):
        with open("years.json", "r") as k:
            dumping = json.load(k)
        dumping[datelist[0]][datelist[1]][datelist[2]] = int(self.userinput.text)
        with open("years.json", "w") as k:
            json.dump(dumping, k)

    pass
class ThirdWindow(Screen):
    def maibevetelhozzaadas(self):
        with open("years.json", "r") as k:
            dumping = json.load(k)

        dumping[datelist[0]][datelist[1]][datelist[2]] = dumping[datelist[0]][datelist[1]][datelist[2]] + int(
            self.userinput.text)

        with open("years.json", "w") as k:
            json.dump(dumping, k)
    pass
class FourthWindow(Screen):
    def adotthonapbevetel(self):
        with open("years.json", "r") as k:
            dumping = json.load(k)

        adatum = self.userinput.text
        datumlist = adatum.split(".")
        bevetel = 0
        ahonap = list(dumping[datumlist[0]][datumlist[1]].values())
        for i in ahonap:
            bevetel += i

        show_popup("A bevétel %s.%s hónapban: %s" % (datumlist[0], datumlist[1], bevetel))

    pass
class FifthWindow(Screen):
    def beveteladottnap(self):
        with open("years.json", "r") as k:
            dumping = json.load(k)

        datum = self.userinput.text
        datum = datum.split(".")

        show_popup(str(dumping[datum[0]][datum[1]][datum[2]]))

    pass
class SixthWindow(Screen):


    pass
class SeventhWindow(Screen):
    def bevetelmodositasadottnap(self):
        with open("years.json", "r") as k:
            dumping = json.load(k)

        datum = self.userinput.text
        datum = datum.split(".")

        dumping[datum[0]][datum[1]][datum[2]] = int(datum[3])

        with open("years.json", "w") as k:
            json.dump(dumping, k)

    pass
class EighthWindow(Screen):

    pass


class WindowManager(ScreenManager):
    pass




kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyMainApp().run()