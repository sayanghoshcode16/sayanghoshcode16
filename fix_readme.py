import re

def fix_readme():
    with open('c:\\Users\\sayan\\OneDrive\\Desktop\\cyber ripo\\Readme\\README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix social icons: put them on a single line, remove newlines, remove spaces inside <a>
    # Find the social block: between "Connect with me:" and "Languages and Tools:"
    social_start = content.find('<h3 align="left">Connect with me:</h3>')
    lang_start = content.find('<h3 align="left">Languages and Tools:</h3>')
    
    if social_start != -1 and lang_start != -1:
        social_block = content[social_start:lang_start]
        # Find all <a> tags in the social block
        a_tags = re.findall(r'<a href="[^"]+" target="_blank">\s*<img src="[^"]+" alt="[^"]+" height="30" width="40" />\s*</a>', social_block)
        if a_tags:
            # Clean spaces inside
            clean_a_tags = [re.sub(r'>\s+<img', '><img', t) for t in a_tags]
            clean_a_tags = [re.sub(r'/>\s+</a>', '/><\/a>', t) for t in clean_a_tags]
            # Join with a single space
            new_social_block = '<h3 align="left">Connect with me:</h3>\n' + ' '.join(clean_a_tags) + '\n\n'
            content = content[:social_start] + new_social_block + content[lang_start:]

    # Refresh lang_start after modification
    lang_start = content.find('<h3 align="left">Languages and Tools:</h3>')
    stats_start = content.find('<h3 align="left">GitHub Stats & Trophies:</h3>')
    
    if lang_start != -1 and stats_start != -1:
        lang_block = content[lang_start:stats_start]
        # Find all <a> tags in the languages block
        a_tags = re.findall(r'<a href="[^"]+" target="_blank" rel="noreferrer">\s*<img src="[^"]+" alt="[^"]+" width="40" height="40"/>\s*</a>', lang_block)
        if a_tags:
            # Clean spaces inside
            clean_a_tags = [re.sub(r'>\s+<img', '><img', t) for t in a_tags]
            clean_a_tags = [re.sub(r'/>\s+</a>', '/><\/a>', t) for t in clean_a_tags]
            # Join with a single space
            new_lang_block = '<h3 align="left">Languages and Tools:</h3>\n' + ' '.join(clean_a_tags) + '\n\n'
            content = content[:lang_start] + new_lang_block + content[stats_start:]

    with open('c:\\Users\\sayan\\OneDrive\\Desktop\\cyber ripo\\Readme\\README.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    fix_readme()
