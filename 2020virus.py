from covid import Covid
covid=Covid()
data=covid.get_data()

total_active=covid.get_total_active_cases()
print("total active cases: ",total_active)
conf_cases=covid.get_total_confirmed_cases()
print("confirmed cases: ",conf_cases)

x=str(input("enter the name of the coutry: "))

country_cases=covid.get_status_by_country_name("italy")
print("total cases: ",country_cases)
