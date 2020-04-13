import sys

'''a function to get data from user'''
 
def data():
    region = str("Africa")
    aveAge = float(19.7)
    avgDailyIncomeInUSD = float(5.50)
    avgDailyIncomePopulation = float(0.71)
 
    # reported cases
    
    while True:
        try:
            reportedCases = int(input("Provide Reported Cases in " + str(region) + ": \n"))
        except ValueError:
            print("Please enter a valuable answer!! \n ")
            continue
        else:
            break
 
    # total beds
    
    while True:
        try:
            totalHospitalBeds = int(input("Provide Total Amount Of Beds In " + str(region) + ": \n"))
        except ValueError:
            print("Please enter a valuable answer!! \n ")
            continue
        else:
            break
 
    # current population
    
    while True:
        try:
            population = int(input("Provide Current Population in " + str(region) + ": \n"))
        except ValueError:
            print("Please enter a valuable answer!!\n ")
            continue
        else:
            break
 
    # time to elapse
    
    while True:
        try:
            timeToElapse = int(input("Provide a date to estimate how the economy would be affected: \n "))
        except ValueError:
            print("Please enter a valuable answer!! \n ")
            continue
        else:
            break
 
 
    # period type
    
    while True:
        periodType = input("Calculate in Days,Weeks or Months?:  \n ")
        if periodType.lower() not in ("days", "months", "weeks"):
            print("Please select a valid option \ntype days,months or weeks! \n ")
        else:
            break
        if periodType == "months":
            int(timeToElapse * 30)
        elif periodType == "weeks":
            int(timeToElapse * 7)
        else:
            break
 
    return region, aveAge, avgDailyIncomeInUSD, reportedCases, avgDailyIncomePopulation, population, \
           totalHospitalBeds, timeToElapse, periodType
 
 
'''impact function'''
 
