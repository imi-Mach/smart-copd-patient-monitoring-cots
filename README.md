# smart-copd-patient-monitoring-cots
The Smart COPD patient monitoring uses this code for emulating commercial of the shelf (COTS) devices that interact with a Vue.js frontend.

## Dependencies
* Stable version of Python3 that supports GPIO modules.
* Raspberry Pi (preferablly 3 or higher).
* Operating System that works with the previous 2 dependencies (this project was tested with a linux based OS).
* Text editor to adjust code (incase the pins are not available on Raspberry Pi).
* Sensors that are compatible with Raspberry Pi (most if not all Arduino sensors should work fine).

## Rationale
* Raspberry Pi is better for multi-tasking than Arduino. However, the trade off is that the device is not best suited for focusing on collecting data. This trade off is fine since we are not focused on instrumental accuracy. Raspberry Pi is flexiable in that we can isolate code to a particular environment. This does decreased portability, but the team's objective only needs the device to work as a proof of concept.