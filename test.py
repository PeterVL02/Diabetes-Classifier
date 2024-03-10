from tqdm import tqdm

counter = []
for i in tqdm(range(100000)):
    for j in range(100):
        counter.append((i,j))
print(f'{len(counter):,}')
    
