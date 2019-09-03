

String inputString = "";         // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
    // initialize serial:
    Serial.begin(115200);
    // reserve 200 bytes for the inputString:
    inputString.reserve(64);
}

char delim = ',';
float host_lane = 0;
float host_spd = 15;
float obj_lane = 0;
float rel_dist = 50;
float obj_spd = 0;
float emergency = 0;

// car properties
float obj_width = 75;
float obj_height = 150;
float car_width = 75;
float car_height = 150;

// road properties
float left_barrier = 288;
float right_barrier = 512;
String move_direction = "N";

void loop() {
    static String dir = "N";
    int count = 0;
    // print the string when a newline arrives:
    if (stringComplete) {
        for (int i = 0; i < inputString.length(); i++) {
            if (inputString[i] == ',') {
                count++;
            }
        }

        if (count == 4) {
            char s[200];
            char* t;
            //      Serial.println(inputString);
            unsigned int l = inputString.length();
            inputString.toCharArray(s, l > 64 ? 64 : l);
            t = strtok(s, &delim);

            while (t != NULL) {;
                host_lane = String(t).toInt();
                t = strtok(NULL, &delim);
                host_spd = String(t).toInt();
                t = strtok(NULL, &delim);
                obj_lane = String(t).toInt();
                t = strtok(NULL, &delim);
                rel_dist = String(t).toInt();
                t = strtok(NULL, &delim);
                emergency = String(t).toInt();
                t = strtok(NULL, &delim);

                //      Serial.print("Car x: ");
                //      Serial.print(car_x, DEC);
                //      Serial.print(" Car y: ");
                //      Serial.print(car_y, DEC);
                //      Serial.print(" Obj x: ");
                //      Serial.print(obj_x, DEC);
                //      Serial.print(" Obj y: ");
                //      Serial.println(obj_y, DEC);
            }

            //////////////////////////////////////////////////////////////////////////
            // change logic below this line
            //
            // variables:
            //   car_x, car_y - for car position
            //   obj_x, obj_y - for object position
            //   left_barrier, right_barrier - for the edges of the road
            //   (untested) car_width, car_height, obj_width, obj_height
            //
            // change dir to either:
            //
            //  "L" to move left
            //  "R" to move right
            //  "N" to stay in the same position
            //
            //////////////////////////////////////////////////////////////////////////
            if (host_lane==obj_lane){
              if(rel_dist < 100){
                if (host_lane == 0){
                  dir = "L";
                }
                else{
                  dir = "R";
                }              
              }
              else{
                dir = "N";
              }
            }
            else{
              dir = "N";              
            }
            
            //////////////////////////////////////////////////////////////////////////
            // ^^ change logic above this line
            //////////////////////////////////////////////////////////////////////////

            Serial.println(dir);

        }
        // clear the string:
        inputString = "";
        stringComplete = false;
    }
}

/*
   SerialEvent occurs whenever a new data comes in the hardware serial RX. This
   routine is run between each time loop() runs, so using delay inside loop can
   delay response. Multiple bytes of data may be available.
 */
void serialEvent() {
    while (Serial.available()) {
        // get the new byte:
        char inChar = (char)Serial.read();
        // add it to the inputString:
        inputString += inChar;

        // if the incoming character is a newline, set a flag so the main loop can
        // do something about it:
        if (inChar == '\n') {
            stringComplete = true;
        }
    }
}
