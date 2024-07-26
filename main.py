from flask import Flask, request, jsonify, render_template
import scrap_data_eksi as sde
import scrap_data_twitter as sdt
import scrap_data_facebook as sdf
import scrap_data_letterboxd as sdl
import visualize as vs
app = Flask(__name__)
def scrape_and_visualize(search_data, function_type, social_media_platform):
    if social_media_platform == 'Twitter':
        if function_type== "Kullanici":
            word_counts_twitter =sdt.get_word_counts_user(search_data)
        else:
            word_counts_twitter =sdt.get_word_counts(search_data)
        vs.visualize(word_counts_twitter,"Twitter "+search_data)
    elif social_media_platform == 'Eksi':
        if function_type== "Kullanici":
            word_counts_eksi =sde.get_word_counts_user("https://eksisozluk.com/biri/"+search_data)
        else:
            word_counts_eksi =sde.get_word_counts("https://eksisozluk.com/"+search_data)
        vs.visualize(word_counts_eksi,"Ekşi Sözlük "+search_data)
    elif social_media_platform == 'Facebook':
        word_counts_facebook = sdf.get_word_counts_facebook(search_data)
        vs.visualize(word_counts_facebook,"Facebook "+search_data)
    elif social_media_platform == 'Letterboxd':
        if function_type== "Kullanici":
            word_counts_letterboxd =sdl.get_word_counts_user(search_data)
        else:
            word_counts_letterboxd = sdl.get_word_counts(search_data)
        vs.visualize(word_counts_letterboxd,"Letterboxd "+search_data)






    else:

        return jsonify({'error': 'Belirtilen sosyal medya platformu desteklenmiyor.'}), 400


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            if 'searchData' in data and 'functionType' in data and 'socialMediaPlatform' in data:
                search_data = data['searchData']
                function_type = data['functionType']
                social_media_platform = data['socialMediaPlatform']
                scrape_and_visualize(search_data, function_type, social_media_platform)
                return jsonify({'message': f'Gönderilen arama verisi: {search_data}, functionType: {function_type}, socialMediaPlatform: {social_media_platform}'})
            else:
                return jsonify({'error': 'Veri eksik veya geçersiz.'}), 400
        else:
            return jsonify({'error': 'Geçersiz veri formatı. JSON bekleniyor.'}), 400



if __name__ == '__main__':
    app.run(debug=True)
