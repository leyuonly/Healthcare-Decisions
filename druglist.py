import csv


def d_type(medication):  # takes medication name and returns mode of action of drug
    medl = medication.lower()
    if medl == "lisinopril" or medl == "ramipril":
        drug_type = 1

    elif medl == "losartam" or medl == "valsartan":
        drug_type = 2

    elif medl == "amlodipine" or medl == "nifedipine":
        drug_type = 3

    elif medl == "hydrochlorothiazide" or medl == "hctz" or medl == "chlorthalidone":
        drug_type = 4
    else:
        drug_type = 0
        print("Sorry but this medication is invalid or not registered")

    return drug_type  # 0 is invalid, 1 is ACE-i, 2 is ARB, 3 is CCB, 4 is thiazide


path = "drugs.csv"  # program takes csv files in the format of __name,dose__
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
druglist = []  # new list of drugs including

for drug in reader:
    name = drug[0]
    dose = float(drug[1])
    mech = d_type(name)
    druglist.append([name, dose, mech])
dl = druglist

print(dl)
