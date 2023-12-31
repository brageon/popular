infile = "boa.txt"
outfile = "bob.txt"
delete_list = ["div", "br", "class", "</>", "<\>", "post_message", "post-clamped-text", "</a>", "href"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
        
        
