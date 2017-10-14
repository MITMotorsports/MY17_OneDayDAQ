#include <wiringPi.h>
#include <fstream>
#include <iostream>
using namespace std;

#define DEBUG false

int main(void) {
	wiringPiSetup();
	
	ifstream in("/home/pi/pins/shutdown.pin");
	int pin;
	in>>pin;
	#if DEBUG
		cout<<"Pin is: "<<pin<<endl;
	#endif
	
	pinMode(pin, INPUT);
	pullUpDnControl(pin, PUD_DOWN);
	
	for(;;) {
		delay(250);
		#if DEBUG
			cout<<digitalRead(pin)<<endl;
		#endif
		if (digitalRead(pin))
			system("sudo shutdown now");
	}
	return 0;
}
