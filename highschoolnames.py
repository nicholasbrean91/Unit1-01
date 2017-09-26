# Created by: Nicholas Brean
# Created on: 12-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-02
# This peogram displays Hello World but in GUI

import ui

def mths(sender):
	view['Main_label'].text = 'Mother teresa Go titans'
	
def Joes(sender):
	view['Main_label'].text = 'Saint Joes Go Jaguares'

def Marcs(sender):
	view['Main_label'].text = 'Saint Marcs Go Lions'


view = ui.load_view()
view.present('sheet')
