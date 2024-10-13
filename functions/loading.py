import os
from typing import List, Dict

# import logging
# logging.basicConfig(level=logging.DEBUG)


def load_blog_entries(folder_path: str) -> List[Dict[str, str]]:
  entries = []

  # TODO: make path more relative
  for filename in sorted(os.listdir(folder_path), reverse=True):
    if filename.endswith(".txt"):
      name_parts = filename.split('-')
      date, title = name_parts[0], name_parts[1:]

      date = "".join(date).replace('_', '-')
      title = " ".join(title).replace('_', ' ').replace('.txt', '')
      filename_clean = filename.replace('.txt', '')

      entries.append({'date': date, 'title': title, 'filename': filename_clean})

  return entries
