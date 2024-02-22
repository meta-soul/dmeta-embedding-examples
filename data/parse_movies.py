import csv

def main(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as csvfile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['NAME']
            storyline = row['STORYLINE']
            storyline = storyline.replace('·', ' ')
            if name and storyline:
                generes = row['GENRES']
                if generes:
                    generes = generes.replace('/', '、')
                
                actors = row['ACTORS']
                actors = actors.replace('·', ' ')

                if actors:
                    actors = actors.replace('/', '、')
                
                directors = row['DIRECTORS']
                directors = directors.replace('·', ' ')

                if directors:
                    directors = directors.replace('/', '、')
                
                regions = row['REGIONS']
                if regions:
                    regions = regions.replace('/', '、')

                sentence_parts = [f'电影名称：{name}', f'故事情节：{storyline}']
                if generes:
                    sentence_parts.append(f'电影类型：{generes}')
                if actors:
                    sentence_parts.append(f'电影主演：{actors}')
                if directors:
                    sentence_parts.append(f'电影导演：{directors}')
                if regions:
                    sentence_parts.append(f'国家或地区：{regions}')
                
                sentence = '。'.join(sentence_parts)
                sentence = sentence.replace('。。', '。')
                outfile.write(sentence)
                outfile.write('\n\n')

if __name__ == '__main__':
    main("./movies.csv", "./movie_desc-10m.txt")
