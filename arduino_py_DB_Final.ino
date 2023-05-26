#define LED_PIN 8
#define BUTTON_PIN 7

byte lastButtonState = LOW;
byte ledState = LOW;

unsigned long debounceDuration = 100; // millis
unsigned long lastTimeButtonStateChanged = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);
}

void loop() {
  if (millis() - lastTimeButtonStateChanged > debounceDuration) {
    byte buttonState = digitalRead(BUTTON_PIN);
    
    if (buttonState != lastButtonState) {
      lastTimeButtonStateChanged = millis();
      lastButtonState = buttonState;
      
      
      
      if (buttonState == LOW) {
        ledState = (ledState == HIGH) ? LOW: HIGH;
        digitalWrite(LED_PIN, ledState);
        if(ledState==HIGH){Serial.println("1");}
        if(ledState==LOW){Serial.println("0");}
       
        
        
      }
      
    }
  }
  



}