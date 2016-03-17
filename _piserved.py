# This is a demo for Apache mod_python written as a way to show how to control hardware via the web.
# Written by Leland Green... Released under MIT license.
# Part of the repository:
# https://github.com/lelandg/PWM-Servo-Hat-Through-Apache-Demo

from Adafruit_PWM_Servo_Driver import PWM
# import picamera # For some reason, creating an instance of the camera
# "crashes" the app and it returns an empty response. On my TODO list.
import time
from jsonrpc import ServiceMethod


@ServiceMethod
def echo(msg):
    return msg


@ServiceMethod
def index(req):
    # s = PiServed()
    # for j in range(0, 100):
    #    s.pan_left()
    # for j in range(0, 100):
    #    s.pan_right()
    return "Here's the _piserved.index()"

# Which servos to use:

cameraTiltServo = 14
cameraPanServo = 15

STEPSERVOS = True # When True, the movement will be made slower and smoother, so it does not jerk

# Initialise the PWM device using the default address
# pwm = PWM(0x40, debug=True)
pwm = PWM(0x40)
pwm.setPWMFreq(60)  # Set frequency to 60 Hz

panServoMin = 160L
panServoMax = 620L
tiltServoMin = 230L
tiltServoMax = 320L
panCenter = ((panServoMax - panServoMin) / 2) + panServoMin
tiltCenter = ((tiltServoMax - tiltServoMin) / 2) + tiltServoMin


class PiServed:
    currentTilt = tiltCenter
    currentPan = panCenter

    def __init__(self):
        self.camera = None
        self.set_pan(self.currentPan)
        self.set_tilt(self.currentTilt)

        # Caution: This causes the current request to abort and you get an empty response error.
        # self.camera = picamera.PiCamera(sensor_mode=4)  # A hack! Pin 0 causes it to not light at all.
        # self.camera.led = True
        # self.camera.resolution = (1920, 1080)
        # self.camera.start_preview()

    @ServiceMethod
    def set_tilt(self, tilt):
        if (tiltServoMin <= tilt <= tiltServoMax) or 0 == tilt:
            step = 1
            if tilt < self.currentTilt:
                step = -1
            if STEPSERVOS:
                for j in range(self.currentTilt, tilt, step):
                    self.currentTilt = j
                    pwm.setPWM(cameraTiltServo, 0, self.currentTilt)
                    time.sleep(0.001)
            # range returns one "less" than the max, so go ahead and call this either way
            self.currentTilt = tilt
            pwm.setPWM(cameraTiltServo, 0, self.currentTilt)
            # set_servo_pulse(cameraTiltServo, self.cameraTilt)
            # pwm.setPWM(cameraTiltServo, 0, 0)

    @ServiceMethod
    def set_pan(self, pan):
        if (panServoMin <= pan <= panServoMax) or 0 == pan:
            if STEPSERVOS:
                step = 1
                if pan < self.currentPan:
                    step = -1
                for j in range(self.currentPan, pan, step):
                    self.currentPan = j
                    pwm.setPWM(cameraPanServo, 0, self.currentPan)
                    time.sleep(0.001)
            # range returns one "less" than the max, so go ahead and call this either way
            self.currentPan = pan
            pwm.setPWM(cameraPanServo, 0, self.currentPan)
            # set_servo_pulse(cameraPanServo, self.cameraPan)
            # pwm.setPWM(cameraPanServo, 0, 0)

    @ServiceMethod
    def tilt_up(self):
        if 0 == self.currentTilt:
            self.currentTilt = tiltServoMin
        elif self.currentTilt < tiltServoMax + 10:
            self.set_tilt(self.currentTilt + 10)

    @ServiceMethod
    def tilt_down(self):
        if self.currentTilt > tiltServoMin - 10:
            self.set_tilt(self.currentTilt - 10)

    @ServiceMethod
    def pan_left(self):
        if self.currentPan < panServoMax + 10:
            self.set_pan(self.currentPan + 10)

    @ServiceMethod
    def pan_right(self):
        if self.currentPan > 10:
            self.set_pan(self.currentPan - 10)

    @ServiceMethod
    def pan_center(self):
        self.set_pan(panCenter)

    @ServiceMethod
    def tilt_center(self):
        self.set_tilt(tiltCenter)

    @ServiceMethod
    def get_tilt(self):
        return self.currentTilt

    @ServiceMethod
    def get_pan(self):
        return self.currentPan

    @ServiceMethod
    def close(self):
        if self.camera:
            self.camera.stop_preview()
        pwm.setPWM(cameraPanServo, 0, 0)
        pwm.setPWM(cameraTiltServo, 0, 0)


def set_servo_pulse(channel, pulse):
    """
    :param channel:
    :param pulse:
    """
    pulseLength = 1000000  # 1,000,000 us per second
    pulseLength /= 60  # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096  # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)

# service = PiServed()

# import sys
# def main(argc = len(sys.argv), argv = sys.argv):
#    service = PiServed()
#    s = "service = %s, tilt = %d, pan = %d" % (service, service.GetTilt(), service.GetPan())
#    print s
#    return s

# if __name__ == "__main__":
#    main()
#     print "This is a mod_python module for Apache web server.\r\n" +\
#           "There is no command line interface at this time."
