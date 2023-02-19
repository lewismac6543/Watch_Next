import spacy

# Loading the language model
nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):

    # Read the movies file
    with open('movies.txt', 'r') as file:
        movies = file.read().splitlines()

    # Split each line into the movie title and description
    movie_titles = []
    movie_descriptions = []
    for movie in movies:
        title, desc = movie.split(" :")
        movie_titles.append(title)
        movie_descriptions.append(desc)

    # Calculating the similarity between the inputted description and each movie description
    similarity_scores = []
    for movie_description in movie_descriptions:
        doc1 = nlp(description)
        doc2 = nlp(movie_description)
        similarity_scores.append(doc1.similarity(doc2))

    # Find the movie with the highest similarity score
    max_index = similarity_scores.index(max(similarity_scores))
    
    # Return the movie title with the highest similarity score
    return movie_titles[max_index]

# Setting the description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Calling the function
next_movie = find_similar_movie(description)

# Outputting the result of the function
print(next_movie)