# Character-Level Statistical Language Model

> A character-level statistical language model built completely from scratch in Python using N-Grams, Recursive Backoff, Laplace Smoothing, and Trie-based lexical constraints.

This project explores how classical language models worked before the era of Transformers by implementing every major component from scratch. Rather than relying on neural networks, this project predicts text statistically using character-level N-Gram probabilities while enforcing valid English word construction through a Trie.

The goal of this project is educational: to understand how language models generate text, how smoothing techniques affect probability distributions, and how search algorithms interact with statistical models.

---

# Features

- Character-level tokenizer
- Character N-Gram Language Model
- Recursive Backoff for unseen contexts
- Laplace (+1) Smoothing
- Trie-based English dictionary constraints
- Sentence Autocomplete
- Probability-based next-character prediction
- Recursive word generation
- Modular architecture for experimenting with different smoothing algorithms

---

# Project Structure

```
.
├── tokenizer.py          # Character tokenizer and encoding utilities
├── predictor.py          # N-Gram model construction and probability computation
├── ngramPredictor.py     # Recursive Backoff + Trie-based prediction
├── generator_MAIN.py     # Sentence autocomplete interface
├── pdfParser.py          # Corpus generation from PDFs
└── README.md
```

---

# How It Works

The language generation pipeline is:

```
Input Prompt
      │
      ▼
Character Tokenizer
      │
      ▼
N-Gram Probability Model
      │
      ▼
Recursive Backoff
      │
      ▼
Probability Distribution
      │
      ▼
Trie Prefix Validation
      │
      ▼
Autocomplete Suggestions
```

Unlike neural language models, every prediction is computed directly from character frequency statistics collected from the training corpus.

---

# Recursive Backoff

If an exact N-Gram context has never been observed in the corpus, the model recursively reduces the context size.

Example:

```
Predict using:

abcdef

↓

bcdef

↓

cdef

↓

def

↓

ef

↓

f
```

until a known context is found.

This significantly reduces the number of unknown contexts while preserving as much contextual information as possible.

---

# Laplace Smoothing

The current implementation uses Add-One (Laplace) smoothing.

For every character,

```
P(c | context)
=
(count(context,c)+1)
/
(count(context)+V)
```

where

- `count(context,c)` is the number of occurrences of the character after the context
- `count(context)` is the number of occurrences of the context
- `V` is the vocabulary size

---

# Trie-based Lexical Constraints

One limitation of character-level language models is that they often generate invalid words.

To solve this, every predicted character is validated against a Trie built from the English dictionary provided by the `wordfreq` package.

Example:

```
Current Prefix

pyth

↓

Possible Characters

i
o
x
z

↓

Trie Validation

pythi ✓

pytho ✓

pythx ✗

pythz ✗
```

Only valid prefixes continue expanding.

---

# Sentence Autocomplete

Instead of generating unrestricted text, the model currently behaves as a statistical autocomplete engine.

Example

```
Input

The sky is bl

↓

Suggestions

blue
black
blank
```

The full sentence provides contextual information for the N-Gram predictor while only the current word is constrained using the Trie.

---

# Why Character-Level?

Character-level language models

- require no predefined vocabulary
- naturally handle unknown words
- demonstrate how language models work internally
- provide a clean platform for experimenting with smoothing algorithms

Although slower than word-level models, they provide much greater insight into statistical language modeling.

---

# Current Limitations

This project intentionally avoids neural networks.

As a result:

- Fixed context window
- No semantic understanding
- No world knowledge
- No attention mechanism
- No long-term memory
- Slower generation compared to modern LLMs

These limitations are precisely what motivated the development of RNNs, LSTMs, and eventually Transformers.

---

# Future Work

This project is designed to become an experimentation platform for classical language modeling techniques.

Planned additions include:

- Good-Turing Smoothing
- Witten-Bell Smoothing
- Absolute Discounting
- Kneser-Ney Smoothing
- Beam Search
- Perplexity Evaluation
- Probability Visualization
- Search Tree Visualization
- Interactive comparison of smoothing algorithms
- Word-level language models

Ultimately, the goal is to reproduce and visualize the results presented in:

> Stanley F. Chen and Joshua Goodman
>
> "An Empirical Study of Smoothing Techniques for Language Modeling"

---

# Technologies Used

- Python
- wordfreq
- Standard Library

No machine learning frameworks were used.

---

# Learning Objectives

This project explores:

- Statistical Language Modeling
- Character-Level N-Grams
- Probability Estimation
- Recursive Backoff
- Smoothing Techniques
- Trie Data Structures
- Autocomplete Systems
- Classical Natural Language Processing

---

# Example

```
Prompt

Machine lear

↓

Predicted Continuations

learning
learner
learned
```

The model ranks suggestions according to statistical likelihood while ensuring that generated words remain lexically valid.

---

# Motivation

Modern language models such as GPT are built upon decades of research in statistical language modeling.

This project serves as a from-scratch implementation of the classical techniques that preceded neural language models, providing an intuitive understanding of how probability, smoothing, lexical constraints, and search combine to generate text.

Rather than competing with modern LLMs, this project aims to explain why they work.