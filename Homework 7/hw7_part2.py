import json
if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
#Collecting User Input
min_year = input("Min year => ").strip()
print(min_year)
max_year = input("Max year => ").strip()
print(max_year)
imdb_w = input("Weight for IMDB => ").strip()
print(imdb_w)
twitter_w = input("Weight for Twitter => ").strip()
print(twitter_w)
genre = input("\n" + "What genre do you want to see? ").strip()
print(genre)
#Creating a list of all genres
genres = ["comedy", "adventure", "action","drama", "romance","crime","action","sci-fi","fantasy","mystery","musical","family","animation","documentary"]
#Creating a while loop for the body of the program to repeat unless stopped by the user
while genre.lower() != "stop" : 
#Appending all movies which fit user specified criteria for time period into a new list movies_in_years
    if genre.lower() in genres : 
        movies_in_years = []
        for i in movies.keys() :
            temp_dict = dict() 
            if movies[i]['movie_year'] >= int(min_year) and movies[i]['movie_year'] <= int(max_year) : 
                temp_dict[i] = movies[i]
                movies_in_years.append(temp_dict)
            
#Appending all movies from user specified time period which fit the genre described into new list genre_spec
        genre_spec = []
        for i in movies_in_years : 
            if genre.lower() == "sci-fi" : 
                genre = "Sci-Fi"
                if genre in list(i.values())[0]['genre'] : 
                    genre_spec.append(i)
            else : 
                if genre.capitalize() in list(i.values())[0]['genre'] : 
                    genre_spec.append(i)
#Calculating and storing all weightings of each movie in list weights and creating a placeholder list meant to link the 
#location of the weight to the movies name
        weights = []
        place_holder_list = []
        for i in genre_spec : 
            for x in i.keys() : 
                imdb_rating = i[x]['rating']
                if x in ratings.keys() :
                    if len(ratings[x]) < 3 : 
                        continue
                    else : 
                        twitter_rating = sum(ratings[x]) / len(ratings[x])
                        weighting_formula = ((float(imdb_w) * imdb_rating) + (float(twitter_w)*twitter_rating))/(float(imdb_w)+float(twitter_w))
                        weights.append(weighting_formula)
                        place_holder_list.append(i)
                else : 
                    continue
#Processing and printing output from weights and place_holder_list
        max_loc = weights.index(max(weights))
        min_loc = weights.index(min(weights))

        print("\n" + "Best:")
        print("       ", "Released in " + str(list(place_holder_list[max_loc].values())[0]['movie_year']) + ", " +  str(list(place_holder_list[max_loc].values())[0]['name']) + " has a rating of " + "{:.2f}".format(max(weights)))
        print("\n" + "Worst:")
        print("       ", "Released in " + str(list(place_holder_list[min_loc].values())[0]['movie_year']) + ", " +  str(list(place_holder_list[min_loc].values())[0]['name']) + " has a rating of " + "{:.2f}".format(min(weights)))
        genre = input("\n" + "What genre do you want to see? ").strip()
        print(genre)
    else : 
        print("\n" + "No " + genre.capitalize() + " movie found in " + str(min_year) + " through " + str(max_year))

        genre = input("\n" + "What genre do you want to see? ").strip()
        print(genre)
        continue
