#include <CayenneMQTTESP8266.h>

#define CAYENNE_DEBUG
#define CAYENNE_PRINT Serial

// WIFI credentials
char ssid[] = "WorkShop";
char password[] = "m,./@1234";

// Cayenne credentials
char username[] = "50457b00-f653-11e9-a38a-d57172a4b4d4";
char mqtt_password[] = "d02f0fa606e75ca84124ef4564b50c5c292b6886";
char client_id[] = "66c01550-857e-11eb-a2e4-b32ea624e442";

void setup() {
  Cayenne.begin(username, mqtt_password, client_id, ssid, password);
  pinMode(0, OUTPUT);
//  digitalWrite(0, HIGH);
}

// the loop function runs over and over again forever
void loop() {
  Cayenne.loop();
}

CAYENNE_IN(0)
{
  digitalWrite(0, getValue.asInt());
}
