import time
import mouse

wait=1

def back():
  mouse.click(151,101)
  time.sleep(wait)

def show():
  mouse.click(1254,716)
  time.sleep(wait)

def insert():
  mouse.click(306,148)
  time.sleep(wait)

# TODO: return back level
def shapes():
  insert()
  mouse.click(303,135)
  time.sleep(wait)

def home():
  mouse.click(164,371)
  time.sleep(wait)

def zoomin():
  mouse.click(164,407)
  time.sleep(wait)

def zoomin():
  mouse.click(164,446)
  time.sleep(wait)


### main

# down 1-12
# home 13
# up   14-28

# zoomlevel from home to down 12
# home 13
# to up 14

# TODO back level arg
back()
# back()
# back()
# shapes()

# mouse.click(326,512)
# mouse.click(731,447)

mouse.drag(1034,113,1034,719)
