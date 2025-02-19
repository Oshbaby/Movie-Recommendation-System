# Movie Recommendation System

![Movie Recommender](https://img.shields.io/badge/Streamlit-Web%20App-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![GitHub](https://img.shields.io/badge/GitHub-Open%20Source-success)

Welcome to the **Movie Recommendation System** repository! This project is a web-based movie recommendation system built using **Streamlit** and powered by **Python**. It suggests movies based on user preferences by analyzing movie data and using cosine similarity to find similar movies. The system also fetches movie posters using **The Movie Database (TMDb) API** to provide a visually appealing experience.

---

## Features

- **Movie Selection**: Users can select a movie from a dropdown list.
- **Personalized Recommendations**: The system recommends 5 movies similar to the selected movie.
- **Movie Posters**: Displays movie posters for recommended movies using TMDb API.
- **User-Friendly Interface**: Built with Streamlit for a clean and intuitive UI.

---

## How It Works

1. **Data Preprocessing**:
   - The dataset (`tmdb_5000_movies.csv`) is preprocessed to extract relevant features such as movie titles, genres, keywords, cast, and crew.
   - Text data (e.g., genres, keywords) is cleaned, stemmed, and converted into a format suitable for vectorization.
   - A **CountVectorizer** is used to convert text data into numerical vectors.
   - **Cosine Similarity** is calculated to measure the similarity between movies.

2. **Recommendation Algorithm**:
   - When a user selects a movie, the system identifies the most similar movies based on cosine similarity scores.
   - The top 5 similar movies are recommended to the user.

3. **Poster Fetching**:
   - The system uses the **TMDb API** to fetch movie posters for the recommended movies.

4. **Streamlit Web App**:
   - The web app is built using **Streamlit**, providing an interactive interface for users to select movies and view recommendations.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Pandas
- Scikit-learn
- Requests
- NLTK

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK Data**:
   ```python
   import nltk
   nltk.download('punkt')
   ```

4. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

5. **Access the Web App**:
   - Open your browser and go to `http://localhost:8501`.
   - Select a movie from the dropdown and click **"Show Recommend"** to get personalized movie recommendations.

---

## File Structure

```
movie-recommendation-system/
│
├── app.py                  # Streamlit web application
├── movie_list.pkl          # Pickle file containing movie data
├── similarity.pkl          # Pickle file containing similarity matrix
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── artifacts/              # Directory for storing pickle files (optional)
```



## Screenshots

![Screenshot 1](screenshots![Screenshot 2025-02-19 142306](https://github.com/user-attachments/assets/e520f86c-ad60-4578-bf2c-1a949578d8ad)
*Movie selection and recommendation interface.*

![Screenshot 2](screenshots![Screenshot 2025-02-19 142325](https://github.com/user-attachments/assets/c642310c-a1cb-493f-80a6-f84e9b89893f)

*Recommended movies with posters.*

---

---

## Usage

1. **Select a Movie**:
   - Choose a movie from the dropdown menu.

2. **Get Recommendations**:
   - Click the **"Show Recommend"** button to view the top 5 recommended movies along with their posters.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the web app.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For vectorization and cosine similarity.
- **TMDb API**: For fetching movie posters.
- **NLTK**: For text preprocessing and stemming.

---

## Future Enhancements

- Add user authentication to save preferences.
- Allow users to rate movies and improve recommendations based on user feedback.
- Integrate more advanced recommendation algorithms (e.g., collaborative filtering).
- Add a search bar for easier movie selection.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [The Movie Database (TMDb)](https://www.themoviedb.org/) for providing the API to fetch movie posters.
- [Streamlit](https://streamlit.io/) for making it easy to build interactive web apps.

---

## Contact

For any questions or feedback, feel free to reach out:

- **Name**: [Osho Emmanuel]
- **Email**: [Emmanuel.osho022@]
- **GitHub**: [https://github.com/Oshbaby]

---

Enjoy exploring movies with the **Movie Recommendation System**! 🎥🍿

---



