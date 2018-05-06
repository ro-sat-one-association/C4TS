#include <ctime>
#include <iostream>
using namespace std;
time_t start, actual, collect, aprs, coord;

void setup(){
    start   = time(NULL);
    collect = 0;
    aprs    = 0;
    coord   = 0;
    
}

void loop(){
    actual = time(NULL);
  //  if(actual - collect > 1){
        cout<<"COLLECT\n";
        system("python /home/pi/Final/collect.py");
        collect = time(NULL);
    //}
    if(actual - aprs > 120){
        cout<<"APRS\n";
        system("python /home/pi/Final/sendAPRS.py");
        aprs = time(NULL);
    }
    if(actual - coord > 600){
        cout<<"COORD\n";
        system("python /home/pi/Final/sendCoord.py");
        coord = time(NULL);
    }  
}

int main(){
    setup();
    
	while(true)
        loop();
	return 0;
}
