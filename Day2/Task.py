def get_movies(actor):
    movies = {
        "Vijay": ["Ghilli", "Thuppakki", "Mersal", "Master", "Leo", "Pokkiri", "Kaththi", "Sarkar", "Bigil", "Theri"],

        "Ajith": ["Mankatha", "Billa", "Viswasam", "Veeram", "Yennai Arindhaal", "Valimai", "Vedalam", "Aarambam", "Thunivu", "Citizen"],

        "Rajinikanth": ["Baasha", "Sivaji", "Enthiran", "Jailer", "Padayappa", "Annamalai", "Kabali", "Petta", "Muthu", "Chandramukhi"],

        "Suriya": ["Ghajini", "Vaaranam Aayiram", "Singam", "Ayan", "Soorarai Pottru", "Jai Bhim", "24", "Kaakha Kaakha", "Vel", "Pasanga 2"],

        "Dhanush": ["Asuran", "VIP", "Karnan", "Thiruchitrambalam", "Polladhavan", "Aadukalam", "Maari", "Velaiilla Pattadhari", "Captain Miller", "Raayan"],

        "Sivakarthikeyan": ["Doctor", "Don", "Amaran", "Remo", "Varuthapadatha Valibar Sangam", "Ethir Neechal", "Maaveeran", "Rajini Murugan", "Namma Veettu Pillai", "Kedi Billa Killadi Ranga"]
    }

    return movies.get(actor, [])


def print_movies(actor, top_x):
    movie_list = get_movies(actor)

    if not movie_list:
        print("Actor not found!")
        return

    print(f"\nHere are the top {top_x} super hit movies of {actor}")

    for i in range(top_x):
        print(f"{i+1}. {movie_list[i]}")


top_x = int(input("Please enter top x number (1-10): "))

if 1 <= top_x <= 10:
    actor = input("Please enter the actor name: ")
    print_movies(actor, top_x)
else:
    print("Please enter a number between 1 and 10")

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
