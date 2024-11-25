# %%
from scipy.stats import linregress
import numpy as np
import math
import openai
import os
import seaborn as sns
import pandas as pd
from itertools import combinations
import matplotlib.pyplot as plt
import re
from datasets import load_dataset
import spacy
from collections import Counter
import itertools
from tqdm import tqdm

# Load the English model in spaCy
nlp = spacy.load("en_core_web_sm")

# Load the dataset in streaming mode
dataset = load_dataset("HuggingFaceFW/fineweb", split='train', streaming=True)

# Parameters
num_data = 3000000  # Adjust this number as needed

# Initialize counters and storage for PII data
pii_counts = Counter()
pii_values = Counter()
pii_counts_per_doc = []
extracted_pii_data = []

# Regex patterns for additional PII types
email_pattern = re.compile(r'\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
phone_pattern = re.compile(
    r'\b(?:\+?(\d{1,3})?[-.\s]?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9}))\b')
ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

# Modify the function to filter out years in the range 1900–2100 for phone numbers

# Function to validate PII entities


def is_valid_pii(entity, entity_type):
    if entity_type == 'PERSON':
        return entity.isalpha() and len(entity) > 1  # Basic name validation
    elif entity_type == 'PHONE_NUMBER':
        # Check if the phone number has at least 7 digits (adjust as needed)
        # Remove non-numeric characters
        digits_only = re.sub(r'\D', '', entity)
        return len(digits_only) >= 7  # Require at least 7 digits to be valid
    elif entity_type == 'EMAIL':
        # Valid email format
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', entity)
    elif entity_type == 'IP_ADDRESS':
        return re.match(r'^\d{1,3}(\.\d{1,3}){3}$', entity)  # Simple IP format
    elif entity_type in ['LOC', 'GPE']:
        # Exclude short numbers, generic codes, etc.
        return entity.isalpha() and len(entity) > 2
    return True


# Processing documents with tqdm
for sample in tqdm(itertools.islice(dataset, num_data), total=num_data, desc="Processing Documents"):
    text = sample['text']
    pii_count_in_doc = 0
    sample_pii = {'text': text, 'extracted_pii': {}}

    # Extract PII using spaCy for names, locations
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'GPE', 'LOC'] and is_valid_pii(ent.text, ent.label_):
            pii_counts[ent.label_] += 1
            pii_values[ent.text] += 1
            pii_count_in_doc += 1
            if ent.label_ not in sample_pii['extracted_pii']:
                sample_pii['extracted_pii'][ent.label_] = []
            sample_pii['extracted_pii'][ent.label_].append(ent.text)

    # Extract PII using regex for emails, phone numbers, IP addresses
    for pattern, label in [(email_pattern, 'EMAIL'), (phone_pattern, 'PHONE_NUMBER'), (ip_pattern, 'IP_ADDRESS')]:
        matches = pattern.findall(text)
        flattened_matches = [''.join(match) if isinstance(
            match, tuple) else match for match in matches]
        for match in flattened_matches:
            if is_valid_pii(match, label):
                pii_counts[label] += 1
                pii_values[match] += 1
                pii_count_in_doc += 1
                if label not in sample_pii['extracted_pii']:
                    sample_pii['extracted_pii'][label] = []
                sample_pii['extracted_pii'][label].append(match)

    pii_counts_per_doc.append(pii_count_in_doc)
    extracted_pii_data.append(sample_pii)

# Metrics and data for visualization
metrics = {
    'PII Counts by Type': pii_counts,
    'Top PII Instances': pii_values.most_common(10),
    'PII Counts per Document': pii_counts_per_doc,
    'Extracted PII Data': extracted_pii_data
}


# %%
# Display extracted PII data (example)
print("\n--- Extracted PII Data (Sample) ---")
# Display first 3 samples
for i, pii_data in enumerate(extracted_pii_data[:3]):
    print(f"Sample {i+1}: {pii_data['extracted_pii']}")

# %% [markdown]
# Visualization

# %%
# Import necessary libraries

# Ensure plots display within the notebook (if using Jupyter)
%matplotlib inline

