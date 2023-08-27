import re

def extract_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        prompt_id = 1
        headline_id = 1
        curr_headline = [-10, -9, -8]
        for line in file:
            if "prompt_id" in line:
                print()
                print("Prompt ID: ", prompt_id)
                prompt_id += 1
                headline_id = 1
            
            if "headline_id" in line:
                print()
                print("Headline ID: ", headline_id)
                headline_id += 1
                
            if line.startswith("Human:") and "<|im_end|>" in line:
                print(line.strip())
            
            if line.startswith("Output:") and "<|im_end|>" in line:
                curr_headline.append(headline_id)
                if curr_headline[-1] != curr_headline[-2]:
                    print(line.strip())
                
            if re.match('Comedic:', line) and "<|im_end|>" in line:
                if curr_headline[-1] != curr_headline[-2]:
                    print(line.strip())
            
            if re.match('Comedy:', line) and "<|im_end|>" in line:
                if curr_headline[-1] != curr_headline[-2]:
                    print(line.strip())
            
            if re.match('Comedic Headline:', line) and "<|im_end|>" in line:
                if curr_headline[-1] != curr_headline[-2]:
                    print(line.strip())
            
extract_lines_from_file('dumps/iteration1.txt')
