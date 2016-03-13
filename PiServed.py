import _piserved 
service = _piserved.PiServed()

page_text = """
<html>
<head>
</head>
<body>
<FORM value="form" action="/PiServed/show_info" method="post">
    <P>
    <INPUT type="submit" name="tiltup" value="Tilt Up"></P>
    <P>
    <INPUT type="submit" name="panleft" value="Pan Left">&nbsp;&nbsp;
    <INPUT type="submit" name="panright" value="Pan Right"><BR>
    </P>
    <P>
    <INPUT type="submit" name="tiltdown" value="Tilt Down"><BR>
    </P>
    <P>
    Set Pan:    <input type="text" name="setpan"><BR><BR>
    Set Tilt:   <input type="text" name="settilt"><BR><BR>
    Zero: <INPUT type="submit" name="zero" value="Zero Both"><BR><BR>
    <INPUT type="submit" value="Submit">
    </P>
</FORM>

<P>Current Tilt: %s <br>Currnt Pan: %s
</P>
</body>
</html>
"""


def index(req):
    req.content_type = 'text/html'
    s = "Here's the index again!"
    s += page_text % (service.get_tilt(), service.get_pan())
    req.write(s)
    #return s


def show_info(req):
    form = req.form
    req.content_type = 'text/html'
    req.write("form = %s" % (str(form), ))
    if form.has_key('tiltup'):
        service.tilt_up()
        req.write("<br>called service.tilt_up()")
    elif form.has_key('tiltdown'):
        service.tilt_down()
        req.write("<br>called service.tilt_down()")
    elif form.has_key('panleft'):
        service.pan_left()
        req.write("<br>called service.pan_left()")
    elif form.has_key('panright'):
        service.pan_right()
        req.write("<br>called service.pan_right()")
    if form.has_key('setpan'):
        pan=form['setpan']
        if pan.isdigit():
            service.set_pan(int(pan))
    if form.has_key('settilt'):
        tilt=form['settilt']
        if tilt.isdigit():
            service.set_pan(int(tilt))
    if form.has_key('zero'):
        service.set_pan(0L)
        service.set_tilt(0L)
    s = page_text % (service.get_tilt(), service.get_pan())
    req.write(s)


if __name__ == "__main__":
    # from jsonrpc import ServiceProxy
    # s = ServiceProxy("http://localhost/services/PiServed.py")
    print "tilt = %d, pan = %d" % (service.get_tilt(), service.get_pan())
    #print "%s" % (index(),)