def impact(region, aveAge, avgDailyIncomeInUSD, reportedCases, avgDailyIncomePopulation, population, \
           totalHospitalBeds, timeToElapse, periodType):
    currentlyInfected = int(reportedCases * 10)
    infectionByrequestedTime = int(currentlyInfected * 512)
    hospitalBedsByRequestedTime = int(totalHospitalBeds * (1 - 0.35))
    casesByrequestedTime = int(infectionByrequestedTime * 0.15)
    casesForICUByRequestedTime = int(infectionByrequestedTime * 0.05)
    casesForVentilatorsByRequestedTime = int(infectionByrequestedTime * 0.02)
    dollarsInFlight = int((infectionByrequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / timeToElapse)
 
    return currentlyInfected, infectionByrequestedTime, hospitalBedsByRequestedTime, casesByrequestedTime, \
           casesForICUByRequestedTime, casesForVentilatorsByRequestedTime, dollarsInFlight
 
 
''' severe function to calculate impact cases'''
 
def severeImpact(region, aveAge, avgDailyIncomeInUSD, reportedCases, avgDailyIncomePopulation, population, \
                 totalHospitalBeds, timeToElapse, periodType1):
    scurrentlyInfected = int(reportedCases * 50)
    sinfectionByrequestedTime = int(scurrentlyInfected * 512)
    shospitalBedsByRequestedTime = int(totalHospitalBeds * (1 - 0.35))
    scasesByrequestedTime = int(sinfectionByrequestedTime * 0.15)
    scasesForICUByRequestedTime = int(sinfectionByrequestedTime * 0.05)
    scasesForVentilatorsByRequestedTime = int(sinfectionByrequestedTime * 0.02)
    sdollarsInFlight = int((sinfectionByrequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD) / timeToElapse)
 
    return scurrentlyInfected, sinfectionByrequestedTime, shospitalBedsByRequestedTime, scasesByrequestedTime, \
           scasesForICUByRequestedTime, scasesForVentilatorsByRequestedTime, sdollarsInFlight
 
 
'''estimator funtion to print out the results'''
 
def estimator(region, aveAge, avgDailyIncomeInUSD, reportedCases, avgDailyIncomePopulation, population, \
              totalHospitalBeds, timeToElapse, currentlyInfected, infectionByrequestedTime, \
              hospitalBedsByRequestedTime, casesByrequestedTime, casesForICUByRequestedTime, \
              casesForVentilatorsByRequestedTime, dollarsInFlight, scurrentlyInfected, sinfectionByrequestedTime, \
              shospitalBedsByRequestedTime, scasesByrequestedTime, \
              scasesForICUByRequestedTime, scasesForVentilatorsByRequestedTime, sdollarsInFlight, periodType):
 
    print(str(region) + " has " + str(reportedCases) + " reported cases \n ")
    print("There are likely to be " + str(currentlyInfected) + " currently infected person(s) in " + str(region) + "\n")
    print("There are also likely to be " + str(scurrentlyInfected) + " unreported cases in " + str(region) + "\n ")
    print(str(infectionByrequestedTime) + " person(s) are likely to be infected in 28 days from now. \n ")
    print(str(
        sinfectionByrequestedTime) + " person(s) are likely to be infected in 28 days from now considering unreported cases. \n ")
 
    print(str(scasesByrequestedTime) + " severe cases are likely to require Hospitals. \n ")
    
    if (int(shospitalBedsByRequestedTime) < 350):
        bedneeded = 350 - shospitalBedsByRequestedTime
        amountofbed = "There are not enough Beds, and we need " + str(bedneeded) + " more Beds"
    elif (int(shospitalBedsByRequestedTime) > 350):
        amountofbed = "There are enough Beds"
    elif (int(shospitalBedsByRequestedTime) < 0):
        amountofbed = "Were fucked"
    print("We have " + str(shospitalBedsByRequestedTime) + " amount of Beds, " + str(amountofbed) + " \n ")
 
    
 
    print(str(casesForICUByRequestedTime) + " person(s) are likely to require ICU \n ")
    print(str(scasesForICUByRequestedTime) + " person(s) are likely to require ICU considering unreported cases \n ")
 
    
 
    if (int(casesForVentilatorsByRequestedTime) < 350):
        ventneeded = 350 - scasesForICUByRequestedTime
        ventilator = "There are not enough Ventilators, and we need " + str(ventneeded) + " more Ventilators."
 
    elif (int(casesForVentilatorsByRequestedTime) > 350):
        ventilator = "There are enough Ventilators."
 
    elif (int(casesForVentilatorsByRequestedTime) == 0.0):
        ventilator = "Were soooo fucked"
 
    print("We have " + str(casesForVentilatorsByRequestedTime) + " amount of Ventilators, " + ventilator + " \n ")
 
    print("The Economy of " + str(region) + " is likely to lose " "$ daily in " +  str(sdollarsInFlight) +  \
          str(timeToElapse) + str(periodType))
 
 

 
'''main function to assign variables'''

def main():
    region, aveAge, avgDailyIncomeInUSD, reportedCases, avgDailyIncomePopulation, population, \
    totalHospitalBeds, timeToElapse, periodType = data()
 
    #impact
    currentlyInfected, infectionByrequestedTime, hospitalBedsByRequestedTime, casesByrequestedTime, \
    casesForICUByRequestedTime, casesForVentilatorsByRequestedTime, dollarsInFlight = impact(region, aveAge, \
                             avgDailyIncomeInUSD,
                             reportedCases,
                             avgDailyIncomePopulation,
                             population, \
                             totalHospitalBeds,
                             timeToElapse, periodType)
 
    #severe
    scurrentlyInfected, sinfectionByrequestedTime, shospitalBedsByRequestedTime, scasesByrequestedTime, \
    scasesForICUByRequestedTime, scasesForVentilatorsByRequestedTime, sdollarsInFlight = severeImpact(region, aveAge, \
                              avgDailyIncomeInUSD,
                              reportedCases,
                              avgDailyIncomePopulation,
                              population, \
                              totalHospitalBeds,
                              timeToElapse,
                              periodType)
 
    
    estimator(region, aveAge, avgDailyIncomeInUSD, reportedCases, avgDailyIncomePopulation, population, \
              totalHospitalBeds, timeToElapse, currentlyInfected, infectionByrequestedTime, \
              hospitalBedsByRequestedTime, casesByrequestedTime, casesForICUByRequestedTime, \
              casesForVentilatorsByRequestedTime, dollarsInFlight, scurrentlyInfected, sinfectionByrequestedTime, \
              shospitalBedsByRequestedTime, scasesByrequestedTime, \
              scasesForICUByRequestedTime, scasesForVentilatorsByRequestedTime, sdollarsInFlight, periodType)
 
 
main()