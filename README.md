# PWM-Servo-Hat-Through-Apache-Demo
This is a demo of controlling the Adafruit PWM/Servo Pi Hat through an Apache-served web page.

This is intended to be an "educational piece". You are welcome to do whatever you'd like with the code. (MIT license.) It is useful to show how a Python script can be used through Apache.

You should be able to easily extend this concept to control **any** hardware on your RPi through Python, and control anything else on any Linux platform. (You may need to configure the security first on other platforms other than the RPi, both embedded and otherwise.)

Requirements:
* Raspberry Pi with a PWM/Servo Pi Hat from Adafruit Industries (https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/)
* Apache web server (sudo apt-get install apache2 -y)
* mod_python Apache module (sudo apt-get install libapache2-mod-python -y)
* Adafruit library for the hat (https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code)
* Connect the tilt servo to PWM/Servo Pi Hat PWM connection 7 and the pan servo to 8, by default.

I simply copied the scripts from the PWM folder of the Adafruit library into the same directory as I placed these script files. You can just drop them in your /var/www/html, or create a separate directory for them. (I will not get into how to add a directory to Apache since there are multiple tutorials online and since I just use /var/www/html.)

If you install to /var/www/html, you can then point your browser to http://localhost/PiServed. Click some buttons or input some values and then click some buttons. Watch your servos move. :)

Please let me know if you have any thoughts or questions. Feel free to create issues, even if they're "only" to discuss the project (as recommended by GitHub's own best-use policy example).
