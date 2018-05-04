#include "MPU9250.h"
#include <stdio.h>
#include <wiringPi.h>

#define FREQ 1000 //ms, sample rate

// an MPU9250 object with its I2C address 
// of 0x68 (ADDR to GRND) and on Teensy bus 0
MPU9250 IMU(0x68);

float ax, ay, az, gx, gy, gz, hx, hy, hz, t;
int beginStatus;

static void setup() {
  // start communication with IMU and 
  // set the accelerometer and gyro ranges.
  // ACCELEROMETER 2G 4G 8G 16G
  // GYRO 250DPS 500DPS 1000DPS 2000DPS
  beginStatus = IMU.begin(ACCEL_RANGE_2G,GYRO_RANGE_250DPS);
}

static void printData(){

  // print the data
  FILE *f = fopen("MPU.txt", "a+");
  
  fprintf(f, "%6.6f\t", ax);
  fprintf(f, "%6.6f\t", ay);
  fprintf(f, "%6.6f\t", az);
          
  fprintf(f, "%6.6f\t", gx);
  fprintf(f, "%6.6f\t", gy);
  fprintf(f, "%6.6f\t", gz);
  
  fprintf(f, "%6.6f\t", hx);
  fprintf(f, "%6.6f\t", hy);
  fprintf(f, "%6.6f\t", hz);
          
  fprintf(f, "%6.6f\n", t);
  
  fclose(f);
  
}

static void loop() {
  if(beginStatus < 0) {
    delay(1000);
    fprintf(stderr, "IMU initialization unsuccessful\n");
    fprintf(stderr, "Check IMU wiring or try cycling power\n");
    delay(10000);
  }
  else{
    /* get the individual data sources */
    /* This approach is only recommended if you only
     *  would like the specified data source (i.e. only
     *  want accel data) since multiple data sources
     *  would have a time skew between them.
     */
    // get the accelerometer data (m/s/s)
    IMU.getAccel(&ax, &ay, &az);
  
    // get the gyro data (rad/s)
    IMU.getGyro(&gx, &gy, &gz);
  
    // get the magnetometer data (uT)
    IMU.getMag(&hx, &hy, &hz);
  
    // get the temperature data (C)
    IMU.getTemp(&t);
  
    // print the data
    printData();
  
    // delay a frame
    delay(FREQ);
  
    /* get multiple data sources */
    /* In this approach we get data from multiple data
     *  sources (i.e. both gyro and accel). This is 
     *  the recommended approach since there is no time
     *  skew between sources - they are all synced.
     *  Demonstrated are:
     *  1. getMotion6: accel + gyro
     *  2. getMotion7: accel + gyro + temp
     *  3. getMotion9: accel + gyro + mag
     *  4. getMotion10: accel + gyro + mag + temp
     */
  
     /* getMotion6 */
    // get both the accel (m/s/s) and gyro (rad/s) data
    IMU.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
    // get the magnetometer data (uT)
    IMU.getMag(&hx, &hy, &hz);
  
    // get the temperature data (C)
    IMU.getTemp(&t);
  
    // print the data
    printData();
  
    // delay a frame
    delay(FREQ);
  
    /* getMotion7 */
    // get the accel (m/s/s), gyro (rad/s), and temperature (C) data
    IMU.getMotion7(&ax, &ay, &az, &gx, &gy, &gz, &t);
    
    // get the magnetometer data (uT)
    IMU.getMag(&hx, &hy, &hz);
  
    // print the data
    printData();
  
    // delay a frame
    delay(FREQ);
  
    /* getMotion9 */
    // get the accel (m/s/s), gyro (rad/s), and magnetometer (uT) data
    IMU.getMotion9(&ax, &ay, &az, &gx, &gy, &gz, &hx, &hy, &hz);
  
    // get the temperature data (C)
    IMU.getTemp(&t);
  
    // print the data
    printData();
  
    // delay a frame
    delay(FREQ);
  
    // get the accel (m/s/s), gyro (rad/s), and magnetometer (uT), and temperature (C) data
    IMU.getMotion10(&ax, &ay, &az, &gx, &gy, &gz, &hx, &hy, &hz, &t);
  
    // print the data
    printData();
  
    // delay a frame
    delay(FREQ);
  }
}

int main(int argc, char ** argv) {

    setup();

    while (true) {
        loop();
    }
}
