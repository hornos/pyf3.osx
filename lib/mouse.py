import sys
import time
from Quartz.CoreGraphics import *

def event(type, x, y):
  theEvent = CGEventCreateMouseEvent(None, type, (x,y), kCGMouseButtonLeft)
  CGEventPost(kCGHIDEventTap, theEvent)

def move(x,y):
  event(kCGEventMouseMoved, x,y)

def clickdn(x,y):
  event(kCGEventLeftMouseDown, x,y)

def clickup(x,y):
  event(kCGEventLeftMouseUp, x,y)

def click(x,y):
  clickdn(x,y)
  clickup(x,y)

def _drag(x,y):
  event(kCGEventLeftMouseDragged, x,y)

def drag(x1,y1,x2,y2):
  clickdn(x1,y1)
  time.sleep(1)
  _drag(x2,y2)
  time.sleep(1)
  clickup(x2,y2)
  time.sleep(1)

def position():
  return CGEventGetLocation(CGEventCreate(None))