# Create the output directory if it doesn't exist
os.makedirs('./pics', exist_ok=True)

# Set general plot style for all plots
sns.set(style="whitegrid")

# --- Code starts here ---

# 1. Calculate General Statistics

# Extract PII counts by type from metrics
pii_counts = metrics['PII Counts by Type']

# Convert to a pandas DataFrame for easier plotting
pii_counts_df = pd.DataFrame.from_dict(
    pii_counts, orient='index', columns=['Count']).reset_index()
pii_counts_df.rename(columns={'index': 'PII Type'}, inplace=True)

# Display the DataFrame
print("PII Counts by Type:")
print(pii_counts_df)

# Bar chart for PII counts by type
plt.figure(figsize=(10, 6))
sns.barplot(data=pii_counts_df, x='PII Type', y='Count', palette='Blues_d')
plt.title('Count of Each PII Type Overall', fontsize=18, fontweight='bold')
plt.xlabel('PII Type', fontsize=14)
plt.ylabel('Total Count', fontsize=14)
plt.savefig('./pics/pii_count_by_type.pdf', format='pdf')
plt.show()

# Rate of Each PII Type Occurring Per Document

# Total number of documents processed
total_documents = len(extracted_pii_data)

# Calculate the rate (number of documents containing each PII type divided by total documents)
pii_document_counts = Counter()
for sample in extracted_pii_data:
    for pii_type in sample['extracted_pii'].keys():
        pii_document_counts[pii_type] += 1

# Convert to DataFrame
pii_rate_df = pd.DataFrame.from_dict(pii_document_counts, orient='index', columns=[
                                     'Documents with PII']).reset_index()
pii_rate_df.rename(columns={'index': 'PII Type'}, inplace=True)
pii_rate_df['Rate per Document (%)'] = (
    pii_rate_df['Documents with PII'] / total_documents) * 100

# Display the DataFrame
print("\nRate of Each PII Type Occurring in Documents:")
print(pii_rate_df)

# Bar chart for PII rate per document
plt.figure(figsize=(10, 6))
sns.barplot(data=pii_rate_df, x='PII Type',
            y='Rate per Document (%)', palette='Purples')
plt.title('Rate of Each PII Type Occurring per Document',
          fontsize=18, fontweight='bold')
plt.xlabel('PII Type', fontsize=14)
plt.ylabel('Rate per Document (%)', fontsize=14)
plt.savefig('./pics/pii_rate_per_document.pdf', format='pdf')
plt.show()

# 2. Identify Most Common Individual Entities for Each PII Type

# Initialize a dictionary to hold counts for each PII type
pii_entity_counts = {}

# Iterate over extracted PII data to collect entity counts
for sample in extracted_pii_data:
    for pii_type, entities in sample['extracted_pii'].items():
        if pii_type not in pii_entity_counts:
            pii_entity_counts[pii_type] = Counter()
        pii_entity_counts[pii_type].update(entities)

# For each PII type, get the top 50 entities
top_entities_per_pii = {}
for pii_type, counter in pii_entity_counts.items():
    top_entities_per_pii[pii_type] = counter.most_common(
        50)  # Changed to top 50

# Display the top entities
for pii_type, top_entities in top_entities_per_pii.items():
    print(f"\nTop 50 Entities for PII Type '{pii_type}':")
    for entity, count in top_entities:
        print(f"{entity}: {count}")

# Plotting the top 50 entities for each PII type
valid_palettes = ['Set1', 'Set2', 'Set3', 'Pastel1', 'Pastel2']
for i, (pii_type, top_entities) in enumerate(top_entities_per_pii.items()):
    # Prepare data
    entities, counts = zip(*top_entities)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=list(entities), y=list(counts),
                palette=valid_palettes[i % len(valid_palettes)])
    plt.title(
        f"Top 50 Most Frequent Entities for {pii_type}", fontsize=18, fontweight='bold')
    plt.xlabel(f"{pii_type} Entities", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f'./pics/top_entities_{pii_type.lower()}.pdf', format='pdf')
    plt.show()

# 3. Determine Common PII Type Combinations

# Initialize a Counter for combinations
combination_counts = Counter()

