# Game tracker
## An online application for tracking, monitoring statistics and viewing information about games
### Functional requirements
- **Registration and authorization**
   - As a new user, I want to be able to register an account by providing a username, email, and password
   - As a registered user, I want to be able to log into my account using my username/email and password
- **Search**
   - As a user, I want to be able to search for games by title, genre, or platform
   - As a user, I want to be able to filter games by genre and platform
   - As a user, I want to be able to sort games by title, release date, or rating
- **User game lists**
   - As a user, I want to be able to create a new game lists
   - As a user, I want to be able to add games to my lists
   - As a user, I want to be able to view and edit my game lists
- **Revisiting the news**
   - As a user, I want to be able to view a list of news related to games
- **Reviews and ratings**
   - As a user, I want to be able to leave reviews and ratings for games
   - As a user, I want to be able to view other users' reviews and ratings for games
- **User profile**
   - As a user, I want to be able to view my profile, which includes my game lists and reviews
   - As a user, I want to be able to edit my profile information
- **Administration**
  - As an administrator, I want to be able to add, edit, and delete games, genres, platforms, and news
  - As an administrator, I want to be able to manage users (e.g., block, delete)

### System behaviours

1. **User Management**
    - Register a new user account.
    - Login a user.
    - Logout a user.
    - View user profile details and activity.
    - Edit user profile information.

2. **Game Information**
    - Get detailed information about a specific game.
    - Search for games based on title, genre, or platform.
    - View a list of all games or filtered by genre/platform.

3. **User Game Lists**
    - Add a game to a user's list (completed, playing, abandoned, plan to play).
    - Remove a game from a user's list.
    - View a user's game lists.
    - Update the status of games in a user's list.

4. **Reviews and Ratings**
    - Create a new review for a game.
    - Update an existing review.
    - Remove a review.
    - Read reviews for a specific game.

5. **News**
    - Read news articles related to games.
    - Search for news articles by keyword or game.

### REST API endpoints

| Endpoint                              | Method | Description                              |
|---------------------------------------|--------|------------------------------------------|
| /api/users/register                   | POST   | Register a new user                      |
| /api/users/login                      | POST   | Login a user                             |
| /api/users/logout                     | POST   | Logout a user                            |
| /api/users/{userId}                   | GET    | Get user profile details                 |
| /api/users/{userId}                   | PUT    | Update user profile                      |
| /api/games/{gameId}                   | GET    | Get game details                         |
| /api/games/search                     | GET    | Search for games                         |
| /api/games                            | GET    | Get a list of games (with optional filters) |
| /api/users/{userId}/gamelists         | GET    | Get a user's game lists                  |
| /api/users/{userId}/gamelists/{gameId}| POST   | Add a game to a user's list              |
| /api/users/{userId}/gamelists/{gameId}| DELETE | Remove a game from a user's list         |
| /api/reviews                          | POST   | Submit a review for a game               |
| /api/reviews/{reviewId}               | PUT    | Update a review                          |
| /api/reviews/{reviewId}               | DELETE | Delete a review                          |
| /api/games/{gameId}/reviews           | GET    | Get reviews for a game                   |
| /api/news                             | GET    | Get news articles (with optional filters)|
| /api/news/search                      | GET    | Search for news articles                 |

