OutC = [['A', 'B', 'C', 'D', 'E'],# 0 -> 5
               #0    1    2    3    4
               ['F', 'G', 'H', 'I', 'J'],# 1 -> 5
               #0    1     2    3   4
               ['K', 'L', 'M', 'N', 'O'],# 2 ->5
               #0    1     2    3     4
               ['P', 'Q', 'R', 'S', 'T'],# 3 ->5
               #0    1     2    3    4
               ['U', 'V', 'W', 'X', 'Y']# 4 -> 5
               #0     1     2     3    4
               ]# 5 -> 1
               #0
               
InnC = [['A', 'B', 'C', 'D', 'E'],# 0 -> 5
               ['F', 'G', 'H', 'I', 'J'],# 1 -> 5
               ['K', 'L', 'M', 'N', 'O'],# 2 ->5
               ['P', 'Q', 'R', 'S', 'T'],# 3 ->5
               ['U', 'V', 'W', 'X', 'Y']# 4 -> 5
               ]# 5 -> 1
EndPoint = "Z"                
PointE = OutC[0][0]
SavSecuPoint = [PointE]
#		ENCRYPTION
def indexSearchSecKey(K , arr):
	if isinstance(K , str):
		for i in range(len(arr)):
		    for j in range(len(arr[i])):
		    	if arr[i][j] == K:
				    return i , j
				    
	elif isinstance(K , int):
		limit = 0
		for i in range(len(arr)):
			for j in range(len(arr[i])):
				if K == limit:
					return arr[i][j]
				limit+=1
					
def checkKey(K):
		if K <= 25:
			if K == 25:
				SavSecuPoint.append(EndPoint)
				return SavSecuPoint
			else:
				SavSecuPoint.append(indexSearchSecKey(K , InnC))
				return SavSecuPoint

def ModifyArr(K , savPoint , arr):
	ModifyArrT = []
	StanderdArr = []
	limit = K
	Restof = 26 - limit
	St = 1
	sav = 0
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			#print(arr[i][j])
			if savPoint[1] == arr[i][j]:
				sav+=1
				ModifyArrT.append(arr[i][j])
				continue
				
			if savPoint[1] != arr[i][j] and sav == 0:
				StanderdArr.append(arr[i][j])
				
			if sav <= Restof and sav == 1:
				ModifyArrT.append(arr[i][j])
	#print(StanderdArr)	
	ModifyArrT.append('Z')
	for i in range(len(StanderdArr)):
		ModifyArrT.append(StanderdArr[i])
	return ModifyArrT
	
def StanderdArray(Arr):
	res = []
	for i in range(len(Arr)):
		   for j in range(len(Arr[i])):
				  res.append(Arr[i][j])
	res.append('Z')
	return res

def SCStr(str1 , K):
	lest = []
	for i in range(len(str1)):
		if str1[i] == " ":
			continue
		else:
			lest.append(str1[i])
	Encrypt = ""
	stand = StanderdArray(OutC)
	mod = ModifyArr(K , SavSecuPoint,OutC)
	for le in range(len(lest)):
		for st in range(len(stand)):
			for mo in range(len(mod)):
				if lest[le] == stand[st] and stand.index(stand[st]) == mod.index(mod[mo]):
					Encrypt += mod[mo]
				
	return Encrypt

#		DECRYPTION
def SDCStr(str1 , K):
	lest = []
	for i in range(len(str1)):
		if str1[i] == " ":
			continue
		else:
			lest.append(str1[i])
		
	Dencrypt = ""
	stand = StanderdArray(OutC)
	mod = ModifyArr(K , SavSecuPoint,OutC)
	for le in range(len(lest)):
		for mo in range(len(mod)):
			for st in range(len(stand)):
				if lest[le] == mod[st] and stand.index(stand[st]) == mod.index(mod[mo]):
					Dencrypt += stand[st]
				
	return Dencrypt
#		STRUCTER FLOW IPUML
def theMainList():
	print("[1] Encrypt Message")
	print("[2] Decrypt Message")
	print("[3] Exit")
	try:
		cho = int(input("choice: "))
		if isinstance(cho , int) or cho <= 3 and cho >= 1:
			return cho
	except:
		print("Error in your choice please, Don't enter string letters, Enter Integer number only..\n")
		theMainList()

def ifErr():
	while(True):
		con = theMainList()
		if con == 1:
			encryptFlow()
		elif con == 2:
			decryptFlow()
		elif con == 3:
			exit()
		else:
			print("Error in your choice please,s Choice another one between 1 to 3.\n")
			ifErr()

def decryptFlow():
	try:
		Message = str(input("Enter The Encrypted Message: "))
		Key = int(input("Enter Message Security Key(0 to 25): "))
		if isinstance(Key , int):
			print("Security Key: " ,checkKey(Key) )
			print(ModifyArr(Key , SavSecuPoint,OutC))
			print("\nYour Message Has Decrypted:-> " , SDCStr(Message.upper() , Key) , "\n")
	except:
		print("Please Enter Integer Number Only For Your Security Key.\n")
		ifErr()
	print("------------------------------------------------------------------------------\n")

def encryptFlow():
	try:
		Key = int(input("Enter Security Key(0 to 25): "))
		if isinstance(Key , int) and Key >= 0 and Key <= 25 :
			print("Security Key: " ,checkKey(Key) )
			print(ModifyArr(Key , SavSecuPoint,OutC))
			writeM = str(input("Enter your message for encryption: "))
			print("\nYour Message Has Encrypted:-> " , SCStr(writeM.upper() , Key) , "\n")
	except:
		print("Please Enter Integer Number Only For Your Security Key.\n")
		ifErr()
	print("------------------------------------------------------------------------------\n")

def main():
	print("-----------------------------THE CIPHER WHEEL PROGRAME-----------------------------")
	print("Letters: " , StanderdArray(OutC) , " :Your Wheel")
	print("-----------------------------------------------------------------------------------")
	UsActive = input("Enter Y/y To Start (OR N/n To Exit):")
	#             START PROGRAM
	if UsActive == "Y" or UsActive == "y" or UsActive == "yes" or UsActive == "YES" or UsActive == "Yes" or UsActive == "yES" or UsActive == "yEs" or UsActive == "yeS":
		while(True):
			con = theMainList()
			if con == 1:
				encryptFlow()
			elif con == 2:
				decryptFlow()
			elif con == 3:
				exit()
			
		
	#             END PROGRAM
	elif UsActive == "N" or UsActive == "n" or UsActive == "no" or UsActive == "NO" or UsActive == "No"or UsActive == "nO":
		exit()
	
	else:
		print("Please Enter Y/y Or N/n To Know What You Want?.\n")
		main()


main()