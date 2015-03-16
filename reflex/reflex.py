# codeskulptor.org assignment URLs
# http://www.codeskulptor.org/#user39_LLhFvv4zTv_0.py
# http://www.codeskulptor.org/#user39_LLhFvv4zTv_11.py
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    minutes = int((t - tenths)/600)
    seconds = int((t - (minutes*600))/10)
    if seconds < 10:
        str_seconds = "0" + str(seconds)
    else:
        str_seconds = str(seconds)
    out_string = str(minutes) + ":" + str_seconds + "." + str(tenths)
    return out_string
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval


# define draw handler

    
# create frame


# register event handlers


# start frame
