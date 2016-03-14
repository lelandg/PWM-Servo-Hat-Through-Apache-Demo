# PWM-Servo-Hat-Through-Apache-Demo
A demo of controlling the Adafruit PWM/Servo hat through an Apache-served web page

This is intended to be an "educational piece". You are welcome to do whatever you'd like with the code. (MIT license.) It is useful to show how a Python script can be used through Apache.

Requirements:
* Raspberry Pi with a PWM/Servo Hat from Adafruit Industries (https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/)
* Apache
* mod_python Apache module. 
* Adafruit library for the hat (https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code)
* Connect the tilt servo to PWM/Servo connection 14 and the pan servo to 15.

I simply copied the scripts from the PWM folder of the Adafruit library into the same directory as I placed these script files. You can just drop them in your /var/www/html, or create a separate directory for them. (I will not get into how to add a directory to Apache since there are multiple tutorials online.)

If you install to /var/www/html, you can then point your browser to http://localhost/PiServed. Click some buttons or input some values and then click some buttons. Watch your servos move. :)

Please let me know if you have any questions. Feel free to create issues, even if they're only for questions about the project.
