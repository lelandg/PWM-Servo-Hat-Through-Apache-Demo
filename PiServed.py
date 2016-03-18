import _piserved

service = _piserved.PiServed()

page_text = """
<html>
<head>
</head>
<body>
<FORM value="form" action="/PiServed/show_info" method="post">
<table width="800" align="center" border="2">
    <tr>
        <td align="center">
            <table columns="2" cellpadding="5" cellspacing="5">
                <tr>
                    <td colspan="2">
                    <strong>Incremental Movement</strong>
                    </td>
                </tr>
                <tr>
                    <td colspan="2" align="center">
                        <INPUT type="submit" name="tiltup" value="Tilt Up">
                    <td>
                </tr>
                <tr>
                    <td align="center">
                        <INPUT type="submit" name="panleft" value="Pan Left" size="20" maxlength="4">
                    </td>
                    <td align="center">
                        <INPUT type="submit" name="panright" value="Pan Right" size="20" maxlength="4">
                    </td>
                <tr>
                    <td colspan="2" align="center">
                        <INPUT type="submit" name="tiltdown" value="Tilt Down">
                    </td>
                </tr>
            </table>
            <br>
            <table columns="2" cellpadding="5" cellspacing="5">
                <tr>
                    <td colspan="2" align="center">
                    <strong>Set specified values.</strong><br><sub>(Will be validated to be within range.)</sub>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        Set Pan:<br><input type="text" name="setpan" colspan="2">
                    </td>
                    <td align="center">
                        Set Tilt:<br><input type="text" name="settilt" colspan="2">
                    </td>
                </tr>
                <tr>
                    <td colspan="2" align="center">
                        <INPUT type="submit" value="Submit">
                    </td>
                </tr>
            </table>
            <br>
            <table columns="2" cellpadding="5" cellspacing="5">
                <tr>
                    <td colspan="2">
                    <strong>Minimums and Maximums</strong>
                    </td>
                </tr>
                <tr>
                    <td colspan="2" align="center">
                        <input type="submit" name="mintilt" value="Min Tilt">
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <input type="submit" name="minpan" value="Min Pan">
                    </td>
                    <td align="center">
                        <input type="submit" name="maxpan" value="Max Pan">
                    </td>
                </tr>
                <tr>
                    <td colspan="2" align="center">
                        <input type="submit" name="maxtilt" value="Max Tilt">
                    </td>
                </tr>
            </table><br>
            <table columns="2" cellpadding="5" cellspacing="5">
                <tr>
                    <td colspan="2" align="center">
                        <strong>Centering</strong>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <input type="submit" name="centerpan" value="Center Pan">
                    </td>
                    <td align="center">
                        <input type="submit" name="centertilt" value="Center Tilt">
                    </td>
                </tr>
            </table>
            <br>
            <table columns="2" cellpadding="5" cellspacing="5">
                <tr>
                    <td colspan="2">
                    <strong>Minimums and Maximums</strong> <br><sub>(for both servos)</sub>
                    </td>
                </tr>
                <tr>
                    <td align="center" colspan="2">
                        <INPUT type="submit" name="zero" value="Min Both">
                    </td>
                </tr>
                <tr>
                    <td align="center" colspan="2">
                        <INPUT type="submit" name="max" value="Max Both">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
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
    # return s


def show_info(req):
    form = req.form
    req.content_type = 'text/html'
    req.write("form = %s" % (str(form),))
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
    elif form.has_key('centerpan'):
        service.pan_center()
        req.write("<br>called service.center_pan()")
    elif form.has_key('centertilt'):
        service.tilt_center()
        req.write("<br>called service.center_tilt()")
    elif form.has_key('minpan'):
        service.set_pan(160)
        req.write("<br>called service.set_pan(160)")
    elif form.has_key('maxpan'):
        service.set_pan(620)
        req.write("<br>called service.set_pan(620)")
    elif form.has_key('mintilt'):
        service.set_tilt(240)
        req.write("<br>called service.set_tilt(240)")
    elif form.has_key('maxtilt'):
        service.set_tilt(320)
        req.write("<br>called service.set_tilt(320)")
    if form.has_key('setpan'):
        pan = form['setpan']
        if pan.isdigit():
            service.set_pan(int(pan))
    if form.has_key('settilt'):
        tilt = form['settilt']
        if tilt.isdigit():
            service.set_pan(int(tilt))
    if form.has_key('zero'):
        service.set_pan(160L)
        service.set_tilt(160L)
    if form.has_key('max'):
        service.set_pan(620L)
        service.set_tilt(320L)
    s = page_text % (service.get_tilt(), service.get_pan())
    req.write(s)


if __name__ == "__main__":
    # from jsonrpc import ServiceProxy
    # s = ServiceProxy("http://localhost/services/PiServed.py")
    print "tilt = %d, pan = %d" % (service.get_tilt(), service.get_pan())
    # print "%s" % (index(),)
