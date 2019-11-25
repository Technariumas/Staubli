/*
 * DFRemote example. Demonstrates DFRemote library.
 * In this specific example, pins 2 and 3 were wired as pushbuttons (active low).
 * Pins 5,6 and 7 were wired to LEDs.
 */

// Create global object to communicate with Dragonframe

DFRemote df_remote = DFRemote();

/*
 * Arduino calls this function once, at the start of your program.
 */
void setup()
{
  // set up serial port to 57600 kbps
  Serial.begin(57600);

  /*
   * Activate one or more input pins, associating them with Dragonframe commands.
   */

  // When input pin 2 goes LOW, send DF a SHOOT 1 frame command
  df_remote.activatePin(2, LOW, DF_SHOOT_CMD, 1);
  
  // When input pin 3 goes LOW, send DF a DELETE command
  df_remote.activatePin(3, LOW, DF_DELETE_CMD);
  
  /*
   * Other commands are:
   *   DF_PLAY_CMD - toggles playback
   *   DF_LIVE_CMD - goes to live (also re-engages live view)
   */
  
  
  /*
   * Configure output pins. This is optional, if you want to control
   * another device (or just turn on an LED).
   *
   * The choice of output pins below was purely optional, but it corresponds
   * to how they are used in the loop() function in response to DF messages.
   */
  pinMode(5, OUTPUT); // SHOOT SIGNAL
  digitalWrite(5, LOW);

  pinMode(6, OUTPUT); // DELETE SIGNAL
  digitalWrite(6, LOW);

  pinMode(7, OUTPUT); // Position frame SIGNAL
  digitalWrite(7, LOW);
  
}

/**
 * Arduino calls this function repeatedly as the main program loop.
 */
void loop()
{
  // tell dsm to check for inputs and send messages to DF if needed
  df_remote.processPins();
  
  // read serial messages from DF
  int cmd = df_remote.processSerial();
  
  /**
   * The following examples take messages from DF
   * and turn a digital I/O pin high for 0.5 seconds.
   * You can take any action (or no action).
   */
  if (cmd == DF_SHOOT_MSG)
  {
    digitalWrite(5, HIGH);
    delay(500);
    digitalWrite(5, LOW);
  }
  if (cmd == DF_DELETE_MSG)
  {
    digitalWrite(6, HIGH);
    delay(500);
    digitalWrite(6, LOW);
  }
  if (cmd == DF_POSITION_MSG)
  {
    digitalWrite(7, HIGH);
    delay(500);
    digitalWrite(7, LOW);
  }
  
}
