from Adafruit_PWM_Servo_Driver import PWM
import picamera
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


# Initialise the PWM device using the default address
# pwm = PWM(0x40, debug=True)
pwm = PWM(0x40)
pwm.setPWMFreq(60)  # Set frequency to 60 Hz

servoMin = 0L  # Min pulse length out of 4096
servoMax = 1000L  # Max pulse length out of 4096
cameraServoMin = 0L  # Min pulse length out of 4096
cameraPanServoMax = 2000L  # Max pulse length out of 4096
cameraTiltServoMax = 1000L
cameraPanCenter = (cameraPanServoMax - cameraServoMin) / 2
cameraTiltCenter = (cameraTiltServoMax - cameraServoMin) / 2
cameraTiltServo = 14
cameraPanServo = 15


class PiServed:
    def __init__(self):
        self.camera = None
        self.set_pan(cameraPanCenter)
        self.set_tilt(cameraTiltCenter)

        # self.camera = picamera.PiCamera(sensor_mode=4)  # A hack! Pin 0 causes it to not light at all.
        # self.camera.led = True
        # self.camera.resolution = (1920, 1080)
        # self.camera.start_preview()

    @ServiceMethod
    def set_tilt(self, tilt):
        if (cameraServoMin <= tilt <= cameraTiltServoMax) or 0 == tilt:
            self.cameraTilt = tilt
            pwm.setPWM(cameraTiltServo, 0, self.cameraTilt)
            #set_servo_pulse(cameraTiltServo, self.cameraTilt)
            # pwm.setPWM(cameraTiltServo, 0, 0)

    @ServiceMethod
    def set_pan(self, pan):
        if (cameraServoMin <= pan <= cameraPanServoMax) or pan == 0:
            self.cameraPan = pan
            pwm.setPWM(cameraPanServo, 0, self.cameraPan)
            #set_servo_pulse(cameraPanServo, self.cameraPan)
            # pwm.setPWM(cameraPanServo, 0, 0)

    @ServiceMethod
    def tilt_up(self):
        if self.cameraTilt < cameraTiltServoMax + 10:
            self.set_tilt(self.cameraTilt + 10)

    @ServiceMethod
    def tilt_down(self):
        if self.cameraTilt > cameraServoMin - 10:
            self.set_tilt(self.cameraTilt - 10)

    @ServiceMethod
    def pan_left(self):
        if self.cameraPan > 10:
            self.set_pan(self.cameraPan - 10)

    @ServiceMethod
    def pan_right(self):
        if self.cameraPan < cameraPanServoMax + 10:
            self.set_pan(self.cameraPan + 10)

    @ServiceMethod
    def get_tilt(self):
        return self.cameraTilt

    @ServiceMethod
    def get_pan(self):
        return self.cameraPan

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
