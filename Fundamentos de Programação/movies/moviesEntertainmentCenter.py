import freshTomatoes
import media

toyStory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toyStory.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.showTrailer()

wonder = media.Movie("Wonder",
                     "portrays a boy with a facial deformity known as treacher Collins",
                     "https://upload.wikimedia.org/wikipedia/pt/f/f1/Wonder_%28filme%29.png",
                     "https://www.youtube.com/watch?v=6g80d7igX0k")
#print(wonder.storyline)
#wonder.showTrailer()

schoolOfRock = media.Movie("School of Rock",
                           "storyline",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "Storyline",
                          "https://vignette.wikia.nocookie.net/disney/images/c/c8/Ratatouille_poster.jpg/revision/latest?cb=20150415014434&path-prefix=pt-br",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnightInParis = media.Movie("Midnight In Paris",
                              "Storyline",
                              "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                              "https://www.youtube.com/watch?v=FAfR8omt-CY")
                              
hungerGames = media.Movie("Hunger Games",
                          "Storyline",
                          "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
                          "https://www.youtube.com/watch?v=FovFG3N_RSU")

#movies = [toyStory, avatar, wonder, schoolOfRock, ratatouille, midnightInParis, hungerGames]
#freshTomatoes.openMoviesPage(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
