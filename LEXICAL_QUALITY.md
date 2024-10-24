# Lexical quality

This is a quick overview of the work I've done today for the Lemon AI coding task. Given the time constraints, I've prioritised getting _something_ done even if it fell short of the deliverables.

## Decisions
Here is a list of decisions I've made:
- First and foremost, my notion of lexical quality only takes spelling into account. I thought it would be better to get this done end-to-end than to spend lots of time including other metrics.
    - It shouldn't be hard to add other metrics (grammatical correctness, readability, coherence). They would all go in the same place, namely [`lexical_quality.py`](./cleanlab/lexical_quality.py), and this wouldn't alter the overall flow of the feature.
- I decided not to create a sample dataset to demonstrate the solution.
    - This is because after implementing the example from the docs it became apparent that even before making any changes the Cleanlab model wasn't reliably outperforming the original model, so it would be very hard to demonstrate that my changes were any better than doing nothing at all. So there is no markdown report.
- Loads more tests need adding; I only added [a few simple unit tests](tests/test_lexical_quality.py) that sense-check the lexical quality calculations.

## How to run this
- Follow the instructions in `DEVELOPMENT.md` to set up your environment. I've added one small package to `requirements-dev.txt` (namely `pyspellchecker`); the instructions covered in `DEVELOPMENT.md` will ensure that this is installed alongside all other packages.
- With the `venv` activated, run `python playground.py`.


