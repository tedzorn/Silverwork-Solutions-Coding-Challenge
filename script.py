from statistics import mean
from statistics import median
import json

# Opening JSON file
f = open('loans.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)

#The json object we will output
dct={}


#LoanAmount information
lst=[]
for i in data:
    for key, value in i.items():
    	if key=="LoanAmount":
    		lst.append(value)
dct["LoanAmountSummary"] = {	
		"Sum": round(sum(lst), 2),
		"Average": round(mean(lst), 2),
		"Median": round(median(lst), 2),
		"Minimum": round(min(lst), 2),
		"Maximum": round(max(lst), 2),
	}

#SubjectAppraisedAmount information
lst=[]
for i in data:
    for key, value in i.items():
    	if key=="SubjectAppraisedAmount":
    		lst.append(value)
dct["SubjectAppraisedAmountSummary"] = {	
		"Sum": round(sum(lst), 2),
		"Average": round(mean(lst), 2),
		"Median": round(median(lst), 2),
		"Minimum": round(min(lst), 2),
		"Maximum": round(max(lst), 2),
	}

#InterestRate information
lst=[]
for i in data:
    for key, value in i.items():
    	if key=="InterestRate":
    		lst.append(value)
dct["InterestRateSummary"] = {	
		"Sum": round(sum(lst), 2),
		"Average": round(mean(lst), 2),
		"Median": round(median(lst), 2),
		"Minimum": round(min(lst), 2),
		"Maximum": round(max(lst), 2),
	}

#Send output to monthlySummary.json
a_file = open("monthlySummary.json", "w")
text = json.dumps(dct, indent=4)
print(text, file=a_file)
a_file.close()



#Now we will make our second file where we organize by state
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

dct2={}

lst=[]
for state in states:
	for i in data:
		if i["SubjectState"]==state:
			dct2[state]={}
			#LoanAmount information for each state
			lst=[]
			for i in data:
			    for key, value in i.items():
			    	if int(key=="LoanAmount") & int(i["SubjectState"]==state):
			    		lst.append(value)
			dct2[state]["LoanAmountSummary"] = {	
					"Sum": round(sum(lst), 2),
					"Average": round(mean(lst), 2),
					"Median": round(median(lst), 2),
					"Minimum": round(min(lst), 2),
					"Maximum": round(max(lst), 2),
				}

			#SubjectAppraisedAmount information for each state
			lst=[]
			for i in data:
			    for key, value in i.items():
			    	if int(key=="SubjectAppraisedAmount") & int(i["SubjectState"]==state):
			    		lst.append(value)
			dct2[state]["SubjectAppraisedAmountSummary"] = {	
					"Sum": round(sum(lst), 2),
					"Average": round(mean(lst), 2),
					"Median": round(median(lst), 2),
					"Minimum": round(min(lst), 2),
					"Maximum": round(max(lst), 2),
				}

			#InterestRate information for each state
			lst=[]
			for i in data:
			    for key, value in i.items():
			    	if int(key=="InterestRate") & int(i["SubjectState"]==state):
			    		lst.append(value)
			dct2[state]["InterestRateSummary"] = {	
					"Sum": round(sum(lst), 2),
					"Average": round(mean(lst), 2),
					"Median": round(median(lst), 2),
					"Minimum": round(min(lst), 2),
					"Maximum": round(max(lst), 2),
				}
			

# print(json.dumps(dct2, indent=4))

#Send output to monthlyByState.json
a_file = open("monthlyByState.json", "w")
text = json.dumps(dct2, indent=4)
print(text, file=a_file)
a_file.close()




# Closing file
f.close()