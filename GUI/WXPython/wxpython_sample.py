'''
Install below pytohn module before you run this code
>>> pip install wxpython --upgrade
'''

import wx # import wx module
app = wx.App() # define an object of application class

# Create a top level window as object of wx.Frame class. Caption and size parameters are given in constructor.
window = wx.Frame(None, -1, title = "wxPython Title", size = (300,200), style = wx.DEFAULT_FRAME_STYLE, name = "frame") 

# Although other controls can be added in Frame object, their layout cannot be managed. 
# Hence, put a Panel object into the Frame.
panel = wx.Panel(window) 

# Add a StaticText object to display ‘Hello World’ at a desired position inside the window.
label = wx.StaticText(panel, label = "Hello World", pos = (100,50), style = wx.ALIGN_LEFT) 

# Activate the frame window by show() method.
window.Show(True) 

# Enter the main event loop of Application object.
app.MainLoop()
