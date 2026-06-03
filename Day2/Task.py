movies = {
    "Vijay": ["Ghilli", "Thuppakki", "Mersal", "Master", "Leo", "Pokkiri", "Kaththi", "Bigil", "Theri", "Sarkar"],

    "Ajith": ["Mankatha", "Billa", "Viswasam", "Veeram", "Vedalam",  "Aarambam", "Yennai Arindhaal", "Citizen", "Thunivu", "Valimai"],

    "Rajinikanth": ["Baasha", "Sivaji", "Enthiran", "Jailer", "Padayappa", "Annamalai", "Kabali", "Petta", "Muthu", "Chandramukhi"],

    "Suriya": ["Ghajini", "Vaaranam Aayiram", "Singam", "Ayan", "Soorarai Pottru", "Jai Bhim", "24", "Kaakha Kaakha", "Vel", "Pasanga 2"],

    "Dhanush": ["Asuran", "VIP", "Karnan", "Thiruchitrambalam", "Polladhavan", "Aadukalam", "Maari", "Velaiilla Pattadhari", "Captain Miller", "Raayan"],

    "Sivakarthikeyan": ["Doctor", "Don", "Amaran", "Remo", "Maaveeran", "Ethir Neechal", "Rajini Murugan", "Namma Veettu Pillai", "Varuthapadatha Valibar Sangam", "Kedi Billa Killadi Ranga"]
}

top_x = int(input("Please enter top x number (1-10): "))
actor = input("Please enter the actor name: ")

if actor in movies and 1 <= top_x <= 10:
    print(f"\nHere are the top {top_x} super hit movies of {actor}")

    for i in range(top_x):
        print(f"{i+1}. {movies[actor][i]}")
else:
    print("Invalid actor name or number")

# Output 
Please enter top x number (1-10): 7
Please enter the actor name: Suriya

Here are the top 7 super hit movies of Suriya
1. Ghajini
2. Vaaranam Aayiram
3. Singam
4. Ayan
5. Soorarai Pottru
6. Jai Bhim
7. 24
PS C:\Users\Saindhavi\Desktop\Intern> 
