# pcs_final
We provided an SMS service that can remote simulation running on your PC. 

## Usage
1. Make a Twilio account
2. Open terminal and enter the command
```
python3 final/final.py
```
3. The server will run on 127.0.0.1:5000, use ngrok to let external network be able to connect to your local port
4. Hook up your server to your twilio account
5. Enjoy the service!

## Modify guide
Put your simulation in 
```
final/simulation.py
```
Note that "log" is the variable that will be output by the SMS service.

## Twilio guide
Some simple commands has been written in 
```
twilio/
```
You can learn from the simple codes

## Multiprocessing guide
Some simple commands has been written in 
```
sync/
```
You can learn from the simple codes

## Note
```
sync/
twilio/
```
The two folders has nothing to do with the final version of our SMS service,
however it's the first step of our service and we eventually combined them together, which became our service.

