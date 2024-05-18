from hidden import text

# `text` bevat een hele lange string (het hele script voor Bee Movie)
print(f'het script van Bee Movie is {len(text)} woorden lang!')

#> TIP: Probeer van alle strings die je print mooie stukjes tekst te maken, met een beetje uitleg wat wat er geprint wordt betekent
# Dus niet: 	>>> 42
# Maar: 		>>> Het antwoord op het leven, het universum en alles is 42

# > Tel hoe vaak het woord 'bee' (of 'Bee', of 'BEE' etc. ) voorkomt in deze tekst
# Hint: Je kunt de hele string hoofdletters of kleine letters te maken, dan hoef je niet voor elke variatie op het woord 'bee' te checken. bee! en Bee worden nu bijvoorbeeld als losse woorden gezien.
#print(text)
nieuwe_text = text.lower()
aantal_bee = nieuwe_text.count('bee')
print(f'het aantal bijtjes is {aantal_bee}!')

# > Wat is de eerste plek waar het woord 'bee' staat?
print(nieuwe_text.find('bee'))

# > Wat is de laatste plek waar het woord 'bee' staat? 
print(nieuwe_text.rfind('bee'))

# > Het eerste karakter in de tekst heeft nu nog geen hoofdletter. Gebruik uit de gegeven documentatie een functie om alleen de allereerste letter in een hoofdletter te veranderen.
nieuwe_text.capitalize()

# > Er is ook een functie in de documentatie die dit voor _ieder_ woord doet. Pas die ook toe.
nieuwe_text.title()

# > Hoe vaak komt elke klinker voor? 
aantal_a = nieuwe_text.count('a')
aantal_e = nieuwe_text.count('e')
aantal_o = nieuwe_text.count('o')
aantal_i = nieuwe_text.count('i')
aantal_u = nieuwe_text.count('u')
aantal_klinkers = aantal_a + aantal_e + aantal_o + aantal_i + aantal_u
print(aantal_klinkers)

# > De volgende regel code gaat teken voor teken over de hele tekst heen. De variabele teken is dus steeds een nieuw karakter uit de tekst. Voeg op de lege plek een check toe die print of de variabele `teken` een getal is.

# Deze code constructie noemen we een 'for loop'. We gaan het hier later nog over hebben.

for teken in text:
	# Voeg hier je if statement toe
  if teken.isnumeric():
		# print hier welk getal het was
    print(teken)
  
# > Wat was het laatst gevonden getal? En wat is de eerste plek waarop dit getal in de tekst staat? 

print(nieuwe_text.find("7"))

