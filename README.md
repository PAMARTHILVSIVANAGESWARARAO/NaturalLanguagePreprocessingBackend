# N-Gram Flask API

Simple Flask-based REST API to generate **Unigram, Bigram, Trigram, 4-gram** representations and **Perplexity** for a given sentence.

---

## Base URL


Api Link :- "https://naturallanguagepreprocessingbackend.onrender.com"


---

## API Status

| Route | Method | Input (JSON) | Description |
|------|--------|-------------|-------------|
| `/` | GET | — | Health check – confirms API is running |
| `/unigram` | POST | `{ "sentence": "text" }` | Unigram probability chain |
| `/bigram` | POST | `{ "sentence": "text" }` | Bigram probability chain |
| `/trigram` | POST | `{ "sentence": "text" }` | Trigram probability chain |
| `/fourgram` | POST | `{ "sentence": "text" }` | 4-gram probability chain |
| `/perplexity` | POST | `{ "sentence": "text" }` | Perplexity value |


**Response**
```json
{
  "message": "API is running"
}
