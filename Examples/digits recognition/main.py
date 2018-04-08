from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
import os
import time
import random
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
import numpy
import scipy.special
import time
from nn import NeuralNetwork

neurons = [784, 100, 100, 10]
nn2 = NeuralNetwork(neurons, 0.3)

fn = ""
class MyWidget(BoxLayout):
    def openTraining(self, path, filename):

        global fn
        fn = filename[0]
        App.get_running_app().filen =fn
        print(App.get_running_app().filen)
        print(type(App.get_running_app().filen))
        with open(os.path.join(path, filename[0])) as f:
            global data_list
            data_file=f
            data_list = data_file.readlines()
            data_file.close()


    def train(self):
        onodes = 10

        for record in data_list:
            all_values = record.split(",")
            input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            target = numpy.zeros(onodes) + 0.01
            target[int(all_values[0])] = 0.99
            App.get_running_app().nn2.train(input, target)


            #testing


    def selected(self, filename):
        print ("selected: %s" % filename[0])

    def openTesting(self, path, filename):
        global fn2
        fn2 = filename[0]
        App.get_running_app().filen2 = fn2
        with open(os.path.join(path, filename[0])) as f:
            global data_list2
            data_file = f
            data_list2 = data_file.readlines()
            data_file.close()





class FirstScreen(Screen):
    def changename(self):
        print(self.ids)
    pass

class SecondScreen(Screen):
    pass


class Load2(Screen):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])

class MyScreenManager(ScreenManager):
    fn=fn
    def goback(self):
        self.current= 'first'

class ScreenManagerApp(App):


    neuronsstring = 'neurons:   '+ '   '.join(str(e) for e in neurons)
    trainingit= NumericProperty(0)
    filen = StringProperty("select file")
    filen2 = StringProperty('select file')
    trainingres= StringProperty("")
    testres = StringProperty("")
    def reset(self):
        global nn2,neurons
        nn2= NeuralNetwork(neurons,0.3)
        App.get_running_app().trainingit=0
    def train(self):
        start =time.time()
        onodes = 10

        for record in data_list:
            all_values = record.split(",")
            input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            target = numpy.zeros(onodes) + 0.01
            target[int(all_values[0])] = 0.99
            nn2.train(input, target)
        end = time.time()
        elapsed = end-start
        print(str(elapsed))
        App.get_running_app().trainingres="Trainging succesful  " + str(round(elapsed,3)) +"s"
        App.get_running_app().trainingit+=1


    def test(self):
        onodes = 10
        sum = 0
        n = 0
        for record in data_list2:
            all_values = record.split(",")
            input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            target = numpy.zeros(onodes) + 0.01
            target[int(all_values[0])] = 0.99
            n += 1
            print("test:" + str(n))
            max = 0
            for i in range(len(nn2.query(input))):
                # print(nn2.query(input))
                # #print(nn2.query(input)[i][0])
                if (nn2.query(input)[i][0] > max):
                    max = nn2.query(input)[i][0]
                    max_index = i

                # print(max)
            print("neural network quess:" + str(max_index))
            print("correct value:" + str(all_values[0]))
            if (str(max_index) == all_values[0]):
                sum += 1

        print("accuracy: " + str(sum / 100))

        App.get_running_app().testres = "Testing succesful, accuracy  " + str(100*sum/len(data_list2))+"%"
    def build(self):
        root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    id : screenmanager
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:
    Load2:
<FirstScreen>:
    canvas:
        Color:
            rgb:[.30,.30,.30]
        Rectangle:
            pos: self.pos
            size: self.size
    name: 'first'
    BoxLayout:
        id : 'box1'
        orientation: 'vertical'
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'NeuralNetwork'
                font_size: 25
                pos:(400,520)
                canvas.before:
                    Color:
                        rgb:[.25,.25,.25]
                    Rectangle:
                        pos: self.pos
                        size: self.size
            Label:
                text:app.neuronsstring
            Label:
                text:"training iterations:  " +str(app.trainingit)
                
            Label:
            Label:
            BoxLayout:
                Label:
                Label:
                Label:
                Label:
                Button:
                    text: "reset"
                    on_press: app.reset()
                Label:
                    size_hint_x:0.2
            Label:
                size_hint_y: 0.2
        
        BoxLayout:
            id: 'box2'
            orientation: "horizontal"
            BoxLayout:
                canvas.before:
                    Color:
                        rgb:[.3,.3,.3]
                    Rectangle:
                        pos: self.pos
                        size: self.size 
                orientation: "vertical"
                Label:
                    text:"Training"
                    
                    font_size:20
                    canvas.before:
                        Color:
                            rgb:[.25,.25,.25]
                        Rectangle:
                            pos: self.pos
                            size: self.size
                Label:
                    
                BoxLayout
                    
                    Label:
                    Button:
                        text: 'Open training file'
                    
                        font_size: 15
                        on_release: app.root.current = 'second'
                    Label:
                Label:
                    id: 'testing'
                    text: 
                Label:
                    text: app.filen
                BoxLayout
                    
                    Label:
                    Button:
                        text: 'Train'
                    
                        font_size: 15
                        on_release: app.train()
                    Label:
                Label:
                    text: app.trainingres
            BoxLayout:
                canvas.before:
                    Color:
                        rgb:[.3,.3,.3]
                    Rectangle:
                        pos: self.pos
                        size: self.size 
                orientation: "vertical"
                Label:
                    text:"testing"
                    
                    font_size:20
                    canvas.before:
                        Color:
                            rgb:[.25,.25,.25]
                        Rectangle:
                            pos: self.pos
                            size: self.size
                Label:
                    
                BoxLayout
                    
                    Label:
                    Button:
                        text: 'Open testing file'
                    
                        font_size: 15
                        on_release: app.root.current = 'load2'
                    Label:
                Label:
                    
                Label:
                    text: app.filen2
                BoxLayout
                    
                    Label:
                    Button:
                        text: 'Test'
                    
                        font_size: 15
                        on_release: app.test()
                    Label:
                Label: 
                    text: app.testres
           
<SecondScreen>:
    name: 'second'
    MyWidget:
        orientation: 'vertical'
        id: my_widget
        
        FileChooserIconView:
            color:1,30,1,1
            id: filechooser
            size_hit_y:
            on_selection: my_widget.selected(filechooser.selection)
            
            Widget:
                Button:
                    size:(100,50)
                    text: "open"
                    on_press: app.root.current = 'first'
                              
                    on_release: my_widget.openTraining(filechooser.path, filechooser.selection)
                    
        
<Load2>
    name: 'load2'
    MyWidget:
        orientation: 'vertical'
        id: my_widget
        
        FileChooserListView:
            color:1,30,1,1
            id: filechooser
            size_hit_y:
            on_selection: my_widget.selected(filechooser.selection)
            
            Widget:
                Button
                    size:(100,50)
                    text: "open"
                    on_press: app.root.current = 'first'
           
                    on_release: my_widget.openTesting(filechooser.path, filechooser.selection)           
        ''')
        return root_widget

ScreenManagerApp().run()