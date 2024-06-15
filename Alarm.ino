#include <avr/pgmspace.h>

const int buzzerPin = 2;
const int lightPin  = 4;
const int sensorPin = 7;
void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(lightPin, OUTPUT);
  pinMode(sensorPin, INPUT_PULLUP);
}
void loop() {
 int sensorVal = digitalRead(sensorPin);
  if (sensorVal == HIGH){
    delay(500);
    digitalWrite(lightPin, HIGH);
    tone(buzzerPin, 10); // Play a tone of 1000 Hz
    
    delay(200); // Wait for a second

    digitalWrite(lightPin, LOW);
    noTone(buzzerPin); // Stop the tone
  }
  delay(100); // Wait for a second agaiN
}