# Iterate over each document to find combinations
for sample in extracted_pii_data:
    pii_types_in_doc = list(sample['extracted_pii'].keys())
    # Generate all possible combinations of PII types in the document
    for r in range(2, len(pii_types_in_doc) + 1):
        for combo in combinations(sorted(pii_types_in_doc), r):
            combination_counts[combo] += 1

# Get the top 10 most frequent combinations
top_combinations = combination_counts.most_common(10)

# Display the top combinations
print("\nTop 10 Most Frequent PII Type Combinations:")
for combo, count in top_combinations:
    print(f"{' + '.join(combo)}: {count}")

# Prepare data
combos, counts = zip(*top_combinations)
combo_labels = [' + '.join(combo) for combo in combos]

plt.figure(figsize=(12, 6))
sns.barplot(x=list(combo_labels), y=list(counts), palette='coolwarm')
plt.title("Top 10 Most Frequent PII Type Combinations",
          fontsize=18, fontweight='bold')
plt.xlabel("PII Type Combinations", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./pics/top_pii_combinations.pdf', format='pdf')
plt.show()


# %%


# %%


# %%


# %%


# %%


# %%


# %%

openai.api_key = 'YOUR_API_KEY'


def get_average_probability(text):
    response = openai.Completion.create(
        model="davinci-002",  # Make sure this model is accessible and appropriate
        prompt=text,
        max_tokens=1,  # To ensure the prompt tokens are processed
        logprobs=5,
        echo=True      # Ensures the input tokens are returned with logprobs
    )

    # Extract log probabilities for input tokens
    logprobs = response['choices'][0]['logprobs']
    token_logprobs = logprobs['token_logprobs']

    # Filter out None values from log probabilities
    valid_logprobs = [lp for lp in token_logprobs if lp is not None]

    if not valid_logprobs:
        return None  # Return None if no valid log probabilities exist

    # Calculate average log probability and convert it to probability
    avg_log_prob = sum(valid_logprobs) / len(valid_logprobs)
    avg_prob = math.exp(avg_log_prob)

    return avg_prob


# Example usage
text = "hello world"
average_prob = get_average_probability(text)
print(f"Average Probability: {average_prob}")

# %%

data = {}

for i, (pii_type, top_entities) in enumerate(top_entities_per_pii.items()):
    for entity, count in zip(*top_entities):
        prob = get_average_probability(entity)
        data[entity] = (count, prob)

# Extract x and y values
x_vals = np.array([item[0] for item in data.values()])
y_vals = np.array([item[1] for item in data.values()])

# Define a threshold to remove outliers based on the standard deviation
threshold = 2.5  # Points beyond 2.5 standard deviations are considered outliers

# Identify non-outlier indices for both x and y values
x_zscores = (x_vals - x_vals.mean()) / x_vals.std()
y_zscores = (y_vals_adjusted - y_vals_adjusted.mean()) / y_vals_adjusted.std()
non_outlier_indices = (np.abs(x_zscores) < threshold) & (
    np.abs(y_zscores) < threshold)

# Filter out outliers
x_vals_filtered = x_vals[non_outlier_indices]
y_vals_filtered = y_vals_adjusted[non_outlier_indices]

# Linear regression on filtered data
slope, intercept, r_value, p_value, std_err = linregress(
    x_vals_filtered, y_vals_filtered)

# Print the regression parameters
regression_params = {
    "Slope": slope,
    "Intercept": intercept,
    "R-squared": r_value**2,
    "P-value": p_value,
    "Standard Error": std_err
}

regression_params


# %%
# Plotting the filtered data and regression line
plt.figure(figsize=(10, 6))
plt.scatter(x_vals_filtered, y_vals_filtered,
            color='darkblue', alpha=0.6, label='Filtered Data')

# Plot the regression line
plt.plot(x_vals_filtered, intercept + slope * x_vals_filtered,
         color='red', label='Regression Line')

# Add labels and title
plt.title('Occurrences vs. Generation Probability with Regression Line')
plt.xlabel('Occurrences in Training Data')
plt.ylabel('LLM Generation Probability')
plt.legend()
plt.grid(True)
plt.show()
