from flask import Flask, render_template, redirect, url_for
import frontmatter
import os
import mistune

app = Flask(__name__)
markdown = mistune.create_markdown()

@app.route('/')
def home():
    tiles = []
    for filename in os.listdir('offerings'):
        if filename.endswith('.md'):
            with open(f'offerings/{filename}') as f:
                post = frontmatter.load(f)
                tiles.append({
                    'title': post['TITLE'],
                    'summary': post['SUMMARY'],
                    'icon': post['ICON'],
                    'url': filename[:-3]  # remove .md
                })
    return render_template('home.html', tiles=tiles)

@app.route('/<name>')
def offering(name):
    with open(f'offerings/{name}.md') as f:
        post = frontmatter.load(f)
        post.content = markdown(post.content)
        return render_template('offering.html', post=post)

@app.route('/submit-api-key', methods=['POST'])
def submit_api_key():
    api_key = ""
    # Do something with the API key...
    
    # Then redirect to the "in-progress" page
    return redirect(url_for('in_progress'))

@app.route('/in-progress')
def in_progress():
    # Render your 'in-progress' page here
    return render_template('progress.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
