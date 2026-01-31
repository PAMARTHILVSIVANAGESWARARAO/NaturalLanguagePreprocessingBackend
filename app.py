from flask import Flask, request, jsonify
from collections import Counter
import math

app = Flask(__name__)

def tokenize(sentence):
    return ["<s>"] + sentence.split()

def unigram_func(sentence):
    tokens = tokenize(sentence)
    unigram = Counter(tokens)
    total = sum(unigram.values())

    probs = [f"P({w})" for w in tokens]
    return {"unigram": probs}

def bigram_func(sentence):
    tokens = tokenize(sentence)
    unigram = Counter(tokens)
    bigram = Counter(zip(tokens[:-1], tokens[1:]))

    probs = ["P(<s>)"]
    for i in range(1, len(tokens)):
        probs.append(f"P({tokens[i]}|{tokens[i-1]})")

    return {"bigram": probs}

def trigram_func(sentence):
    tokens = tokenize(sentence)
    probs = ["P(<s>)"]

    for i in range(2, len(tokens)):
        probs.append(f"P({tokens[i]}|{tokens[i-2]},{tokens[i-1]})")

    return {"trigram": probs}

def fourgram_func(sentence):
    tokens = tokenize(sentence)
    probs = ["P(<s>)"]

    for i in range(3, len(tokens)):
        probs.append(f"P({tokens[i]}|{tokens[i-3]},{tokens[i-2]},{tokens[i-1]})")

    return {"fourgram": probs}

def perplexity_func(sentence):
    tokens = tokenize(sentence)
    unigram = Counter(tokens)
    bigram = Counter(zip(tokens[:-1], tokens[1:]))

    V = len(unigram)
    log_prob = 0
    N = 0

    for i in range(1, len(tokens)):
        prob = (bigram[(tokens[i-1], tokens[i])] + 1) / (unigram[(tokens[i-1],)] + V)
        log_prob += math.log(prob)
        N += 1

    ppl = math.exp(-log_prob / N)
    return {"perplexity": ppl}

@app.route("/unigram", methods=["POST"])
def unigram_route():
    sentence = request.json["sentence"]
    return jsonify(unigram_func(sentence))

@app.route("/bigram", methods=["POST"])
def bigram_route():
    sentence = request.json["sentence"]
    return jsonify(bigram_func(sentence))

@app.route("/trigram", methods=["POST"])
def trigram_route():
    sentence = request.json["sentence"]
    return jsonify(trigram_func(sentence))

@app.route("/fourgram", methods=["POST"])
def fourgram_route():
    sentence = request.json["sentence"]
    return jsonify(fourgram_func(sentence))

@app.route("/perplexity", methods=["POST"])
def perplexity_route():
    sentence = request.json["sentence"]
    return jsonify(perplexity_func(sentence))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
