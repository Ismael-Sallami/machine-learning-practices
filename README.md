# machine-learning-practices

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-F7931E)
![Keras](https://img.shields.io/badge/Keras-3-D00000)
[![checks](https://img.shields.io/github/actions/workflow/status/Ismael-Sallami/machine-learning-practices/ci.yml?branch=main&logo=github&label=checks)](https://github.com/Ismael-Sallami/machine-learning-practices/actions/workflows/ci.yml)
![license](https://img.shields.io/badge/license-MIT-4c1)

Four notebooks that go from a logistic regression to a sequence-to-sequence chatbot, each
one explaining why the model was chosen before showing that it works.

## Context

Coursework for **Aprendizaje Automático**, year 4 of the double degree in Computer Science
and Business Administration, University of Granada (2025-26). The three practices are solo
work; the final project is joint work with **Jesús Rodríguez González**.

## The problem

Each practice picks a family of methods and asks the same thing: choose a model, justify the
choice, tune it and measure it honestly. The interesting part is not fitting the model, it is
deciding what counts as a good result for each kind of problem, which is different when
labels exist, when they do not, and when the input is a sequence.

## The solution

| Notebook | Problem | What it uses |
| --- | --- | --- |
| `practice-1-supervised-learning` | Classification with labels | Logistic regression, k-nearest neighbours, SVM and random forest, compared after a `GridSearchCV` and a proper train/test split |
| `practice-2-unsupervised-learning` | Structure without labels | K-Means and DBSCAN for clustering, Apriori and FP-Growth for association rules |
| `practice-3-deep-learning` | Images and text | A Keras network on MNIST, and sentiment analysis on the IMDB reviews |
| `project-seq2seq-chatbot` | Conversation | An encoder-decoder with LSTM, trained to answer rather than to classify |

The notebooks are mostly prose: 63 markdown cells against 17 of code in the first one, 92
against 27 in the second. That ratio is deliberate. The code that fits a model is four lines;
the part worth keeping is why that model and what the numbers mean.

## Layout

```
src/     the four notebooks, one per practice and one for the project
docs/    the notes handed in with the first two practices
tools/   the check the CI runs
```

## Requirements

- Python 3.12, `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `mlxtend` and `keras`.
- The notebooks were written for Google Colab and run there without installing anything.

## Build and run

```bash
jupyter lab src/practice-1-supervised-learning.ipynb
```

Or open any of them in Colab. The datasets come from the libraries themselves —
`keras.datasets.imdb`, `keras.datasets.mnist`— or are downloaded by the notebook, so there
is no data directory to prepare.

What runs without the datasets is the check:

```bash
python3 tools/check-notebooks.py
```

## Results

The CI output on every push:

```
ok    src/practice-1-supervised-learning.ipynb: 80 cells, 17 of them code
ok    src/practice-2-unsupervised-learning.ipynb: 119 cells, 27 of them code
ok    src/practice-3-deep-learning.ipynb: 45 cells, 12 of them code
ok    src/project-seq2seq-chatbot.ipynb: 29 cells, 9 of them code

4 notebooks are valid and their code parses
```

Every notebook keeps its outputs, so the metrics, the confusion matrices and the plots are
visible on GitHub without running anything.

## What I learned

- The metric is part of the modelling. Accuracy on an unbalanced problem, or the silhouette
  of a clustering nobody can interpret, are numbers that look like results and are not.
- Deep learning did not replace the earlier practices, it changed the questions. On tabular
  data a random forest with a grid search was still the thing to beat.
- **Limitations:**
  - The notebooks cannot be executed in the CI: their datasets are downloaded at runtime and
    training the chatbot needs a GPU. The check validates the file and parses every code
    cell, and the badge says `checks`, not `tests`.
  - Outputs are committed, which is what makes them readable on GitHub and also what makes
    the diffs unreadable. It is a trade, and the reader won.
  - Text and comments are in Spanish.

## Author and licence

Ismael Sallami Moreno. The final project is joint work with Jesús Rodríguez González.
Released under the MIT licence (see `LICENSE`).
