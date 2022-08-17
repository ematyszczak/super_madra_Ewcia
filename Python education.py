print("Witaj w kalkulatorze!")
def dodawanie(firstDigit, secondDigit):

   wynik = firstDigit + secondDigit  #definiuje dodawanie
   return print(wynik)
   

def odejmowanie(firstDigit, secondDigit):

   wynik = firstDigit - secondDigit  #definiuje odejmowanie
   return print(wynik)

def mnozenie(firstDigit, secondDigit):

   wynik = firstDigit * secondDigit  #definiuje mnozenie
   return print(wynik)

def dzielenie(firstDigit, secondDigit):

   wynik = firstDigit / secondDigit  #definiuje dzielenie
   return print(wynik)

def dzialanie():
   dzialanie = input("wybierz działanie: dodawanie, odejmowanie, mnozenie bądź dzielenie\n")
   if dzialanie != "dodawanie" and dzialanie != "odejmowanie" and dzialanie != "mnozenie" and dzialanie != "dzielenie":
      print("błędnie wprowadzona odpowiedź")
      exit()

   print("podaj pierwsza liczbe")

   notDigit = str(input())  #wprowadzenie str
   counter = 0
   while not notDigit.isdigit():  #user musi wprowadzic liczbe
      counter = counter + 1
      notDigit = input("Wprowadź poprawną liczbę. \n")
      if counter == 3:
         print("skup sie!")

   firstDigit = float(notDigit)  #zmiana na float, zeby dalo sie liczyc #smart

   print("podaj druga liczbe")

   notDigit2 = str(input())
   counter1 = 0
   while not notDigit2.isdigit():

      counter1=counter1 + 1
      notDigit2 = input("Wprowadź poprawną liczbę. \n")
      if counter1 == 3:
         print("ogarnij się jebany debilu")

   secondDigit = float(notDigit2)

   if dzialanie == "dodawanie":

      dodawanie(firstDigit, secondDigit)


   elif dzialanie == "odejmowanie":

      odejmowanie(firstDigit, secondDigit)
   
   elif dzialanie == "mnozenie":

      mnozenie(firstDigit, secondDigit)

   elif dzialanie == "dzielenie":

      dzielenie(firstDigit, secondDigit)

dzialanie()

wybor = input("Super! Czy chcesz wykonywac dalsze obliczenia? Zaznacz 'tak' lub 'nie'\n")
if wybor == "tak":
   dzialanie()
else:
   Print("W takim razie dzieki za uzywanie kalkulatora!")

wybor = input("Super! Czy chcesz wykonywac dalsze obliczenia? Zaznacz 'tak' lub 'nie'\n")
if wybor == "tak":
   dzialanie()
else:
   print("W takim razie dzieki za uzywanie kalkulatora!")








