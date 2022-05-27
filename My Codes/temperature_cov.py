should_continue = True


while should_continue == True:
  print ("Hello, this is a Temperature Converter App")
  current_unit= input("Which temperature unit do you want to convert? \n Input C for Celsius, \n K for Kelvin,\n F for Fahrenheit:\n")
  convert_to = input("Which temperature unit do you want to convert to? \n Input C for Celsius,\n K for Kelvin,\n F for Fahrenheit:\n ")


  # Fahrenheit to celcius
  if current_unit== "F" and  convert_to== "C" :
      print("Good, let's get started. \n You want to convert from FAHRENHEIT to CELSIUS ")
      Fahr = float(input('Write temperature in Fahrenheit = '))
      Cels = (Fahr - 32) * 5 / 9
      Cels3 = "{:.3f}". format(Cels)
      Cels = float(Cels3)
      print('Tempearture in Celsius = ' + str(Cels))

  #  Fahrenheit to Kelvin
  elif current_unit == "F" and convert_to == "K" :
      print("Good, let's get started. \n You want to convert from FAHRENHEIT to KELVIN ")
      FAHr = float(input('Write temperature in Fahrenheit = '))
      KELv = (FAHr - 32) * 5 / 9 + 273.15
      KELv3 = "{:.3f}". format(KELv)
      KELv = float(KELv3)
      print('Tempearture in Kelvin = ' + str(KELv))


    # Kelvin to Celsius

  elif current_unit	 == "K" and convert_to== "C" :
      print("Good, let's get started. \n You want to convert from Kelvin to Celcius")
      kelv = float(input('Write temperature in Kelvin = '))
      cELS = kelv - 273.15
      cELS3 = "{:.3f}". format(cELS)
      cELS = float(cELS3)
      print('Tempearture in Celsius = ' + str(cELS))


  # Kelvin to Fahrenheit
  elif current_unit == "K" and convert_to == "F" :
      print("Good, let's get started. \n You want to convert from Kelvin to Fahrenheit ")
      Kelv = float(input('Write temperature in Kelvin = '))
      fahr = (Kelv - 273.15) * 9 / 5 + 32
      fahr3 = "{:.3f}". format(fahr)
      fahr = float(fahr3)
      print('Tempearture in Fahrenheit = ' + str(fahr))


      # Celsius to Fahrenheit

  elif current_unit== "C" and convert_to == "F" :
      print("Good, let's get started. \n You want to convert from Celcius to Fahrenheit ")
      cels =float(input('Write temperature in Celsius = '))
      fahr = (cels * 9 / 5) + 32
      fahr3 = "{:.3f}". format(fahr)
      fahr = float(fahr3)
      print('Tempearture in Fahrenheit = ' + str(fahr))

      # Celsius to Kelvin

  elif current_unit == "C" and convert_to == "K" :
      print("Good, let's get started. \n You want to convert from Celsius to Kelvin")
      CELS = float(input('Write temperature in Celsius = '))
      KELV = CELS + 273.15
      KELV3 = "{:.3f}". format(KELV)
      KELV = float(KELV3)
      print('Tempearture in Kelvin = ' + str(KELV))

  # If current_unit is equal to convert_to

  elif current_unit == convert_to:
      print("You have entered the wrong command.")
      print("Thanks for the using my Temperature Converter")

  run_again = input("Run again? ")
  if run_again == 'NO':
    should_continue = False
