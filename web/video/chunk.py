import os
def chunk_html_file(input_file, output_folder, chunk_size=1024 * 1024):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(input_file, 'rb') as f_in:
        chunk_num = 0
        while True:
            data = f_in.read(chunk_size)
            if not data:
                break
            output_file = os.path.join(output_folder, f"mv{chunk_num}.html")
            with open(output_file, 'wb') as f_out:
                f_out.write(data)
            chunk_num += 1
    return chunk_num

input_file = 'view.html'
output_folder = 'chunk'

num_chunks = chunk_html_file(input_file, output_folder)
print(f"Created {num_chunks} chunks.")