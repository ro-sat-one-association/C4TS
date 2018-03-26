#include <ESP8266WiFi.h>
#include "src/MPU9250.h"
#include "src/IMUResult.h"
#include "src/quaternionFilters.h"



#define serialDebug true  // Set to true to get Serial output for debugging
#define baudRate 115200


#define samplingRateInMillis 100

///////////////////////////////////////////////////////////////////
#define declination 6.08 //http://www.ngdc.noaa.gov/geomag-web/#declination . This is the declinarion in the easterly direction in degrees.  
#define calibrateMagnetometer false  //Setting requires requires you to move device in figure 8 pattern when prompted over serial port.  Typically, you do this once, then manually provide the calibration values moving forward.
MPU9250 myIMU;
IMUResult magResult, accResult, gyroResult, orientResult;


void setup()
{

  Serial.begin(baudRate);
  Serial.setDebugOutput(true); //Used for more verbose wifi debugging

  //Start IMU.  Assumes default SDA and SCL pins 4,5 respectively.
  myIMU.begin();


  //This tests communication between the accelerometer and the ESP8266.  Dont continue until we get a successful reading.
  //It is expected that the WHO_AM_I_MPU9250 register should return a value of 0x71.
  //If it fails to do so try the following:
  //1) Turn power off to the ESP8266 and restart.  Try this a few times first.  It seems to resolve the issue most of the time.  If this fails, then proceed to the followingn steps.
  //2) Go to src/MPU9250.h and change the value of ADO from 0 to 1
  //3) Ensure your i2c lines are 3.3V and that you haven't mixed up SDA and SCL
  //4) Run an i2c scanner program (google it) and see what i2c address the MPU9250 is on.  Verify your value of ADO in src/MPU9250.h is correct.
  //5) Some models apparently expect a hex value of 0x73 and not 0x71.  If that is the case, either remove the below check or change the value fro 0x71 to 0x73.
  byte c;
  do
  {
    c = myIMU.readByte(MPU9250_ADDRESS, WHO_AM_I_MPU9250);
    if (c != 0x71)
    {
      Serial.println("Failed to communicate with MPU9250");
      Serial.print("WHO_AM_I returned ");
      Serial.println(c, HEX);
      delay(500);
    }
  } while (c != 0x71);

  Serial.println("Successfully communicated with MPU9250");


  // Calibrate gyro and accelerometers, load biases in bias registers, then initialize MPU.
  myIMU.calibrate();  
  myIMU.init();
  if (calibrateMagnetometer)
    myIMU.magCalibrate();
  else
    myIMU.setMagCalibrationManually(-202, 43, -506);    //Set manually with the results of magCalibrate() if you don't want to calibrate at each device bootup.
                                                       //Note that values will change as seasons change and as you move around globe.  These values are for zip code 98103 in the fall.

  Serial.println("Accelerometer ready");


  accResult.setName("acc");
  gyroResult.setName("gyro");
  magResult.setName("mag");
  orientResult.setName("orien");
}

uint32_t lastSample = 0;
void loop()
{

	// If intPin goes high, all data registers have new data
	// On interrupt, check if data ready interrupt
	if (myIMU.readByte(MPU9250_ADDRESS, INT_STATUS) & 0x01)
	{
		myIMU.readAccelData(&accResult);
		myIMU.readGyroData(&gyroResult);
		myIMU.readMagData(&magResult);
	}


  myIMU.updateTime();
  MahonyQuaternionUpdate(&accResult, &gyroResult, &magResult, myIMU.deltat);
  readOrientation(&orientResult, declination);
  
	if (millis() - lastSample > samplingRateInMillis)
	{


    lastSample = millis();

		
		
		if (serialDebug)
		{
			accResult.printResult();
			gyroResult.printResult();
			magResult.printResult();
			orientResult.printResult();
		}
   

		myIMU.sumCount = 0;
		myIMU.sum = 0;

	}  
}


void readResult(IMUResult result, String &payload)
{   
  String resName;
  result.getName(resName);

  float vals[3];
  String names[3];

  names[0]=resName+"_x";
  names[1]=resName+"_y";
  names[2]=resName+"_z";

  vals[0] = result.getXComponent();
  vals[1] = result.getYComponent();
  vals[2] = result.getZComponent();

}

