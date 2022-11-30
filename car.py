command = ""
started = False
while True:
      command = input(">").lower()
      if command == "start":
         if started:
            print ("already started")
         else:
            started = True
            print("car started...")
      elif command == "stop":
         if not started:
            print("already stopped")
         else:
            started = False   
            print("car stopped.")  
      elif command == "help":
         print('''
start - to start the car
stop - to stop the car
quit - to quit        
          ''')
      elif command == "quit":
         break
      else:
         print("purila da venna")
