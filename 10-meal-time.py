def main():
	current_time = convert(input("Time : "))

	if current_time >= 7 and current_time <= 8:
		print("breakfast time")
	elif current_time >= 12 and current_time <= 13:
		print("lunch time")
	elif current_time >= 18 and current_time <= 19:
		print("dinner time")
	else:
		print("its not eating time")

def convert(time):
	if time.strip()[-1].isdigit():
		time = time.replace(" ", "").split(":")
	
		time[0] = float(time[0])
		time[1] = ((float(time[1])*100)/60)/100
	else:
		half = time.strip()[-4:]
		time = time.replace(" ", "")[:-4].split(":")
	
		time[0] = float(time[0])
		time[1] = ((float(time[1])*100)/60)/100

		if half == "p.m.":
			time[0] += 12
	
	return sum(time)

if __name__ == "__main__":
    main()
