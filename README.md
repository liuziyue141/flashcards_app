# LIGN101 Flashcard Study Assistant

## Overview
A Django-based flashcard application specifically designed for UCSD's LIGN101 students. This interactive study tool combines traditional spaced repetition learning with AI-powered study recommendations, helping students master linguistics concepts more effectively.

## Features
- **Topic-Based Flashcards**: Organized sets of flashcards covering 6 main LIGN101 topics
- **Source Attribution**: Each flashcard includes references to specific lectures and slide numbers
- **Spaced Repetition System**: Uses the Leitner system with 5 boxes for optimal learning
- **Smart Study Planning**: AI-powered study recommendations based on performance
- **Progress Tracking**: Monitor mastery of different topics and concepts
- **Source Verification**: Direct links between flashcard content and course materials

## Technical Implementation
### Frontend
- HTML5
- CSS (Simple.css framework)
- Responsive design for desktop and mobile devices

### Backend
- Django web framework
- SQLite database
- GPT API integration for flashcard generation and study recommendations

### AI Integration
- Custom prompt engineering for accurate content generation
- Data preprocessing of lecture materials
- Intelligent study plan generation based on user performance

## Installation
1. Clone the repository
```bash
git clone [repository-url]
cd lign101-flashcards
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up the database
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

## Usage
1. Navigate to the homepage
2. Select a linguistics topic
3. Study flashcards using the spaced repetition system
4. Mark cards as "Known" or "Need Review"
5. Request personalized study recommendations based on performance

## Project Development
- Based on Real Python's flashcard tutorial
- Enhanced with custom features for LIGN101 specific needs
- Improved with GPT integration for content generation
- Optimized through:
  - Lecture slide preprocessing
  - Topic-based content organization
  - Advanced prompt engineering techniques

## Contributors
Ziyue Liu Application developer
Samuel Chu Prompt Engineer
Aaryan Agrawal Prompt Engineer

## Acknowledgments
- Real Python for the base flashcard tutorial
- UCSD LIGN101 course materials
- OpenAI for GPT API integration
