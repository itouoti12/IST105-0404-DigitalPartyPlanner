import sys

party_dic = {
  "20" :"Cake",
  "21" :"Balloons",
  "10" :"Music System",
  "5" :"Lights",
  "8" :"Catering Service",
  "3" :"DJ",
  "15" :"Photo Booth",
  "7" :"Tables",
  "12" :"Chairs",
  "6" :"Drinks",
  "9" :"Party Hats",
  "18" :"Streamers",
  "4" :"Invitation Cards",
  "2" :"Party Games",
  "11" :"Cleaning Service",
}

def calc_base_party_code(partyItemList):
    partyCode = int(partyItemList[0])
    for idx,partyItem in enumerate(partyItemList):
        if idx == 0:
            continue
        partyCode = partyCode & int(partyItem)
    return partyCode

def adjust_party_code(basePartyCode):
    adjustedPartyCode = basePartyCode
    formula =""
    message = "Chill vibes only!"
    if basePartyCode == 0:
        adjustedPartyCode = adjustedPartyCode + 5
        formula = f"{adjustedPartyCode} + 5"
        message = "Epic Party Incoming!"
    elif basePartyCode > 5:
        adjustedPartyCode = adjustedPartyCode -2
        formula = f"{adjustedPartyCode} - 2"
        message = "Let's keep it classy!"

    return adjustedPartyCode, message, formula

def show_party_items():
    print("<div>0: Cake</div>")
    print("<div>1: Balloons</div>")
    print("<div>2: Music System</div>")
    print("<div>3: Lights</div>")
    print("<div>4: Catering Service</div>")
    print("<div>5: DJ</div>")
    print("<div>6: Photo Booth</div>")
    print("<div>7: Tables</div>")
    print("<div>8: Chairs</div>")
    print("<div>9: Drinks</div>")
    print("<div>10: Party Hats</div>")
    print("<div>11: Streamers</div>")
    print("<div>12: Invitation Cards</div>")
    print("<div>13: Party Games</div>")
    print("<div>14: Cleaning Service</div>")


def getSelectedItemNames(partyItemList):
    selectedList = []
    for itemCode in partyItemList:
        item = party_dic.get(itemCode)
        selectedList.append(item)
    
    return ",".join(selectedList)



def main():
    partyItemCsv = sys.argv[1] #10,30,3,....
    partyItemList = partyItemCsv.split(",")
    if len(partyItemList) == 0:
        print("<h2>Please select party item options.</h2>")
    else:
        print("<h2>Available Party Items:</h2>")
        print("<br/>")
        show_party_items()
        print("<br/>")
        print(f"<strong>Enter item indices separated by commas(e.g.,0,2):{partyItemCsv}</strong>")
        print("<br/>")
        selectedItems = getSelectedItemNames(partyItemList=partyItemList)
        print(f"<strong>Selected Items:</strong>{selectedItems}")
        print("<br/>")
        basePartyCode = calc_base_party_code(partyItemList=partyItemList)
        print(f"<strong>Base Party Code:</strong>{'&'.join(partyItemList)} = {basePartyCode}")
        print("<br/>")
        adjustedPartyCode, message, formula = adjust_party_code(basePartyCode=basePartyCode)
        print(f"<strong>Adjusted Code:</strong>{formula} = {adjustedPartyCode}")
        print("<br/>")
        print(f"<strong>Final Party Code:</strong>{adjustedPartyCode}")
        print("<br/>")

        print(f"<strong>Message:{message}</strong>")
        print("<br/>")






main()
