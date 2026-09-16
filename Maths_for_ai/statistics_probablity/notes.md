# Statistics & Probability Notes

Foundational math for understanding data, uncertainty, and algorithms like Naive Bayes.

---

## 1. Descriptive Statistics

### Mean (average)
Sum of all values, divided by count.

$$
\text{mean} = \frac{\sum \text{values}}{\text{count}}
$$

Example: `[4, 8, 6, 10, 2]` → `(4+8+6+10+2)/5 = 6`

### Median
The middle value when data is sorted. More robust to outliers than the mean.

Example: sorted `[2, 4, 6, 8, 10]` → median = `6`

**Why it matters:** adding an extreme outlier (e.g. `1000`) barely moves the median, but drags the mean way up. This is why things like "median household income" use median, not mean.

### Mode
The most frequently occurring value.

Example: `[1, 2, 2, 3, 4]` → mode = `2`

### Variance
How spread out the data is from the mean. Steps: distance from mean → square it → average the squares.

$$
\text{variance} = \frac{\sum (x - \text{mean})^2}{\text{count}}
$$

Example: `[4, 8, 6, 10, 2]`, mean = 6
- differences: `-2, 2, 0, 4, -4`
- squared: `4, 4, 0, 16, 16`
- variance = `(4+4+0+16+16)/5 = 8`

### Standard Deviation
Square root of variance — brings the units back to match the original data (variance's squaring makes units meaningless, e.g. "dollars squared").

$$
\text{std\_dev} = \sqrt{\text{variance}}
$$

Example: `√8 ≈ 2.83`

**Why it matters for ML:** feature scaling/normalization uses standard deviation so no feature dominates a model just because its raw numbers are bigger (e.g. "house price in dollars" vs "number of bedrooms").

---

## 2. Probability Basics

$$
P(\text{event}) = \frac{\text{favorable outcomes}}{\text{total outcomes}}
$$

Example: rolling a die
- `P(rolling a 4) = 1/6`
- `P(rolling even) = 3/6 = 0.5`

### Independent events (AND)
Events that don't affect each other — multiply their probabilities.

$$
P(A \text{ and } B) = P(A) \times P(B)
$$

Example: `P(heads, heads) = 0.5 × 0.5 = 0.25`

### Conditional Probability
Probability of A, **given** B already happened. Written `P(A|B)`.

The "given" changes what's actually being measured — e.g. P(likes coffee | is a programmer) is a different, more specific question than P(likes coffee) in general.

---

## 3. Bayes' Theorem

Flips a known conditional probability around to answer the question you actually care about.

$$
P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}
$$

**Example — spam detection:**
- `P(spam) = 0.20` (20% of all emails are spam)
- `P("free" | spam) = 0.60` (60% of spam contains "free")
- `P("free") = 0.15` (15% of all emails contain "free")

$$
P(\text{spam} \mid \text{"free"}) = \frac{0.60 \times 0.20}{0.15} = 0.80
$$

80% chance an email is spam, given it contains "free."

**Why it matters:** this exact mechanic — updating a belief based on new evidence — is the entire foundation of the **Naive Bayes** classifier (Month 3, supervised learning).

---

## 4. Probability Distributions

- **Normal distribution (bell curve):** values cluster around the mean, tapering off symmetrically. Common in real-world data — heights, test scores, measurement error.
- **Binomial distribution:** models number of successes across a fixed number of yes/no trials (e.g. "how many heads in 10 coin flips").

Don't need to memorize formulas yet — recognizing the shape and knowing when each applies is enough for now. Gets more concrete once plotting real data in Matplotlib/Seaborn.

---

## 5. Central Limit Theorem (CLT)

**Claim:** take many random samples from *any* population (even a non-normal one), calculate the mean of each sample — the distribution of those sample means approximates a **normal distribution**, given a large enough sample size (commonly 30+).

**Example:** a single die roll is uniformly distributed (1–6, all equally likely) — not normal at all. But:
1. Roll the die 30 times, average those 30 rolls → one "sample mean"
2. Repeat many times → many sample means
3. Plot all the sample means → this plot looks like a bell curve

**Why it matters for ML:** it's the theoretical backbone behind confidence intervals, bootstrapping, and statistical tests working reliably even on messy, non-normal real-world data.

---

## Common Mistakes to Watch For

- Confusing `P(A|B)` with `P(B|A)` — these are NOT the same thing. (This mix-up is exactly what Bayes' theorem exists to correct for.)
- Forgetting that probabilities change on subsequent draws when sampling **without replacement** (e.g. picking balls from a bag — the total count shrinks after each draw).
- Using mean when median would better represent data that has outliers.
- Treating variance and standard deviation as interchangeable — variance's units are squared and not intuitively meaningful; std dev is the one you usually want to *interpret*.

---

## Still to Come

- Formal probability distribution formulas (PDF/CDF) — as needed later
- Hypothesis testing, p-values, confidence intervals — likely to resurface during model evaluation