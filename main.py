from imu import MPU6050
from machine import Pin, SoftI2C

# You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(21), sda=Pin(22))
#sensor=mpu6050(axis='all',scl=22,sda=21)
#sensor.calibrate()

print('I2C SCANNER')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:', len(devices))

  for device in devices:
    print("I2C hexadecimal address: ", hex(device))
 
#mpu = MPU6050()

#while True:
    # Accelerometer Data
#    accel = mpu.read_accel_data() # read the accelerometer [ms^-2]
#    aX = accel["x"]
#    aY = accel["y"]
#    aZ = accel["z"]
#    print("x: " + str(aX) + " y: " + str(aY) + " z: " + str(aZ))