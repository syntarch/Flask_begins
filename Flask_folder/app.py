from flask import Flask, render_template
app = Flask(__name__)

videos = [{'id': '1', 'title': 'Где ещё в нашей Солнечной системе может существовать жизнь?',
                  'videoid': 'https://www.youtube.com/embed/_l-_3pwJQ3s'},
          {'id': '2', 'title': 'Astrobiology: the search for life beyond earth',
                  'videoid': 'https://www.youtube.com/embed/K-N0_kMvtFU'},
          {'id': '3', 'title': 'Towards the search for life on other earths',
                  'videoid': 'https://www.youtube.com/embed/qAYqK9lAxic'},
          {'id': '4', 'title': 'How NASA is answering the question: are we alone',
                  'videoid': 'https://www.youtube.com/embed/Lp7BL-UI0Rw'}]

playlists = {'about_astrobiology': {'title': 'Об Астробиологии', 'videos': ['2']},
             'life_search': {'title': 'Поиск жизни за пределами Земли', 'videos': ['1', '3', '4']}}

@app.route('/')
def main():
    return render_template('index.html', playlists=playlists)

@app.route('/playlists/<playlist_name>')
def playlist(playlist_name):
    current_playlist = playlists[playlist_name]
    new_playlist = []
    number = 1
    for video in videos:
        if video['id'] in current_playlist['videos']:
            video['number_id'] = str(number)
            new_playlist += [video]
            number += 1
    return render_template('playlist.html', new_playlist=new_playlist)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/videos_list')
def videos_list():
    return render_template('videos.html', videos=videos)

@app.route('/videos/<id>')
def video(id):
    return render_template('video.html', id=id, videos=videos)

@app.errorhandler(404)
def page_not_found(error):
    return 'Такой страницы нет'


if __name__ == '__main__':
    app.run()
