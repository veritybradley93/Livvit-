import unicodecsv

def get_matching_rows(filename, vegetarian, coeliac, cuisine, borough):
	with open(filename) as csvfile:
		reader = unicodecsv.DictReader(csvfile, dialect='excel')

		results= []

		for row in reader:

			if vegetarian:
				matches_veg = (row['Vegetarian'] == vegetarian)
			else:
				matches_veg = True


			if coeliac:
				matches_coeliac = (row['Coeliac'] == coeliac)
			else:
				matches_coeliac = True


			if cuisine:
				matches_cuisine = (row['Cuisine'] == cuisine)
			else:
				matches_cuisine = True


			if borough:
				matches_borough = (row['Borough'] == borough)
			else: 
				matches_borough = True 		


			if(matches_veg and matches_coeliac and matches_cuisine and matches_borough):
				results.append(row)

	return results 			

			


print get_matching_rows('exercise_rest.csv', vegetarian="", coeliac="Yes", cuisine="Indian", borough="Islington")