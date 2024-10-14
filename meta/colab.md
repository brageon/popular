# Code Anywhere

B.ipynb make a PDF from A.ipynb if you want to build a report.
```
from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir('/content/drive/MyDrive/')

!apt-get update
!apt-get install -y texlive-xetex
!xelatex -version
!jupyter nbconvert UD.ipynb --to pdf
ls ..
```
Here is my report for *rest*.
```
%%writefile sort.py
import subprocess
result = subprocess.check_output(["python", "rst.py"]).decode("utf-8")
shortx = subprocess.check_output(["sort", "-k2", "-nr"], input=result.encode("utf-8")).decode("utf-8")
print(shortx)

%run sort.py

!rm -rf ~/.pyperclip/
!rm -rf /usr/local/lib/python3.7/dist-packages/pyperclip-*.dist-info/
!rm -rf /usr/local/lib/python3.7/dist-packages/pyperclip/

import os, shutil
source_folder = os.path.join('/content/drive/MyDrive/App/colin/colin')
destination_folder = os.path.join('/content/drive/MyDrive/App/colin2')
shutil.move(source_folder, destination_folder)
```
Here is NLP wrangling.
```
%%writefile wsf.py
import os, re, glob
def remove_extra_spaces(file_path):
  with open(file_path, "r") as f:
    text = f.read()
  text = re.sub("\s+", " ", text)
  with open(file_path, "w") as f:
    f.write(text)
def main():
  file_list = glob.glob("*.txt")
  for file_name in file_list:
    remove_extra_spaces(file_name)
if __name__ == "__main__":
  main()

%%writefile calf.py
def get_words(file_path, start_index, end_index):
  with open(file_path, "r") as f:
    contents = f.read()
  words = contents.split()
  return words[start_index:end_index]
if __name__ == '__main__':
  file_path = "nu.txt"
  star, den = 0, 2200
  words = get_words(file_path, star, den)
  print(words)

%%writefile mix.py
from collections import defaultdict
KD = '9 4 7 6 5 4 4 4 5 5'
DE = '6 4 4 6 6 7 5 4 6 6 8 8 5 5 7 4 7 6 6 4 6 4 64 4 4 5 4 5 5 2 3 7 5 6'
def jaccard_similarity(s1, s2):
  s1_set = set(s1)
  s2_set = set(s2)
  intersection = s1_set & s2_set
  union = s1_set | s2_set
  return len(intersection) / len(union)
best_matches = defaultdict(list)
best_similarity = 0
for i in range(len(DE)):
  for j in range(i + 1, len(DE) + 1):
    substring = DE[i:j]
    similarity = jaccard_similarity(substring, KD)
    #similarity = levenshtein_distance(substring, KD)
    if similarity > best_similarity:
      best_similarity = similarity
      best_matches.clear()
      best_matches[similarity].append(substring)
      best_matches[similarity].append(i)
    elif similarity == best_similarity:
      best_matches[similarity].append(substring)
      best_matches[similarity].append(i)
for similarity, matches in best_matches.items():
  for substring, position in zip(matches[::2], matches[1::2]):
    redis = position / 2
    print(f"Similarity: {similarity:.3f}")
    print(f"Substring: {substring}")
    print(f"Position: {redis}")
    print("=" * 20)
```
Here is visuals.
```
%%writefile zet.py
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
def riemann_zeta(s, meshgrid_points=1000):
  x = np.linspace(-10, 10, meshgrid_points)
  y = np.linspace(-10, 10, meshgrid_points)
  X, Y = np.meshgrid(x, y)
  Z = X + 1j * Y
  return Z, np.log(Z**s)
s = complex(0.1, 2.0)
Z, result = riemann_zeta(s)
print(f"The value of Zeta({s}) is: {result}")
plt.contourf(Z.real, Z.imag, result.imag, levels=200, cmap='hot')
plt.colorbar()
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.title('Complex logarithm of Riemann Zeta function')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
def load_matrix(file_path):
  with open(file_path, "r") as f:
    data = f.readlines()
    matrix = np.array([[float(item) for item in line.split()] for line in data])
    return matrix
def z_score_normalize(matrix):
  mean = np.mean(matrix)
  std = np.std(matrix)
  z_score_matrix = (matrix - mean) / std
  return z_score_matrix
def main():
  matrix = load_matrix("mi/m0.txt")
  z_score_matrix = z_score_normalize(matrix)
  x, y = np.meshgrid(np.arange(matrix.shape[1]), np.arange(matrix.shape[0]))
  plt.pcolormesh(x, y, z_score_matrix)
  plt.colorbar()
  plt.show()
if __name__ == '__main__':
  main()

from PIL import Image
def overlay_pictures(picture1, picture2):
  if picture1.size[0] < picture2.size[0] or picture1.size[1] < picture2.size[1]:
    picture1 = picture1.resize((max(picture1.size[0], picture2.size[0]), max(picture1.size[1], picture2.size[1])), Image.ANTIALIAS)
  elif picture2.size[0] < picture1.size[0] or picture2.size[1] < picture1.size[1]:
    picture2 = picture2.resize((max(picture2.size[0], picture1.size[0]), max(picture2.size[1], picture1.size[1])), Image.ANTIALIAS)
  output_picture = Image.new("RGB", (picture1.size[0], picture1.size[1]), "white")
  output_picture.paste(picture1, (0, 0))
  transparency_mask = picture2.copy()
  transparency_mask = transparency_mask.convert("L")  # Convert to grayscale
  transparency_mask = transparency_mask.point(lambda x: x * 0.5)  # Apply a transparency effect
  output_picture.paste(picture2, (0, 0), mask=transparency_mask)
  output_picture.save("imp.png")
if __name__ == "__main__":
  picture1 = Image.open("inp_1.png")
  picture2 = Image.open("inp_2.png")
  overlay_pictures(picture1, picture2)
```
Here is ZIP wrangling.
```
import os, sys
from google.colab import drive
drive.mount('/content/drive')
nb_path = '/content/notebooks'
os.symlink('/content/drive/MyDrive/App', nb_path)
sys.path.insert(0,nb_path)

from google.colab import files
files.download('dis.zip')

import zipfile
with zipfile.ZipFile('colin.zip', 'r') as zip_ref:
  zip_ref.extractall('colin')

%%writefile nn.py
import os
os.chdir('slate2')
os.rename("slate2 (1).zip", "slate2.zip")

!unzip -qq -o trans5.zip

%%writefile zi.py
import os, shutil, zipfile
zip_file_path = 'slate2/slate2.zip'
temp_dir = '/content/temp'
os.makedirs(temp_dir, exist_ok=True)
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)
files = os.listdir(temp_dir)
for file in files:
    if file.endswith('.xml') or file.endswith('.anc'):
        os.remove(os.path.join(temp_dir, file))
with zipfile.ZipFile(zip_file_path, 'w') as zip_ref:
    for file in files:
        file_path = os.path.join(temp_dir, file)
        if file.endswith('.txt'):
            zip_ref.write(file_path, file)
shutil.rmtree(temp_dir)

%%writefile zy.py
import os, zipfile
folder_path = '/content/drive/MyDrive/App/trans/disi'
output_path = '/content/drive/MyDrive/App/trans/dis.zip'
with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      file_path = os.path.join(root, file)
      zipf.write(file_path, os.path.relpath(file_path, folder_path))
```
