#include <SparkFunMPU9250-DMP.h>
#include <SPI.h>
#include <SD.h>

#define SerialPort Serial

MPU9250_DMP imu;

const int chipSelect = 10;

void setup() 
{
  SerialPort.begin(9600);

  Serial.print("Initializing SD card...");

  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    return;
  }
  Serial.println("card initialized.");
  
  // Call imu.begin() to verify communication with and
  // initialize the MPU-9250 to it's default values.
  // Most functions return an error code - INV_SUCCESS (0)
  // indicates the IMU was present and successfully set up
  if (imu.begin() != INV_SUCCESS)
  {
    while (1)
    {
      SerialPort.println("Unable to communicate with MPU-9250");
      SerialPort.println("Check connections, and try again.");
      SerialPort.println();
      delay(5000);
    }
  }

  // Use setSensors to turn on or off MPU-9250 sensors.
  // Any of the following defines can be combined:
  // INV_XYZ_GYRO, INV_XYZ_ACCEL, INV_XYZ_COMPASS,
  // INV_X_GYRO, INV_Y_GYRO, or INV_Z_GYRO
  // Enable all sensors:
  imu.setSensors(INV_XYZ_GYRO | INV_XYZ_ACCEL | INV_XYZ_COMPASS);

  // Use setGyroFSR() and setAccelFSR() to configure the
  // gyroscope and accelerometer full scale ranges.
  // Gyro options are +/- 250, 500, 1000, or 2000 dps
  imu.setGyroFSR(2000); // Set gyro to 2000 dps
  // Accel options are +/- 2, 4, 8, or 16 g
  imu.setAccelFSR(2); // Set accel to +/-2g
  // Note: the MPU-9250's magnetometer FSR is set at 
  // +/- 4912 uT (micro-tesla's)

  // setLPF() can be used to set the digital low-pass filter
  // of the accelerometer and gyroscope.
  // Can be any of the following: 188, 98, 42, 20, 10, 5
  // (values are in Hz).
  imu.setLPF(5); // Set LPF corner frequency to 5Hz

  // The sample rate of the accel/gyro can be set using
  // setSampleRate. Acceptable values range from 4Hz to 1kHz
  imu.setSampleRate(10); // Set sample rate to 10Hz

  // Likewise, the compass (magnetometer) sample rate can be
  // set using the setCompassSampleRate() function.
  // This value can range between: 1-100Hz
  imu.setCompassSampleRate(10); // Set mag rate to 10Hz
}


void printIMUData(void)
{  
  float accelX = imu.calcAccel(imu.ax);
  float accelY = imu.calcAccel(imu.ay);
  float accelZ = imu.calcAccel(imu.az);
  float gyroX = imu.calcGyro(imu.gx);
  float gyroY = imu.calcGyro(imu.gy);
  float gyroZ = imu.calcGyro(imu.gz);
  float magX = imu.calcMag(imu.mx);
  float magY = imu.calcMag(imu.my);
  float magZ = imu.calcMag(imu.mz);
  
  SerialPort.println("Accel: " + String(accelX) + ", " +
              String(accelY) + ", " + String(accelZ) + " g");
  SerialPort.println("Gyro: " + String(gyroX) + ", " +
              String(gyroY) + ", " + String(gyroZ) + " dps");
  SerialPort.println("Mag: " + String(magX) + ", " +
              String(magY) + ", " + String(magZ) + " uT");
  SerialPort.println("Time: " + String(imu.time) + " ms");
  SerialPort.println();
  
}

void loop() 
{
  if (imu.dataReady()){
      imu.update(UPDATE_ACCEL | UPDATE_GYRO | UPDATE_COMPASS);
      String dataString = "";
      printIMUData();
      File dataFile = SD.open("datalog.txt", FILE_WRITE);
      if (dataFile) {
         dataFile.print("Accel: ");
         dataFile.print(imu.calcAccel(imu.ax));
         dataFile.print(", ");
         dataFile.print(imu.calcAccel(imu.ay));
         dataFile.print(", ");
         dataFile.print(imu.calcAccel(imu.az));
         dataFile.print("\n");
         
         dataFile.print("Gyro: ");
         dataFile.print(imu.calcGyro(imu.ax));
         dataFile.print(", ");
         dataFile.print(imu.calcGyro(imu.ay));
         dataFile.print(", ");
         dataFile.print(imu.calcGyro(imu.az));
         dataFile.print("\n");

         dataFile.print("Mag: ");
         dataFile.print(imu.calcMag(imu.ax));
         dataFile.print(", ");
         dataFile.print(imu.calcMag(imu.ay));
         dataFile.print(", ");
         dataFile.print(imu.calcMag(imu.az));
         dataFile.print("\n\n\n");
         
         dataFile.close();
      }
    else {
      Serial.println("error opening datalog.txt");
    } 
  }
}


