COUNTRIES_DATA = {
  "China" : 143,
  "India" : 136,
  "USA" : 32,
  "Pakistan" : 21
}

def country_data(country_prompt):
  return (country_prompt, COUNTRIES_DATA.get(country_prompt, "Country not found!\n"))


def prompt_system_for_countries(input_prompt):
  if input_prompt == "print":
    for country, population in COUNTRIES_DATA.items():
      print(country, "=>", population, "\n")
  elif input_prompt == "add":
    new_country = input("Please enter new country name: ")
    if new_country not in COUNTRIES_DATA:
      new_country_population = int(input(f"Enter the population for {new_country}: "))
      COUNTRIES_DATA[new_country] = new_country_population
      print(f"RESULT: {country_data(new_country)}")
  elif input_prompt == "remove":
    country_to_remove = input("Enter the country to remove: ")
    if country_to_remove in COUNTRIES_DATA:
      COUNTRIES_DATA.pop(country_to_remove)
      print(f"{country_to_remove} is removed from the data!\n")
    else:
      print("Country doesn't exists in the data.\n")
  elif input_prompt == "query":
    query_country = input("Enter country name to query: ")
    if query_country in COUNTRIES_DATA:
      print(f"{COUNTRIES_DATA[query_country]}\n")
    else:
      print(f"{query_country} doesn't exist in the data\n")
  else:
    print("prompt is wrong!")
  
flag = True
while flag:
  input_prompt = input("Please write command to perform action: ")
  prompt_system_for_countries(input_prompt)
  program_continue = input("Would you want another session?(y/n): ")
  if program_continue == "n":
    flag = False
  else:
    continue

print("Thanks for using the system!\n")