from english_words import get_english_words_set

print("Loading English words...")
# Use both 'web2' and 'gcide' sources
english_words = get_english_words_set(['web2', 'gcide'], lower=True, alpha=True)
# This will combine words from both dictionaries, filtering for lowercase and alphabetic.

# Now, re-run this test code:
print("--- Testing word presence directly from english-words library (web2 + gcide) ---")
print(f"Is 'book' in the set? {'book' in english_words}")
print(f"Is 'books' in the set? {'books' in english_words}")
print(f"Is 'cloud' in the set? {'cloud' in english_words}")
print("---------------------------------------------------------------------")

print(f"Total words loaded: {len(english_words)}")